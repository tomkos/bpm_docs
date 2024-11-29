<!-- image -->

# Terminating a process instance

## About this task

Because
a process instance terminates immediately, without waiting for any
outstanding subprocesses or activities, you should only take this
action in exceptional situations.

## Procedure

1. Retrieve the process instance that is to be terminated.
ProcessInstanceData processInstance = 
       process.getProcessInstance("CustomerOrder");
2. Terminate the process instance. If you terminate
a process instance, you can terminate the process instance with or
without compensation. 
To terminate the process instance with
compensation:PIID piid = processInstance.getID();
process.forceTerminate(piid, CompensationBehaviour.INVOKE\_COMPENSATION);
To
terminate the process instance without compensation:PIID piid = processInstance.getID();
process.forceTerminate(piid);
If
you terminate the process instance with compensation, the compensation
of the process is run as if a fault had occurred on the top-level
scope. If you terminate the process instance without compensation,
the process instance is terminated immediately without waiting for
activities, to-do tasks, or inline invocation tasks to end normally. 
Applications
that are started by the process and stand-alone tasks that are related
to the process are not terminated by the force terminate request.
If these applications are to be terminated, you must add statements
to your process application that explicitly terminate the applications
started by the process.