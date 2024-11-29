# Identify infinite loops in process applications

- An infinite loop between activities in a BPD. An infinite loop
can occur in a BPD. For example, if there is conditional logic that
is implemented by a gateway where the process flow loops back to a
system task based on the value of a variable, and the exit condition
never occurs, the loop might not exit. After you identify the process
that is running for a long time, you can view the process steps, and
if you see a step that has a large number of total steps, you might
have an infinite loop within a BPD. You can identify the process instance
in the Process Inspector by using the process
id, and terminate the process.
- An infinite loop between service steps in an integration service.
If a process is running with a large number of steps within a particular
service, you might have an infinite loop within the service. Go to
the Services page and use the Halt
Service button to interrupt the service.
- An infinite loop within a server script step. For example, a JavaScript
block that is in a continuous loop, which is  usually indicated by
a single JavaScript activity that is taking a lot of time. Note: The Halt
Process button cannot interrupt a currently running JavaScript.
- An infinite loop between and event producer and an event consumer.
For example, a process that loops between message send and message
receive events. This situation might be indicated by many instances
of a process being created in a very short duration.

## Example: Infinite loop in a BPD

- From the Most Expensive Processes list
in the Summary page, you can identify the process
app that is taking the longest time. The list shows the total time
for each process, which includes the time that is taken by the services
within the process.
- You can drill into a process to view the time that is taken by
each step in the process (total duration), and the number of times
a step has been executed (total instances).

<!-- image -->

<!-- image -->

<!-- image -->