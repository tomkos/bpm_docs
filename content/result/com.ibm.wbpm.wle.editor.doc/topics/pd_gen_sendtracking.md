# Sending tracking definitions to Performance Data Warehouse

## Before you begin

## About this task

When developing on the Workflow Center server,
be sure to send definitions when you make changes. For process applications
deployed in runtime environments, snapshot any changes and deploy
the new snapshot to ensure that the data you want to collect is available
in the runtime environment.

The method of sending tracking definitions
varies depending on the type of server you are using.

| Server                                   | Description                                                                                                                                                                                                                                                                                                                                       | How to send tracking definitions                                                                                                                                                                                                |
|------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Workflow Center server                   | When you use autotracking, manually create or edit tracking groups, or perform any other task in the Designer in IBM Process Designer to capture performance data, you must send these tracking requirements to the Performance Data Warehouse if you plan to run your processes on the Workflow Center server to test data tracking and reports. | In Process Designer, click Update Tracking Definitions in the Overview page of the Process App Settings.                                                                                                                        |
| Workflow servers in runtime environments | When you deploy snapshots of process applications on workflow servers in runtime environments, all tracking definitions are automatically sent to the Performance Data Warehouse in the selected runtime environment. This ensures that your data is tracked as expected when instances of your processes are run in the runtime environment.     | There is no need to send tracking definitions unless a problem occurs during snapshot deployment. If a problem does occur, you can select the Update Tracking Definitions option for the snapshot in the Process Admin Console. |

## Results

When you send tracking definitions, either directly or
as part of a snapshot deployment, the Performance
Data Warehouse establishes the structure in its database to hold the
data that is generated by the workflow server when you run instances
of your processes. These tracking requirements are called definitions
because they establish the database schema in the Performance
Data Warehouse to accommodate the tracked data generated by the process
server.