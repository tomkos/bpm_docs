<!-- image -->

# BPEL process types

## Long-running processes

A long-running BPEL
process is interruptible, and each step of the process can run in
its own physical transaction. Long-running BPEL processes can wait
for external stimuli. Examples of external stimuli are events that
are sent by another business process in a business-to-business interaction,
responses to asynchronous invocations, or the completion of a human
task.

A long-running process has the following characteristics:

- Runs in multiple transactions.
- Interacts with services synchronously and asynchronously.
- Its state is stored in the runtime database, which makes the process
forward-recoverable.

## Microflows

A microflow runs in one physical
thread from start to finish without interruption. Microflows are sometimes
referred to as non-interruptible BPEL processes. Microflows can have
different transactional capabilities. A microflow participates in
the unit of work that can be either a global transaction or an activity
session.

A microflow has the following characteristics:

- Runs in one transaction or activity session.
- Normally runs for a short time.
- Its state is transient, and it is therefore not stored in the
runtime database.
- It typically invokes services synchronously.
- It can have only non-interruptible child processes.
- It cannot contain human tasks, wait activities, non-initiating
receive activities, or pick activities.