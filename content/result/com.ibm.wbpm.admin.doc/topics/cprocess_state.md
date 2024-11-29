<!-- image -->

# State transition diagrams for BPEL process instances

## Conventions
used in these diagrams

| Symbol   | Explanation                                                                                                                |
|----------|----------------------------------------------------------------------------------------------------------------------------|
|          | Transient state. These states are not visible.                                                                             |
|          | Persistent state.                                                                                                          |
|          | Transient end state.                                                                                                       |
|          | Persistent end state.                                                                                                      |
|          | State transitions that are triggered automatically by Business Flow Manager.                                               |
|          | State transitions that are the result of an external interaction using an API.                                             |
|          | State transitions that are controlled by Business Flow Manager, or are the result of an external interaction using an API. |

## State transition diagram for microflow instances

A
microflow is considered to be stateless because the process is always
run in a transaction and instance information is not persisted for
navigating the process instance. However, depending on the process
definition and how Business Flow Manager is configured, the state
of a microflow can be exposed in Common Base Events or in the audit
log.

The following diagram shows the states that a microflow
instance can have.

After
normal initiation of the process instance, the first process state
a process instance reaches is the running state (1). When a process
instance runs normally through to completion, the process state changes
from running to finished (2). If a fault reaches the process boundary,
the process is put into the failing state (3). The process stays
in the failing state while the fault handler runs. After this,
the process instance is put into the failed state (4).

All of
these state transitions are triggered by Business Flow Manager. After
a microflow starts, you cannot influence these automatic steps.

## State transition diagram for long-running
process instances

<!-- image -->

The running, finished, failing, and failed states,
and the state transitions between them are the same as for microflows.

A
process instance is terminated by either an external request, or a
terminate activity. The termination of a process instance can span
multiple navigation steps and therefore multiple chained transactions,
for example, to terminate long-running activities or subprocesses.
During this termination phase, the process instance is in the terminating
state (5), (14), (18). When all of the long-running parts of the process
are terminated, the state of the process instance also changes to
terminated (6).

When a child process ends successfully and the
parent process fails later, the child process can be compensated.
During compensation, the child process is in the compensating state
(7). If compensation ends successfully, the child process is put into
the compensated state (8). If compensation is not successful, the
child process is put into the compensation-failed state (9). These
state transactions are initiated by the parent process automatically.

If the navigation of the process instance is still active, that is, it is in the running, or
failing state, it can be suspended with an API request. It can then be reactivated either after a
specified time, or by a resume request. The state of the process changes from running or failing to
suspended (11), (12) with the suspend request, and from suspended to running or failing with the
resume request (10), (13). A process in the suspended state can also be terminated (14). Only
high-level process instances can be suspended and resumed. However, the suspend or resume state is
propagated to the child processes.

When a process reaches one of the end states, finished, terminated, or failed, it can be started
again with a restart API request (15), (16), (17). Only high-level process instances can be
restarted, while only child process instances can be compensated.

A process instance
can be deleted when it reaches an end state (19). The process can
be deleted automatically if the automatically delete on
completion attribute is set accordingly, or it can be triggered
by an explicit delete request.

<!-- image -->