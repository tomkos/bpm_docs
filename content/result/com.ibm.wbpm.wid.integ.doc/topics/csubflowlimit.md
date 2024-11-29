<!-- image -->

# Mediation subflow limitations

- You cannot use a Policy Resolution primitive in a subflow
- You cannot specify a context element within a subflow. Context
elements that are available in the parent flow are also available
to mediation primitives in the subflow.
- When you are debugging a subflow, be aware of these limitations:
    - You cannot step into a subflow. You must set a breakpoint
in the subflow in order to view the subflow execution.
    - You cannot step out of subflow. If you try to step
over the last primitive in the subflow, the flow will run to completion.
To workaround this limitation, set a breakpoint in the main flow after
the subflow primitive.
- If the subflow is contained within an aggregation block (an aggregation
block is a group of mediation primitives that occur between a Fan
Out mediation primitive and a Fan In mediation primitive) of the parent
flow then a Service Invoke mediation primitive in the subflow will
not be considered as part of this aggregation from an Asynchronous
Deferred response invocation style. Read the following topic for a
description on the invocation styles available: How to process mediations in parallel

## Related concepts

- Mediation subflows

## Related tasks

- Creating a new mediation subflow
- Editing a mediation subflow
- Copying part of a mediation flow into a subflow
- Adding a mediation subflow in a mediation flow
- Using Service Invoke in a subflow
- Synchronizing a subflow instance and implementation

## Related information

- Promoting properties in a subflow
- Changing the input or output message type in a subflow