# Assigning teams to BPDs and lanes (deprecated)

## Before you begin

To perform this task, you must start the Process Designer desktop
editor. For information about how to create a team, see Creating a team.

## About this task

You can assign teams to activities that are implemented
as user tasks (including ad hoc activities), to lanes, and as instance
owners in the Overview page of the BPD editor.
Teams that are assigned to activities and lanes determine which users
can work on tasks in Process Portal. If
a team is assigned to a user task activity, members of that team can
work on that task in Process Portal. If
a team is assigned to a lane, members of that team can work on all
the tasks that are part of that lane. If both a user task activity
and the lane in which it is contained have teams that assigned to
them, the team that is assigned to the activity is used.

If
a user task implements an ad hoc activity, members of the team that
is assigned to the lane or members of a task-specific team can work
on the task. The instance owners team and lane teams are authorized
to perform actions that are related to an ad hoc activity, such as
starting a manual activity.

Members of the instance owners team
can start the task in Process Portal, and
can start, disable, and enable ad hoc activities in the BPD. For instances
that they own, they can reassign user tasks, set their due dates and
the priority of tasks.

## Procedure

To assign a team of instance owners to a BPD:

1. Open the desktop Process Designer (deprecated).
2. Open the process application that contains the business
process definition (BPD).
3. In the BPD Overview, select a team for Instance
owners, or create a new team.

To assign teams to lanes:

1. In the BPD diagram, click the lane in which you want to
make the assignment.
2. In the Behavior section of the properties, click Select to
choose the team that you want to use as the default team for this
lane. You need a default lane assignment to ensure that
any activities that are not otherwise routed have an automatic default
assignment. By default, the All Users team is assigned to each lane
in the BPD. You can use this default team for running and testing
your BPD in the Inspector. The All Users team includes all users in
the system who are members of the tw\_allusers security
group.Note: If the default team assigned to the
lane that is currently used for activity is changed, the team filter
service definitions are removed from the Assignments tab.
3. Choose the team from the library.

To assign teams to activities, see Assigning teams to BPD activities

1. Click Save in the main toolbar.