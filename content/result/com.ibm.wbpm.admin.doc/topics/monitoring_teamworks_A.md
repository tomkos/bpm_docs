# Capturing process instrumentation data

## Before you begin

## Procedure

- To access the Instrumentation monitor and display the mostrecent data:
    1. In the side menu of the Process Admin Console, click Monitoring
to list the available monitoring options.
    2. Click the Instrumentation option.
    3. Click the Refresh button.
    4. To automatically refresh the displayed data, select
the time interval that you want from the drop-down menu.
    5. To reset all values to 0, click the Reset button. 
This enables you to monitor performance as data is collected.
- To log instrumentation data to an external .dat file: CAUTION: Logging instrumentation data to an external.dat file generates a lot of data and impacts both the processor andmemory consumption of the system. Limit the use of logging to investigateperformance issues with the server only.

1. In the side menu of the Process Admin Console, click Monitoring
to list the available monitoring options.
2. Click the Instrumentation option.
3. Click the Start Logging button.
The Instrumentation monitor displays the path and file
to which the data is saved. The file is created and stored on the
host of the IBM® Business Automation Workflow server
that you are currently monitoring.
4. Click the Stop Logging button
to end data capture to the log file.

## What to do next

- Disabling process instrumentation data

If Business Automation Workflow instrumentation appears to use large amounts of memory, you can disable this service or the collection of Business Automation Workflow runtime statistics by adding specific settings to the 100Custom.xml file.
- Using process instrumentation data for cache tuning

In the Server Admin area of the Process Admin Console, you can select Monitoring > Instrumentation to display process instrumentation data in the Instrumentation monitor. If the displayed data indicates an unexpectedly high number of cache misses for the cache settings, you might be able to edit the 100Custom.xml files and override the problematic default values of the cache settings; however, not all caches are configurable. The persistent object (PO) factory cache settings and repository cache settings are reflected in the PO Factory and Repository sections of the Instrumentation monitor. In some situations, you might need to override the default values for the cache settings with new values.
- Cache and cache-related settings

In IBM Business Automation Workflow, there are numerous cache and cache-related settings. If your data indicates a problem with the settings, you can edit the 100Custom.xml files for many of the settings or configure the property in the WebSphere administrative console for others and override the problematic default values of the settings.