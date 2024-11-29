<!-- image -->

# Fault raising in BPEL processes

To propagate faults to the caller of the process, you use
the reply activity with a fault specification.

## Throw and rethrow activities for fault raising

A
throw activity in a BPEL process can throw any type of fault, including
standard faults, but the intended usage pattern is to throw business faults.
A fault thrown by a throw activity should be caught and handled in the BPEL process. If a process with a request-response interface does not handle a
fault in the process, the process ends with a bpws:missingReply standard
fault. For a client application, this fault is returned in a StandardFaultException
object.

You cannot return a business fault with a
throw activity. You must use a reply activity to return a business fault to
the process client. A reply activity can only return a business fault that
is defined on the interface that the process implements.

A rethrow activity
can be used in a fault handler to rethrow the fault to the next enclosing
scope. This might be useful when you want to do some fault handling on the
current scope, such as triggering specific compensation handlers, and still
want to make the enclosing scopes aware of this issue. You can also use a
rethrow activity when the current fault handler cannot handle the fault, and
you want the fault to be propagated to a fault handler that is defined on
one of the enclosing scopes, or on the process.

The rethrow activity
can only be used within a fault handler because existing faults can be rethrown
only from fault handlers.

## Fault raising in Java snippets

- raiseFault(QName fault, String variableName);
- raiseFault(QName fault);

```
javax.xml.namespace.QName fault = new javax.xml.namespace.QName
   ("http://process/UpdateCustomerRecordProcess/Interface0/", "IncompleteData");
raiseFault(fault);
```

Do not throw a ServiceBusinessException
object directly, but use the raiseFault message to do so.

## Fault propagation to the caller

The reply activity
with a fault specification propagates the specified fault to the caller of
the request-response operation. The reply activity can only return a fault
that is defined on the interface that the process implements. This method
is useful when the BPEL process cannot properly respond to the caught
fault, but the process initiator can respond to it. For example, if the caller
passes an account number that is not found by the BPEL process, the process
should reply to this service call with an AccountNotFound fault.

A
reply activity with a fault specification does not complete the process. The
navigation of the process continues until it reaches an end state.