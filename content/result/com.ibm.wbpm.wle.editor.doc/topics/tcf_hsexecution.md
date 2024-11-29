# Saving the state of a client-side human service during execution

## About this task

- The ability to save execution context applies only to root client-side human services that run
within process instances. The execution context for root client-side human services that are used as
dashboards, stand-alone services, or URLs cannot be saved. In heritage human services, you enable
users to save the execution context on the activity or step, not at the sequence-flow level.
- To incrementally save your progress in a client-side human service that
runs as a process, you must specify the save settings at the client-side human service level. If the
client-side human service calls another service, such as an integration service or a general
service, and there are steps in the called service for which Save execution
context is selected, the save settings in the called service are ignored. To ensure that
your save settings take effect, specify them in the client-side human service itself, either on the
incoming connection to the called service or on the outgoing connection.

When you save the execution context, you save the state of the client-side human service while it
runs, including the current state of the variables and the position in the diagram. You can also specify how to save any changes to the shared business objects in your client-side
human service.

## Procedure

To enable users to save the execution context of the client-side human
service:

1. Open the client-side human service that you want to model in the
Diagram view.
2. In the diagram, select a point where you want users to
be able to save the current progress. For example, you
can choose to allow users to save the execution context between two
coaches, so that they can complete one page and come back to the next
page later.
3. Under Implementation > Settings, ensure that Save execution context for task implementation is
selected.

Tip: By default, saving the execution
context before the service completion is enabled for any task implementation. However, when a
client-side human service is embedded, this default behavior does not apply, and you must specify
whether you want to save the execution context of the embedded service before the flow returns to
the parent service. To save the execution context of a layered task implementation, select the
incoming connection to the end node in the diagram and, under Settings,
select Save execution context of layered task implementation.
4. To save your changes to the shared business objects, select Update content objects
and shared business objects when saving the execution context to make the changes to the
shared business objects available to all the instances that are using the same business
objects.
5. Repeat steps 2 and 3 for each point in the sequence flow
where you want runtime users to be able to save the execution context.
6. Click Save or Finish Editing.