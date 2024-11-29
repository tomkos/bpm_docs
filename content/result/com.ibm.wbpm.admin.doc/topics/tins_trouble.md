# Troubleshooting installation and configuration

## Procedure

1. Read any error messages from the installation process.

 See the following topic for an explanation: Messages and known issues during installation and profile creation. If the message
corresponds to any of those described, correct the problem, clean up any installed portions, and try
to reinstall.
2. If you have successfully created a server profile, use the Quick Start console or the
command-line method to start the server.
3 Verify that the server starts and loads properly by looking for a running Java™ process and the Open for e-business message in theSystemOut.log and SystemErr.log files. If no Java process exists or if the message is notdisplayed, examine the same logs for any miscellaneous errors. Correct any errors and try again. You can find the SystemOut.log and SystemErr.log filesin the following platform-specific directories:

If no Java process exists or if the message is not
displayed, examine the same logs for any miscellaneous errors. Correct any errors and try again.

    - On Linux® and UNIX
platforms:
profile\_root/logs/servername
    - On Windows platforms:
profile\_root\logs\servername
4. Use the Quick Start console or the command-line method to stop the server, if it is
running.
5. If you want to use a Snoop Servlet
to verify the ability of the web server to retrieve an application from IBM Business Automation Workflow, see Default Application in the WebSphere® Application Server Network Deployment documentation.
6. Start the administrative console.

## What to do next

On the product support web site, you can review current
information about resolutions to known problems, and you can read
documents that can save you time gathering the information that you
need to resolve a problem. Before opening a PMR, see the IBM Business Automation Workflow support page.

- Case configuration tasks fail when the external Content Platform Engine is used with existing IBM Case Manager object stores

When you run the Define the Default Project Area case configuration task for the Development environment or the Define Target Environment case configuration task for the production environment, the task fails.
- Messages and known issues during installation and profile creation

Some of the most commonly found error messages encountered when installing and configuring can be addressed with actions that resolve the underlying problems.
- Installation and profile creation log files

Various log files are created during installation and uninstallation of IBM Business Automation Workflow and during profile creation, augmentation, and deletion. Consult the applicable logs if problems occur during these procedures.
- Launching Installation Manager directly on 64-bit systems

You can launch Installation Manager directly, for IBM Business Automation Workflow on 64-bit systems.
- Warnings about GTK or ulimit on Linux or UNIX when installing or migrating

On the Linux or UNIX operating system, when you are installing or migrating, you might see a warning about 32-bit GTK libraries or increasing your ulimit.
- Resolving licensing issues when only a deployment manager is created on a machine

If IBM Business Automation Workflow is installed on a machine and only a deployment manager node is created, the IBM License Metric Tool (ILMT) will count the Business Automation Workflow processor value units (PVU). This happens because the licensing inventory software has no way to distinguish between a Business Automation Workflow deployment manager installation and a Business Automation Workflow node installation.
- Troubleshooting problems creating database tables

While trying to create database tables for the Business Process Manager database and the Performance Data Warehouse database, you might get errors or exceptions that prevent you from creating the tables. Your bootstrap operation also fails.
- Troubleshooting Oracle transaction recovery messages

You must apply special grants for Oracle transaction recovery to work correctly.
- Error running bootstrap command or creating profiles with SQL Server databases

If you are using Microsoft SQL Server databases, and you create the BPMDB or PDWDB databases with a case-sensitive collation attribute, then when you use the bootstrapProcessServerData command to load the databases with configuration data, you will get an error. If you are using PMT or manageProfiles create the profile, the profile will be created with partial success, and the profile log file will indicate failure running bootstrapProcessServer.ant.
- Problems testing a connection to a data source in a network deployment

In a network deployment environment, testing a connection to the cell-level jdbc/WPSDB data source can fail, with the error message UndefinedVariableException: Undefined Variable variable\_name, where variable\_name is a variable name such as WAS\_INSTALL\_ROOT, DB2\_JCC\_DRIVER\_PATH,  ORACLE\_JDBC\_DRIVER\_PATH, UNIVERSAL\_JDBC\_DRIVER\_PATH or PUREQUERY\_PATH. However, this does not necessarily indicate that you will have run time errors.
- Troubleshooting the launchpad application or Quick Start

If the launchpad application or Quick Start does not start, try the following troubleshooting tips.
- Diagnosing a failing Ant configuration script

Determine whether a product installation problem on an operating system is caused by a failing Apache Ant configuration script.
- DB2 log file error: SQL1092N "USERID does not have the authority to perform the requested command or operation"

After you install IBM Db2® Standard Edition, if you use the domain user ID to create a new database and tables, you might see an error in the DB2 log files. Follow these steps to enable the domain user ID to access the database.
- Profile creation failure due to insufficient free space

If you experience a system crash or an exception while attempting to create profiles, it may be caused by insufficient free space in the temporary directory.
- Recovering from profile creation failure after using the BPMConfig command

If the profile creation step fails after running theBPMConfig command, you need to delete the profiles and drop the databases that you created.
- Successful installation reported after profile creation failure

If the profile creation step fails during a custom installation, the failure is not recognized by Installation Manager, which reports a successful installation. This problem occurs only on Windows platforms.
- Recovering from profile creation or augmentation failure

The Profile Management Tool can experience failures when creating new or when augmenting existing profiles. The same can occur using the manageprofiles command-line utility. If such a failure occurs, first check the log files as described in this topic, then follow the recovery instructions described, depending on the situation.
- Cluster member startup timeout errors reported in deployment manager log

If the deployment environment startup takes longer than the default timeout setting, you will see an exception in the deployment manager log. Provided the cluster members eventually start, you can ignore the exception.
- Reinstallation cannot create new profile when using the Typical installation and configuration option

If you try to reinstall the product to the same location using the Typical installation and configuration option, or if you try to reinstall after a failed uninstall, the installation might fail because a new profile cannot be created.
- Resolving a DB2 process load issue

You can encounter unexpected process load issues when running DB2
- Uninstalling multiple server and tooling products causes errors

Uninstalling multiple products (for example, IBM Business Automation Workflow and IBM Integration Designer) at the same time might cause Installation Manager errors or warnings.
- Installing a snapshot fails when single sign-on has been configured

Installing a snapshot from IBM Workflow Center to IBM Workflow Server can fail if single sign-on has been configured.
- Installing a snapshot fails after message confirms installation

Installing a snapshot on IBM Workflow Center has a message that confirms the snapshot is installed and then moments later issues a message claiming the installation failed.
- Quick Start shortcut missing from Start Programs menu after successful installation of IBM BPM on Windows Server 2012 or Windows 8

After the successful installation of IBM Business Process Manager on Microsoft Windows Server 2012 or Windows 8, when you click Start > Programs > IBM > deployment\_environment\_name, the Quick Start shortcut might be missing from the displayed menu. Other user-specific shortcuts, such as the profile shortcuts, might be missing also.
- Deployment environment is missing in the WebSphere administrative console on Linux

After installing IBM BPM on Linux and creating the deployment environment with the BPMConfig command, there is no deployment environment listed in the Servers > Deployment Environments panel of the WebSphere administrative console.
- Heritage Process Portal or dashboard theme fails to load

If you open Heritage Process Portal (deprecated) or a dashboard and it is not displaying correctly, its theme might not have loaded properly.
- Error displaying embedded IBM Content Navigator window in coach

If you are using IBM Business Automation Workflow V19.0.0.3 or V20.0.0.1 with embedded IBM Content Navigator topology, when you embed an IBM Content Navigator window into a coach using a custom HTML iFrame, an error message appears.
- setBPMExternalECM command fails

When you configure IBM Business Automation Workflow with the AdminTask.setBPMExternalECM command, you might see the following error: CWMCB0195E: The source file of the copy operation does not exist.
- NPE exceptions when loading IBM Content Navigator client jars

When you stop the workflow environment with embedded IBM Content Navigator, you might see the following exception in the SystemOut.log  of workflow application cluster member server. You can safely ignore this exception. When the IBM Content Navigator application is stopped, it starts applicationTerminate for all plug-ins, including workflow plug-ins. This error can be ignored as no applicationTerminate function is defined in workflow plug-ins.