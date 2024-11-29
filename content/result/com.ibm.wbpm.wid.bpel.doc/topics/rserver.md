<!-- image -->

# Server tab: BPEL process editor

- Process and most activities
- Invoke, snippet, data map, and human task activities
- Receive and receive choice activities

## Process and most activities

## Invoke, snippet, data map, and human task
activities

- Commit before
- Use this setting if the transactions that precede it must be
fully committed before it can begin. This activity will still tolerate
being in a transaction with other activities that follow it.

- Commit after
- Use this setting if your activity must be committed immediately
after it has completed. This activity will still tolerate being in
a transaction with other activities that precede it.

- Participates
- Use this setting if this activity does not require a commit to
occur either before or after it, and where it can coexist within a
transaction where one or more other activities will be invoked.

- Requires own
- Use this setting when this activity must be isolated within its
own transaction.

If you need guaranteed
transaction boundaries, it is a good practice to factor out the business
logic that needs to be executed in a single transaction into a microflow
and invoke it as a subprocess. The logic of a microflow is always
run in a single transaction.

- Same as Process
- Select this to match the Continue processing upon unhandled
faults setting for this activity to that of the BPEL process.
This default setting can be configured in the Defaults tab for the
process as a whole. If you set this activity to match this default
setting, then it will change should the default setting change. This
is especially useful in programming situations when the Continue
processing upon unhandled faults setting may need to be changed,
and you don't want to have to manually modify it for each individual
activity.

- No
- When No is chosen, and there is no fault
handler defined on the enclosing scope, then the activity is put into
the stopped state, and a work item for the process administrators
is created so that the problem can be repaired. Potentially, this
option allows you to simply pause the process to have the problem
fixed. This is especially useful in a process that has been running
for a long time. This setting overrides the default setting.

- Yes
- When Yes is selected, then in the event
of a fault during process execution, the fault is sent to the fault
handler of the activity's enclosing scope. If this is insufficient
to deal with the fault, then it is rethrown to the next enclosing
scope. If the fault reaches the outermost scope, the process terminates.
This setting overrides the default setting.

## Receive and receive choice activities

The
contents of the Server tab depend on whether you have the Create
a new process instance if one does not already exist check
box selected on the Details tab.

- Commit After
- Use this setting if the new process instance must be committed
immediately after the receive activity or the receive case of the
receive choice activity has completed. This setting is appropriate
if you invoke the process instance using a synchronous API call.

- Participates
- Use this setting if new process instance does not require a commit
after the receive activity or the receive case of the receive choice
activity has completed. This setting is required if you want to invoke
the process instance using the API initiateAndClaimFirst() which
allows you to create a new process instance and immediately claim
the first human task. .

If you need guaranteed
transaction boundaries, it is a good practice to factor out the business
logic that needs to be executed in a single transaction into a microflow
and invoke it as a subprocess. The logic of a microflow is always
run in a single transaction.

## Related concepts

- Key concepts for BPEL business processes
- Working with BPEL extensions
- Choosing between long-running processes and microflows
- Best Practice: When to not use the BPEL extensions

## Related tasks

- Compensating activities in a long-running process
- Compensating a microflow