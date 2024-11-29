# Managing workflow servers

The following sections explain how to access the Process Admin Console to perform administrative
tasks and also provide a list of the types of tasks that you can perform with links to detailed
information and procedures.

```
install\_root/profiles/profile\_name/config/cells/cell\_name/nodes/node\_name/servers/server\_name/process-center/config/100Custom.xml
```

To find the same files and resources for the Workflow Center server, replace
process-server with process-center.

- Accessing the Process Admin Console

Use the Process Admin Console to manage the workflow servers in your runtime environments, as well as the playback server on IBM Business Automation Studio.
- Modifying the Process Admin Console settings and behavior

Administrators can customize the Process Admin Console by adding new pages with new functionality or by removing the pages and functions included by default. You can also restrict access to both the pages that you add and the default pages. To reduce server loading, you can change the refresh interval.
- Configuring access to a secure application server

If a WebSphere Service Registry and Repository (WSRR) registry is running on a remote WebSphere Application Server that has security enabled, you need to configure IBM Workflow Server to enable users in IBM Process Designer to view available WSRR services.
- Restricting installation access to runtime servers

You must authorize users with the appropriate type of access, depending on the environment: administrative access to install to workflow servers in production environments, write access to install to any non-production workflow server, or read access to install to workflow servers in development environments.
- Viewing the status of process instances and applications

In the Process Admin console, you can use the Process Status summary to view the status of process instances and process applications that are running on a specific workflow server.
- Detecting and ending infinite loops in JavaScript activities

Infinite loops can occur in JavaScript and Java code that runs in process instances. You can configure loop detection parameters in the 100Custom.xml file to detect infinite loops and optionally ending them.
- Modifying runtime server configuration properties

In some cases, you might need to make changes to runtime configuration settings, such as modifying proxy settings or modifying workflow server connection properties. You can update configuration properties in the 100Custom.xml file, by using the Process Admin Console, by using wsadmin commands, or by calling the Operations REST APIs, depending on the type of change required.
- Managing workflow server caches and databases

The workflow server caches and databases normally run efficiently and without issues. However, in some cases particular problems come up that require you to use the utilities covered in this section.
- Managing exposed process values (EPVs)

Exposed process values (EPVs) are variables that certain users can change when processes are running on the playback server or a workflow server in your test, production, or other runtime environment.
- Monitoring workflow servers

The Process Admin Console enables you to monitor the performance of the workflow servers in your environment. And, when necessary, you can view IBM Business Automation Workflow logs to help resolve issues.
- Monitoring processes and services in the Process Admin Console

To identify performance issues with your process application, view the performance data available in the Process Monitor page of the Process Admin Console. Identify process applications that have bottlenecks, drill into the process application to identify the steps that are expensive, and learn how long it takes to run services.
- Enabling servers for Java debugging

 Traditional: 
 Use the Java debugging mode to trace and debug a running server.
- Enabling the audit log

 Traditional: 
 You can enable an audit log to track changes that are made by administrators in the Process Admin Console.