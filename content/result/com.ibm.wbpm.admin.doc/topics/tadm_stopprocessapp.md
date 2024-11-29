# Deactivating and stopping installed process applications

## About this task

Deactivating a snapshot allows all existing process instances to complete, but no new process
instances can be started.

You cannot deactivate the default snapshot if you have more than one snapshot of a process
application installed on the server. In this case, you must first designate another snapshot as the
default version. You can deactivate the snapshot only when it is no longer the default version. If
the default snapshot is the only snapshot installed on the server, you can deactivate it with no
further action. However, Business Automation Workflow administrators can
deactivate the only Process Portal default snapshot
(SYSRP) application from the Process Admin Console. Deactivating the
SYSRP application causes artifacts inside SYSRP to be deactivated also. For example, the
Work dashboard disappears from Process Portal if no other SYSRP
snapshot is activated.

- If your process application uses a BPEL process as the main entry component, you must stop the
corresponding BPEL template in the WebSphere administrative console. See Administering BPEL
process and task templates.
- Additionally, if this BPEL process invokes a process, you must allow any existing instances to
complete after you stop the template but before you deactivate the snapshot. See Administering
BPEL process and task templates.
- In all cases, you must clean up the associated process instance data from the Business Process
Choreographer database, as described in Cleanup procedures for Business Process
Choreographer.

## Procedure

1. From the Process Admin Console Installed Apps
page, select the installed snapshot.
2. Deactivate the snapshot by clicking Deactivate
Application.
3. If the snapshot contains advanced content, stop it by clicking Stop
Application.

- Whether process instances run in deactivated snapshots

If you deactivate a snapshot, starting new process instances and progressing existing instances might be impacted.