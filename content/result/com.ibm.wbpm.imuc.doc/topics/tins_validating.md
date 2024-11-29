# Validating your environment

- Verifying the status of your environment using the Health Center

After you have finished installing IBM Business Process Manager or at any time thereafter, you can use the Component Health Center in the administrative console to check the status of the configured components in your deployment environment. Examples of configured components include IBM Workflow Server, IBM Workflow Center, and Performance Data Warehouse.
- Verifying the status of your environment using the BPMConfig command

After you have finished installing Business Automation Workflow or at any time thereafter, you can use the BPMConfig command-line utility to generate a status report for the configured components in your deployment environment. Examples of configured components include IBM Workflow Server, Workflow Center, and Performance Data Warehouse.
- Using the BPMConfig command to export database information for performance analysis

You can use the BPMConfig command to export database information for performance analysis. The exported information is obtained from the databases for IBM Workflow Server and Performance Data Warehouse (PDW), which reside on machines in your deployment environment that are running DB2, Oracle, or SQL Server. The exported information includes a variety of statistics, such as statistics relating to database version, buffer pools, tables, and table spaces.
- Using the BPMConfig command to export system data for performance analysis

You can use the BPMConfig command to export system data for performance analysis. The exported system data is obtained from all node machines and database machines that are running in a specified Business Automation Workflow deployment environment. The exported data includes a variety of statistics, such as the operating system level, virtual memory statistics, CPU states, running processes, and storage input and output statistics.
- Capturing metrics for monitoring concurrent users and activities

You can capture metrics to monitor usage for the IBM Business Automation Workflow Concurrent User license option. You can audit and report on concurrent users, and the number of Workflow and Content activities.