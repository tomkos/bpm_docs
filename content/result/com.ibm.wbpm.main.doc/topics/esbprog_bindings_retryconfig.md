<!-- image -->

# Retry configuration

- a module labeled StockServiceModule
- a number of service integration bus destinations created by SCA to support asynchronous
communication
- one of service integration bus destinations labeled
sca/StockServiceModule

## Example scenario

If a request involves passing a message between a JMS or WebSphere MQ export and a component, the
number of retries is always 1 more than the value entered for the Maximum failed
deliveries count. The example scenario explains how destinations are used to route a
message from a JMS export to a component using a  Maximum failed deliveries
count of 5.

Figure 1. Retry configuration

<!-- image -->

As shown in Figure 1:

At 1a and 1b, the message is collected from the JMSExport1 external destination, which is
Module1.JMSExport1\_RECEIVE\_D\_SIB. It is delivered to the target component,
which is Pojo1.

At 2, Pojo1 returns a system error.

At 3a and 3b, the message is rolled back to the location where it was collected,
Module1.JMSExport1\_RECEIVE\_D\_SIB.

Figure 2. Retry configuration

<!-- image -->

As shown in Figure 2:

At 4, after the message is rolled back to
Module1.JMSExport1\_RECEIVE\_D\_SIB, the underlying system redelivers the
message to JMSExport1 based on the Maximum failed
deliveries setting.

At 5, the JMSExport1 binding detects a redelivered message and forwards
the message to the sca/Module1 destination.

At 6, the message is delivered to Pojo1.

At 7, Pojo1 returns a system error.

At 8, the message is rolled back to sca/Module1. From
sca/Module1, the message is redelivered to Pojo1 four
more times.

As a result, Pojo1 is started six times.

## Advanced invocation style determination

To understand how system exceptions are handled, the type of invocation style that is used for
the invocation must be considered.

An asynchronous call always results in an asynchronous invocation. A synchronous call can have
varying results. If the target service has an asynchronous implementation, the system can switch a
synchronous invocation into an asynchronous invocation. Certain import bindings such as JMS imports
have an asynchronous implementation. If the target service is a component with asynchronous
implementation, an asynchronous hop (message serialization and de-serialization to a destination) is
placed in front of the component.

Figure 3. Invoke an asynchronous import

<!-- image -->

Figure 4. Invoke synchronous import as asynchronous

<!-- image -->

## Failed messages

In Workflow Server, after the retry limit is reached, the message is
routed to an exception destination as specified in the Exception destination
field of the module destination. By default this destination is set to the recovery exception
destination. For example, a server with the node name WPSNode and Server name
server1, has the recovery exception destination of
WBI.FailedEvent.WPSNode.server1.

Each server has one recovery exception destination. In general, all regular destinations created
on the SCA system bus are configured to route failed messages to the recovery exception destination.
Alternatively, regular destinations on the SCA application bus are configured to route failed
messages to the SCA application bus system exception destination. If a JMS export picks up a message
from the SCA application bus and experiences a rollback situation, the failed message is routed to
the SCA application bus system exception destination instead of the WebSphere Business Integration
recovery exception destination.

When a system failure occurs, in addition to capturing the failed message at the exception
destination, a failed event is generated that represents the system error and is stored into the
Recovery database, where it can be accessed using failed event manager.

Failed events are not created for synchronous invocations. They are created when clients use an
asynchronous invocation pattern and a ServiceRuntimeException is thrown by the
service provider.