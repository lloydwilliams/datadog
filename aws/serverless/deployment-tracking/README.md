# AWS Serverless Deployment Tracking

How to configure (Datadog Docs): https://docs.datadoghq.com/serverless/deployment_tracking/

## [Setup](https://docs.datadoghq.com/serverless/deployment_tracking/#setup)

Datadog collects code and configuration change events for your AWS Lambda functions from AWS CloudTrail.

If you haven’t already, set up the [Amazon Web Services](https://docs.datadoghq.com/integrations/amazon_web_services/#setup) integration first. Then, add the following permission to the policy document for your AWS/Datadog role:

```text
cloudtrail:LookupEvents
```



![Screen Shot 2021-10-19 at 4.04.25 PM](images/DatadogAWSIntegrationPolicy.png)



The AWS Lamda tile within Datadog (https://app.datadoghq.com/account/settings#integrations/amazon-lambda) should be configured.

![Screen Shot 2021-10-19 at 4.01.18 PM](images/AWS_Lambda_Integration.png)

Make sure that the status of your AWS Lambda integration is OK.

![Screen Shot 2021-10-19 at 4.07.14 PM](images/AWSLambdaStatusOK.png)

Deployment tracking information is made available via AWS Cloudtrail which must be enabled from the Datadog Integration tile.

https://app.datadoghq.com/account/settings#integrations/amazon-cloudtrail



![Screen Shot 2021-10-19 at 4.26.08 PM](images/AWSCloudTrail.png)



![AWSCloudTrail2](images/AWSCloudTrail2.png)

Click the "Install Integration" button to complete the set-up.

![AWS_Serverless_Deployments](images/AWS_Serverless_Deployments.png)

If you click in the Deployment Event Time, a new tab will open to show you the deployment in the Events list.

![AWS_Serverless_Deployment_Event](images/AWS_Serverless_Deployment_Event.png)

If you are experiencing issues, make sure that your AWS IAM Policy has all the appropriate permissions:

 ![AWS_Lamba_Integration_Problem](images/AWS_Lamba_Integration_Problem.png)