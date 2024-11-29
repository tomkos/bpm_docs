<!-- image -->

# Instance-based authorization roles for BPEL processes and activities

## Authorization roles for actions on BPEL processes

The
people assigned to process roles are authorized to perform the following
actions:

| Role                           | Authorized actions                                                                                                                                                                                                                                                                                                                                                                                                                   |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Process starter                | View the properties of the associated process instance, and its input and output messages.                                                                                                                                                                                                                                                                                                                                           |
| Process reader                 | View the properties of the associated process instance, and its input and output messages. Members of this role also automatically become the reader for activities, and the inline to-do tasks (including the subtasks, follow-on tasks, and escalations) that are associated with human task activities.                                                                                                                           |
| Process administrator          | Administer process instances, intervene in a process that has been initiated, create, delete, and transfer work items, change the navigation of the process at run time, for example, by skipping activities. Members of this role also automatically become the administrator for activities, and the inline to-do tasks (including the subtasks, follow-on tasks, and escalations) that are associated with human task activities. |
| Process activity administrator | Repair activities in a process.                                                                                                                                                                                                                                                                                                                                                                                                      |
| Scope reader                   | View the properties of the activities and variables in the scope. Members of this role also automatically become the reader for the properties of activities, and the inline to-do tasks (including the subtasks, follow-on tasks, and escalations) that are associated with human task activities in the scope.                                                                                                                     |
| Scope administrator            | Administer the activities in the scope, including updating variables for activities, skipping activities, and canceling skip requests. Members of this role also automatically become the administrator for activities, and the inline to-do tasks (including the subtasks, follow-on tasks, and escalations) that are associated with human task activities in the scope.                                                           |

The process starter is a role that is used by Business
Flow Manager for process navigation and the invocation of external
services. If a process instance still exists in the database, do not
delete the user ID of the process starter from your user registry
so that the navigation of the process can continue, unless you have
transferred the process ownership to another user.

| Role                           | People assignment                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Process starter                | The process starter can be specified by assigning an inline human task to the initiating receive or pick (receive choice) activity of a process.                                                                                                                                                                                                                                                                                                                                                    |
| Process reader                 | The process reader is specified by setting the reader role on the administration task that is associated with the process. This role is inherited by all of the activities in the process.                                                                                                                                                                                                                                                                                                          |
| Process administrator          | The process administrator is defined by an administration task that is assigned to the process. This role is inherited by all of the activities in the process.                                                                                                                                                                                                                                                                                                                                     |
| Process activity administrator | The process activity administrator is defined by an administration task that is associated with the process. The administrator role defined on this task is also used as the process activity administrator. Note: This administration task is different from the one that is used to determine the process administrator. The activity administration task that is defined on the process level is the default administration task for activities that do not have an administration task defined. |
| Scope reader                   | The scope reader is specified by setting the reader role on the administration task that is associated with the scope. This role is inherited by all of the activities in the scope.                                                                                                                                                                                                                                                                                                                |
| Scope administrator            | The scope administrator is defined by an administration task that is assigned to the scope. This role is inherited by all of the activities in the scope.                                                                                                                                                                                                                                                                                                                                           |

## Authorization roles for actions on activities

When
you model a human task and include it as a human task activity in
a BPEL process, the owner of the task automatically becomes the activity
owner. Members of roles that are defined for a human task inherit
the same role on the corresponding human task activity. Business Flow
Manager uses the activity roles for navigation and authorization. The
potential starters of an inline invocation task are the potential
starters of the associated receive or pick (receive choice) activity,
or the event handler.

The instance-based roles for activities
are authorized to perform the following actions:

| Role                       | Authorized actions                                                                                                             |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Activity reader            | View the properties of the associated activity instance, and its input and output messages.                                    |
| Activity editor            | Actions that are authorized for the activity reader, and write access to messages and other data associated with the activity. |
| Potential activity starter | Actions that are authorized for the activity reader. Members of this role can send messages to receive or pick activities.     |
| Potential activity owner   | Actions that are authorized for the activity reader. Members of this role can claim the activity.                              |
| Activity owner             | Work on and complete an activity. Members of this role can transfer their work items to an administrator or a potential owner. |
| Activity administrator     | Repair activities that are stopped due to unexpected errors, and force complete long-running activities.                       |

## Default people assignments for process roles

| Roles for BPEL processes   | If the role is not defined in the process model ...   |
|----------------------------|-------------------------------------------------------|
| Process administrator      | Process starter becomes process administrator         |
| Process reader             | No reader                                             |

In addition, if you do not define an invocation task
to create and start the BPEL process, the default people assignment
criteria, Everybody, is used for the potential
starters of the process.