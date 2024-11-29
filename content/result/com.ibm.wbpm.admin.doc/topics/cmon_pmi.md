<!-- image -->

# Monitoring performance

Whether you are tuning service components for optimal efficiency or diagnosing a poor
performance, it is important to understand how the various run time and application resources are
behaving from a performance perspective. The Performance Monitoring Infrastructure (PMI) provides a
comprehensive set of data that explains the runtime and application resource behavior. Using PMI
data, the performance bottlenecks in the application server can be identified and fixed. PMI data
can also be used to monitor the health of servers.

The PMI is included in the base WebSphere® Application
Server
installation. This section provides only supplemental information about performance monitoring as it
relates to the service components specific to IBM® Business Automation Workflow; therefore, consult the information in the
WebSphere Application
Server documentation for using PMI with other
parts of the entire product.

- Successful invocations.
- Failed invocations.
- Elapsed time for event completion.

You can also monitor performance statistics derived from the service invocations of applications
by using the Application Response Measurement (ARM) statistics. These statistics measure the actual
runtime processes that underlie the process server service component events making up an enterprise
application. You can derive various performance measurements for the processing of your applications
using these statistics.

- Performance Monitoring Infrastructure statistics

You can monitor three types of performance statistics using the Performance Monitoring Infrastructure: the number of successful invocations, the number of failures, and the elapsed time to completion of an event. These statistics are only available for events that have event natures of type ENTRY, EXIT, and FAILURE.
- Application Response Measurement statistics for the Service Component Architecture

There are 25 performance statistics that you can monitor at the Service Component Architecture (SCA) level. You can use these Application Response Measurement (ARM) statistics, which are either counters or timers, to measure invocations to and responses from services in various patterns.