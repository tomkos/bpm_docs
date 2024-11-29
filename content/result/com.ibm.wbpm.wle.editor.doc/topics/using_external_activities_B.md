# Creating an external implementation (deprecated)

## Before you begin

To perform
this task, you must be in the IBM® Process
Designer desktop
editor, which is deprecated.

## About this task

Using the external implementation function is similar
to using the service functions like an integration service or human
service. However, unlike those service functions that are designed
for a specific area like a web service invocation or client side human
service flow, the external implementation is more generic in nature.
When a step in a business process is implemented with an external
implementation, the business process halts and waits for input from
the external application.

To create an external implementation,
use the Web APIs or REST APIs as discussed in the previous topic.

When you create an external implementation in IBM Process
Designer,
you need to know the properties to use to identify and run the custom
application. If you did not build the custom application, you need
to coordinate with the developers to ensure that you provide the appropriate
properties in IBM Process
Designer.

## Procedure

1. Open the desktop Process Designer (deprecated).
2. Open a process application in the Designer view.
3. Click the plus sign next to Implementation and
select External Implementation from the list
of components.
4. Supply a descriptive name for the new external implementation.
5. Click Finish.
6. In the Common section of External
Implementation, optionally provide a description in the
Documentation text box.
7 In the Custom Properties section, specify the propertiesto identify and run the external application. Note: You can add custom properties to pass static metadataabout the implementation to the external application. For dynamicdata, which would be different for each process instance or environment,use the Parameter Details section as outlinedin the following step.
    - For example, for an external Eclipse RCP application, you might
add custom properties to pass the Java class name of the form to use
for an activity or an application-specific identifier to look up the
implementation by another means. Alternatively, you might use the
external application name or system ID to find the implementation.
    - You can create parameters with a special meaning. For example,
suppose you need to pass a URL address as a custom property. In the Custom
Properties section, you could use url as
the name and then add a value that is the URL itself (http://mysite.com...).
    - You can also use this section to pass data to variables in a client
that were instantiated with a constructor.
8. Required for Process Portal: In
the URL section, specify the URL template for
the external implementation. When a user opens a task in Process Portal, the
URL template is used to call the appropriate external implementation.
To include runtime information, such as the task local and environment
context, use replacement variables that are surrounded by curly brackets
in the URL Template text. Process Portal automatically
appends the REST URL to the restUrlPrefix parameter
to indicate where task related operations can be performed. Tip: To ensure that the external implementation can identify
the current task, it is a good idea to include the task ID in the
URL template. For example, /MyExternalApp/ExternalImpl.jsp?taskId={tw.system.task\_id}&lastName={tw.local.lastName}
9. In the Parameters section, add the
parameters for the external implementation by clicking Add
Input or Add Output. For
example, if the external implementation provides an interface in which
a manager can either approve or reject an expense report, it might
include input parameters for the expense report data and output parameters
for the decision that the manager makes and the justification for
his decision. Be sure to account for all process data that the external
implementation requires to complete successfully and also for any
data required from the external activity by subsequent activities.
10. In the Ajax Services section, specify
the Ajax services that your external implementation is authorized
to call.  Click Add and, from the
list of available Ajax services, select the services that can be called
from your external implementation. If no Ajax services are available
for selection, you can click the plus sign (+) next to User Interface > Ajax Service to create one. See Building an Ajax service.
11 Use Authorize Ajax Services to authorize the Ajax services that can becalled from this external implementation. You have the following options:

- If there are services listed in the Ajax Services list, select
Authorize Ajax Services to enable an authorization check be run on the listed
services at run time. Only the listed Ajax services are authorized for the call.
- If the Ajax Services list is empty and you select the check box, no
Ajax service is authorized for the call.
- If you clear the check box, you disable the runtime authorization check and allow this
external implementation to call any Ajax service.
12. Click Save in the main toolbar.

## What to do next

You can use an external implementation with IBM Process
Portal.
In the Custom Properties section add the URL for IBM Process
Portal as
shown earlier.

## Related concepts

- Business Automation Workflow web service APIs programming guide

## Related information

- REST API programming for BPDs and BPEL processes