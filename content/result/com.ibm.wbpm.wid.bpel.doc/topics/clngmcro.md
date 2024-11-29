<!-- image -->

# Choosing between long-running processes and microflows

To begin with, you need to understand the basic differences between
microflows and long-running processes. While they are both considered
business processes, a microflow is contained within a single transaction,
however a long-running process can be multitransactional, and can
run over an extended period of time (see the Business processes topic
in the related links for more information). If your process requires
more than one transaction, it must be a long-running process. If your
process can be designed either way, then consider:

1. If your process will need to stop at any point and wait for external
input, either in the form of an event or a human task, then
you must use a long-running process. Microflows are not interruptible.
2. If you do not have IBM® extensions enabled
for this process, then you cannot use a microflow. A microflow is
an IBM enhancement of the BPEL
programming language, and so will not be an option if these extensions
are disabled.
3. If you have a short series of steps to model and want them executed
very quickly in the runtime environment, then use a microflow.
4. If you have elements in your process that you would like to run in
parallel, use a long-running process. Each of the parallel paths
must run within its own transaction, and its transactional behavior
must be either commit before or requires
own.

Before you make any final decision on whether to use long-running
processes or microflows, you should review the information in the
topic Synchronous-over-asynchronous
invocation.

## Related concepts

- Key concepts for BPEL business processes
- Working with BPEL extensions
- Best Practice: When to not use the BPEL extensions

## Related tasks

- Compensating activities in a long-running process
- Compensating a microflow

## Related reference

- Server tab: BPEL process editor