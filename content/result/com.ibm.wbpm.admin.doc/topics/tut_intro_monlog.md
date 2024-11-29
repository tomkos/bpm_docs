<!-- image -->

# Tutorial: Logging service component events

The scenario you will follow for this example will show you how to select service component event
points for monitoring in applications already deployed and running on a server. You will see how the
monitoring function fires an event whenever the processing of an application reaches one of those
event points. Each of those fired events takes the form of a standardized Common Base Event, which
is published as an XML string directly to a log file.

## Objectives of this tutorial

- Select service component event points to monitor, with the output published to the server
loggers.
- View the stored events in the log files.

## Time required to complete this tutorial

This tutorial requires approximately 15-20 minutes to complete.

## Prerequisites

- Configured and started a server.
- Configured Common Event Infrastructure.
- Enabled the diagnostic trace service on the server.
- Installed and started the Samples Gallery application on the server.
- Installed and started the business rules sample application on the server. Follow the
instructions on the Samples Gallery page to set up and run the business rules sample
application.

- Example: Monitoring events in the logger

For monitoring with logging, you can use the administrative console to manage the details for event types. This example shows the use of the console to change the level of detail recorded for some event types and to use a text editor to open the trace.log file to view the information for individual events.