# Integrating with Case Analyzer

## About this task

For reporting on cases and tasks that are currently active, Case Analyzer provides Cases In Progress
and Tasks In Progress cubes. The Cases In Progress cube has metrics for case-related details, such
as the current case count and the average age of cases. Tasks in Progress metrics can provide
details such as current task count, wait time, processing time, and task age.

For historical reporting and analysis, the Case Analyzer provides Case Load and
Task Load cubes. Case Load metrics can provide details, such as outgoing
and incoming case numbers and average completion time for the various
time periods. Task Load metrics provide details such as incoming and
outgoing task numbers, and average wait time, ready time, processing
time, and completion time for the various time periods.

To use
the values of case, task, and workflow data fields in case analytic
reports, you must identify which data fields will be exposed, specify
their properties as dimensions or measures, and specify the appropriate
OLAP cube to store the data. The values for  case, task, and workflow
data fields, which come from the Content Platform Engine and the workflow system,
are stored in the Case Analyzer database.

- Microsoft Excel reports
available when you install the Case Analyzer client
- Reports in the IBM®
Cognos® Analytics console.

To view business activity data that is specific to case management, you can use the IBM Case
Monitor dashboard. For more information, see Integrating with the IBM Case Monitor Dashboard.

- Administering the Case Analyzer store

You can use Case Analyzer tools to administer the Case Analyzer store. This is done by using the Case Analyzer Process Task Manager and Case Analyzer compression tools.
- Installing the Case Analyzer reporting tools

You can use Case Analyzer reporting tools to work with reporting components like Case Analyzer SSAS OLAP  service and sample reports for Cognos and Excel of a Case Analyzer store. The default installation of these tools supports Microsoft SQL Server version up to 2016. If you are using the latest versions of Microsoft SQL server, you can manually copy the required contents from MSSQL\_2017\_2019\_2022 folder into the installation folder or run upgrade\_reporting\_tools.bat batch script to copy these files automatically according to the steps described in the readme.txt.
- Enabling Case Analyzer to update completed cases

By default, Case Analyzer ignores the updated case events that are generated after a case is completed. You can enable Case Analyzer to process the updates.
- Case Analyzer OLAP integration using IBM Cognos Analytics

The IBM Cognos Analytics integration can provide historical analytics for case trends and patterns. For example, you can get data on the average time to complete cases or business tasks during a specific time interval. You can also find the number of cases that were created, that are currently active, or that are complete during a specific time interval.
- Integrating with Case Analyzer to create Microsoft Excel reports

The client software provided with Case Analyzer provides Microsoft Excel reporting. After you install and configure the Case Analyzer client, you can customize the reports and publish them to the web.