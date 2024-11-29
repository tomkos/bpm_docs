<!-- image -->

# Activity session qualifier

An activity session can be longer-lived than a global
transaction and can encapsulate global transactions. Activity sessions
are used to scope or coordinate local transactions. They are used
for microflows when it is not possible to use a global transaction
- for example, when the microflow uses more than one resource that
only supports one-phase-commit. Activity sessions provide a solution
by coordinating the one-phase commit process. If an activity session
rolls back, changes are undone. An activity session context can be
longer lived than a global transaction context and can encapsulate
global transactions.

Microflows run on one physical thread from
start to end without interruptions. As the name suggests, microflows
are small in footprint and fast in execution. A microflow requires
a transaction, but that can be a global transaction or a local one
inside an activity session.

Location: The activity session
qualifier can be set on an implementation.

- True - There must be an established activity session
in order to run this component. The runtime environment may use the
provided activity session for the execution of this implementation,
or if none is provided, the runtime environment will create a new
activity session.
- False - The component does not run under an activity
session, even if one is propagated to the hosting runtime environment.
- Any  (default) - If an activity session has been propagated
from the client, the runtime environment will dispatch methods from
the component in the activity session; otherwise, the component will not run
under any activity session.

Application:  Activity sessions were implemented
for use with BPEL and compensation.

## Programming notes

Global transaction qualifiers
and activity session qualifiers are mutually exclusive.