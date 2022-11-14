Here is an example of setting up process monitoring for WebLogic:



#### Datadog Config

![image-20221114074740763](images/image-20221114074740763.png)

sudo -u dd-agent -- datadog-agent check process

![image-20221114074817769](images/image-20221114074817769.png)

#### Datadog Metrics:

![image-20221114074834021](images/image-20221114074834021.png)



![image-20221114074846136](images/image-20221114074846136.png)



#### Datadog Monitors:

![image-20221114074902706](images/image-20221114074902706.png)



![image-20221114074911575](images/image-20221114074911575.png)



![image-20221114074920228](images/image-20221114074920228.png)



#### Slack "Warning" when CPU > 60%

![image-20221114074934694](images/image-20221114074934694.png)

*Keep in mind that the monitor in this example has an evaluation window of **5 mins**.
This smoothes out temporary spikes, but you can use a lower time frame to get notified sooner of the process CPU crossing the threshold.*



![image-20221114075002825](images/image-20221114075002825.png)



![image-20221114075018337](images/image-20221114075018337.png)

Slack message when the monitor has recovered

![image-20221114075047072](images/image-20221114075047072.png)

#### APM Service Page:

![image-20221114075105505](images/image-20221114075105505.png)



### APM Monitors:

![image-20221114075118961](images/image-20221114075118961.png)



![image-20221114075126165](images/image-20221114075126165.png)



#### Custom Dashboards:



![image-20221114075139512](images/image-20221114075139512.png)



![image-20221114075146129](images/image-20221114075146129.png)



#### Out-of-the-box Dashboards:

![image-20221114075204830](images/image-20221114075204830.png)



![image-20221114075211675](images/image-20221114075211675.png)



![image-20221114075219346](images/image-20221114075219346.png)



#### Watchdog Insights:

Even without configuring alerts, you many see "Watchdog Insights" pop up in pink in various section of Datadog.



![image-20221114075233200](images/image-20221114075233200.png)



![image-20221114075240151](images/image-20221114075240151.png)



![image-20221114075246440](images/image-20221114075246440.png)















