# Service component monitoring overview

IBM® Business Automation Workflow provides
capabilities for monitoring service components to aid in system administration
functions, such as performance tuning and problem determination. It
goes beyond these traditional functions by also providing the capability
for persons who are not necessarily information technology specialists
to continually monitor the processing of the service components within
the applications deployed on your system. By overseeing the overall
processing flow of the interconnected components, you can ensure that
your system is producing what you expect it to produce.

IBM Business Automation Workflow operates on the installation of
WebSphere® Application
Server, and, consequently, uses much of the
functionality of the application server infrastructure for monitoring system performance and
troubleshooting. It also includes some extra functionality that is designed for monitoring service
components. This section focuses on how you monitor server-specific service components. It is
intended to supplement the monitoring and troubleshooting topics found in the WebSphere Application
Server Information Center; therefore; refer to that
documentation for details of the other monitoring capabilities in the combined product.

- Why use monitoring?

You monitor service components within IBM Business Automation Workflow to assess performance, to troubleshoot problems, and to evaluate the overall processing progress of service components that make up the applications deployed on your system.
- What do you monitor?

You can monitor service component events in IBM Business Automation Workflow by selecting certain points that a service component event reaches during processing. Each service component defines these event points, which generate (or fire) an event when the application processes at that given point. You can also monitor performance statistics for service component events.
- How do you enable monitoring?

There are several methods that you can use to specify service component event points for monitoring, depending on the type of monitoring you are planning to do.