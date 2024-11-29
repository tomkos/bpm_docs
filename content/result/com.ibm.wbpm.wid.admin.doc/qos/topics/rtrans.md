<!-- image -->

# Transaction qualifier

Transaction qualifiers are designed to ensure that any
operations that are interdependent are either all completed successfully
or all canceled successfully.

Location: The transaction
qualifier is set on the implementation.

- Global - A global transaction is a unit
of work in a distributed transaction processing environment in which
multiple resource managers may be enlisted. If the client propagates
a transaction and a component is configured to join that transaction,
then this component will run under that transaction. That is to say,
resources updated by the component are committed when the client commits
the transaction. If either of these conditions are missing, the component
runs under a new global transaction that is committed when the operation
completes.
- Local (default) - This setting is required
when a component implementation is not capable of participating in
a two-phase commit protocol. Sometimes ACID coordination of multiple
resource managers is not needed. In such scenarios, running business
logic in a local transaction performs better than in a global transaction.
Therefore, the component runs in a local transaction, even if a transaction
is propagated to the hosting runtime environment. Local transactions
are not propagated to services invoked by the component. The local
transaction joins an activity session if one is active. If an activity
session is not currently active, one is automatically started.
- Any - If a global transaction context has
been propagated from the client, the runtime environment will dispatch
methods from the component in a global transaction; otherwise, the
runtime environment will establish a local transaction environment.
- Local application - If this option is selected,
the component processing occurs within a WebSphere local transaction containment that is managed
by the application. It is the responsibility of the application to
commit or roll back transactions. (Selecting this option is equivalent
to setting the transaction descriptor to Not Supported and
setting the LocalTranResolver to application for an enterprise
JavaBeans.)

## Programming notes

Global transaction qualifiers
and activity session qualifiers are mutually exclusive.