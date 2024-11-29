<!-- image -->

# Error handling in the mediation flow component

## Fail terminal

Mediation primitives that process messages have a fail terminal. When there is a failure in the
mediation primitive, the fail terminal is called and exception information is sent, along with the
input message. The exception information is stored in the failInfo element in the message context. A
message showing the failInfo is shown in Figure 1. You
must wire the fail terminal of a mediation primitive to another mediation primitive in order to
access the failInfo.

Figure 1. The failInfo element in the message context

<!-- image -->

## Runtime failure in the mediation primitive

When a failure occurs in a mediation primitive, the unwired fail terminal sends a runtime
exception, and the flow is considered to have failed. If the mediation flow component is running
under a global transaction (default), primitives that use resources that participate in the global
transaction will rollback.

Figure 2. Runtime failure and rollback transaction

<!-- image -->

When the flow is reconfigured, a global transaction is configured, and a failure occurs again in
the Custom mediation primitive, the flow fails. If the Log mediation primitive has its transaction
mode property set to same, the log entry will be rolled back as a part of the global
transaction, and no entry will occur in the database. If the transaction mode property was set to
new, then the log to the database commits outside the global transaction so an entry will
still occur in the database.

## Modelled faults

1. input
2. output
3. fault

- An Input Fault node is created when a source operation has a modelled fault message
defined. The Input Fault node has an input terminal for each fault message type that is defined in
the source operation. Any message that is sent to an Input Fault node will result in a modelled
fault error message being returned from the source operation. Wiring to this node means that the
fault message is returned to the service requester. The Input Fault node is created in the request
and response flows.
- A Callout Fault node is created in the response flow for each target operation that has a
modelled fault defined. The Callout Fault node has an out terminal for each fault message type that
is defined in the target operation. When a modelled fault occurs, the Callout Fault node sends a
message to the mediation primitive or node to which it is wired.

Figure 3. Example of a modelled fault

<!-- image -->

## Unmodeled faults

Errors that are returned, and are not defined as WSDL faults are called unmodeled faults. There
is no Input or Callout Fault node created for these types of faults in the mediation flow editor. In
this case, the input message type is sent to the Callout Response node's fail terminal. The failure
information is captured in the failInfo element of the message context.

To handle an unmodeled fault, you can wire the fail terminal of a Callout Response node to a
mediation primitive. For example, you could wire the fail terminal on a Callout Response node to a
Message Logger mediation primitive to log all unmodeled faults. You can set a property on the
Callout Response node to determine whether the entire request message or just the message header
information should be passed out of the fail terminal (there can be a performance overhead if you
choose to pass the entire request message).

If the fail terminal on the Callout Response node is not wired and an unmodeled fault is
received, a mediation runtime exception will occur.

## Stop mediation primitive

The Stop mediation primitive has one input terminal and no out terminals. When the fail or out
terminal on a mediation primitive is wired to the Stop mediation primitive, that particular branch
comes to an end.

The mediation flow editor generates warnings if the out terminal of a mediation primitive is not
wired. The Stop mediation primitive is used to stop these warnings. In the runtime, out terminals
that are not wired are automatically propagated to stop.

Figure 4. Stop mediation primitive

<!-- image -->

## Fail mediation primitive

The Fail mediation primitive can be used if you want to stop the flow and send a runtime
exception. You can wire the out or fail terminal on a mediation primitive, to the Fail mediation
primitive. If the mediation flow component is running under a global transaction, mediation
primitives participating in the global transaction will rollback.

## Faults in the Service Invoke mediation primitive

- Modelled faults, which are sent through the out terminal.
- Unmodeled faults, which are sent through the fail terminal.

- Error flow

A mediation flow component has an error flow for each source operation. The error flow acts as a catch-all for messages that are propagated from any unwired fail terminal on any primitive or node, in either a request or a response flow.
- Common patterns of usage for error handling

When a service component is called synchronously or asynchronously unexpected runtime errors can occur. In SCA, error handling is put in place to make sure that a message is not lost. This topic provides information on how messages are handled by the SCA runtime when an error occurs. You will find information for both synchronous and asynchronous invocation styles.

<!-- image -->