# Managing tokens

Think of a token as an active execution step within the process. To ensure process instances run
successfully, you might need to move or delete the related tokens during or after instance
migration.

Tokens exist on each active activity and each timer and message event on an active activity. When
instance migration causes orphaned tokens, you must decide what to do with potential orphaned tokens
or risk that the process instances won't complete. For example, you installed a new version of a
process application. The new version cleaned up a number of activities that are no longer used from
the earlier version. However, there are tokens that still exist for some of these unused activities.
You must either delete or move these orphaned tokens or the migrated process instances might be
unable to complete.

When orphaned tokens are deleted or moved, the process instance tries to resume at the next
activity that contains tokens. If no tokens exist, the process completes. For example, if you have
an activity that contains three tasks (Task A, Task B, and Task C) and Task A is currently running,
Task A has the token. If you delete the token while Task A is running, Task B and Task C won't run
and the process instance is considered complete.

The easiest way to identify and manage orphaned tokens is to generate a migration policy file and
use it to specify whether each potential orphaned token should be moved or deleted during instance
migration. If you migrate process instances without using a policy file, orphaned tokens might be
created. In this case, you can use the REST API client to delete or move these orphaned tokens. You
can also use the web Process Inspector to delete orphaned tokens.

You might also need to move tokens or reset tasks that are not orphaned. In these cases you must
use REST APIs. When a token is moved to the same activity, it resets the associated task, which
completes the previous task and generates a new copy of the same task. This approach is especially
helpful when you must incorporate variable definition changes that might have been made to the
task's variables.

## Important considerations

Take care when making decisions
about whether to delete or move tokens. Here are some of the specific
cases to keep in mind while you are making those choices:

- Make sure that the instances complete if orphaned tokens are created on event gateways before
you migrate an instance.
- You can move an orphaned token from one activity to another activity
in the same process or subprocess.
- You can move an orphaned token from an activity in a process to
an activity in any of its subprocesses.
- You can move an orphaned token from an activity in a subprocess
to an activity in its parent process.
- You cannot move an orphaned token from an activity in an event
subprocess to an activity outside that event subprocess.
- You cannot move an orphaned token from an activity outside an
event subprocess to an activity in that event subprocess.
- You cannot move an orphaned token in a linked process to its parent
process or to another linked process.
- You can only delete or move a token that is a leaf node in the
execution tree; any parent orphaned tokens will be handled implicitly.
For example, suppose an activity implemented as a subprocess is deleted
in a new snapshot. Deleting an orphaned token in the subprocess will
also delete the orphaned token on the parent activity.
- For a parallel gateway, both branches must complete to complete
the process successfully. Therefore, if you choose to delete an orphaned
token on one branch of a parallel gateway, the process using the parallel
gateway will never be able to complete.
- When you move a token, you are actually deleting it from one activity
and creating a new copy of it attached to a different activity. This
behavior creates a limitation if you are using multiple instances
of nested business objects. For example, if you have an activity that
has three tokens associated with it and you move those tokens to a
second activity, only one token is created on the second activity.

| Source Activity Location   | Target in Same Process    | Target in Parent Process    | Target in Child Subprocess 	   | Target in Child Event Subprocess 	   | Target in Child Linked Process   |
|----------------------------|---------------------------|-----------------------------|--------------------------------|--------------------------------------|----------------------------------|
| Process                    | Yes                       | N/A                         | Yes                            | No                                   | No                               |
| Subprocess                 | Yes                       | Yes                         | Yes                            | No                                   | No                               |
| Event subprocess           | Yes                       | No                          | Yes                            | No                                   | No                               |
| Linked process             | Yes                       | No                          | Yes                            | No                                   | No                               |

- Generating an instance migration policy file to manage orphaned tokens

Use a policy file to proactively compare snapshots before instance migration to identify the potential locations of orphaned tokens and specify whether each orphaned token should be deleted or moved.
- Changing the security policy

If you are upgrading from an earlier version of IBM® Business Automation Workflow, you might need to configure the security policy before you can move or delete a token.