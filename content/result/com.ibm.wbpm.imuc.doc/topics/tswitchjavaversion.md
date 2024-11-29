# Switching the edition of Java used in Business Automation Workflow

## Before you begin

Before you use the managesdk command to switch Java editions,
read the WebSphere Application
Server topic managesdk command to ensure that you have met any preconditions for running
the command.

## About this task

Business Automation Workflow 24.x supports
only Java 8.

Java snippets, Java conditions, and Java expressions
in BPEL processes must use Java 6 syntax instead of Java 7 or Java
8 syntax.

## Procedure

To switch Java editions:

1. Run the managesdk -listAvailable command
to display a list of all SDK names in your environment, as described
in the managesdk command topic.  install\_root/bin/managesdk.sh -listAvailable

CWSDK1003I: Available SDKs:
CWSDK1005I: SDK name: 1.6\_64 
CWSDK1005I: SDK name: 1.8\_64
CWSDK1001I: Successfully performed the requested managesdk task. If
Java 8 is not installed, follow the instructions in Installing and uninstalling SDK Java Technology Edition
Version 8.0
2. To switch the Java edition that is used for the command-line
environment and all future profiles, run the following two commands:
 install\_root/bin/managesdk.sh -setCommandDefault -sdkName 1.8\_64
install\_root/bin/managesdk.sh -setNewProfileDefault -sdkName 1.8\_64 After
you run these commands, any new profiles that you create will use
Java 8.
3 If you want to switch the Java edition that is used for existing profiles,complete the following steps:
    1. Stop your deployment manager, cluster members, and all
node agents. Confirm that the deployment manager server
has stopped.
    2. Switch the SDK version for the deployment manager profile
by running the managesdk -enableProfile command
as shown in the following example:  install\_root/bin/managesdk.sh -enableProfile -profileName DmgrProfile -sdkName 1.8\_64
4 Switch the Java edition that is used for the node and clustermembers. Repeat this step for each managed node of the deploymentmanager.

1. Restart your deployment manager. For example,
run the following command:install\_root/bin/startManager.sh -profileName DmgrProfile
2. Synchronize the managed node by running the syncNode command.
The following snippet is an example of how to run the command:install\_root/bin/syncNode.sh dmgrHostName.ibm.com 8879 -profileName Node1Profile -user AdminUser -password AdminPasswordUse
the deployment manager host name and SOAP port number for your environment.
3. Run the managesdk -enableProfile command
from the bin directory of the Business Automation Workflow installation
that hosts the managed node. The following snippet is an
example of how to run the command:install\_root/bin/managesdk.sh -enableProfile -profileName Node1Profile -sdkName 1.8\_64 -user AdminUser -password AdminPassword -enableServers
4. Synchronize the managed node by running the syncNode command
again, for example: install\_root/bin/syncNode.sh dmgrHostName.ibm.com 8879 -profileName Node1Profile -user AdminUser -password AdminPasswordUse
the deployment manager host name and SOAP port number for your environment.
5. Validate the changes by running the managesdk -listEnabledProfileAll command
as shown in the following example:  install\_root/bin/managesdk.sh -listEnabledProfileAll
CWSDK1004I: Profile DmgrProfile :
CWSDK1006I: PROFILE\_COMMAND\_SDK = 1.8\_64
CWSDK1008I: Node MyCellManager01 SDK name: 1.8\_64
CWSDK1009I: Server dmgr SDK name: 1.8\_64

CWSDK1004I: Profile Node1Profile :
CWSDK1006I: PROFILE\_COMMAND\_SDK = 1.8\_64
CWSDK1008I: Node my-Node01 SDK name: 1.8\_64
CWSDK1009I: Server BPMDE.SingleCluster.Node01.0 SDK name: 1.8\_64
CWSDK1009I: Server nodeagent SDK name: 1.8\_64
CWSDK1001I: Successfully performed the requested managesdk task.
6 If you have an Oracle database, complete the followingsteps to update the Oracle JDBC providers with the appropriate OracleJDBC driver for the Java edition you switched to:

1. Open the WebSphere administrative console.
2. In the tree view, expand Resources > JDBC and then select JDBC providers.
The JDBC Providers panel opens.
3. In the JDBC Providers panel, click the link of the desired Oracle
JDBC provider to open the editing panel.
4 In the Class path text box, change thefollowing class path for the Oracle JDBC driver to the appropriateJAR file for the Java edition that you switched to: ${ORACLE\_JDBC\_DRIVER\_PATH}/jdbc\_driver\_jar Specifythe jdbc\_driver\_jar as listed:

```
${ORACLE\_JDBC\_DRIVER\_PATH}/jdbc\_driver\_jar
```

Specify
the jdbc\_driver\_jar as listed:

    - With Oracle 12cR2,
Java 8 is supported with the ojdbc8.jar or ojdbc10.jarJDBC
drivers. Before you can use this driver, you must apply the WebSphere Application
Server 8.5.5.12 interim fix PI86830.
5. Click Apply.
6. Repeat the previous three steps for each of the remaining Oracle
JDBC providers.
7. When you have updated the last remaining Oracle JDBC provider,
click Save to save the changes to the master
configuration.
8. Stop and restart your deployment manager.
7. Start your nodes and deployment environment again (in that
order).

## Related information

- managesdk command