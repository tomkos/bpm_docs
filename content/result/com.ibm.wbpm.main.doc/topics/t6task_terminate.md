<!-- image -->

# Terminating a task instance

## Procedure

1. Retrieve the task instance to be terminated. Task taskInstance = task.getTask(tkiid);
2. Terminate the task instance. TKIID tkiid = taskInstance.getID();
task.terminate(tkiid);The task instance
is terminated immediately without waiting for any outstanding tasks.