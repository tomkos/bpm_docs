<!-- image -->

# Raising faults

## Raising a fault using throw and rethrow activities

A throw activity in a BPEL process can throw any fault, including
standard faults, but the intended usage pattern is to throw business
faults. An exception thrown by a throw activity can be caught and
handled within the BPEL process. If a fault that is thrown by a throw
activity is not handled within a process with a request-response interface,
either business or standard fault, it is returned as a runtime exception
to the process caller.

A rethrow activity can be used in a fault handler
to rethrow the fault to the next enclosing scope. Implementing a rethrow
activity is useful when you want to do fault handling on the current
scope, such as triggering specific compensation handlers, and still
want to make the enclosing scopes aware of this issue. You can also
use a rethrow activity when the current fault handler cannot handle
the fault and wants to propagate it to an outer-scoped fault handler.
In the absence of a rethrow activity, a fault propagated to a higher
level using a throw activity is a new fault. When a rethrow activity
is invoked, the fault is the same instance. The rethrow activity is
available only within a fault handler because only an existing fault
can be rethrown.

## Using reply activities to send a fault to the caller

The reply activity propagates a fault to the client that initiated,
or called, the process. A reply with a fault activity can only return
a fault that is defined on the interface that the process implements.
A reply activity is useful when the BPEL process cannot properly respond
to the caught fault, and the process initiator might be better equipped
to respond. For example, if the client passes an account number that
is not found by the BPEL process, the process replies to the service
call with an AccountNotFound fault.

A reply with a fault activity
does not exit the process and return to the caller immediately. The
navigation of the process continues until it reaches an end state.
So make sure by the logic in your process that the normal reply activity
is not executed in case the fault reply has been executed.

## Related concepts

- Fault activities
- BPEL process compensation
- Fault handling and compensation handling in BPEL processes

## Related tasks

- Using fault handlers
- Continue processing upon unhandled faults
- Typing fault variables