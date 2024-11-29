# Enabling tasks to be reassigned at run time

## About this task

- If the client-side logic includes a postpone event, the current user can use the navigationoptions of the postpone event to return to the task list or to a different user interface when he isdone working with the task. The current user, who no longer owns the task, cannotmanipulate the state or data associated with the task, therefore no data save is performed after thepostpone event. When the service execution reaches the postpone event, one of the following actions occurs: Restriction: To maintain data integrity, the last data save must occur within the sameclient-side human service as the postpone event, otherwise the new task owner would not be able toresume the task.
    - If the task is not claimed when the postpone event is executed, the new owner resumes the task
at the node that follows the postpone event.
    - If the task is already claimed when the postpone event is executed, the new owner resumes the
task at the last save point prior to the task reassignment.
- If the client-side logic includes an end event, the end event ends the flow for the current
user, but does not end the task and does not perform any data save either. When claimed by the next
owner, the task is resumed at the last save point, which is located before the last service
call.

The following procedure is provided as an implementation example for a task reassignment. You can
use a different implementation to meet your business needs.

## Procedure

To enable users to reassign a task:

1. Open the appropriate process application.
2 Create a general system service for the task reassignment:
    1. Click the plus sign (+) next to Implementation, and create a general
system service.
    2. Add a server script to the service and connect it to the start and end events.
    3. In the Implementation properties of the server script, enter the
JavaScript code that includes the logic for task reassignment. For example,
tw.system.currentTask.reassignBackToRole();.
3. Open the client-side human service that you want to work with.
4. In the Diagram view, add the service node for task
reassignment. For example, the service can be implemented as a general system service,
but the implementation can use any service type that can be called from a service
node.
5. In the Behavior implementation properties of the service, select
Call a service, and then specify the general system service that you created
earlier.
6. Add an event  to the diagram.
 The default implementation is a stay-on-page event.
7 Convert the stay-on-page event into a postpone event and configure it:

1. Select the stay-on-page event and, in its implementation properties, under Event
Type, select Postpone
.

Tip:  If the postpone option is not available, switch to Overview
and check the Use as setting of the client-side human service. The postpone
event takes effect when you selected Task (Service contained in a process).
See Defining usage settings for client-side human services.
2. In the diagram, connect the postpone event to the node where you want the task work to be
postponed, and add an outgoing connection from the postpone event to the node where you want work to
be resumed by the new task owner.
3. In the Implementation properties, under Event
Navigation, specify a navigation option for the postpone event, which determines what
the user will see after the service is postponed.
 You can choose between Default (behavior provided by the hosting UI),
Go to the instance details UI, or Go to a specified
URL.Tip:  Navigation occurs only if the hosting user interface provides
navigation support.
8. In the Diagram view, add another stay-on-page event to the diagram, and
connect it to the postpone event in the subflow that contains the service node for task
reassignment.
9. Click Save or Finish Editing.