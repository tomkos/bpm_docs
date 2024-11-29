<!-- image -->

# Suspending and resuming a BPEL process

## Before you begin

## About this task

You might want to suspend a process instance, for example,
so that you can configure access to a back-end system that is used
later in the process. When the prerequisites for the process are met,
you can resume the process instance. You might also want to suspend
a process to fix a problem that is causing the process instance to
fail, and then resume it again when the problem is fixed.

To
suspend a process instance, it must be in the running or failing state.
The caller must be a process administrator or a system administrator. However,
if Business Flow Manager is using the alternative process administration
mode that restricts process administration to system administrators,
then only callers in the BPESystemAdministrator role can perform this
action.

## Procedure

1. Get the running process, CustomerOrder, that you want to
suspend. ProcessInstanceData processInstance = 
                    process.getProcessInstance("CustomerOrder");
2. Suspend the process instance. PIID piid = processInstance.getID(); 
process.suspend( piid );
This action suspends the specified
top-level process instance. The process instance is put into the suspended
state. In this state, activities that are started can still be finished
but no new activities are activated. Subprocesses with the autonomy
attribute set to child are also suspended if they are in
the running, failing, terminating, or compensating state. Inline tasks
and stand-alone tasks that are associated with this process instance
are not suspended.
3. Resume the process instance. process.resume( piid );
This action puts the process instance and its subprocesses
into the states they had before they were suspended.