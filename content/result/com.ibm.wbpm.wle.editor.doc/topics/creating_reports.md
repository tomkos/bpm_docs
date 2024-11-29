# Defining reports in Process Designer (deprecated)

## Before you begin

The reporting functionality was deprecated in Business Automation Workflow V8; by
default it is not enabled. To enable reporting, in Process Designer go
to File > Preferences > IBM BPM > Capabilities, and enable the Backward Compatibility capabilities.

To perform
this task, you must be in the IBM® Process
Designer desktop
editor, which is deprecated.

Ensure
that autotracking is enabled for the business process definition (BPD).

Ensure
that the tracked data is current by selecting File > Update tracking definitions.

## Procedure

1. Open the desktop Process Designer (deprecated).
2. Open the process application.
3. Click File > Ad
Hoc Report Analysis.
4. Define the content of the report.  Select the
variables for the X and Y axes from the corresponding bindings lists.
You can also specify a time period filter and a business data filter.
5. Click the Refresh icon to preview
the chart.
6. When you are satisfied with the appearance of the chart
and the data, click the Create Report from Chart button.
7. In the Create Report window, give
the report a name, and click Finish.
8 Create the scoreboard to display the report.
    1. In the library for the BPD, expand Performance,
and select ScoreBoard from the list of components.
    2. In the New Scoreboard window, give
the dashboard a name, select a layout, and click Finish.
9 Assign the report to the dashboard.

1. In the Scoreboard window in the Reports section,
click Add, and then the report.
2. In the Layout section, select
the Enabled check box, and type a title in
the ScoreBoard title field. This
title is what Process Portal users
see in the list of dashboards.
3. In the Exposing section, click Select next
to the Exposed to field, and select the team
whose members can view this dashboard in Process Portal.

## Results

When you log in to Process Portal as
a member of a team to whom the dashboard is exposed, you can see the
new dashboard in the list of dashboards. Click the dashboard to display
the report.

## What to do next

After installing a process application snapshot that includes
the dashboard, you can adjust the members of the team to whom the
dashboard is exposed.

- Defining a custom layout Process Designer for reports (deprecated)

When you define a report in Process Designer, you can select an existing chart layout (for example, one of the layout included in the System Data toolkit), to display resulting data, or you can create a custom layout.