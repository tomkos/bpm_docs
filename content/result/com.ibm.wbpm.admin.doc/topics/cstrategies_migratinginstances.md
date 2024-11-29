# Development strategies for migrating instances

See Snapshot and instance migration overview for an overview of the migration process.

## General principles

- Before you attempt an instance migration, make sure that the instances complete if orphaned
tokens are created on event gateways.
- Consider the process and its variables as the interface and process instances as
the realization of that interface.
- Depending on the settings,  you can migrate both active and closed tasks associated with a
process into the current process version. To avoid exceptions, ensure the process can resolve the
execution context for any migrated task.
- The new process version must be designed to provide backward compatibility
to instances that you want to migrate.
- If you have removed a task, it is sometimes possible to account
for the difference by moving the resulting orphaned token, although
there are limitations to this capability.

## Design-time considerations

In most cases,
deprecate entities that you no longer want rather than deleting them.
See the information about teams, undercover agents, services, and
variables for some specific examples of this advice.

Here are
some hints to aid you in successfully migrating instances.

- Do not change the SCA service interface on any receiving message
events, that is, the type of the message business object type, the
identifier of the service, and the correlation specification, including
its variable.
- Do not delete any receiving message event that is triggered by
SCA invocation.
- Do not rename or delete any variable that is used as a Process
Instance Identifier.
- Do not change the type nor the type definition of any variable
that is marked as a Process Instance Identifier.

- Having a process in a toolkit can result in process instances running in the toolkit. You cannot
migrate a process instance that is running in a toolkit.
- When all tokens in a process have ended or been deleted then the process will be completed.
Deleting orphaned tokens could lead to a process completing prematurely.

- It is recommended that you do not move objects between toolkits or the process application. This
could lead to broken references in your application, which will cause behavior similar that
encountered when the objects are deleted. Although you can fix broken references, you will still
have problems with instance migration, task migration, or running active tasks after migration (if
the execution context referenced the impacted objects).
- It is recommended that you do not delete toolkit references because this can lead to broken
references in your application.

- Do not change the type of environment variables.
- You can migrate runtime environment variable changes when snapshot data migration is triggered.
For more information, see Snapshot and instance migration overview.
- You can remove an environment variable as long as the process
no longer refers to it. Because environment variables are accessed
through JavaScript, removing them is less problematic than removing
local variables.

- New event subprocesses will not get tokens when instances are migrated. Any new event
subprocesses will only be executable for new instances.
- Tokens sitting on the start event of an event subprocess cannot be managed with an instance
migration policy file. This can lead to orphaned tokens if an event subprocess is deleted. However,
these orphaned tokens will not prevent the process from completing.
- If you accidentally removed an event subprocess, the revert option can be used on the containing
process to roll back to a previous version of the process. Replacing the existing event subprocess
with a new one will not enable you to move tokens from the existing subprocess to the new one.

- You can migrate runtime EPV changes when snapshot data migration is triggered. For more
information, see Snapshot and instance migration overview.
- Migrating the historical EPV data has a greater impact on task EPV lookups when
In-Progress Tasks Use New Values is not set. For more information, see Creating exposed process values (EPVs).

- For a parallel gateway, both branches must complete to complete
the process successfully. Therefore, if you choose to delete an orphaned
token on one branch of a parallel gateway, the process using the parallel
gateway will never be able to complete.

- If migration occurs while a task is running, the user interface from the old version is still
displayed. Refreshing or clicking Next has no effect. You need to restart or
claim the task after migration.
- If you must update the service of a task or coaches within the service and you want all existing
instances to use the new service or the updated coaches, programmatically move the active token back
to the activity that uses the service. For more information, see Managing tokens.
This action will restart the associated task.
- If an inline user task in a process was postponed before the migration and the process was
modified, programmatically move the active token back to the activity that uses the service. For
more information, see Managing tokens. This action will restart the associated
task.

- You can add a linked process if there is no token to be honored.

- You can merge team contents when snapshot data migration is triggered. For more information, see
Snapshot and instance migration overview.
- Do not change the assignment of a task to a new team. A team is determined when the task is
created, not when the task is claimed or migrated. If a task is assigned the Employees role in the
original instance, that assignment is migrated to the new instance. Only members of that team can
claim the task.
- Avoid deleting teams and the deprecated dynamic task assignment options because existing tasks
will be unable to migrate their associated team to the target snapshot. The tasks will continue to
use the teams associated with the source snapshots and will prevent the source snapshot from being
deleted until the tasks are deleted.

- If a service was used but is no longer needed, leave it in the
process application but mark it as deprecated. You can change the
service to a no-operation service by directly joining the start event
to the end event in your diagram.

- As part of the instance migration, active and completed tasks are migrated depending on the
migrate-tasks setting.
- Don't change the assignment of a task to a new team. See the section about Teams in this
topic.
- Orphaned tokens associated with tasks can be moved or delete. See the section about Orphaned
tokens in this topic. When the tokens are moved or deleted the current task is completed.
- In some cases, you must restart the task to pick up changes like variable definition changes.
Tasks can be restarted only by using the move REST API.
When
moving the token back to the same activity, the previous task is completed and a new version of the
task is started.

- An undercover agent (UCA) responds according to the settings from
the old snapshot. That is, an active UCA still listens to events from
the tip or from a previous version, even after migration. Therefore,
do not delete or replace a UCA.

- Your new process version or service must provide backward compatibility to the instances that
you want to migrate.
- Do not remove variables.
- Do not rename variables, or if you must, introduce the new variable
with a new name, and deprecate the old variable. In this case, deprecating
means to leave the variable unchanged and do not use it any more.
- Do not change the type of your variables, for example from a simple
to a complex variable. If you must change a variable type, introduce
a new variable with the new type, and deprecate the old variable.
- Business object definitions are versioned like other snapshot artifacts. The definition versions
being used by process or task variables are not updated after they have been instantiated, which
might lead to behavioral differences between new and existing instances if the variable definitions
change.
- If new process variables are added, they are null or initialized with their default values if
they are defined. Ensure existing instances can handle these new variables regardless of where in
the process the tokens are when the variable is added.

- You can move tokens between process activities but not between the events attached to those
activities. One or more events can be attached to an activity; they are stored in a collection
that is a property of the activity object. Therefore, when a token is moved from one activity to
another in a process diagram, an event attached to the next activity becomes active only when that
activity is reached.
For more information, see Modeling
message events.
- If you migrate currently running instances to a new version of the snapshot, problems can occur
if the new version removes steps or other components from the process. When instances that are
running on a server have tokens on process or service-level components that were removed in the new
snapshot, the migration can fail. Tokens indicate where a runtime instance is running. Tokens can be
present on an activity, a conditional sequence line, a coach, a service call, and numerous other
elements.
For more information about orphaned tokens and advice about how to move or delete
them, see Managing tokens.