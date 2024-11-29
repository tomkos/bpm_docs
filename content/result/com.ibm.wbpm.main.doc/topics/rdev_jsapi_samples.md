# JavaScript reference examples

- Starting a new process

A new instance of a process can be started by using the tw.system.startProcessByName() function.
- Getting the current process instance

The current process instance can be retrieved through the TWProcessInstance variable called tw.system.currentProcessInstance.
- Getting the current userid

The current user ID can be retrieved through the TWUser variable in tw.system.user.
- Getting the name of the current process or service flow

For logging purposes, it is sometimes useful to access the name of the process or service flow that contains the currently executing script.
- Returning the owner of a task

You can know the identity of a user who has completed a given task.
- Returning a list of reference links

You can return a list of all reference links of the current process application or toolkit on a server by running the tw.system.model.processApp.getLinks() method.
- Extracting a managed file

If a process application or a toolkit contains a managed file, you can extract it from the runtime to evaluate its content.
- Searching processes and tasks

You can retrieve data from process and task instances by using a JavaScript TWSearch object to define which columns to retrieve, what filters to apply, how to sort and organize the results. You can also parse the results into a list of variables.
- Calling Java through JavaScript (deprecated)

JavaScript inside Business Automation Workflow can invoke Java through the Live Connect technology.
- Working with document attachments

Document attachments can be associated with process instances. These can be added through coach controls or through programmatic additions.
- Interacting with cases and activities from processes or service flows

You can interact with cases and case activities from processes or service flows by using a script that contains JavaScript methods to call case APIs. This enables you to work with the values of case properties, such as multivalued properties or business objects.
- Retrieving data from XML

The following examples show you how to pull data out from an XMLDocument (or any XML type) using the following XML.