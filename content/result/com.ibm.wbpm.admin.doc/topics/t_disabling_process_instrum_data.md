# Disabling process instrumentation data

## About this task

In high-load scenarios, when a lot of instrumentation is created in a short period,
instrumentation data can appear in memory-heap dumps to be using a lot of memory. Examples of
high-load scenarios are the excessive use of team filter services or large JavaScript code that
calls many Business Automation Workflow APIs. If such processing
occurs over a long period, the heap that the collected instrumentation data uses grows continuously
because more data is generated than used. In such cases, depending on the available heap size,
out-of-memory situations can occur even if instrumentation data does not use all the heap space.

From Business Automation Workflow V8.5.7.0 on, you can reduce
memory use by disabling Business Automation Workflow instrumentation
and the collection of Business Automation Workflow runtime
statistics. Instrumentation and collection of runtime statistics are enabled or disabled separately
for IBM® Workflow
Server, IBM Workflow
Center, and the Performance Data Warehouse
server.

## Procedure

- To disable Business Automation Workflow instrumentation for
IBM Workflow
Server or IBM Workflow
Center, add the following
enable-instrumentation setting to the 100Custom.xml file
in the process-server or process-center configuration directory. For the Performance Data Warehouse
server, do the same in the configuration directory for the Performance Data Warehouse.

<server>
   <enable-instrumentation merge="replace">false</enable-instrumentation>
</server>

If this property is not set or is set to true, Business Automation Workflow instrumentation is enabled for the appropriate
server.
- To disable the collection of Business Automation Workflow
runtime statistics for IBM Workflow
Server or IBM Workflow
Server, add the following
collect-runtime-stats setting to the 100Custom.xml file in
the process-server or process-center configuration directory. For the Performance Data Warehouse
server, do the same in the configuration directory for Performance Data Warehouse.

<server>
   <collect-runtime-stats merge="replace">false</collect-runtime-stats>
</server>

If this property is not set or is set to true, the collection of
Business Automation Workflow runtime statistics is enabled for the
appropriate server.