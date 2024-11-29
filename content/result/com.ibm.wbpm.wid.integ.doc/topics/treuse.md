<!-- image -->

# Reusing mediation logic

## About this task

- Mediation subflows

A mediation subflow is a pre-configured set of mediation primitives that are wired together to realize a common pattern or use case. Mediation subflows are run in the context of a parent flow, and can be reused in mediation flows or in subflows.
- Creating a new mediation subflow

A mediation subflow can be used in multiple mediation flows. You create a mediation subflow implementation, and you can then use the subflow in a mediation flow by dropping the subflow implementation onto the mediation flow. This task describes how to create a mediation subflow implementation.
- Editing a mediation subflow

To implement the logic of a mediation subflow by adding and configuring mediation primitives, use the Mediation Subflow editor.
- Copying part of a mediation flow into a subflow

In the mediation flow editor, you can copy a portion of the mediation flow into a mediation subflow, which can then be re-used in other mediation flows or subflows.
- Adding a mediation subflow in a mediation flow

A mediation subflow is a preconfigured set of mediation primitives that are wired together to realize a common pattern or use case. Mediation subflows can be reused in mediation flows or in subflows.
- Promoting properties in a subflow

Promoting the property of a mediation primitive in a mediation flow allows an administrator to change the value of the property at run time. When you promote a property in a subflow, it becomes a property of the subflow instance. You can then set the value of the property in the mediation flow, or further promote the property in the parent mediation flow.
- Changing the input or output message type in a subflow

When you create a mediation subflow, the message types of the input and output terminals are undefined, which implies that the subflow can handle any kind of message. You can change the input or output message type to allow the subflow to only accept that particular message type.
- Using Service Invoke in a subflow

You can call an intermediary service in a mediation subflow by using Service Invoke.
- Synchronizing a subflow instance and implementation

When you change the implementation of a mediation subflow, you may see this error in the subflow instance in the parent mediation flow: "CWZMV0004E: The test subflow mediation does not match the implementation". Use the Quick fix action to synchronize the subflow instance with the implementation.
- Mediation subflow limitations

Limitations of mediation subflows