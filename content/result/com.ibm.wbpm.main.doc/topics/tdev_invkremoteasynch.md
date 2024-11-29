<!-- image -->

# Configuring servers to invoke services asynchronously

## Before you begin

## About this task

## Procedure

1 Collect information about each server involved in the communication. For the purpose of thistask, Figure 1 contains theinformation to use in the configuration: Figure 1. Invoking a service on a different system Note: For simplicity, only the servers involved in this communication ineach cell is shown and each server resides on a different physical machine. However, theconfiguration for cross-cluster asynchronous invocation can apply for the configuration in the samecell too. Draft comment: lesnider Added "However, the configuration for cross-clusterasynchronous invocation can apply for the configuration in the same cell too." for APAR280613. You need the following information for both the originator and targetservers:

Figure 1. Invoking a service on a different system

<!-- image -->

    - Host IP address
    - Cell
    - Node
    - Server
    - Bus name
    - Messaging engine
    - Failed Event Queue name
2. Install the applications.
3. Create a foreign bus on each server pointing to the other server and set the routing definition
type to Direct, service integration bus link.

For more information, see Connecting service integration buses to use point-to-point messaging.
From the example, the configuration of the foreign bus and SIB mediation link on System A
isName of Service integration bus to connect to (the foreign bus): 
SCA.SYSTEM.ABCNode01Cell.Bus
Gateway messaging engine in the foreign bus: 
ABCNode01.server1-SCA.SYSTEM.ABCNode01Cell.Bus
Service integration bus link name: TestCrossCell
Bootstrap service integration bus provider endpoints: 
9.26.237.144:7277:BootstrapBasicMessaging
The configuration of the foreign bus and SIB mediation link on System B
isName of Service integration bus to connect to (the foreign bus): 
SCA.SYSTEM.WBINode01Cell.Bus
Gateway messaging engine in the foreign bus: 
WPSNode.server1-SCA.SYSTEM.WBINode01Cell.Bus
Service integration bus link name: TestCrossCell
Bootstrap service integration bus provider endpoints: 
9.26.237.118:7276:BootstrapBasicMessaging

Attention: The port number in the bootstrap is the SIB endpoint address port. If you
enabled security, you must use the secure SIB endpoint address port.
4. Synchronize the SIB mediation links by restarting the servers.

You should see messages that are similar to these messages:
[9/25/09 8:04:23:406 CDT] 00000034 SibMessage I [:] CWSIT0032I:
The service integration bus link TestCrossCell from messaging engine 
WPSNode01.server1-SCA.SYSTEM.WPSNode01Cell.Bus in bus SCA.SYSTEM.WPSNode01Cell.Bus 
to messaging engine ABCNode01.server1-SCA.SYSTEM. ABCNode01Cell.Bus in bus SCA.SYSTEM. 
ABCNode01Cell.Bus started.
5. Display the destinations for each service module.
6. Modify the default forwarding path of outgoing destinations of the invoking service module that
must be wired to targets on the other system.

Select Applications > SCA modules, choose module and then click
SCA system bus destinations.
The destination to wire has importlink in the destination name, for example on
System A the destination would be
sca/AppA/importlink/test/sca/cros/simple/custinfo/CustomerInfo. Modify the path
by prefixing the foreign bus name to the destination name. From the example, the foreign bus name
for the second system is SCA.SYSTEM.ABCNode01Cell.Bus. The result is
SCA.SYSTEM.ABCNode01Cell.Bus:sca/AppA/importlink/
test/sca/cros/simple/custinfo/CustomerInfo
7. So that the response message can be sent to correct response queue, create a destination
sca/<SourceModuleName> in the System B with forward routing set to
foreignbus:sca/<SourceModuleName>. Set the exception destination to local FEM
queue. In this case, the local FEM queue is
SCA.SYSTEM.WBINode01Cell.Bus:sca/AppA.Draft comment: lesnider 
Added this
new step 7 for APAR 280613.
8. Optional: 
If you enabled security on the systems, add sender roles to the foreign buses.
Make sure to define the user each application uses on both systems from the operating system
command prompt.
The command to add the role iswsadmin $AdminTask addUserToForeignBusRole -bus busName 
		-foreignBus foreignBusName -role roleName -user userNamewhere
busName
The name of the bus on the system where you enter the command.
foreignBusName
The foreign bus you are adding the user to.
userName
The user ID to add to the foreign bus.

## What to do next