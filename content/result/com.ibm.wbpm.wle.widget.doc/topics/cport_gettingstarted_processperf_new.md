# The Process Performance dashboard

- Overview page
- Diagram page

## Prerequisites

- To see the Process Performance dashboard,
you must be a member of the Process Owner team.
- To see a specific process, you must be a
member of the team that is assigned to the Expose Performance
Metrics setting for the business process definition. Only
the default snapshot is considered when determining whether you have
access to a process.
- Traditional: 
 To see
timing intervals in the Average Duration section, they must be specified for
the process.

## Overview page

- If your administrator deleted completed instances from the system,
these instances are not included in the performance statistics.
- In Business Automation Workflow earlier
than 8.5, the completion date for process instances is not stored. Depending on how your
administrator set up the Process Portal index, the average
instance duration and instance completion statistics might not include instances that were completed
in an earlier version.

- Identify instances that are overdue or at risk by using the pie
chart to filter the list of instances. Clear the filter by clicking
the selected pie slice again.

- Change the time interval that is used on the x-axis. For
example, to investigate the instance closure or arrival rate during
a day, change the time interval to Hours.
- See the net change for a bar in the chart by hovering
over the bar.

Reworked tasks are indicated by an extra bar on the chart;
a bar is added every time that the task is reworked. A reworked
task is a task that is performed multiple times. The reason
for the rework might be because the work on the task does not meet
the completion criteria. For example, if the work on a task requires
an approval, and the approval is rejected, then the work on the task
must be repeated one or more times until it is approved. The length of the
bar indicates the average amount of time that is spent doing rework for the activity.

- See a summary of the instance that shows by how much an overdue or at risk
instance might miss the deadline by hovering over an entry in the list.
- Pin open the instance summary if, for example, you want to compare
several instances at the same time.
- See the instance details by selecting the entry in the instances list. The instance details page is shown.

## Diagram page

This
page shows the overall status of the tasks in the open instances.
Based on the information in the status indicators, you can identify
which tasks are causing bottlenecks.

- Traditional:  Identify instances
that need attention by clicking the status indicator for a task. The instances list is filtered to
show the instances that contain this task.
- See the tasks in linked processes or subprocesses by double-clicking
the corresponding symbol in the diagram.
- Traditional:  See the instance
details by selecting the entry in the instances list. The instance details page is shown.