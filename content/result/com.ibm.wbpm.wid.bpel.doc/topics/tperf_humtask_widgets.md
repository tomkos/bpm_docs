<!-- image -->

# Improving performance when using human task list widgets

## About this task

## Procedure

To check the target services configuration in the administrative
console, complete the following steps:

1. Open the administrative console.
2. Select the Servers tab in the navigation
bar.
3. Select WebSphere application servers server type and choose
the application server on which you run Business Space. 
The page to configure an application server opens.
4. In the Additional Properties section
select the REST service endpoint registration entry.  The
REST service endpoint registration page opens.
5. Check the service endpoint target values for the process
services and the task services REST endpoint types.  The
default setting is Federated REST services.

## Related concepts

- Types of human task
- Inline and stand-alone human tasks
- Task templates
- Task instances
- Human task clients
- Human task user interfaces
- Versioning of human tasks
- To-do tasks and collaboration tasks with parallel ownership
- Lifecycle of a human task

## Related tasks

- Setting human task preferences

## Improving performance

### Procedure

To improve the performance, complete the following steps:

1. Change the Business Space target services configuration
in the administrative console by following the steps in the previous
task.
2. Change the process services to the Business Process Choreographer
REST services endpoint of the application server that is running your
processes and human tasks.
3. Click OK to save the configuration
changes.
4. Log out and then log in again to Heritage Process Portal.