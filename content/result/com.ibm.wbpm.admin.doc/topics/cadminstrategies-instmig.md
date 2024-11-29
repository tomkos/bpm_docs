# Administrative strategies for migrating snapshots and instances

Also, check for orphaned tokens before you migrate instances. If potential orphaned tokens are
found, have your development team complete the 'instance migration policy file'. For more
information, see Generating an instance migration policy file to manage orphaned tokens.

- (Optional)Use blackout periods to prevent events from firing during the
migration. In the Process Admin Console Event Manager, schedule a blackout period so events are not
activated during instance migration. For more information, see Creating and maintaining blackout periods.
- Suspend all process instances for a particular snapshot by running the
BPMDeactivate command and by using the
-suspendAllBPDInstances parameter. Use the
BPMProcessInstancesResumption command to resume the instances after the migration
is completed. For more information, see BPMDeactivate command and BPMProcessInstancesResumption command.

- Number of instances to migrate
- Number of tasks to migrate
- The execution context size for instances and tasks - Execution context size is impacted mainly
by the complexity of the process or task and the variable sizes.
- The complexity of the processes
- How fast the database performs the write actions.

Performance improves if tasks are cleaned up before instances are migrated. To clean up
tasks, you can use the BPMTasksCleanup command. For more information, see BPMTasksCleanup wsadmin command.

- <thread-pool-size> - Use this option to set how many concurrent threads
are used to process the instance migrations. Increasing the thread pool size in turn increases the
load on the system and database while reducing the instance migration total time.
- <migrate-tasks> - Use this option to choose which tasks are migrated
during instance migration. If fewer tasks are migrated, the performance improves. Note: If tasks are
not migrated, deleting the source snapshot might be blocked.
- <defer-ec> - Use this option to defer when the task execution contexts
are updated. If this option is enabled, execution context is updated when the task is first used,
which reduces the instance migration time but might impact task usage.