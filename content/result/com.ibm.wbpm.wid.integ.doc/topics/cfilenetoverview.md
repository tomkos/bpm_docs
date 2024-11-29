<!-- image -->

# Integrating BPEL processes with IBM Business Automation
Workflow
cases

Integration Designer and IBM® Business Automation
Workflow offer
a way of using both approaches together. From a case management task,
a BPEL process created in Integration Designer can be
invoked. The process can be a microflow, that is, responds immediately,
or long running, that is, takes longer to respond as the process is
more complex. To provide access to a microflow or a long-running process,
you use the external service wizard in Integration Designer to create
a web service.

In addition, an Enterprise Content Management adapter is offered
to allow interaction with an IBM Business Automation
Workflow repository.

The information in this section focuses on using the external
service wizard in Integration Designer to create
a web service. To see how to create a task in IBM Business Automation
Workflow that
uses this web service, see the information in IBM Case Manager.

- Creating a web service to implement a IBM Business Automation Workflow task

IBM Business Automation Workflow tasks integrate with BPEL processes through a web service which you can build by using the Integration Designer external service wizard. The web service can be implemented in the following ways: a microflow process, which provides a synchronous response; a long-running process, which provides an asynchronous response; or any combination of Service Component Architecture components.
- Editing and validating exports used with IBM Business Automation Workflow activities

As the case design or BPEL process evolves, the input and output parameters can change. If the web service needs to be moved to a different server to do an integration test, for example, then the host name, port and path can change. You can edit the input and output parameters then validate your changes.
- Deleting a web service export used with a IBM Business Automation Workflow task

Changes to your case management task may require deleting the web service export used with it.
- Design considerations for web services used with IBM Business Automation Workflow tasks

You should be aware of some differences when working with IBM Business Automation Workflow tasks.