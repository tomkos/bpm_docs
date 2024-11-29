<!-- image -->

# Tutorial: Service component performance monitoring

For service component event points that you monitor, you can publish to the Performance
Monitoring Infrastructure (PMI) and view the resulting performance statistics on the Tivoli® Performance Viewer (TPV). This exercise demonstrates how
performance monitoring of service component event points differs from monitoring using the Common
Event Infrastructure (CEI) server and loggers. The major difference that you notice is that you
select an entire service component element for performance monitoring, instead of individual events
with specific natures. Because IBM® Business Automation Workflow can
monitor performance only on service component elements having events with ENTRY, EXIT, and FAILURE
natures, you have only those kinds of service component elements available to you to select for
monitoring.

- Successful invocation - the firing of an event of nature type EXIT that follows a corresponding
ENTRY event.
- Failed invocation - the firing of an event with a FAILURE nature following a corresponding ENTRY
event.
- Time for successful completion - the elapsed time between the firing an ENTRY event and the
firing of the corresponding EXIT event point.

## Objectives of this tutorial

- Select the performance statistics of service component elements that you want to monitor.
- View and interpret the resulting performance statistics.

## Time required to complete this tutorial

This tutorial requires approximately 15-20 minutes to complete.

## Prerequisites

- Configured and started a server.
- Enabled the PMI on the server.
- Installed and started the Samples Gallery application on the server.
- Installed and started the business rules sample application on the server. Follow the
instructions on the Samples Gallery page to set up and run the business rules sample
application.

- Example: Monitoring service component performance

For monitoring performance, you can use the administrative console to select service components for monitoring and view performance measurements. This example shows the use of the console to monitor performance statistics.