<!-- image -->

# Configuring logging for service component events

IBM® Business Automation Workflow uses the extensive logging
facilities of the underlying WebSphere Application
Server to allow
you to capture the events fired by server monitoring at service component event points. You can use
the administrative console to specify the particular service component event points that you want to
monitor, the amount of payload detail contained in the resulting service component events, and the
method used to publish the results, such as to a file of a certain format, or directly to a console.
Monitor logs contain events encoded in Common Base Event format, and you can use the information
contained in the event elements to trace problems with the processing of your service components.

The functionality of WebSphere Application
Server logging and
tracing capabilities is documented in considerable detail in the WebSphere Application
Server documentation, with complete details of how
logging and tracing is used within the entire product. This section provides only supplemental
information about logging as it relates to the service components that are specific to IBM Business Automation Workflow. Consult the information in the WebSphere Application
Server documentation for using logging and trace with
other components of the entire product.

- Enabling the diagnostic trace service

Use this task to enable the diagnostic trace service, which is the logging service that can manage the amount of detail contained in the service component event.
- Configuring logging properties using the administrative console

Use this task to specify that the monitoring function publish service component events to a logger file.
- Tutorial: Logging service component events

For service component event points that you monitor, events can be published to the logging facilities of the underlying WebSphere Application Server. This tutorial guides you through an example of setting up monitoring with logging, and how to view events stored in a log file.
- Audit logging for business rules and selectors

You can set up IBM Business Automation Workflow to automatically log any changes made to business rules and selectors.