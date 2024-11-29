# Installing IBM Business Automation
Workflow on AIX or Linux using
a typical installation and configuration path

The typical installation option is the simplest and quickest method
for installing and configuring IBM Business Automation
Workflow.

- Linux on Power LE does not support typical installation.
- The launchpad does not start in a Linux or AIX environment if you are using Firefox 45 or later.
See PortableApps.com Project on SourceForge to download portable
Firefox 44, or download an older version of Firefox from Mozilla's index
of Firefox releases.
- IBM Business Automation
Workflow Enterprise Service Bus does not support
typical installation.

## About this task

From the product launchpad, the typical installation process installs the
software, configures the deployment manager and managed-node profiles, and configures a
single-cluster deployment environment that consists of one node and one server. It also installs IBM WebSphere SDK Java Technology Edition 8 (Java 8).

| Database   | What is installed                                                                                                                                                                                                                   | Installation guide                                                                                         |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| None       | Installation Manager, Java 8, Db2 Standard Edition, WebSphere Application Server Network Deployment, Business Automation Workflow                                                                                                   | Installing and configuring IBM Business Automation Workflow with a new Db2 database server on Linux        |
| Db2        | Installation Manager, Java 8, WebSphere Application Server Network Deployment, Business Automation Workflow, connection to your Db2 database server according to your Launchpad input (database hostname, port, JDBC driver)        | Installing and configuring Business Automation Workflow with a Db2 database server on AIX or Linux         |
| Oracle     | Installation Manager, Java 8, WebSphere Application Server Network Deployment, Business Automation Workflow, connection to your Oracle database server according to your Launchpad input (database hostname, port, JDBC driver)     | Installing and configuring IBM Business Automation Workflow with an Oracle database server on AIX or Linux |
| SQL Server | Installation Manager, Java 8, WebSphere Application Server Network Deployment, Business Automation Workflow, connection to your SQL Server database server according to your Launchpad input (database hostname, port, JDBC driver) | Installing and configuring IBM Business Automation Workflow with an SQL Server database server on Linux    |

- Installing and configuring IBM Business Automation Workflow with a new Db2 database server

Using the typical installation option, you can install Db2® on Linux on Intel systems, and configure the required databases for IBM Business Automation Workflow. If you are installing on Linux for z or Linux on Power, use the instructions for installing onto and configuring an existing database. Select the typical installation only if you have administrative privileges (are a root user) and do not have an existing Db2 database server on the system.
- Installing and configuring IBM Business Automation Workflow with a Db2 database server

You can install IBM Business Automation Workflow using an existing IBM Db2 database server.
- Installing and configuring IBM Business Automation Workflow with an Oracle database server

You can install IBM Business Automation Workflow using an Oracle database server.
- Installing and configuring IBM Business Automation Workflow with an SQL Server database server

You can install IBM Business Automation Workflow using a Microsoft SQL Server database server.