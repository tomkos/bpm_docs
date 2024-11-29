# Assigning a primary queue to more than one role

## About this task

The CB\_PrimaryQueue attribute for a role is automatically
defined when you create a role for a solution in Case Builder. Renaming the role does
not affect the queue name that was created when the role was first
created in Case Builder.

Step Designer displays role swimlanes, but the steps that are defined in each role swimlane are
assigned to a primary queue of a role. By defining the same primary queue to more than one role, you
are enabling multiple roles to use the same work queue. In other words, all steps that are defined
in a role swimlane where the primary queue is being shared can be processed by any role that has
that same CB\_PrimaryQueue attribute value.

## Procedure

To assign the same primary queue to more than one role:

1. In Case Builder create two roles, for example,
Role 1 and Role 2.
2. After you create a case type, open the Activity page
and click Activity > New Activity to create a new activity for the solution.
3. Save and close the solution.
4. In a stand-alone IBM
FileNet Process Designer, open the solution for
editing the FileNet P8 activity workflow.
5. Select the case type.
6 Assign the primary queue attribute for Role 1 to Role2 . Role 2 now has the same primary queue as Role 1.
    1. Click Views > Roles.
    2. Select Role 1 and open the Custom
Attributes tab to view the value set for the CB\_PrimaryQueue
attribute.
    3. Select Role 2, open the Custom
Attributes tab, update the value for the CB\_PrimaryQueue
attribute to the value that is set for Role 1.
7. Go to File > Solution, and then save and close the solution in IBM
FileNet Process Designer.
8. In Case Builder,
open the solution, or ensure that the solution is in edit mode.
9. In the Activity page of Case Builder
click the Edit steps icon for the new activity to open the Step Designer so
that you can design the activity process map.
Only one of the roles is an option as a role swimlane, but all steps that are assigned to that
swimlane are available to view by both Role 1 and Role 2 in
the Case Client.