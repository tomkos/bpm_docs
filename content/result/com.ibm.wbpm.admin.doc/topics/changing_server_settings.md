# Changing server settings in the Process Admin Console

## About this task

During the life of an application in a runtime environment, some of the settings might change.
One example is the password, which usually expires after a set time. To avoid installing a new
snapshot every time you need to change a server property, use the Process Admin Console to edit the
server settings for a specific installed process application snapshot.

You can configure and change connection information in the designer. If you want to change the
server settings for active snapshots, edit the settings in the Process Admin Console. Changes there
are applied to the existing instances.

You must specify separate settings
for each server.

## Procedure

1. Log in to the Process Admin Console and
select Installed Apps.  You
see the list of installed snapshots.
2. Click the overflow menu of a snapshot and select App Details. Then
click the Servers tab.
3. Select a server from the list. The current
server settings are displayed.
4. Edit the settings that you want to change.
5. Click Apply or Cancel.

## What to do next

- Changing web service server settings

During development, you can add a web service server to a process application. However, with time the configuration values that are used at development time may change. You can change the configuration values of a web service server at run time to accommodate these new circumstances.
- Changing REST server settings

During development, process authors can define REST server settings for external services on the Servers tab for each process application. After a process application is installed on a workflow server in a different environment (for example, test, staging, or production), you might need to configure REST Server properties at run-time.
- Changing Enterprise Content Management server settings

You can edit Enterprise Content Management server settings for installed process application snapshots using the Process Admin Console.
- Enterprise Content Management configuration settings: technical details

There are two methods available to make a call to an Enterprise Content Management server, depending on the context from which the call is made. Understanding the details of how those calls are made will help you configure settings correctly and change the default settings if that action becomes necessary.
- Enabling or disabling event subscriptions

In the Process Admin Console, you can enable or disable event subscriptions for the default snapshot on a workflow server. However, you cannot enable or disable event subscriptions for other types of snapshots on a workflow server and you cannot enable or disable event subscriptions in Workflow Center.
- Changing IBM Case Manager server settings

You can edit IBM Case Manager server settings for installed process application snapshots using the Process Admin Console.
- Changing IBM ODM server settings

You can edit IBM® Operational Decision Manager server settings for installed process application snapshots using the Process Admin Console.