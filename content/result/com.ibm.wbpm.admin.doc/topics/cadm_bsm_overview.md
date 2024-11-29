<!-- image -->

# Administering business state machines

A business state machine is used to represent an event-driven business process. Within a business
state machine there are many instances. You can administer and debug business state machine
instances using:

- correlation set properties
- display states

## Correlation set properties

To distinguish one business state machine instance from another, a correlation set is used to
uniquely identify a state machine instance. For example, a correlation set properties could be a
customer ID and state. If you want to administer a particular instance, you need the values of the
correlation set properties. Correlation set properties are defined in Integration Designer and viewed in Business Process Choreographer
Explore.

You can define only one correlation set in Integration Designer. Multiple correlation sets are not allowed.

## Display states

A display state variable indicates the current state of a particular business state machine
instance. Knowing the last committed state is useful for debugging or administrating business state
machines. Display states are defined in Integration Designer
and viewed in Business Process Choreographer Explorer.

The display state variable may not always show the most current state of a business state machine
instance. If an instance is actively processing an event, the in-memory copy of the display state
variable may be different from the last committed value. What you see in Business Process
Choreographer Explorer is the display state value that was last written to disk. If a business state
machine instance is processing an event, the in-memory value of the variable will not be written to
disk until the transaction is completed.

- Finding business state machine instances

View correlations set properties to find and administer a particular business state machine instance.
- Viewing display states

View display states to administer or debug business state machine instances.

## Related tasks

- Finding business state machine instances
- Viewing display states