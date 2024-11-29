# Tracing problems related to persistence

## About this task

Business processes model the flow of business in an organization.
The model at run time stores and retrieves data such as employee names
and bank accounts. The storage of data and access to data is transparent
to the business process user but it is important for the business
process application developer to understand how databases and EJBs
store that data in the background. Moreover, when performance problems
arise linked to persistence, the application developer needs to have
appropriate traces to diagnose where the problems likely reside.

A
detailed log setting can be used to capture a trace of persistence
problems. To set this detailed log on, follow these steps:

## Procedure

1. In the Integrated Solutions Console, expand Troubleshooting and
select Logs and trace.
2. In the Logging and tracing page,
click your server name. On the following page, click Change
log detail levels. These log levels let you control the
events that are captured by the logs.
3. Select either Configuration or Runtime.
Adding a trace using the Configuration tab
will require restarting the server. Adding a trace using the Runtime tab
will take effect immediately.
4. Expand All Components. Scroll down
the list to WLE.wle\_repocore.* Selecting this
item or some of its subsets results in logging traces of persistence-related
elements in the repository. You can choose to log all messages and
traces or a specific level.
5. These logs can help you or those in support analyzing performance
problems linked to persistence. Once selected, remember to save your
changes to logging and tracing in the Integrated Solutions Console.