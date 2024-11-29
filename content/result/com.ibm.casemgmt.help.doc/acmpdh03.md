# Creating more than one in-basket in IBM
FileNet Process Designer

## About this task

For example, role A might want to see work from role B or
the supervisor role might want to see the work items from all roles. Or, role A
might want to see their work items in different views, for example, one view might show the status
and another view might show the arrival date.

If you define role A for a solution that is called My
Solution that has the solution prefix myso, Case Builder defines a queue name of
myso\_roleA. If you define role B for the same solution,
Case Builder defines a queue that
is named myso\_roleB. In addition, Case Builder defines a default role-based
queue in-basket for both roles. After you define these roles and complete the initial solution
definition in Case Builder, you
can create another in-basket in IBM
FileNet Process Designer so that you enable another
view for role B.

## Procedure

To create a new in-basket in IBM
FileNet Process Designer:

1 In a stand-alone IBMFileNet Process Designer , open the solution forediting the FileNet P8 activity workflow.
    1. In IBM
FileNet Process Designer, go
to File, click Solution, then edit.
    2. Go to the following path within the design object store: Click
Browse to browse the Root Folder, click IBM
Case Manager, click Solutions, enter the solution
name.
    3. Select the case type, and then open any activity.
2. Go to
View > In-baskets.
3. In the In-baskets tab, select the queue from the drop-down list,
select myso\_roleA, and then add or copy the in-basket.
4. In the Queue for in-baskets section click the Add
icon to create a new in basket for queue myso\_roleA.
Optionally, you can select an existing in-basket and click the Copy
icon. Then, edit the copied in-basket to remove, reorder, or add properties.
5. In the Create Columns and Labels tab, click the Add
icon to add properties to display for this in-basket.
You can also create filters for the in-basket.
6 Associate role B with the new in-basket. Note: Commit the changes in Case Builder to save the changes inIBMFileNet Process Designer . The results in role B having access to two different queuesmyso\_roleA and myso\_roleB . Even though roleB associates with the in-basket from role A queue, the primary queuefor role B is still myso\_RoleB . Therefore, if a step is addedto the role B swimlane in the Step Designer, that step is assigned tomyso\_roleB queue.

1. Go to
View > Roles.
2. Select role B and click the Modify icon in the
Select In-baskets and Members tab.
3. Select the new in-basket and click OK.