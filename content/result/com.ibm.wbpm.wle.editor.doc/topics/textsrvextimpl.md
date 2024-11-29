# Invoking an external implementation by using a user task

## About this task

When a user task in a business process is implemented with an external service that has an
external implementation, the business process halts and waits for input from the external
application. The process resumes execution when the task is finished by the external implementation
that uses a web or REST service. For more information, see REST API programming for BPDs and BPEL processes. To create an external implementation with Web APIs, see Business Automation Workflow web service APIs programming guide.

An external service that has an external implementation is created; it cannot be discovered.

## Procedure

To  create an external implementation:

1. In the library navigation, click the + for
Services and select External Service.
2. Select External Implementation and click
Next.
3. Enter a name for your service and then click Finish.
4. A basic external service that has an external implementation is created with no
operations. You should create at least one operation. If your external implementation provides an
interface in which a manager can either approve or reject an expense report, you might further
revise the operation. You might include input parameters for the expense report data and output
parameters for the decision that the manager makes and the justification for the decision. The input
and output parameters define the dynamic data for the operation. These parameters would be different
for each process instance or environment. You can't add faults. 
In the Details section, the name is shown and you can add a description.
5 If you select Binding for an operation,you see that your service has an External implementation bindingtype. If you select an operation, you see sections for the propertiesused in creating an external implementation of an operation. The sectionsare as follows:
    - URL Template (Required for Process Portal): Add the URL to the
external implementation you want to use. When a user opens a task in Process Portal, the URL template is
used to call the appropriate external implementation. To include runtime information, such as the
task local and environment context, use replacement variables that are surrounded by curly brackets
in the URL Template text. Process Portal automatically appends
the REST URL to the restUrlPrefix parameter to indicate where task related
operations can be performed. Tip: To ensure that the external implementation can
identify the current task, it is a good idea to include the task ID in the URL template. For
example,
/MyExternalApp/ExternalImpl.jsp?taskId={tw.system.task\_id}&lastName={tw.local.lastName}
    - Custom Properties: Add the properties in name-value pairs to identify and
run the external implementation. These properties are static configuration values to be queried by
the external implementation. For example, you might add the external application name or system ID
to find the implementation. You can add properties with special meaning. For example, the name
url might be used with a value for the actual URL such as 
http://mysite.com ....
6. Implement all the operations for your service.
7. Click Save or Finish Editing.

## Results

After your service is created, you can select it as an implementation of a user task in a
process. Select the operation that you want to use from the operation drop-down list. See Creating a process.

## Related information

- Creating an external implementation to implement an activity