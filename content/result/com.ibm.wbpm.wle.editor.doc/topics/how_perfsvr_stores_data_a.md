# Tracking IBM Business Automation Workflow performance
data

- Autotracking automatically captures data from tracking points
at the entry and exit of each item in a process (for example, services,
activities, and gateways). To enable autotracking, make sure that Enable
Autotracking is selected under the Tracking tab
of the process. (By default, the checkbox is not selected, which is
better for performance.) Your system administrator can change this
default.
- Tracking groups provide more control over tracked data. For example, use tracking groups track a selected group
of process variables across multiple processes or process applications
and to store tracking points for a timing interval. To enable tracking
groups, make sure that Enable Tracking is selected
under the Overview tab of the process. (By
default, the checkbox is selected.) Your system administrator can
change this default. Note that the Enable Tracking setting
does not apply to services with tracking points. Tracking data is
always enabled when services contain tracking points.

After you configure data tracking for your process, and each time
after that configuration that you update your data-tracking requirements,
you must send the tracking definitions to the Performance Data Warehouse.
When you send tracking definitions, either directly or as part of
deploying a snapshot, the Performance Data Warehouse establishes the
structure in its database to hold the data that Workflow Server generates
when you run instances of your processes. In Business Automation Workflow, these
tracking requirements are called definitions because
they establish the database schema in the Performance Data Warehouse
to accommodate the tracked data that Workflow Server generates.

When you change your tracking requirements in Process Designer, you
must send the definitions to the Performance Data Warehouse. Because
you are developing process applications on a Workflow Center server,
be sure to send definitions after you change each process application.
For process applications that are deployed in runtime environments,
create a snapshot of your changes and deploy the new snapshot to ensure
that the data you want to collect is available in the runtime environment.

- It is not possible to rename a tracking group.
- It is not possible to rename a tracked field.
- It is not possible to have several tracking groups with the same
name.
- It is not possible to have several tracked fields with the same
name but with different types in different tracking groups, either
in the same process or in different processes or toolkits.

- Data tracking considerations

Before you implement data tracking in a process application, make sure you understand the supported data types and naming conventions, as well as any considerations for working with versioned data.
- Autotracking performance data for BPDs

Use autotracking if you want to capture data to quickly configure and publish reports using the ad hoc wizard, or if you want to capture data that automatically includes tracking points at the entry and exit of each item in a BPD. For example, use autotracking if you know that you want to compare the duration for each activity in a BPD.
- Setting up autotracking

You need to set up autotracking before you can use the ad hoc wizard. When autotracking is enabled for a process, data for any nested processes of that process will also be tracked. Subprocesses and services inherit the setting of the parent process.
- Tracking groups of process variables

Use tracking groups if you want to explicitly control your tracked data and tracking points. For example, you can group the variables that you want to track by type, strategically place tracking points in your process, and track variables across multiple processes. With tracking groups, your tracking points can also span multiple processes.
- Creating a timing interval for a business process

To enable process owners to analyze the amount of time that elapses between certain steps in a business process, you can add tracking points to the business process definition (BPD) and then create a timing interval to capture the duration between the defined start and end points.
- Disabling the emission of tracking data

By default, tracking data is emitted to the Performance Data Warehouse. If you do not use the Performance Data Warehouse you can disable the emission of all tracking data.