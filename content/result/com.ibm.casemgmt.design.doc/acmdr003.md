# Administering your case management system

- Restarting components in a single-server environment

Server maintenance and software updates sometimes require a server reboot. You must manually restart the components in your Business Automation Workflow environment on an AIX® or Linux® server. On a Windows server, the components restart automatically.
- Starting and shutting down the system

Restart or shutdown your system for server maintenance or software updates.
- Setting up project areas

Project areas are used to limit the effects of resetting the test environment. This helps other users who work on other projects in the same development environment.
- Adding a case with a second project area user

To add a case with a second project area user in the Case Client, you must create JDBC data sources.
- Setting up target environments

Setting up the target environment includes creating the target object store, creating a workflow system, and running tasks in the Case configuration tool or Case administration client to define and register the target environment. Depending on the solutions that you plan to deploy in the target environment, you might need to run additional configuration tasks.
- Enabling and disabling plug-ins for the IBM Business Automation Workflow desktop

IBM® Business Automation Workflow loads selected plug-ins by default for the IBM Business Automation Workflow desktop and IBM Business Automation Workflow Case administration desktop. You can configure these desktops in the IBM Content Navigator administration desktop to change the plug-ins that are available for the desktop.
- Enabling favorites and sync

Users can create favorites to quickly find the items that they work with frequently. When a user creates a favorite, they can optionally choose to sync the item to their workstation or device so that they always have the latest version of the document available. To enable these features, you must install a sync client and configure settings in the IBM Content Navigator administration desktop.
- Preparing a database for the case history store

If you plan to use the Timeline Visualizer widget to view case history over time, you must prepare a database to record extended case history data.
- Enabling tracing

To enable tracing for the Case Analyzer and Case History components in Business Automation Workflow, install and use the vwtool, which is part of Content Platform Engine Tools.
- Configuring or disabling the Activity Sweep Custom policy

Every three hundred seconds (five minutes), the SweepHandler, initiated by the Activity Sweep Custom policy, checks the status of currently working processes and case activities.
- Enabling or disabling case health analysis

When the case health analysis feature is installed in IBM Business Automation Workflow, you can choose to enable or disable it as required.
- Monitoring system performance

Monitor the performance of IBM Business Automation Workflow by using IBM System Dashboard for Enterprise Content Management.
- Backing up your system

It is a best practice to periodically back up the IBM Business Automation Workflow system so that you can more rapidly recover from the loss of data.
- Restoring your system

You can restore your Business Automation Workflow system by using your latest backups. Work with your backup administrator to understand the backup policy and the best way to perform the restore.
- Updating the Content Platform Engine client connector files

If you are using an external Content Platform Engine, every time you update the version of the external Content Platform Engine, you must run the updateBPMExternalECM command to download the Content Platform Engine libraries on the workflow server.
- Storage area types

A storage area is a place where the Content Platform Engine stores content.
- Configuring a file store for an existing object store

This example shows you how to configure a file store for an existing object store by using a file system path or a mount path.
- Modifying an existing configuration

You can modify an existing configuration profile to change the profile property values or the property values of a task in the profile. For example, you can edit the task properties to correct errors that were found when you ran a task.
- Updating an object store

You can update a design object store or target object store with IBM Business Automation Workflow releases. You can also update an object store to fix problems, such as to re-create any required IBM Business Automation Workflow folders that were accidentally deleted.
- Synchronizing cases with solution data

If you modify a solution after it is deployed, run the case synchronizer utility to update existing instances to match the changes that you made. You can run the utility by using commands or the Case Manager REST protocol.
- Enabling the Browse view in the IBM Business Automation Workflow desktop

If you enabled the IBM Business Automation Workflow plug-in and want users to be able to launch processes from the IBM Business Automation Workflow desktop, you must configure the desktop to display the Browse view.
- Enabling access to case solutions in the IBM Content Navigator desktop with Cases feature

You can use the IBM Content Navigator Cases feature to select the solutions that can be accessed from a desktop.
- Configuring your environment to show display names in Case Client

When you run the Business Automation Workflow environment with an external IBM Content Navigator, you can configure your environment to support by using the LDAP display name for users in widgets and search results in Case Client.
- Customizing the case package PDF file

You can customize the appearance of the PDF file that is included in a case package. For example, you can change the fonts or include a company logo.
- Tuning case management

Reviewing the case management tuning information can help you improve and maintain the performance of the case management features.