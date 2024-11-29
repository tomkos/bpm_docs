# Defining a custom layout Process Designer for
reports (deprecated)

## Before you begin

To perform
this task, you must be in the IBM® Process
Designer desktop
editor, which is deprecated.

## About this task

The reporting functionality was deprecated in Business Automation Workflow V8; by
default it is not enabled. To enable reporting, in Process Designer go
to File > Preferences > IBM BPM > Capabilities, and enable the Backward Compatibility capabilities.

Creating
a custom chart type enables you to control the format of your report
results. For example, the chart types available by default in the
System Data Toolkit may not meet the needs of your users. Or, you
may want to develop customized chart types to meet corporate guidelines.

## Procedure

To create a custom chart type:

1. Open the desktop Process Designer (deprecated).
2. Open the process application.
3. Click the plus sign next to the All category
in the library and select Chart Type from the
list of components.
4. In the New Chart Type window, enter a name for the chart
type and click the Finish button.
5. Optionally provide information about the new chart type
in the Documentation text box.
6. In the Chart Definition text box, enter the Cascading Style Sheet (CSS)
definition for your custom chart type.
By default, the Chart Definition text box includes the CSS framework
for a new definition to help you get started. You can use the framework to build a definition for
the new chart type or you can overwrite the framework by copying and pasting an entire CSS
definition from another application.
7. Click Preview to ensure that the
CSS definition produces the chart layout that you expect. If not,
refine the definition until it meets your needs.
8. Click Save in the main Process Designer toolbar
to save the custom layout.