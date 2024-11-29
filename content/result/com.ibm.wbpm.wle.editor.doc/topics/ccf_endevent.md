# Navigation options for after service completion

The implementation options for the end event indicate the intended behavior upon completion of
the service and determine what the user sees at run time after the client-side human service
completes successfully. For example, the user can see the case details user interface for a case
instance or an Process Portal page if a URL is specified as a JavaScript expression.

| Option                                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Default (behavior provided by the hosting UI) | Complete the client-side human service and go to the default page that is provided by the hosting user interface, such as Process Portal.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Go to the instance details UI                 | Complete the client-side human service and go to the instance details user interface for the case or process instance that the client-side human service runs in. This option applies only to client-side human services that run in a case or process instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Go to a specified URL                         | Specify a relative URL to go to when the service completes. The URL is relative to the hosting user interface, such as Process Portal. Because the URL is specified as a JavaScript expression, you must surround literal values with quotation marks. To return to the page that called the service, enter "BACK" (with quotation marks) as the URL value.Process Portal performs a navigation action when it finds any of the following keywords in the URL: /dashboards, /executecf, /exposedURL, /launchInstanceUI, /launchStartableService, /processes, /launchTaskCompletion, /tasks, /launchProcessDiagram, /launchAuditHistory.  The following examples describe the most common navigation use cases:  Go to a task: "/launchTaskCompletion?taskId=3" Go to a dashboard: "/dashboards/TWP/Team+Performance" or "/teamworks/executecf?processApp=TWP&serviceName=Team+Performance" Go to a service exposed as a URL:  "/teamworks/executecf?processApp=SSP&serviceName=exposedURL" Go to instance details UI: "/launchInstanceUI?instanceId=1214" Go to a startable service: "/launchStartableService?modelID=1.a5ae06a9-681d-4701-9991-fbbbf6da0781&branchID=2063.d367c75b-45ea-4dcf-a483-547ad03d6dcb" Note that /executecf? does not work for a startable service. |

## Communicating with hosting user interfaces through event data

Client-side human services are integrated into hosting user interfaces such as Process Portal, Workplace,  IBM® Content
Navigator, and
Case Client. To ensure an
enhanced user experience through the hosting user interfaces, client-side human services send
message events to communicate their execution status to the hosting user interfaces. One such event
is the onCompleted event, which is sent when the end of a client-side human service
is reached.

You can specify event data in the Implementation properties of the end event
in the client-side human service diagram. The value you specify must be compatible with the JSON
format. If the hosting user interface supports the specified value, it can act on it when it
receives the onCompleted event. The JSON string specified in the data property is
the payload of the message event. After parsing the string, the properties of the resulting object
will include a name that identifies the type of client-side human service event. When the name is
"onCompleted", it will have an eventData property with the value
set on the end event.

```
var autoObject = {};
autoObject.name = "testName";
autoObject.value = "testValue";
autoObject
```

```
{ 
  name: "onCompleted",
  eventData: {name: 'testName', value: 'testValue'},
  ...
}
```