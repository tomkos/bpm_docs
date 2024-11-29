<!-- image -->

# Authorization for creating and starting BPEL processes

In addition, when the process is called by a Service Component
Architecture (SCA) client, you can restrict the set of users that
is allowed to start the process by setting specific SCA security qualifiers
when you install the process.

- Assign an inline invocation task to the initiating receive or
pick (receive choice) activity of the processSome processes might
change sensitive business data and therefore only authorized personnel
should be authorized to create and start these processes. For this
type of process, you can assign a human task to the initiating receive
activity of the process by specifying an inline invocation task for
the process template. The potential starters defined for the inline
invocation task become the potential starters of the process.
The
process can be started either by creating and starting the invocation
task using the Human Task Manager API, or by initiating the process
using the Business Flow Manager API. Both methods result in the same
authorization checks. If an inline task is not specified, anyone can
start the process.
- Assign a stand-alone invocation task to the initiating receiveor pick (receive choice) activity of the processYou can also usea stand-alone invocation task that is wired to the process to performauthorization checks when a process is started. However, considerthe following points if you use a stand-alone invocation task:
    - The authorization check is done only if the process is started
by the invocation task, that is, the check is omitted when the process
is started using the Business Flow Manager API or an SCA client that
is directly wired to the process component.
    - It uses the SCA infrastructure to invoke the process while an
inline task is called directly by Business Flow Manager.
    - You have no access to the process context in the people assignment
criteria definition. This means that stand-alone tasks do not support
dynamic people assignments based on the process context.

If an administration task is assigned to the process, the administrator
role of the administration task is inherited by the process. A process
administrator can perform various actions on the process, including
creating and starting a process instance.

## Related information

- Authorization for interacting with a BPEL process