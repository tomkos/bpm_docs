<!-- image -->

# Fault handling in BPEL processes

Fault handlers can be specified for invoke activities, scopes,
and on the process. Fault links can be specified for generalized-flow
activities. Scopes and all basic activities, except for throw and
rethrow activities, can be the source activity of a fault link.

- If an invoke activity without a fault handler or any other basic
activity is the source of one or more fault links, Business Flow Manager
tries to find a matching fault link. If a fault link is not available,
it then tries to find a matching fault handler on the enclosing scope.
- If an invoke activity or a scope with one or more fault handlers
is the source of one or more fault links, Business Flow Manager tries
to find a matching fault handler. If a fault handler is not available,
it runs the default fault handler and then tries to find a matching
fault link. If a matching fault link is not available, it tries to
find a matching fault handler on the enclosing scope.
- If the fault does not have any associated fault data, Business
Flow Manager uses a fault handler or fault link with the matching
fault name. If a fault handler or fault link is not found, it uses
the catch-all fault handler or fault link if one is available. A fault
without any data cannot be caught by a fault handler or fault link
that has a fault variable defined.
- If the fault has associated fault data, Business Flow Manager
uses a fault handler or fault link with the matching fault name and
a fault variable with a type that matches the type of the fault data.
If a fault handler or fault link is not found that matches the name
and fault data type, it uses a fault handler or fault link without
a fault name and a fault variable with a type that matches the type
of the fault data. If a suitable fault handler or fault link cannot
be found, it uses the catch-all fault handler or fault link if one
is available. A fault with data cannot be caught by a fault handler
or fault link that does not have a fault variable defined.

If a fault is raised that does not match any of the fault handler
or fault link definitions, the default fault handler is started. The
default fault handler is not specified explicitly. The default fault
handler runs all of the available compensation handlers for the immediately
enclosing scopes in the reverse order of completion of the corresponding
scopes. If the scope is the source of one or more fault links, Business
Flow Manager then tries to find a matching fault link. If a matching
fault link is not available or the scope is not the source of any
fault links, the default fault handler rethrows the fault to the next
level, that is, the enclosing scope or the process. On this next level,
Business Flow Manager again tries to match the fault to the fault
handlers or fault links that are available.

If the fault is not caught by any of the specific fault handlers
or fault links, or by the catch-all fault handler or catch-all fault
link, the fault reaches the process scope, and the process ends in
the failed state. Even if a fault handler catches the fault on the
process scope and handles it, the process still ends in the failed
state.

## Fault handler considerations

- Catch a fault and try to correct the problem so that the BPEL
 process continues through to normal completion.
- Catch a fault and find that it is not resolvable at this scope.In this case, you have the following additional options:
    - Throw a new fault.
    - Rethrow the original fault so that another scope can handle it.
    - If this is a request-response operation, reply with a fault response.
    - Invoke a human task to correct the issue.
    - For microflows, if the fault handler cannot resolve the issue,
you might need to roll back the process and compensate it.
    - For long-running processes, also consider using the Continue
On Error setting on the process to handle the fault administratively.

## Fault link considerations

- A fault link is activated for faults that occur within the source
activity only. The evaluation of conditions of normal links is not
part of the execution of the activity.
- If the source activity of the fault link is a scope activity,
the fault handler of the scope activity is evaluated first when a
fault occurs inside the scope. However, the fault handler can rethrow
the fault. In this case, a fault link of the scope can catch the fault
and can be navigated.
- If an activity is the source of multiple fault links, only one
of the fault links can be navigated when a fault occurs.
- The target activity of the fault link will be executed normally.
Compensate and rethrow activities in fault handlers cannot be the
target of a fault link.
- When a fault contains fault data, a variable of the fault data
type needs to be declared on the surrounding scope. The fault link
must reference this variable so that the target activity of the fault
link has access to the fault data.

## Transactional considerations

The process
engine does not force a transaction rollback if a runtime exception
is raised by a called service. However, if the called service participates
in the current transaction and the transaction is marked for rollback,
the current transaction rolls back to the state that the process was
in before the transaction started. If the transaction was triggered
by Business Flow Manager, it is automatically retried and the service
is called again. When the transaction is retried, the Business Flow
Manager can overrule the transactional behavior attribute of the activity,
and introduce additional transaction boundaries in order to determine
the activity that is causing the runtime exception. If the called
service raises the runtime exception repeatedly, the runtime exception
is stored in a separate transaction. During the next retry, the service
is not called again, but the stored exception is restored and the
navigation continues depending on the Continue On Error setting.
For more information about the continue-on-error behavior see Continue-on-error behavior of BPEL processes and activities.

- Retrieval of fault data for BPEL processes

Your process can handle runtime faults and BPEL standard faults. To handle these faults, you might need access to the information about the fault.
- Continue-on-error behavior of BPEL processes and activities

When you define a BPEL process, you can specify what should happen if an unexpected fault is raised and a fault handler is not defined for that fault. You can use the Continue processing upon unhandled faults setting when you define your process to specify that it is to stop where the fault occurs.