# Enabling process instance management

## About this task

- View and change the projected path for a running instance.
- Determine whether a running process instance is on track for completion.
- Change the due date of a running process instance.
- Adjust the due dates and durations of tasks in a process instance.

## Procedure

1. Open the process.
2. Grant users access to the Process Performance dashboard.
Without this access, users cannot see the Process Performance dashboard in Process Portal. To grant access, on
the Overview tab for the process, assign a group to the Expose
Performance Metrics option.
3 Enable due dates and at-risk calculations. Due dates and at-risk calculations are enabled for a process by default in theDetails section on the Overview tab. At run time, duedates are calculated from the creation time of the process instance based on the value of theDue in field and the settings for the work schedule properties. For moreinformation about due date calculations, see Due dates for process instances and activities . Due dates are used inProcess Portal to determine whether a processinstance is on track for timely completion. A process instance becomes at risk of not completing intime when the average time to complete the process exceeds the amount of time left to the due datefor the processinstance:"Process at risk" = (Current Time + Avg Historical Time to Process Completion) > Process Due Date Ifthere is no historical data for this process, the process instance is not at risk. Due dates are shown for the instances of this process in Process Portal . Process owners can modify the due dates in the Gantt chart.

```
"Process at risk" = (Current Time + Avg Historical Time to Process Completion) > Process Due Date
```

    1. Enable the due date. At-risk calculations
require that the due date is enabled.
    2. Set the expected duration of process instances in the Due
in field. By default, each instance is due
8 hours after it is started. If you select Days for
the duration, you can also add hours and minutes to the elapsed time,
for example 2 days, 4 hours, and 30 minutes.
    3. Optional: Set values for the Work
schedule properties. Default values are available
for all the properties.
    4. Optional: Enable at-risk calculations.

Due dates are shown for the instances of this process in Process Portal. Process owners can modify the due dates in the Gantt chart.

4 Enable projected path management. In the Details section on the Overview tab, selectthe Allow projected path management check box to enable projected pathmanagement. By default, projected path management is disabled. There are several routes, or paths, that can be followed to complete a process. With projectedpath management enabled, the projected path for an instance can be displayed on the Gantt chart ifdistinct paths from the start to end nodes are found. If projected path management is not enabled, the Process Performance dashboard and the Ganttchart are affected in the following ways: Attention: When projected path management is enabled, the following modeling constructscan cause performance issues with the projected path calculation at run time and might cause theprocess to end abnormally:

In the Details section on the Overview tab, select
the Allow projected path management check box to enable projected path
management.

By default, projected path management is disabled.

There are several routes, or paths, that can be followed to complete a process. With projected
path management enabled, the projected path for an instance can be displayed on the Gantt chart if
distinct paths from the start to end nodes are found.

- Process Performance dashboard: No estimated completion time for entries in the Instances in
progress list.
- Gantt chart Set Path page: No projected path.
- Gantt chart Gantt View page:
    - No future tasks
    - No estimated completion time
    - Task durations are not editable

- A gateway that causes the process flow to repeatedly loop over a sequence of activities in the
flow path, for example, a flow repeatedly goes from activity1 to activity2 to activity3, then back
to activity1 to start processing the sequence of activities again.
- A gateway that has multiple available paths, which can cause the process to return to a previous
activity in the flow. As a result, part of the process might be repeated multiple times, with
infinite possible permutations of the process path.
- A process with a lot of events that start new processes or cause the process flow to return to
previous activities in the flow. Do not include timer events because the projected path cannot be
calculated at all, as it is not known how long the calculation will need to wait for the timer.
5 Optional: Enable the collection of historical data in thePerformance Data Warehouse. Historical data is used in the Set Path page of the Gantt chart to displaythe traversed path and calculate the projected path for a running process instance. If autotracking is not enabled, the Gantt chart is affected in the following ways:

Historical data is used in the Set Path page of the Gantt chart to display
the traversed path and calculate the projected path for a running process instance.

1. On the Overview tab, ensure that Enable
tracking field is selected.
2. On the Tracking tab, ensure that Enable
Autotracking is selected.
3. Send the updated tracking definitions to the Business Performance Data
Warehouse.

- Historical path information is not available for the instance.
- The projected path through the instance is based on the longest (pessimistic) path and not the
typical historical path.
6. Optional: Enable process owners to analyze the average
amount of time that elapses between steps in the process.

To enable time lapses to be analyzed, include tracking points in the process and create a timing
interval to capture the time between the defined points. If tracking points are defined for the
process, timing intervals are sent to the Performance Data Warehouse and the Process Performance
dashboard includes timing intervals on the Overview page.
7. Click Save or Finish Editing.

## Results

The Process Performance dashboards for processes and instances
in Process Portal are
enabled for process management.

- ACTION\_VIEW\_PROCESS\_DIAGRAM
- ACTION\_VIEW\_CRITICAL\_PATH
- ACTION\_CHANGE\_CRITICAL\_PATH
- ACTION\_CHANGE\_INSTANCE\_DUEDATE

## What to do next

- Due dates for processes and activities

The due date for a process instance is the expected date and time when all activities related to a process instance are complete. Similarly, an activity due date is the expected completion time for an activity. You can use due dates throughout Process Portal to determine if processes instances and activities are on schedule or whether they are at risk of not completing on time.
- Modifying tasks

You can add implementation logic to specify values for runtime configuration properties of a task such as its due date and duration, priority, status, subject, and who can work on the task. The specified values take effect at run time.