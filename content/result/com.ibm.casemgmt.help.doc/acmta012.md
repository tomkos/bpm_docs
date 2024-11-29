# Deleting a case

## Symptoms

You delete the case folder but activity processes are not completely removed. The activity
processes might be orphaned.

## Resolving the problem

There are two ways to delete a case:

- Using the Case Manager REST API for deleting a case. See Deleting a particular case resource.
- Deleting the case manually using the following procedures.

1. Terminating and deleting work items in case activity processes for a case
2. Preparing to reuse documents from cases to be deleted
3. Deleting the case folder

## Terminating and deleting work items in case activity processes for a case

1. In IBM® Administration Console for
Content Platform Engine,
navigate to the appropriate domain, expand Object Stores, and click the name
of the IBM Business Automation
Workflow target
object store that contains the case that you want to delete.
2. Expand the folders in the target object store, then go to
Browse > Root folder > IBM Business Automation
Workflow > Solution Deployments > My
Solution > Case
Types > Cases.
3. Go to the case sequence folder:
Year > Month > Day > number > case\_sequence.
For performance reasons, cases created on the same day are filed under a folder with a random
number between 0001 and 0300. For example,
2013 > 07 > 19 > 0166 > 000000100003.
If a large number of cases are filed on the same day, you might need to use the search function of
the IBM Administration Console for
Content Platform Engine and search
the target object store to find the case.
4. Click the case\_sequence. In the right pane, click the
Tasks tab.
5 In the State column, complete the following actions for tasks that are ina Failed or Working state:
    1. Click the task, then click its Properties tab.
    2. If the task is in a Failed state, and the value of the Disabled state property is
3, ignore this step and continue with step 6.
    3. For failed or working tasks that are not disabled, scroll down to the
ID field and record its value. You will need the task ID in a later step when
you remove the corresponding workflow.
    4. Return to the case\_sequence tab and close the task
tab.
    5. If a task is in a Working state, click Promote. Verify that the task
state is Complete.
6. On the Tasks tab, select each task that is in a
Waiting or Ready state, and then click Delete. Do not delete any tasks in a
Failed state.
7. Close the window.
8. Open the Process Administrator by going to IBM Business Automation
Workflow\_target object
store > Administrative > Workflow
System > Connection
Points > connection\_point.
Right-click the connection point and select Administer Work Items. The
administration connection\_point window is displayed.
9. Under Look for, select Workflows.
10. Under In, select Workflow Roster, which is the
same name as the solution.
11. Under Search mode, select Edit (all fields).
12. Click Find Now.
13. Click View > Show/Hide
Columns.
14. In the Column Selection window, add F\_CaseTask to
Selected Columns, then click OK. Verify that
F\_CaseTask is displayed in the Results window.
15. Use the task ID from step 5.c to
identify the workflow that is associated with each of the tasks that you promoted earlier.
Right-click the workflow and then click Tasks > Delete
Work.
16. Confirm that you want to delete the work items.
17. When the work items are deleted, you can go back to the case folder in step 3 and delete the folder and all its child objects.

## Preparing to reuse documents from cases to be deleted

1. In Administration Console for Content Platform
Engine,
go to the activity sequence folder: Year > Month > Day > number > activity\_sequence. For example, 2013 > 07 > 19 > 0166 > 000000100003.
2. Click the activity\_sequence then, in the right pane,
click the Contents tab and go to the supporting document folder, for example,
Correspondence.
3. Click the document and then click Properties in the new middle tab.
4. Scroll down, click the arrow next to the Associated Case property value
and select Unset Value, and then click Save.
5. In Administration Console for Content Platform
Engine,
right-click the activity\_sequence (for example, 000000100003), and then click
Delete.

## Deleting the case folder

1. In Administration Console for Content Platform
Engine,
navigate to the activity sequence folder: Year > Month > Day > number > activity\_sequence. For example, 2013 > 07 > 19 > 0166 > 000000100003.
2. Right-click activity\_sequence and then click
Delete.
3. Select Delete all objects and their content elements from all folders and
click OK.