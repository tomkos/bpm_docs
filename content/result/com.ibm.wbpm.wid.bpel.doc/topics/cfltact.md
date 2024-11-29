<!-- image -->

# Fault activities

<!-- image -->

- Set Compensate Link
- Use this element with a compensate activity to call a
compensation handler on nested scopes.

<!-- image -->

<!-- image -->

- Catch element
- Use this element within a fault handler to intercept,
and deal with a specific kind of fault. The catch element is always
the first element on the control path of a fault handler, and the
activities that follow it run if the fault conditions you specify
occur. You can catch a built-in fault type, or define one yourself.
On the canvas, each catch shows the name of the fault type that it
will catch, and each is associated with a variable.

- Catch all element
- Use this element within a fault handler to intercept,
and deal with any fault that is not already defined in an existing
catch element. The catch all element is the first object on a control
path, and the activities the follow it run if the fault conditions
you specify occur.

<!-- image -->

<!-- image -->

<!-- image -->

## Related concepts

- Raising faults
- BPEL process compensation
- Fault handling and compensation handling in BPEL processes

## Related tasks

- Using fault handlers
- Continue processing upon unhandled faults
- Typing fault variables