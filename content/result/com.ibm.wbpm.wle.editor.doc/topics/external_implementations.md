# External implementations

- Creating an external implementation to implement an activity

You can implement a user task to use applications outside of IBM Business Automation Workflow (called external implementations), such as by modeling an activity that is implemented by a custom Eclipse RCP or Microsoft .NET application. You could also use a system task to call an external implementation; however, this use of system tasks is deprecated, so use a user task instead.
- Invoking an external implementation by using a user task

You can use an external service that has an external implementation when you want a user task to be implemented by an application outside of IBM Business Automation Workflow. For example, you created your own user interface for your users that you would prefer to use. So you create an external service that has an external implementation to call your own interface.
- Converting external implementations

In previous releases, external implementations were created with the desktop Process Designer. Convert these external implementations to external services so that you can use them in the web-based Process Designer.