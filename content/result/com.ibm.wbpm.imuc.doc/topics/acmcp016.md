# Integrating with Case Analyzer to
create Microsoft Excel
reports

## Before you begin

## About this task

This task provides a high-level view of the configuration
steps. Use the detailed instructions in the Case Analyzer documentation to ensure
successful configuration.

## Procedure

To configure integration with Case Analyzer so that you can create Microsoft Excel reports:

1. Set up the OLAP integration by installing and configuring Case Analyzer.
2. Use the audit configuration wizard in the IBM® Business Automation
Workflow
Case administration client to enable auditing of the desired
case and task properties.
3. Use the FileNet® Process
Task Manager to configure the Case Analyzer settings.
In the Content Platform Engine properties,
for the Object Store Name, enter the name of the IBM Business Automation
Workflow target object store.
For more information, see Configuring Case Analyzer components.
4. Install the Case Analyzer
client.
The client system must have Microsoft Excel and Microsoft SQL Server software installed. You can choose to
install the client with the Case Analyzer installation. For more
information, see Installing Case Analyzer.
5. Use the tasks in the IBM Case Analyzer user guide to configure,
create, use, and publish your reports.
During the configuration,
you must also configure access to the Case Analyzer OLAP database. For more
information, see Configuring Excel Reports for Case Analyzer.