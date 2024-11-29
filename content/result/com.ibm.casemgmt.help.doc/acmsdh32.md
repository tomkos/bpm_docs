# Swimlanes

A swimlane is a partition in the Step Designer canvas
that organizes the role or workgroup responsible for a step. You can
drag and drop steps only to a role or workgroup swimlane in the canvas.
After a step is first assigned to a swimlane, you can move it to another
swimlane only by updating the Swimlane step
property.

You can add two types of swimlanes to the
canvas: role lanes and workgroup lanes. You can assign any role that
is defined in the solution to a role lane. Any steps added to a role
lane are assigned to case workers in that role. You can add workgroups
in Manage Workgroups. Any steps that are added
to a workgroup lane will be in the personal in-basket for users that
are assigned to that workgroup.

| Roles                                                                                          | Workgroups                                                                                                                                                                                                                     |
|------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Roles are created at the solution level and can be reused for more than one task or case type. | Workgroups can be created at the task level. You can also select predetermined workgroups that you create in Case Builder or in IBM® FileNet® Process Designer.                                                                |
| Each role is assigned an in-basket at the solution level.                                      | Workgroups do not have in-baskets. Work assigned to workgroup members is located in the personal in-basket for the member.                                                                                                     |
| The Content Platform Engine creates a work queue for each role in the solution.                | Workgroups are not assigned to a queue. Each member of the workgroup receives the work item. When a work item (step) is assigned to a workgroup to complete, all members of the work group must process and complete the item. |