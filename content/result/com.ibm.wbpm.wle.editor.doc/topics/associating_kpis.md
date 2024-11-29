# Associating KPIs with activities

## About this task

## Procedure

1. Open the desktop Process Designer (deprecated).
2. Open the BPD.
3. Select the activity that you want to associate with a KPI
and go to the KPIs tab in the Properties view.
4. To add a KPI, click Add  and select
the KPI or KPIs that you want. The KPIs in the current process application
and in referenced toolkits, including the System Data toolkit, are
displayed.
5 In the Assignment Settings panel,clear the Use KPI defaults check box if youdo not want to use the default assignments for the selected KPI.
    1. Select the assignment type from the drop-down list.
The assignment type establishes how the value for the KPI is determined.
    2. For KPIs that measure time, the assignment type is Automatic
and cannot be changed. Automatic assignment means that Business Automation Workflow automatically
tracks and stores the values for these KPIs.
    3. For other KPIs, you can choose from the following assignment
types: 

Assignment type
Description

Value per Hour (clock)
Enables you to multiply the specified value
times the total number of hours spent on the activity.

Value per Hour (calendar)
Enables you to multiply the specified value
times the number of working hours spent on the activity.

Absolute Value
Enables you to specify a value for the KPI.

Custom JavaScript
Enables you to supply custom scripts to track
the value for this KPI.

True after N traversals (for Rework KPI only)
Enables you to specify the number of times an
activity must be performed before it is considered rework.
6. In the Threshold Settings area, clear the Use
KPI defaults check box if you do not want to use the default
threshold settings for the chosen KPI. If you do not use
the default thresholds, you can indicate the type of performance that
you expect by providing minimum, expected, and maximum values in the
appropriate fields.Business Automation Workflow uses
the specified thresholds as the range for producing heat maps and
recommendations in the Optimizer. You can also use KPIs to specify
conditions that trigger service level agreements (SLAs).
7. Click the Save icon in the toolbar
to save your changes.