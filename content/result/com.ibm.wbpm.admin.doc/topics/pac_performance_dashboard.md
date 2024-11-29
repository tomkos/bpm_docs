# Traditional: Discovering and managing database performance issues by using the Performance
Dashboard

## Before you begin

- To view the dashboard, you must be member of the PerformanceAdmins
team. For more information, see Business Automation Workflow security roles.
- To include database configuration and meta information in exporteddata, you must have the following database access rights:
    - DB2: select privilege on the DBCFG administrative view, SYSCAT.TABLES
catalog view, and SYSCAT.INDEXES catalog view.
    - Oracle: SELECT permission on the V$SYSTEM\_PARAMETER view
    - SQL Server
        - The VIEW DATABASE STATE permission
        - Select permission on the following system catalog views: sys.configurations, sys.stats, sys.tables, sys.objects,
sys.schemas, sys.index\_columns, sys.indexes, sys.sysindexes, sys.dm\_db\_partition\_stats
        - Permission to view metadata for all BPM tables and BPM indexes

## About this task

It also includes data about
the Process Portal index, such as the number of
updated indexes and the index table rows that you can clean up. For more information, see Cleaning up index tables.

## Procedure

1. Log in to the Process Admin Console.
2. In the side menu of the console, click Performance > Performance Dashboard.
3 Load data into the dashboard. For performancesreasons, when you open the dashboard, it does not contain any data.To display the artifact types and a snapshot of their counts, click LoadData . None of the data is automatically refreshed duringthe session. To load an updated database snapshot, click Refresh .

For performances
reasons, when you open the dashboard, it does not contain any data.
To display the artifact types and a snapshot of their counts, click Load
Data. None of the data is automatically refreshed during
the session. To load an updated database snapshot, click Refresh.

    1. View housekeeping tips. Housekeeping tips
are provided for all artifact types. If you cannot use the generated
wsadmin commands to delete the snapshot associated with an artifact,
follow the links for alternative methods for purging the artifacts.
    2. Generate wsadmin commands. For artifacts
that are associated with a snapshot, you can generate the wsadmin
commands to delete the snapshot from the database. Separate commands
are generated for Workflow Center and Workflow Server.Note: You
cannot run the commands directly from the Performance Dashboard. Instead,
copy the generated commands and run them in the wsadmin scripting
client.
    3. Export data to a .csv file or to a Microsoft Excel file.
The file contains all the data that is shown in the dashboard.
Historical data for the last 100 days is also included. If you have
database access rights, the spreadsheet also includes database meta
information, such as when the statistics were last gathered for the
BPM tables, and general database configuration parameters.