<!-- image -->

# Restarting a BPEL process

## About this task

If the process has more than one receive activity
or pick activity (also known as a receive choice activity) that can
create the process instance, all of the messages that belong to these
activities are used to restart the process instance. If any of these
activities implement a request-response operation, the response is
sent again when the associated reply activity is navigated.

## Procedure

1. Get the process that you want to restart. ProcessInstanceData processInstance = 
                    process.getProcessInstance("CustomerOrder");
2. Restart the process instance. PIID piid = processInstance.getID(); 
process.restart( piid );
This action restarts the specified
process instance.