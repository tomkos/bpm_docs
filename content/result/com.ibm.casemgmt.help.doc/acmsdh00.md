# Adding and deploying a case management solution

## About this task

A solution consists of roles, case types, properties, document categories, and in-baskets. Each
case type contains business rules, views, and activities that are essential for case closure. The
wizard helps building the solution by seamlessly configuring roles, case types, properties, and
document classes. After the solution assets are added, users can add activities and corresponding
steps in the case type section of the user interface.

Each activity can contain a workflow that must be followed to complete the activity. Steps within
a workflow connect through a route defined by connectors. An existing workflow can be reused from a
business process management system.

- A role-based in-basket, which is optional.
- A personal in-basket, which can be common, or based on a role.
- An all-assigned work in-basket.

## Procedure

To build and deploy a solution:

1. You can use Workflow Center or  Case Builder to add a solution that
case workers access from the Case administration client. For more information, see
Adding a solution.
2. To incorporate roles into the solution, see Adding and selecting roles. To add document classes,
see Adding and modifying document classes, and to define properties, see Adding and reusing properties.
3. You can add case types by using the wizard or from the solution home page. For more
information, see Adding and modifying case types.
4. Add properties, views, case folders, business rules, and activities to the case types. For more
information, see Case types, Designing views, Business rules,
and Adding activities.
5. Add steps to the activities. For more information, see Adding activities in solutions.
6. Design the client application by customizing the page layouts. For more information, see Designing the case management client application.
7. Save and close the solution, then commit your changes.

Note: Multiple users can edit solutions simultaneously.
8. If Case Builder is integrated
with a Version Control System (VCS), deliver the changes for the solution. 
Note: When integrated with a VCS, Case Builder enables committing changes,
allowing users to include comments and provide parameter values. Delivering the solution then
establishes a baseline snapshot in
the VCS with the applied changes.
9. Deploy the solution to your development environment and test it in the Case Client.

Important: Each user adding a solution must use their own user ID. Editing the same
solution in multiple browser sessions can result in lost changes.
10. Request the IT administrator to deploy the solution into a production environment with the
Case administration client. Additionally,
configure security for the case types in IBM Administration Console for
Content Platform Engine. For more information,
see Testing your solution.

## Results

- Adding a case solution

A case solution consists of one or more related case types that provide the documents, data, business processing and routing to the case workers. For example, a case solution for a human resources department might include a case type for new hires, a case type for retirement, and a case type for resource actions.
- Promoting case solutions to workflow projects

You can use the Case Builder to promote a case solution to a workflow project, which will enable you to create new case activities that use workflow processes.