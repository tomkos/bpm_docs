# Case Analyzer OLAP integration
using IBM
Cognos Analytics

## Before you begin

## About this task

This task provides a high level view of the configuration
steps. Use the detailed instructions in the Case Analyzer documentation and the IBM
Cognos Analytics documentation to ensure
successful configuration.

## Procedure

To configure integration with Case Analyzer

1. Set up the OLAP integration by installing and configuring Case Analyzer. See Installing the Case Analyzer reporting tools.
2. Use the audit configuration wizard in the IBM Business Automation
Workflow
Case administration client to enable auditing of the desired
case and task properties.
3. Use the FileNet® Process
Task Manager to configure the Case Analyzer settings.
In the Content Platform Engine properties,
for the Object Store Name, enter the name of the IBM Business Automation
Workflow target object store.
For more information, see Configuring Case Analyzer components.
4. Move the report templates to the IBM
Cognos Analytics server, and use the IBM
Cognos Analytics administration console
to set up Case Analyzer reporting.
For more information, see Configure IBM
Cognos Analytics project
for Case Analyzer.