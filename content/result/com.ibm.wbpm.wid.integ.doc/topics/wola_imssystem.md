<!-- image -->

# Transactions, security, and connection properties for an IMS
system

## IMS outbound calling

For IMS (similar to
CICS), you can call IMS transactions that use the WOLA link server
using the native WOLA APIs (Host Service and Receive Request). Using
the IMS Open Transaction Manager Access (OTMA) interface through WOLA,
you can also call IMS transactions and drive them in IMS message processing
regions or fast-path dependent regions. When you target IMS transactions
using OTMA, you do not specify a register name in the connection properties.

## IMS security propagation

For security propagation
and assertion between the WebSphere Application Server for z/OS and
an IMS system, you must use WOLA over the OTMA interface. The WebSphere Application Server for z/OS must
be configured to run with the SyncToThread option
enabled. Also, the IMS OTMA parameter OTMASE=FULL must
be set. With these settings, the user ID under which the WebSphere Application Server for z/OS application
runs is propagated and asserted in the IMS message processing or fast-path
dependent region where the transaction is dispatched. The security
propagation and assertion between the WebSphere Application Server for z/OS and
the IMS system does not apply to IMS batch message processing regions.

In WebSphere Application Server for z/OS,
you may choose to use the security credentials that are already set
on the thread, which by default is the user ID that is running the
server, or you can set the credentials using a JAAS alias.

## IMS connection properties

When creating
the WOLA import and service, you must define the connection properties
for the target IMS system.

In the New External Service wizard,
on the Security and Configuration Properties page,
specify the JNDI name of the connection factory defined on WebSphere Application Server for z/OS or
specify the connection properties for the IMS server in the binding.
If you choose to specify the connection properties, then the managed
connection factory is created during deployment with the specified
properties.

When
targeting an IMS transaction via OTMA then you must set the appropriate
OTMA properties in the connection factory. In the binding, these are
found under the IMS OTMA connection properties area in the Security
and Configuration Properties page, where you must select IMS
OTMA connection properties and select Use OTMA to
set OTMA properties to call IMS transactions instead of using the
native WOLA APIs.

To communicate with a COBOL, PL/I, C, or C++
program on a IMS system, you must set the following properties:

- Group ID - Specifies the target IMS OTMA
name. This value must be a valid OTMA XCF group name.
- Server name - Specifies the target IMS OTMA
server name.
- Sync level - Specifies the OTMA sync level.
For IMS to commit work for a processed transaction after sending the
response to the application server without receiving a positive acknowledgment
that the response was accepted, set the sync level to None. For IMS
to commit the transaction only after receiving a positive acknowledgment,
select Confirm as the sync level. If the acknowledgment is negative,
the inflight work is rolled back.
- Request prefix style - Specifies the prefix
style for inbound messages to the IMS server.
- Response prefix style - Specifies the prefix
style for outbound messages from the IMS server.

For
IMS transactions, when using WOLA over OTMA, the target transaction
is embedded in the inbound message. You do not need to specify the InteractionSpec properties
at the operation level.