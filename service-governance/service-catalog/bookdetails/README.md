This is an example of registering a service using the Datadog Service Catalog. Please see the following link for instructions. 

[Setting up Service Catalog](https://docs.datadoghq.com/tracing/service_catalog/setup/)

Note that this set-up requires first configuring the [GitHub integration](https://docs.datadoghq.com/integrations/github/). 

This folder contains a sample bash script that uses curl to send the service catalog registration information contained in the yaml file to Datadog so that it appears in the SaaS UI so that users can easily reference useful information about the service. 

Use the Ownership tab and information about the team, on-call staff, contacts, source code repository are available. Users can also easily access from the main page any of the telemetry configured.

![service-catalog-1](images/service-catalog-1.png)

Click on a specific service to see more details:

![service-catalog-2](images/service-catalog-2.png) 

Also set-up related dashboards or view service dependencies.

![service-catalog-3](images/service-catalog-3.png)

![service-catalog-4](images/service-catalog-4.png)

You can also see all of the service dependencies using the "Map" button on the main page of the service catalog.![service-catalog-5](images/service-catalog-5.png)



To use the [register](https://github.com/lloydwilliams/datadog/blob/main/servicecatalog/bookdetails/register.sh) script in this folder, you will need to either set your Datadog API key and Datadog APP key (DD_API_KEY and DD_APP_KEY) as environment variables or modify the script. 

Create a [yaml file](https://github.com/lloydwilliams/datadog/blob/main/servicecatalog/bookdetails/bookdetails.yaml) containing the information for your service and replace the file name in the script with the name of your file. 

See the [Service Definition Datadog API](https://docs.datadoghq.com/api/latest/service-definition/) docs for full details. 



