# Creating loops for an activity

## Loop types

You can create and implement loops in several ways. For example, you can include a script
component in a service that iteratively processes records that you retrieve from a database until
all records are processed. Because you can include JavaScript throughout your implementations, you
can easily develop the logic to repeat an action until a certain condition is true.

In addition to implementing loops with scripts, you can configure your process activities for
simple and multi-instance loops, as described in the following table. When you want the runtime task
that results from an activity to be run more than once, you can configure loop behavior for that
activity. You can only configure loop behavior for activities that have incoming or outgoing
sequence flows.

| Loop type           | Description                                                                                                                                                                                                                                                                                                                                                                                                                         |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Simple loop         | When you model an activity with simple loops, the required number of instances is dynamically created, up to the loop maximum value that you specify. A simple-loop activity is run sequentially until the last instance of the activity is run. When you run an activity that is configured for simple loops, a single token is generated and used for each instance of the activity, which, in effect, recycles the runtime task. |
| Multi-instance loop | A multi-instance loop dynamically runs multiple unique instances of the same activity sequentially or in parallel. When you run an activity that is configured for multi-instance loops, a unique token is created for each instance of the activity.                                                                                                                                                                               |

## Performance

Simple and multi-instance loops create tasks from the number of steps in an activity, up to the
maximum number that is specified in the configuration. Loops are not designed to handle hundreds of
tasks or large variable sets to be sent and reviewed. Rather, they are designed for a small number
of tasks, typically less than ten. A higher number might significantly affect performance.
Therefore, preferably set the maximum number of loops to less than 10. For example, if for a hire
approval task, three interviewers out of five need to approve the candidate, you set the approval
task to loop five times and the system creates five tasks. After three of the interviewers approve,
the remaining two tasks are closed and the next step in the activity starts.

For cases where you need to loop over more than 10 tasks, create a load test scenario and test
whether your loop works for your application design. If the loop runs slower than expected, you
might need to change the application accordingly. For example, if your loop of tasks is a process
with many steps and multiple coaches (rather than just one), consider the following approach: use an
undercover agent (UCA) to call a start message event (SME) to create more related instances from
that point, which are worked in parallel to the parent instance on different threads. This way, the
bottleneck is moved from one thread on one server to many threads (M) on many nodes (N).

- Configuring a process activity for simple loops

Follow these steps to configure an activity for simple loops.
- Configuring an activity for multi-instance loops

Using multi-instance loops, you can dynamically run multiple unique instances of the same activity sequentially or in parallel. When you run an activity that is configured for multi-instance loops, a unique token is created for each instance of the activity.
- Associating loop activity instances with different items

In multi-instance loops, you can associate each instance of an activity with a list item.