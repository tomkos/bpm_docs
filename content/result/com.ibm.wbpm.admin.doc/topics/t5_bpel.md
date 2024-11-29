<!-- image -->

# Troubleshooting the administration of BPEL processes and human
tasks

## About this task

## Procedure

- The administrative console stops responding if you tryto stop a BPEL process application while it still has process instances. Before you try to stop the application, you must stop the BPELprocesses so that no new instances are created, and perform one ofthe following actions: Only then can you stop the process application safely. Note: Ifyou only want to prevent the creation of new process instances, stopthe business processes and not the application.
    - Wait for all of the existing process instances to end in an orderly
way.
    - Terminate and delete all of the process instances.
- The administrative console stops responding if you tryto stop a human task application while it still has task instances. To stop the application, you must:

1. Stop the human tasks so that no new instances are created.
2 Perform one of the following actions:
    - Wait for all of the existing task instances to end in an orderly
way.
    - Terminate and delete all task instances.
3. Stop the task application.
- A long-running BPEL process that is started by an invocation
task fails to start. A JSP snippet makes the invocation
task available to users. In the following example, the synchronous
calling pattern createAndCallTask is used. In this
case, the long-running BPEL process fails to start:HumanTaskManager htm = …
TaskTemplate taskTemplate = htm.getTaskTemplate( "start the process" );
Task task = htm.createAndCallTask( taskTemplate.getTKTID() );
while (task.getState() != TASK.TASK\_STATE\_FINISHED)
{
     Sleep(100);
}
A long-running process consists of several transactions
and its invocation style is asynchronous. Therefore it must be started
using the asynchronous calling pattern, createAndStartTask. HumanTaskManager htm = …
TaskTemplate taskTemplate = htm.getTaskTemplate( "start the process" );
Task task = htm.createAndStartTask( taskTemplate.getTKTID() );
while (task.getState() != TASK.TASK\_STATE\_FINISHED)
{
     Sleep(100);
}

In addition, the transaction attribute in the JSP deployment
descriptor must be set to NotSupported. This ensures
that the code snippet is executed without a transaction, and the createAndStartTask method
opens a new transaction to start the process instance. This transaction
is committed when the createAndStartTask method
returns, and the message is visible.
Include a "while" loop
for states other than the finished state. For example, if during the
execution of the process an activity fails, the end state might be
TASK.TASK\_STATE\_FAILED.