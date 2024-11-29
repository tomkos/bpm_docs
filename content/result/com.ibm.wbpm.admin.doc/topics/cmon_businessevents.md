<!-- image -->

# Monitoring service component events

Applications that are deployed on the process server might contain a specification of service
component events that will be monitored for as long as the application runs. If you developed the
application using Integration Designer, you can specify
service component events to monitor continuously. This specification is included as part of the
application, and comes in the form of file with a .mon extension that is read by the process server
when the application is deployed. After the application is started, you will not be able to turn off
monitoring of the service components specified in the .mon file. The documentation for the IBM Business Automation Workflow does not address this type of continuous
monitoring. For more information about this subject, refer to the Integration Designer documentation.

You can use IBM Business Automation Workflow to monitor service
component events that are not already specified in the .mon file of the application. You can
configure the process server to direct the output of the event monitors to a log file, or to a
Common Event Infrastructure server database. The monitored events will be formatted using the Common
Base Event standard, but you can regulate the amount of information contained in each event. Use the
monitoring facilities in IBM Business Automation Workflow to diagnose
problems, analyze the process flow of your applications, or audit how your applications are
used.

- Enabling monitoring of business process and human task events

You must configure IBM Business Automation Workflow to support monitoring of business process and human task service components before you do any actual monitoring of those service component kinds.
- Configuring logging for service component events

You can choose to use the logging facilities of WebSphere® Application Server to capture the service component events fired by process server monitoring. Use the loggers to view the data in events when you diagnose problems with the processing of your applications.