<!-- image -->

# Fault handling and compensation handling in BPEL processes

- Fault raising in BPEL processes

You can raise faults using throw and rethrow activities, or programmatically using a Java snippet activity. The invocation of services can also raise faults.
- Fault handling in BPEL processes

When a fault occurs in a process, the navigation continues with the fault handler or fault link.
- Compensation handling in BPEL processes

Compensation processing is a means of handling faults in a running process instance for which compensation is defined in the process model. Compensation reverses the effects of operations, which were committed up to when the fault occurred, to get back to a consistent state.
- Recovery from infrastructure failures

A long-running BPEL process spans multiple transactions. If a transaction fails because of an infrastructure failure, Business Flow Manager provides a facility for automatically recovering from these failures.

## Related concepts

- Fault activities
- Raising faults
- BPEL process compensation

## Related tasks

- Using fault handlers
- Continue processing upon unhandled faults
- Typing fault variables