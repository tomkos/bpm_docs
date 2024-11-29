<!-- image -->

# People query result post-processing plug-in

You can create a plug-in to add or remove users, or to change user
or group information. You can also use the plug-in to change the result
type, for example, from a list of users to a group, or to everybody.

You can have only one post-processing plug-in; this means that
the plug-in must handle the people query results from all tasks. Your
plug-in can add or remove users, or change user or group information.
It can also change the result type, for example, from a list of users
to a group, or to everybody.

Because the plug-in runs after people resolution completes, any
rules that you have to preserve confidentiality or security have already
been applied. The plug-in receives information about users that have
been removed during people resolution (in the HTM\_REMOVED\_USERS map
key). You must ensure that your plug-in uses this context information
to preserve any confidentiality or security rules you might have.

These classes run in the context of a Java™ Platform, Enterprise Edition (Java EE) Enterprise application. The classes can invoke methods
of other classes. Ensure that the class that you implement and its
helper classes follow the EJB specification. You must implement all
of the methods in the interface. These methods include information
relating to the people assignment criteria for the specific task template,
task or escalation role.

## Choice of interfaces

To implement post-processing
of people query results, you can either use the StaffQueryResultPostProcessorPlugin interface or the StaffQueryResultPostProcessorPlugin2 interface. Both these interfaces have methods for modifying the
query results for tasks, escalations, task templates, and application
components.

If you are implementing a new plug-in, use the
newer StaffQueryResultPostProcessorPlugin2 interface,
which can provide better performance for cases where the post-processing
will yield the same result for a specific task role or escalation
role across all task instances or escalation instances that are based
on the same task template. This interface provides methods for getting
the assignment reason and other application context information about
the task template, escalation template, task instance or escalation
instance.