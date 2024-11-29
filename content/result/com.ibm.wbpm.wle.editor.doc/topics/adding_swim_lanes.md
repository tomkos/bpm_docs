# Adding lanes to a BPD (deprecated)

## Before you begin

To perform
this task, you must be in the IBM® Process
Designer desktop
editor, which is deprecated.

## Procedure

1. Open the desktop Process Designer (deprecated).
2. Open a process application that contains a BPD.
3. Drag a lane from the palette and drop it onto the diagram.
4. In the Properties view, enter a name for the lane.
5. Optional: 
You can also associate a default team with the lane.

When a user task is added to this lane, the initial assignment for the task is the default lane
team. If you do not specify a default lane team, the default team is All Users.
6. Optional: 
You can also create a lane as a system lane, indicating that activities
within it are to be completed by an IBM Business Automation Workflow
system. To make a lane a system lane, select the lane in the diagram then select Is
System Lane in the Properties view. 
Although you can create a system task in non-system lanes, any new tasks in the system lane
are created as system tasks by default. After a system task is created, if you move the task to a
non-system lane, for example a lane associated with a team, it retains a system task type.A
system lane user runs system tasks in system lanes. If the team that is associated with the system
lane has multiple members, the first system lane user who is a member of the team is selected for
running the task.
7. To reorder lanes with respect to one another, right-click a lane and select Move
Lane Up or Move Lane Down.
8. Click Save in the main toolbar.