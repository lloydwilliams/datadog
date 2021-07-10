# Log Processing



## Sending Logs Via Datadog API (HTTP) 

https://docs.datadoghq.com/getting_started/api/

### Datadog Postman Collection

If you'd like to work with a 3rd party tool for making REST API calls to Datadog, Datadog has created a Postman collection that can be imported which has samples of all the API calls that can be made. 

If you'd prefer not to set-up Postman, you can use the curl scripts provided [here](https://github.com/lloydwilliams/datadog/tree/main/logs/time-difference/curl). You can then start at the [Log Pipelines](https://github.com/lloydwilliams/datadog/tree/main/logs/time-difference/tutorial#log-pipelines) section below.

You can click the "Run in Postman" button in the set-up section of the docs and it will import the Datadog collection into your Postman account. 
https://docs.datadoghq.com/getting_started/api/#setup

![GettingStarted](../_resources/GettingStarted.png)



### Sample Collection

This sample collection available [here](https://github.com/lloydwilliams/datadog/blob/main/logs/time-difference/postman/Grok%20Parsing%20Collection.postman_collection.json) is for this tutorial and can be used to send sample logs to Datadog via API. You will need to import it into your Postman (either the desktop version or in the browser version).

![Screen Shot 2021-07-09 at 8.52.23 PM](../_resources/postman1.png)

![Screen Shot 2021-07-09 at 8.55.12 PM](../_resources/postman2.png)

https://github.com/lloydwilliams/datadog/blob/main/logs/time-difference/postman/Grok%20Parsing%20Collection.postman_collection.json

*This is for demo purposes only and is not actively maintained by Datadog, so it may become out-of-date in the future.* 

These requests use an API Key variable called `api_key`in the HTTP Headers section, so you will need to either set a postman environment variable to the value of your own Datadog API Key or remove the variable and put your own Datadog API Key in its place. For more information on how to do this please refer to the [Postman documentation](https://learning.postman.com/docs/sending-requests/variables/). 



![api-key.png](../_resources/bc4cff646ded40e2b6f683552d37693a.png)




![Screen Shot 2021-07-09 at 1.22.11 PM.png](../_resources/0e70931b72be44ab82fbb7f9f2ceba3b.png)

This will allow you to send logs to Datadog via the API. 

The next section will show you how to process the logs so they can look like the image below when they are in Datadog with the 'Account ID' extracted and used as a 'Facet' and the time difference between the dates calculated and set-up as a 'Measure' so that users can filter and sort by these values. 



![Screen Shot 2021-07-09 at 5.23.27 PM.png](../_resources/96fc52e9fa7f4b4a8a6b97ab8f8f1b99.png)



## Log Pipelines

The next step is to create a log pipeline for processing the logs.


![Screen Shot 2021-07-09 at 5.29.05 PM.png](../_resources/9a9d3d57ef29423d9c2aeb5b8b1f63b5.png)


In Datadog, click on Logs, Configuration from the side bar menu or use the direct link: [https://app.datadoghq.com/logs/pipelines](https://app.datadoghq.com/logs/pipelines)

Choose 'Add a new pipeline':

![Screen Shot 2021-07-09 at 5.42.00 PM.png](../_resources/c66e9b9668f54973888d195974133276.png)


The source in this example is defined as "postman", so use a filter that "source:postman" as the pipeline for these logs. Also, give the pipeline a name (e.g. Postman Logs). You can even try sending some logs via API to make sure that the logs are going to this pipeline. 

![Screen Shot 2021-07-09 at 5.38.03 PM.png](../_resources/1ba9a7d239ca4ce19e4a00dec6a48232.png)

If you need to return to this window after the configuration is saved, you may need to click on the 'edit' option to open the box again. 

![Screen Shot 2021-07-09 at 5.36.03 PM.png](../_resources/d9e9a3c893994aa38b6d019c0b927b9d.png)


![Screen Shot 2021-07-09 at 5.33.55 PM.png](../_resources/17036223e10f4c068382e982a5cc0321.png)

### Grok Parser

Underneath this pipeline, choose 'Add Processor'. 



![Screen Shot 2021-07-09 at 5.45.38 PM.png](../_resources/2ef539fe4987433e883d4b49987f1bd1.png)

Click the "Parse My Logs" button. *Note: you may need to make sure that you have sent logs recently or attempt to currently send some more logs.* 

You should see that it found some recent logs and auto-generated some parsing rules:

![Screen Shot 2021-07-09 at 5.46.16 PM.png](../_resources/4ad1e320720847d8bea3819d75c906e6.png)

In this case, you really only need 1 rule, so you can delete the extra log samples and extra rules and use one rule that is slightly modified from the auto-generated rule that looks like this:

```
myRule1 %{date("yyyy-MM-dd HH:mm:ss"):date}\s+%{word:level}\s+Account:\s+%{word:account}\s+Date1:\s+%{date("yyyy-MM-dd HH:mm:ss"):startdate}\s+and\s+Date2:\s+%{date("yyyy-MM-dd HH:mm:ss"):enddate}
```

You will know that it's correct when you see the green check mark which indicates that it matched a rule.
You will also see how it's going to parse the data. 

![Screen Shot 2021-07-09 at 5.53.15 PM.png](../_resources/f0059fbe9a0d42809fa907d5caf977f5.png)

In this case, we want to convert the date to a number of milliseconds, so that we can later easily calculate the duration. 

When the parsing logic is what you want, you can give the Grok Parser a name and 'Save' it.


### Arithmetic Processor

Next we need an 'Arithmetic Processor' to subtract the end date from the start date and to put it in a more user-friendly unit of time. 

You simply add a "Add Processor" again to the same pipeline, but this time choose 'Arithmetic Processor'.

![Screen Shot 2021-07-09 at 6.00.32 PM.png](../_resources/b4f731ce59ea41a2bc4aa2475121c619.png)

Set a target attribute (e.g. datediff) and set the formula to: enddate - startdate (or whatever names you defined in your Grok parser above for the dates). 

![Screen Shot 2021-07-09 at 6.01.56 PM.png](../_resources/a55a68dee680411f80478d17d2575212.png)

Save the Arithmetic Processor. 

Next create another Arithmetic Processor. 
(Of course, you could have done this with 1 Arithmetic Processor, but doing it with 2 may give you some design flexibility in the future.)

Use it to divide the number calculated above (datediff) by 3600000 and assign the target attribute a name like "hoursdiff".

![Screen Shot 2021-07-09 at 6.07.45 PM.png](../_resources/82867f21031442969cb230885b8879c0.png)

Save the second Arithmetic Processor.

### Test the Pipeline Processors

Send some more logs via the Datadog API.
Go to the Logs, Search section and click on one of the logs entries. You should see the 'Event Attributes' that you created.

![Screen Shot 2021-07-09 at 6.25.23 PM.png](../_resources/cde627db50bf4079988ba5c97b78e5b8.png)



## Facets and Measures 


### Facets

Hover just to the left of the 'account' attribute and click on the gear icon. 

![Account.png](../_resources/16a40dc0b20d4f4580e0eaf5802a34dc.png)

Choose the "Create facet for @account" option.

Set the display name (e.g. Account ID), Type as 'String', provide a Group (e.g. Postman) and a Description.

![Screen Shot 2021-07-09 at 6.53.27 PM.png](../_resources/6a011fae240b430d9e35f3d9ac9f9cfb.png)

### Measures

Hover just to the left of the 'hoursdiff' event attribute. Since this is a number, select 'Create measure for @hoursdiff'

![Screen Shot 2021-07-09 at 6.57.56 PM.png](../_resources/0d3a142d11454a27be3865326719780c.png)

Set the display name to "Time Difference". Use this name instead of hours difference because Datadog will automatically create an appropriate string to display based on the amount of time. 

Set the Type to Double. 

Set the Unit to Hour (hr), this tells Datadog that the value that we calculated for this measure was in hours. 

Set the Group to the same group name that you used for the 'Account' Facet above. This will keep these two grouped together in the side Facets section since they are related to the same logs (and it will allow them to both be easily collapsed at the same time when they are not needed). 

Also, supply a Description. 

Save the new Measure. 

Reload the Logs screen in the browser, so it can pick up the new facet and measures in Facets section.

![Facet_Measure.png](../_resources/86b62dfbebda4037b3c7e3c87df884e3.png)

#### Try out the Facets and Measures

Type in the Search Bar (where it says: Filter your logs) `Host:myhostname` you should get only the logs for this hostname.

Open the facet 'Acccount ID' and select which account you are interested in. Notice that it also populates the search bar and will then filter the logs. 

![Screen Shot 2021-07-09 at 7.11.39 PM.png](../_resources/b9cf6a0ee3d14f8083574a515fe6ba0f.png)

Likewise try out the 'Time Difference' facet. You'll notice that instead of check boxes, there are sliders to adjust min and max values.

Click on the header for the 'Service' column and select 'Insert to right'.

![Screen Shot 2021-07-09 at 7.17.11 PM.png](../_resources/2da607e64d03420c9c046b0c0509a97c.png)

Start typing '@hoursdiff', you can select it when it appears. 

![Screen Shot 2021-07-09 at 7.19.11 PM.png](../_resources/91d6c4d079734182b918a2a5a1bae600.png)


Notice that the 'Time Difference' column appears and there is a value for each log.

![Screen Shot 2021-07-09 at 7.20.47 PM.png](../_resources/e04670d44b1a4c20a75a8352d3901865.png)

Click the Column Header and try sorting by 'Time Difference' values. 


![Screen Shot 2021-07-09 at 7.22.23 PM.png](../_resources/1c924afe633544728ba12ba158c34d3f.png)

*Note: you can't do this when you are in 'Live Tail' mode, you must have a fixed time period selected.*

![Screen Shot 2021-07-09 at 7.28.34 PM.png](../_resources/1b379e1eb1544f11b2f713387236b688.png)



# Viewing Logs in Custom Dashboards

## New Dashboard

From the Dashboards menu, select New Dashboard.

Set the Dashboard Name and click on the 'New Dashboard' button. 

![Screen Shot 2021-07-09 at 7.31.05 PM.png](../_resources/35bfb436258c46e9b10b0a13abc9406f.png)


![Screen Shot 2021-07-09 at 7.38.49 PM.png](../_resources/45719f4a02524058b0a4cd75684bdbe5.png)

Click the '+ Add Widgets' button:

Use the arrow on the right to find the 'Log Stream' widget. 

![Screen Shot 2021-07-09 at 7.40.27 PM.png](../_resources/4667acd848284e19943b126c694ba4ee.png)

Drag it onto the canvas.



![Screen Shot 2021-07-09 at 7.41.26 PM.png](../_resources/cdd593ac47bf48708647ada9a4091040.png)

A configuration panel appears.

Set the number of display lines or if you don't want any, toggle the 'Content Column' option. 

![Screen Shot 2021-07-09 at 7.43.19 PM.png](../_resources/51e3d18649f548ebbd12997561f5eed5.png)

Add the columns @account and @hoursdiff and give the graph a title. 
*Note: this won't be an option for you if you did not define the facet and measure in the previous section.*



![Screen Shot 2021-07-09 at 7.46.11 PM.png](../_resources/57ffa0f78be446de9b0b5165b75d5a3d.png)

Click Done and then make the widget wider (if you'd like) by dragging from the bottom right corner. 

![Screen Shot 2021-07-09 at 7.49.05 PM.png](../_resources/62319c7a4fde4dd8aac65dc6bb154941.png)


Note that you can click on any log entry and it will take you back to the Log Search section where you can see all the event attributes and other details. You could potentially pivot to the APM traces a log entry if these logs were generated by an application that has APM tracing enabled and is also writing logs to Datadog via the agent.



## Dashboard Template Variables

Click on 'Add Template Varables' below the dashboard title.


![Screen Shot 2021-07-09 at 7.55.54 PM.png](../_resources/ed0bf82cc962454b8b58e5beff8d611e.png)

After that click on the 'Add Variable' button and create a variable called "host_var" and assign it the Tag or Attribute = 'host' and the Default Value 'myhostname'.

![Screen Shot 2021-07-09 at 7.58.02 PM.png](../_resources/681db1df129a47fdbb14a8cef3fd6980.png)

Modify the Log Stream editor configuration to have '$host_var' in the 'Search Query' and click Done.



![Screen Shot 2021-07-09 at 8.01.16 PM.png](../_resources/24fa4dc54aae49458d6d18b4f678a1c3.png)

You should only see logs from the default hostname.

![Screen Shot 2021-07-09 at 8.02.42 PM.png](../_resources/dcd1697113a24195a50fef1c16977794.png)

Next start to add another variable for the account id by clicking the pencil at the end of the variables.




![Screen Shot 2021-07-09 at 8.04.24 PM.png](../_resources/78d18261e0bd449dae4b230d488841ab.png)

Use the 'Add Variable' button to add the`account_var` variable name and set the 'Tag or Attribute' to `@account`.



![Screen Shot 2021-07-09 at 8.06.45 PM.png](../_resources/8f865b37a031431da757eebff856a121.png)

Click Done.

Next add `$account_var` to the 'Search Query' of the Log Steam Editor widget, like you did with the `$host_var`.

![Screen Shot 2021-07-09 at 8.10.04 PM.png](../_resources/958e5a78058e46d7bb145d3bb94b2770.png)

Click Done and click on the 'account_var' drop-down menu. 

![Screen Shot 2021-07-09 at 8.14.28 PM.png](../_resources/3b0c7aad83b64125a6e1fe4f63ccac62.png)

Select a specific Account Id from the list of 'Associate Values'. Notice that it filtered the logs. You can also use this in combination with the time frame in the top right section. 

Note: if the account ID that you want does not show in the list of associated values, it is still possible to cut and paste it into the box.

![Screen Shot 2021-07-09 at 8.16.31 PM.png](../_resources/4640507031c64d04acd28014436feef4.png)



### Create a Query Widget

Click on the Add Widgets button.

![Screen Shot 2021-07-10 at 8.12.37 AM](../_resources/add_widgets.png)

Drag the Query Value widget to the canvas.

![Screen Shot 2021-07-10 at 8.14.22 AM](../_resources/QueryValue.png)

A configuration panel will appear. 

In the Graph your data section, Choose "Logs" from the drop-down list for metric 'a'. 

Add the variables `$host_var` and `$account_var` in the search box for metric 'a' (with a space between the variable names).

Configure the Units and formatting, so that it shows 0 decimals and none of the boxes are checked.

Experiment with some conditional formatting. For example, if the value is greater than 10 you can show with a Red background, greater than 5 with a Yellow background and less than 5 with a Green background.   

## ![Screen Shot 2021-07-10 at 8.19.29 AM](../_resources/QueryValueConfig.png)

Save the configuration and click on the Close button at the top to close the editing session. 

Try sending some more logs using the API calls and see what happens when you change the values of the variables and the timeframe. 

![Screen Shot 2021-07-10 at 8.36.20 AM](../_resources/dashboard-with-query-value.png)

## Create a Favorite Dashboard

If you like what you've done, click the star icon next to the name of the Dashboard to make it one your favorites. 

![Screen Shot 2021-07-10 at 8.35.10 AM](../_resources/final_dashboard.png)

