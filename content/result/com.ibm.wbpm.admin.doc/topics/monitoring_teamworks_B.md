# Monitoring processes and services in the Process Admin Console

## Before you begin

## About this task

- All monitor and instrumentations data are kept in memory and only show information about a
particular cluster member. Restarting the server clears the data. To view information across
different cluster members, connect to the deployment manager through a JMX console. For more information, see Monitoring MBeans with JConsole.
- The haltProcess() and haltService() methods might not always be able to stop a process instance
or service. The instance or service stops only if it is currently being run by the process and
service engine, and is not stuck inside a service implementation (for example, in the middle of
calling a web Service or running JavaScript).

## Procedure

To view the performance information for your process
apps and services:

- Log in to the Process Admin console, by entering the URL. 
For example: http://servername:9080/ProcessAdmin, where
servername is the name of your server and 9080 is the default
port.
- In the side menu of the Process Admin Console, expand
Monitoring to list the available monitoring options.
- Click the Process Monitor option. 
Note: To invoke this option, you need to be assigned the appropriate security role. This is
accomplished by configuring the console.process.monitor security property in the
BPMConsoleSection configuration object. Information about the
console.process.monitor security property and other security properties is found in
the topic Security configuration properties.
- Switch to the Summary page, whichprovides an overview of active and most expensive processes and services.
    1. To view details of a particular process app, click the
process app. The Processes page opens showing
the details of the process app. You can view the duration of each
step in the process, including the type of activity, such as event,
gateway. You can also view the list of services that are running and
the total duration of each service. You can identify a service to
investigate, for example you might look at the service that is taking
the longest time.
    2. To view details of all active and completed process
apps, click Processes.
- Switch to the Services page and see
a list of all the service steps and their activity types. Here you
can identify the step, for example a coach, that is taking a long
time. You can now try to determine why that particular step has a
long duration. For example, you might notice that a particular coach
is taking a long time to complete, and when you re run the process,
the time might be significantly less, indicating that the performance
issue is most likely due to the initial loading of the model. On further
analysis, you might notice that there are numerous calls to stand-alone
Ajax services, which might affect the scalability and performance
of the coaches, and rework the process app so that the number of such
calls are minimized.
- To stop an active process: The halted process now appears in the Active ProcessesNot Currently Executing list.

1. Click Processes.
2. Under Active Processes Currently Executing,
click the name of the process that you want to stop.
3. Click Halt Process. Note: The Halt Process button
appears only if the process is currently running.
- To stop an active service: The halted service now appears in the Active ServicesNot Currently Executing/Completed Services list.

1. Click the Services option.
2. Under Active Services Currently Executing,
click the name of the service that you want to stop.
3. Click Halt Service. Note: The Halt Service button
appears only if the service is currently running.

- Identify infinite loops in process applications

An infinite loop in a process app or service may cause the application to consume a large amount of processor resources. You can use the monitor page in the Process Admin console to look at the number of times certain steps and services are run in a process app. If you suspect an infinite loop, you can then open the corresponding BPD or service diagram to view the logic.
- Tracking changes in the number instances created and service requests

You can use the Instrumentation page in the Process Monitor to log and track the number of instances that are created and the number of service requests. You can then investigate changes in the data to determine whether there is a problem. For example, if there is a spike in the number of new instances that are created, you can use the data to understand whether the spike is a result of a normal business situation, an application error or a denial of service attack.
- Data displayed in the Process Monitor

The Process Admin Console includes a Process Monitor that enables administrators to view information about the processes and services that are running on Workflow Server. You can use the information to identify any problematic processes or services.
- Interpreting Process Monitor data

There are common assumptions people make when they look at Process Monitor data in the Process Admin Console that might lead them to interpret their process performance incorrectly. Learn about the areas of Process Monitor where users are most likely to misinterpret what the data represents.
- Enabling or disabling logging for terminating or deleting process instances

New messages are logged for terminating or deleting process instances. The message logging is enabled by default, and can be disabled by changing a configuration flag.
- Monitoring MBeans with JConsole

The Process Monitor data in the Process Admin console shows you only data for the cluster member to which it is connected. You can view information for different cluster members by using a JMX-compliant tool such as JConsole. Each cluster member hosts an instance of the MBean, which can be queried individually to get the full picture.