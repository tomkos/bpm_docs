# Configuring the IBM Case Monitor Dashboard

## Procedure

To configure the IBM Case Monitor Dashboard:

1 Prepare the database for the Case Analyzer store. For more information, see Database administrator installation tasks .
    1. Create JDBC data sources. Run the Configure JDBC Data Sources task by using the IBM
FileNet® P8 Configuration Manager.
For more information, see Editing the Configure JDBC Data Sources tasks and Configuration Manager reference.
    2. Create a database connection.
For more information, see Creating a database connection. Based on performance
considerations, you might want to share data sources. For more information, see Sharing data sources. You enter the database schema name when
you configure and enable the Case Analyzer store by using
the IBM Business Automation
Workflow
Case administration client.
2 Create the Case Analyzer store: You can also create a Case Analyzer store by usingAdministration Console for Content PlatformEngine . However, the administration console provides manyoptions that are not used in IBM Business AutomationWorkflow .

1. Log in to the Case administration client.
2. Under the domain, expand Object Stores and click the target object store
in which you want to create the Case Analyzer store.
3. Click New Case Analyzer Store and enter
the information for the new store.

You can also create a Case Analyzer store by using
Administration Console for Content Platform
Engine. However, the administration console provides many
options that are not used in IBM Business Automation
Workflow.

3. Log in to the Case configuration tool and run the
Register the Case Monitor Widgets Package task to add the IBM Case Monitor Dashboard desktop to
IBM Content
Navigator: