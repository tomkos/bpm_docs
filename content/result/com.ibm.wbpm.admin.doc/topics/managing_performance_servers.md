# Managing Business Performance Data Warehouses

Use the Performance Admin Console to work with Performance Data Warehouse queues, manage data
transfer errors, and monitor overall performance. To access the Performance Data
Warehouse, the user must have administrator access. The same access applies to users of the
Performance Admin Console. See Administrative security roles.

## Accessing the Performance Data Warehouse

- Point your web browser to http://[host\_name]:[port]/PerformanceAdmin, providing
the name of the host where the Performance Data Warehouse is installed and the port designated for
the Performance Data Warehouse during Business Automation Workflow
installation.
- If you are working on a Windows host where the Performance Data Warehouse is installed, click Start > IBM Business Automation Workflow > Performance Admin Console .

Log in to the Performance Admin Console with the administrator account and password that was
specified on the Administrative Security page during Business Automation Workflow profile creation.

## Granting access to other users or groups

1. Log in to the administrative console as the primary administrative user.
2. Click Applications > Application Types > WebSphere enterprise applications  > IBM\_BPM\_PerformanceDW\_bpmNode\_server > Security role to user/group mapping.
3. Select the row for the twuser role and click Map
Users or Map Groups.
4. Map the user or group to the twuser role, and click OK.
5. Restart the server.

If
you have configured an endpoint service such as IBM Security Access
Manager WebSEAL, a PerformanceAdmin user must
be authenticated also through WebSEAL in order for the instrumentation page to load properly.

- Viewing and managing Performance Data Warehouse queues

 Traditional: 
As part of Business Automation Workflow maintenance, you might need to view the Performance Data Warehouse load queue to determine which records have yet to be loaded to the database. You might also need to view the error queue to determine whether any errors occurred while data was being loaded from the workflow server to the Performance Data Warehouse.
- Viewing and managing data transfer errors

 Traditional: 
The View Errors page in the Performance Admin Console shows all errors resulting from data transfer between the Workflow Server and Performance Data Warehouse.
- Viewing Performance Data Warehouse statistics

 Traditional: 
The Performance Admin console includes a View Statistics page that you can use to see the number of rows in the tables and views in the Performance Data Warehouse.
- Monitoring the Performance Data Warehouse

 Traditional: 
To assess overall performance, you can view statistics (such as duration) for data transfer and other functions that are run in the Performance Data Warehouse. Use the View Instrumentation page to help identify performance bottlenecks to capture instrumentation data for further analysis.
- Using the Performance Data Warehouse command-line tool (perfDWTool)

 Traditional: 
To ensure that performance databases are performing optimally, use perfDWTool. For example, you can purge records that are no longer needed.
- Disable automatic schema management

 Traditional: 
Use the <automatic-schema-management> configuration property to control automatic schema management for the Performance Data Warehouse.