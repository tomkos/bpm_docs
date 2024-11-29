# Creating and using an emergency repair system

## About this task

To be prepared for setting up an emergency repair system
quickly, you can create the configuration properties file in advance
and define a target system and server. Do not create the server, however,
because servers require active maintenance even if they are not used.
This strategy enables quick setup in case of an emergency without
additional ongoing maintenance.

Use the emergency repair system
only to get the system into a state in which the other servers can
be restarted. The emergency repair system does not create work or
process already-started work. It does not drive or change transactional
recovery or peer recovery, which are handled by other parts of the
system.

<!-- image -->

- This cell has one deployment manager and two custom nodes.
- This cell has a three-cluster deployment environment.
- As is true for all cells, the business process definition (BPD)
engine runs in the application cluster and uses tables in the Business Automation Workflow database
(BPMDB) for process data. The Event Manager and Process Admin Console
are also in the application cluster.
- Incoming HTTP and HTTPS requests are routed through an HTTP server.
The HTTP server knows the endpoints and context roots of the deployed
web modules (such as the Process Admin Console) because of the generated plugin-cfg.xml file.
- JVMs that can use peer recovery are configured to store their
transaction logs on a shared file system.  Each cluster member has
access to the transaction logs of the other cluster members.

<!-- image -->

- Only one member of the application cluster is running. No support
cluster or messaging engine cluster members are running.
- No Event Manager is running.
- Incoming HTTP and HTTPS requests are not routed to the emergency
repair system. Administrators can access the Process Admin Console
directly by using the host:port of the cluster member.
- The transaction log locations are not configured in the emergency
repair system to prevent it from attempting peer recovery.

## Procedure

To create and start an emergency repair system, complete
the following steps:

1. Create and federate a node.
2 Create a member of the application cluster.
    1. To configure the server as an emergency repair server, create
an XML file and name it 120ERS.xml or 120EmergencyRepairMode.xml.
The file must contain the following text:<?xml version="1.0" encoding="UTF-8" ?>
  <properties>
    <!-- Properties to start a system into emergency repair mode -->
    <common merge="mergeChildren">
      <ers-mode merge="replace">true</ers-mode>
    </common>
    <event-manager>
      <scheduler>
        <start-paused merge="replace">true</start-paused>
      </scheduler>
    </event-manager>
  </properties>
    2. Copy the XML file into the config directory
of the repair node on the deployment manager in the same directory
as the 100Custom.xml file. The settings are replicated
from the deployment manager server to the repair node when the node
is started.
3 To start the emergency repair system, start the clustermember. Important:

- Do not start the emergency repair system when the other IBM® Business Automation Workflow servers
are running.
- To prevent the application cluster from attempting peer recovery,
do not configure the transaction log locations for the application
cluster.
- Point the browser directly to the endpoint of the cluster member.
Ensure that the emergency repair system cannot be reached from the
HTTP server.
4. To verify that you successfully created an emergency repair
system, log on to the           Process Admin Console of the cluster
member. The main page shows the following text:             This
system is configured as an emergency repair system.

## Results

The ers-mode parameter limits the commands
and user interfaces that are available to the emergency repair server.

- In the Process Inspector area, all functions
are available.
- In the Server Admin area, the followingfunctions are available:
    - IBM BPM > Task Cleanup
    - Event Manager > Blackout
Periods
    - Event Manager > Synchronous
Queues
    - Admin Tools > Manage
EPVs
    - Alert Definitions >  Process
Instance Alerts
    - Alert Definitions > Task
Alerts
- In the Installed Apps area, the overviewpage is available. The following actions are available: The following tabs are available:

- Activate Application
- Deactivate Application
- Make Default Version

- Exposing
- Servers
- Environment Vars
- Event Subscriptions

- BPMActivate command
- BPMDeactivate command
- BPMGetSnapshotAcronym command
- BPMListProcessApplications command
- BPMProcessInstancesCleanup command
- BPMTasksCleanup wsadmin command

## What to do next

After you complete the repairs, shut down the emergency
repair system. The emergency repair system must not be running when
the other Business Automation Workflow servers
are running.