<!-- image -->

# Enabling common base event generation during store-and-forward processing

## Before you begin

## About this task

It is useful to configure IBM Business Automation Workflow to create common base
events when the store is stopped or started or to adjust or track common base events. Events that
correspond to the Common Base Events specification that are generated during store-and-forward
starts or stops, can be used by custom-made service monitors that are designed to track these
events.

To enable common base event generation during store-and-forward starts or stops, complete steps
in the Procedure section.

## Procedure

1. Open the administrative console.
2. Select Troubleshooting and then Logs and trace.
3. Select a server and then Change log detail levels.
4. Select the Runtime tab.
The Change log detail levels panel defaults to the Configuration tab.
Making changes while the Configuration tab is selected do not take effect until server restart.
Changes to the otherwise identical Runtime tab take effect immediately.
5. Expand all components and type
WBIEventMonitor.CEI.StoreAndForward.*=all.
You can also replace "CEI" with "LOG". The CEI string causes events to appear in the Common
Base Event Browser, while the LOG string will cause events to appear in the trace.log file. You can
select one trace string or both of them at the same time. Note: This string (minus the "=all"
portion) might be available as part of the list of available traces. If it is, then you can select
it from the list and then select All messages and trace instead of typing in
the string. 

Sometimes the logging string does not show up in the administrative console list until the
first common base event occurs. This is a known limitation in the common base event framework. If
you have installed a store-and-forward enabled application, completed the steps in the procedure,
and do not see the WBIEventMonitor.CEI.StoreAndForward string in the list of available traces, type
the trace string (for example, WBIEventMonitor.CEI.StoreAndForward=all) in the box and tracing will
be enabled even if a common base event has not been generated.

## Results