<!-- image -->

# Continue processing upon unhandled faults

## About this task

## Procedure

1 Select one of the following types of activities:
    - invoke activity
    - human task activity
    - snippet activity
    - data map activity
2. In the Server tab of the Properties area, configure the Continue processing
upon unhandled faults field according to the following
three options:

Option
Description

Same as process
Select this to match the Continue processing upon
unhandled faults setting for this activity to that of
the BPEL process. This default setting can be configured in the Defaults tab for the process as a whole. If you set this activity
to match this default setting, then it will change should the default
setting change. This is especially useful in programming situations
when the Continue processing upon unhandled faults setting may need to be changed, and you don't want to have to manually
modify it for each individual activity.

No
When No is chosen, and there is no fault handler defined
on the enclosing scope, then the activity is put into the stopped
state, and a work item for the process administrators is created so
that the problem can be repaired. Potentially, this option allows
you to simply pause the process to have the problem fixed. This is
especially useful in a process that has been running for a long time.
This setting overrides the default setting.

Yes
When Yes is selected, then in the event of a fault
during process execution, the fault is sent to the fault handler of
the activity's enclosing scope. If this is insufficient to deal with
the fault, then it is rethrown to the next enclosing scope. If the
fault reaches the outermost scope, the process will terminate. This
setting overrides the default setting.

## Results

## Related concepts

- Fault activities
- Raising faults
- BPEL process compensation
- Fault handling and compensation handling in BPEL processes

## Related tasks

- Using fault handlers
- Typing fault variables

## Related information

- Continue-on-error behavior of BPEL processes and activities