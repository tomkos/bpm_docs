# Removing a managed node profile from a deployment environment

## Before you begin

## Procedure

1. Stop the deployment manager and all the running server
processes in the managed node, including the node agent process.
2. On the deployment manager, run the following command to
remove the cluster members from the Business Automation Workflow deployment
environment:  BPMConfig -delete -profile dmgr\_profile\_name -de de\_name -node node\_name Running this command does not delete the node. It helps ensure that REST endpoints and JMS
connection factory provider endpoints that refer to the cluster members are updated. For more
information about the command, see BPMConfig -delete.
3. Restart the deployment manager.
4 On the managed node machine, run the following command: manageprofiles -delete -profileName node\_profile\_name By default, a prompt for the credentials to connect to the running deployment manager is displayed.This prompt times out after 1 minute and there are no manageprofiles parametersto specify the credentials on the command line. To avoid the prompt, set the following properties innode\_profile /properties/soap.client.props : Running this command deletes all servers that are not Business Automation Workflow servers, including webservers, and all application module mappings that refer to those servers. It also deletes the nodeitself from the WebSphere® ApplicationServer cell.

```
manageprofiles -delete -profileName node\_profile\_name
```

    - com.ibm.SOAP.loginUserid=admin\_user
    - com.ibm.SOAP.loginPassword=admin\_password

Running this command deletes all servers that are not Business Automation Workflow servers, including web
servers, and all application module mappings that refer to those servers. It also deletes the node
itself from the WebSphere® Application
Server
cell.

5. Optional: If the removed node hosted a web
server, you must update the web server plugin.  For instructions,
see the Plug-ins configuration documentation.
6. Optional: Manually remove any virtual host
aliases that are no longer needed. In the administrative
console, go to Environment > Virtual hosts > default\_host > Host Aliases and delete aliases
that you no longer need.
7 Optional: If you have errors, complete themanaged node removal by running the cleanupNode commandand removing references from the registry.

- If the manageprofiles command fails to connect
to the deployment manager, the following message is displayed: INSTCONFPARTIALSUCCESS:
The profile no longer exists, but errors occurred. The node\_profile/logs/\_nodeuninst.log file
contains the following error: ADMU0040E: Exception on MBean
invocation WebSphere:name=AdminOperations,process=dmgr.
- If the deployment manager was not running at all, the following
message is displayed: INSTCONFSUCCESS: Success: The profile
no longer exists. The node\_profile/logs/\_nodeuninst.log file
contains the following error: ADMU0006E: Exception creating
Deployment Manager connection.

1. Confirm that the deployment manager is running, then run the following command on the
deployment manager to complete the managed node
removal: cleanupNode node\_name -profileName dmgr\_profile\_name -username admin\_user -password admin\_password
For more information, see cleanupNode command.
2 On the computer where the node was deleted, run the following command to removereferences in the registry to deleted profiles:
    - ./manageprofiles.sh -validateAndUpdateRegistry
    - manageprofiles.bat -validateAndUpdateRegistry
8. Remove the managed node profile directory manually by using operating system
commands. The manageprofiles command does not entirely remove the
directory because it still contains log files.
9 Clean up the no longer existing node from the EventManager > Monitor panel by deleting the corresponding line from theLSW\_EM\_INSTANCE (at BPMDB) table. For more information, see Understanding and Tuning the Event Manager . Note: All schedulers that have ever run, are listed in lsw\_em\_instance and areshown on the Event Manager monitor page. If a scheduler is disabled, it updatesor inserts its row at start, so that Event Manager monitor users recognize that the machine isthere, but the scheduler is disabled. The difference between disconnected ,disabled , and paused is only visible by moving your mouse over thered light that is associated with the scheduler instance on the Event Managermonitor page. If a particular machine no longer exists, and you do not want to see it onthe Event Manager monitor page anymore, you can carefully remove its row fromthe lsw\_em\_instance table. The row is recreated when a machine with that namestarts up again.

1. Login to Process Admin Console and select
Event Manager > Monitor. Look at the Scheduler ID column and note the name of
the Scheduler that is associated with the deleted node.
2. At Database layer, back up the LSW\_EM\_INSTANCE table.
3. Delete the row with the following SQL statement: 
db2 "DELETE <schema>.LSW\_EM\_INSTANCE WHERE NAME='<Scheduler\_name>'

For more information, see Understanding and Tuning the Event Manager.