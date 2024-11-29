# Monitoring workflow servers

Read the following sections to learn more.

- Capturing process instrumentation data

The Process Admin Console includes an Instrumentation monitor to help identify performance bottlenecks in Workflow Server and to capture instrumentation data that you can use to further analyze any performance issues.
- Traditional: Discovering and managing database performance issues by using the Performance Dashboard

 You can identify potential performance issues caused by large numbers of artifacts by viewing real-time and historical artifact counts in the Performance Dashboard. To help you manage these issues, the dashboard provides housekeeping tips for each artifact type. If the artifact is associated with a snapshot, you can generate the corresponding wsadmin commands to remove the snapshot from the database. For offline analysis, you can export the data in the dashboard to a spreadsheet.
- Traditional: Identifying resource issues by using the Performance Monitoring

 Traditional: 
 You can identify potential resource issues by monitoring the usage of resources such as CPU, heap, JDBC connections, and thread pools, displaying the real-time historical data, and then looking for a correlation with process instances and tasks. For offline analysis, you can export the data in the dashboard to a spreadsheet.
- Monitoring processes and services in the Process Admin Console

To identify performance issues with your process application, view the performance data available in the Process Monitor page of the Process Admin Console. Identify process applications that have bottlenecks, drill into the process application to identify the steps that are expensive, and learn how long it takes to run services.