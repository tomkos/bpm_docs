<!-- image -->

# Transactions

- A transaction qualifier must be set on the implementation, and
the qualifier must specify a global transaction.
- The implementation must be invoked synchronously.
- The component must join a propagated transaction.
- The transaction cannot be suspended on any of the participating
references.
- The preferred interaction style on a participating interface cannot
influence the invocation style to become asynchronous.

The assembly editor sets the appropriate quality of service qualifiers
for you to ensure that the transaction propagates. However, there
are conditions that attach to specific implementations or bindings
that can affect those settings. These special circumstances are discussed
below.

The assembly editor lets you see a transaction by highlighting
the transaction propagation through components and wires. If you rest
your cursor on a component or wire that is failing to propagate a
transaction, hover help provides guidance in understanding and resolving
the problems. You can change settings right on the wire.
A new qualifiers tab in the Properties view shows quality of service
settings for the entire module. The assembly editor automatically
applies the settings that support transaction propagation and message
reliability. A list of those settings is provided in the table that
follows. See Viewing and changing qualifier settings in the assembly editor for details about
using these features.

| Action                | Quality of service setting                                                                                                                                                                                 |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Add interface         | The join transaction qualifier is added and set to "true".                                                                                                                                                 |
| Add reference         | The suspend transaction qualifier is added and set to "false".  The asynchronous invocation qualifier is added and set to "commit".  The reliability qualifier is added and set to "assured (persistent)". |
| Create implementation | The transaction qualifier is added and set to "global".                                                                                                                                                    |

## Types of transactions

- Local transactions
- Global transactions

A local transaction
cannot propagate. If an activity session context is present, the local
transaction is resolved in its scope automatically by the system.
If an activity session context is not present, the system automatically
resolves the local transaction when the implementation completes.

## Transaction propagation

A primary goal for
transactions is atomicity. A guarantee of atomicity ensures that the
resources are committed as one unit or rolled back as one unit. Transactions
need to propagate from one component to another when those resources
are updated by different components, or by the same component over
multiple invocations.

- Interfaces
- References
- Implementations

Interface qualifiers advertise the qualities supported
by a target service. They represent a contract with the client of
the service. The interface qualifier that affects transactions is
the join transaction qualifier. If a transaction is propagated
by the client, the join transaction qualifier specifies whether or
not the component will join that transaction

Reference qualifiers
advertise the qualities of the invocation that is made using the reference.
The qualifier on a the reference that affects transactions is the suspend
transaction qualifier. When the invocation is synchronous,
the suspend transaction qualifier determines whether client will propagate
the transaction to the target component.

Implementation qualifiers
advertise the qualities used by the implementation. The implementation
qualifier that affects transactions is the transaction qualifier.

## Invocation style

The invocation style of
a service call refers to the type of call the client makes when invoking
the service. The call can be either synchronous or asynchronous.
The style affects whether or not a transaction can propagate to the
target service. Global transactions can only propagate if the client
invokes the target service synchronously.  Global transactions do
not propagate when the client calls the services asynchronously, regardless
of how the qualifiers that affect transaction propagation are set.

- Long-running BPEL process
- Business state machine
- Human task
- JMS, MQ, MQ JMS, and generic JMS imports and exports
- EIS exports

## Preferred interaction style

Preferred interaction
style is an attribute that can be set on the interface of a component,
import, or export in the assembly diagram. The preferred interaction
style of an interface reflects the behavior of the service. When the
system invokes the target implementation asynchronously, the assembly
editor sets the preferred interaction style of that service to asynchronous.
Some implementations allow you to change the preferred interaction
style after it is assigned by the assembly editor. Other implementations
do not, because they are always started asynchronously by the system.
You cannot change the invocation style for long-running BPEL processes,
a business state machines, or a to-do human tasks.

In the case
of exports used with EIS systems, interaction style only applies to
one-way operations and so appears in the user interface as a one-way
operation invocation style with blocking and non-blocking as values.

For more information about long-running processes and microflows, see the IBM Business Automation
Workflow documentation, particularly Transactional behavior of long-running processes and Transactional behavior of microflows.