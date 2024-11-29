<!-- image -->

# Task authorization and work items

Every task role enables users to carry out an exact set of actions
on the associated task. A person's authorization is managed using work items.
A work item represents the relationship of the assigned person to the task
actions implied by the task role.

- The identity of a user or user group
- The identity of the object, for example, human task
or BPEL process, upon which actions can be performed
- The task role that the users are associated with

- As exactly one user ID. This leads to a user work item.
- As exactly one user group ID. This leads to a group work item.
- For every user by using the Everybody people assignment
criteria. This leads to an Everybody work item.

- The user logs in with a user ID that matches the specified user ID for
the user work item
- The logged-on user is a member of the group that corresponds to the specified
group ID for the group work item
- The work item is a work item that is assigned to everybody

The Human Task Manager API provides methods for querying human tasks, escalations,
and other objects. When a query is run, a user's authorization to see the
queried data is ensured by returning only the data for which the user has
a work item. You can also use the API to manage instance-based authorization.
This is done by creating and deleting work items, and by transferring work
items between people. For more information on these API methods, see the Javadoc
for the HumanTaskManager interface in the com.ibm.task.api package.