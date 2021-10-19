# Datadog NodeJS Sample with Hapi and Winston



This sample shows how to integrate Datadog with a microservice running using the Hapi web framework (https://hapi.dev/) for HTTP https://docs.datadoghq.com/tracing/setup_overview/compatibility_requirements/nodejs/#web-framework-compatibility and Winston (https://github.com/winstonjs/winston) for logs https://docs.datadoghq.com/tracing/setup_overview/compatibility_requirements/nodejs/#logger-compatibility.

This will enable you to trace your requests using Datadog APM. https://docs.datadoghq.com/tracing/

https://docs.datadoghq.com/tracing/setup_overview/setup/nodejs/?tab=otherenvironments

![01 NodeJS APM Trace](images/01 NodeJS APM Trace.png)

It will also show you how to correlate your logs with the traces by injecting the trace id into the logs.

https://docs.datadoghq.com/tracing/connect_logs_and_traces/nodejs/

![02 NodeJS Traces with Logs](images/02 NodeJS Traces with Logs.png)

You can create logs with different statuses that will appear color-coded within Datadog.

![03 NodeJS Logs](images/03 NodeJS Logs.png)

You can filter by the status and click on the log to bring up more details. 

![04 NodeJS Logs WARN](images/04 NodeJS Logs WARN.png)

Notice how the logs also correlate back to the APM traces. 

![05 NodeJS Logs with Trace](images/05 NodeJS Logs with Trace.png)

and you will also see how to create logs which contain additional information in the event attributes. 

![06 NodeJS Logs with Error and Event Attr](images/06 NodeJS Logs with Error and Event Attr.png)

You can create facets from any of the event attributes to allow you to analyze the logs any way you want. 