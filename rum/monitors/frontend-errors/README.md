# Datadog RUM Front-End Errors (e.g. JavaScript) 

### **RUM Error Attributes**

[Datadog Docs: RUM Browser Data Collected: Errors](https://docs.datadoghq.com/real_user_monitoring/browser/data_collected/#error-attributes)

| ATTRIBUTE       | TYPE   | DESCRIPTION                                                  |
| --------------- | ------ | ------------------------------------------------------------ |
| `error.source`  | string | Where the error originates from (for example, `console` or `network`). |
| `error.type`    | string | The error type (or error code in some cases).                |
| `error.message` | string | A concise, human-readable, one-line message explaining the event. |
| `error.stack`   | string | The stack trace or complementary information about the error. |

[From Errors to Issues](https://www.datadoghq.com/blog/error-tracking/#from-errors-to-issues)

When Datadog first receives an error event from [Real User Monitoring](https://www.datadoghq.com/product/real-user-monitoring/) (RUM) or APM, it creates a new issue. It then uses the issue to group subsequent errors that have similar messages and stack traces.

## Error Tracking

![001-RUM-Error-Tracking](images/001-RUM-Error-Tracking.png)

![002-RUM-JS-Issue](images/002-RUM-JS-Issue.png)



## Alert when there is a *New Issue* (i.e. Java Script Error)

### Error Tracking Monitor Type

You can use the "Error Tracking" monitor to create an alert when there is an new issue. 

![003-Monitors-Error-Tracking](images/003-Monitors-Error-Tracking.png)



![004-Monitors-New-Issue](images/004-Monitors-New-Issue.png)



## Alert when an Issue has a High Number of Errors

![005-Monitor-Error-Tracking-High-Count](images/005-Monitor-Error-Tracking-High-Count.png)

Be sure to take into account the timeframe for evaluating the query when setting the thresholds.



## RUM Monitor for Console (e.g. JavaScript) Errors

You can also analyze console errors (which are usually JS errors) in the RUM Analytics section. 

![006-RUM-Console-Errors](images/006-RUM-Console-Errors.png)

Then use this criteria to create a RUM Monitor.

![007-RUM-Errors-Console-1](images/007-RUM-Errors-Console-1.png)

Use the button at the end to change the search bar criteria into the syntax that is needed to define the monitor (e.g. @errror.source:console)

![008-RUM-Console-Errors-02](images/008-RUM-Console-Errors-02.png)

 RUM Monitor

![009-RUM-Monitor-Error-Source-Console](images/009-RUM-Monitor-Error-Source-Console.png)

![010-RUM-High-Console-Errors](images/010-RUM-High-Console-Errors.png)

![011-RUM-High-Console-Errors](images/011-RUM-High-Console-Errors.png)