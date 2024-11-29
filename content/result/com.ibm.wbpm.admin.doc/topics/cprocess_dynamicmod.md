<!-- image -->

# Dynamic modification of BPEL process instances

You can dynamically change the process navigation by jumping forward
and back in a process instance, and skipping activities within a process
instance. In these situations, you might also need to modify process
data that is contained in process variables so that the navigation
of the process instance can continue.

Business Process Choreographer Explorer, and the Business Process
Choreographer APIs support the dynamic modification of process instances
at run time. In addition, Business Space powered by WebSphere® supports
redoing parts of a process instance and skipping activities.

## Jump forward and back in a process instance

You
can use jumps within a process instance to dynamically modify a process
instance at run time. You can jump from one activity (source
activity) to another activity (target activity).
 The source activity must be a basic activity in one of the active
states; running, waiting, ready, claimed, or stopped. The target activity
can be a basic activity or a structured activity.

For the Jump API only: The source activity must
be a basic activity in the skipped, finished, failed, or expired state.
It must be the last activity that is navigated on the path that contains
the activity. The associated process instance must be in the suspended
state. When the process instance is resumed, navigation is continued
at the specified target activity.

The source activity is completed,
force-completed, or skipped as part of the jump action. After the
jump, the navigation of the process continues at the target activity.
You can jump forward in the process, that is, the target activity
occurs later in the process instance. You can also jump back to a
prior activity in the process.

Jumps are supported between activities in a sequence activity.
Jumps are also supported on paths without forks and joins in a generalized
flow activity and a parallel-activities activity (also known as a
flow activity). For all of these jump actions, the source and the
target activity must be on the same nesting level within the containing
activity.

Exit conditions on the source activity and for the
entry of the target activity are ignored by a jump action.

To
perform a jump action, you must be the scope administrator of the
enclosing scope, the process administrator, or the system administrator.

## Skip an activity

You can also dynamically
modify a process instance by skipping activities. You can skip a basic
activity that is in one of the active states or a basic activity that
might become active later in the process.

If an active activity
is skipped, the implementation of the activity is terminated, and
the navigation of the process continues after the activity. For example,
if the activity has outgoing links, process navigation continues with
the evaluation of the transition conditions of the links.

If
an activity is skipped that occurs later in the process flow, the
activity is marked for skipping. When the navigation reaches the activity,
the activity is skipped and the navigation continues after the activity.
You can cancel the skip request up until the navigation reaches the
activity.

To skip an activity, you must be the scope administrator
of an enclosing scope, the process administrator, or the system administrator.
In addition, if you are the activity administrator, you can skip an
activity that is currently active.

## Modify variables

When you change the flow
of a process instance at run time, you often also need to update variables
to ensure that the process can flow properly after the jumped or skipped
activity. For example, in a repair scenario you can provide valid
data before the jump action so that subsequent activities can run
successfully based on that data.

- Get the names of all the variables for a given activity
- Get the actual or initial value of a global or local variable
- Set the value of a global or local variable

To view the value of a variable, you must have at least
reader rights for the process or the enclosing scope. To update a
variable, you must be the scope administrator, the process administrator,
or the system administrator.

<!-- image -->