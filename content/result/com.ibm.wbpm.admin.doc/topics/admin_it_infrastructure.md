# Administering the IT infrastructure

For information on tuning, see Chapter 7: IT
monitoring and tuning for    performance testing and managing a production
environment in IBM Business Process Manager V8.5 Performance Tuning
and Best    Practices.

- Starting and stopping your environment

 Traditional: 
 Use commands or the administrative console to stop and start your environment. You can also start or stop individual resources in the runtime environment, including deployment managers, node agents, deployment environments, and clusters.
- Managing workflow servers

Workflow servers run instances of the processes created in the designer.
- Administering deployment environments

 Traditional: 
 Through the administrative console on the deployment manager you administer the deployment environments defined on the deployment manager.
- Administering the BPM document store

 Traditional: 
 A set of commands is provided for administering the BPM document store. These commands enable you to perform various administration tasks, such as managing authorization, migrating documents, and determining the availability of the document store and the status of document migration.
- Maintaining an external Content Platform Engine configuration

Maintenance requires some additional considerations when IBM Business Automation Workflow is configured with an external Content Platform Engine, also called an external Enterprise Content Management (ECM) system. Your maintenance procedures must include Business Automation Workflow, the external Content Platform Engine system, and shared resources.
- Administering work portals

You can configure and administer various aspects of your work portal environment, Workplace, Process Portal or Heritage Process Portal (deprecated), such as configuring runtime behavior and setting up access to various functions.
- Monitoring and maintaining system data

To prevent performance issues, periodically monitor and purge your Process and Performance Data Warehouse databases of data that is no longer required.
- Monitoring concurrent users and activities

Besides capturing metrics to ensure compliance with the IBM Business Automation Workflow Concurrent User license option, you can also collect license compliance records and generate license compliance reports that can be read by the IBM License Metric Tool.
- Administering Business Process Choreographer

You can administer Business Process Choreographer using the administrative console or using scripts.
- Managing events

Events are requests or responses sent from one component to another. You can process events in a specific sequence. When events fail, you can use the failed event manager to view, discard, modify, or resubmit the events. You can also use the Store and forward feature to prevent subsequent failures from occurring when a component calls asynchronously to a service that is unavailable.
- Managing Business Performance Data Warehouses

 Traditional: 
The Business Performance Data Warehouses in your IBM Business Automation Workflow configuration retrieve and store tracked performance data, which enables users in IBM Process Designer to create reports and also analyze processes using the Optimizer.
- Administering access to WSRR

You can create, configure, and view all your WebSphere® Service Registry and Repository (WSRR) access definitions using the administrative console.
- Administering the Application Scheduler

Application Scheduler allows an administrator to schedule the starting and stopping of applications that are installed on IBM Business Automation Workflow. Use the Application Scheduler panel in the administrative console to control the scheduling of any installed application.
- Working with adapters

IBM Business Automation Workflow supports two types of adapters: WebSphere Adapters and WebSphere Business Integration Adapters. Adapters enable business applications to act as services by connecting them to diverse enterprise information systems (EISs), such as databases, enterprise resource planning systems, file systems, and email systems.
- General JVM configuration settings for IBM Business Automation Workflow environments

Guidelines for configuring the JVM garbage collection, heap size, and nursery size settings.
- Monitoring workflow servers

The Process Admin Console enables you to monitor the performance of the workflow servers in your environment. And, when necessary, you can view IBM Business Automation Workflow logs to help resolve issues.
- Troubleshooting IT administration

Log files and the information in this section can help you identify and resolve errors with the IT resources and tools in your system, for example, the failed event manager or the administrative console.