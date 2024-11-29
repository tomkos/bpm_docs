<!-- image -->

# Relationship between human tasks and BPEL processes

Invocation tasks can be associated with receive or pick (receive
choice) activities, or on-event event handlers. These tasks can be
both inline or stand-alone tasks. If you are using the Business Flow
Manager API, only inline invocation tasks can influence the authorization
for invoking the receive or pick activity. By default, everybody is
allowed to send a message to receive or pick activities, or to on-event
event handlers. This includes invoking a BPEL process in the case
of initiating receive or pick activities.

An administration task is associated with every BPEL process. The
administration task determines who is authorized to administer and
read the process. If an administration task is not modeled in IBM® Integration
Designer for
the process, an administration task is created at run time. This task
ensures the default authorization for the BPEL process; the process
starter becomes the only administrator of the process, and readers
are not assigned to the process.

You can model an administration task for each invoke or snippet
activity. This task determines who is allowed to administer the activity
in addition to the process administrators. You can also model a default
activity administration task that applies to every invoke or snippet
activity that has no explicit administration task assigned to it.

Invoke activities have an administration task associated with them.
For snippet activities and synchronous invoke activities, this task
is created only when the activity is stopped after an invocation failure.
The administration task is then used to handle repair requests, such
as force finish and force retry. For asynchronous invoke activities,
the administration task is always created. Thus, an administrator
can force retry or force finish the activity while the activity waits
for the asynchronous response.

Stand-alone to-do tasks can implement asynchronous invoke activities.
These activities also have an administration task associated with
them. Inline to-do tasks implement human task activities. An administration
task is created for these activities at run time.