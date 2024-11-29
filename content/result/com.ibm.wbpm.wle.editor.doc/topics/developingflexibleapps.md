# Developing flexible and efficient process applications

## About this task

## Procedure

- If your process includes user tasks that involve a simple decision, such as to approve or
reject a request or to choose between a set of options, you can design the task so that the business
user can complete it in Process Portal without
having to open the coach for the task. Instead, the user clicks a button or chooses between the
options with a single click.
- If your process must have a low latency, for example, to achieve a
business service level agreement, you can enable the optimization of execution for latency. This
optimization means that one path through the process is performed using a single thread on a cluster
member, other paths are scheduled to use the default shared pool of threads.
- Sometimes multiple sequential tasks in a process are assigned to the same user. You can
configure individual activities to launch automatically if they are assigned to the same person as
the previous task.  In Process Portal, if the
owner of the first task is the same as the owner of the second, the second task will launch
automatically when the first task is complete.
- Not all process activities run predictably in each execution of a process. Sometimes a
user must launch a new task that is outside of the normal process flow. For example, they might need
to cancel the process or they might need to complete a separate but related business action, such as
updating customer contact information. Ad hoc processes are actions that you can expect users to do
at some point during at least some process instances. You can add ad hoc start events and subsequent
activities to your process, and the business user is able to launch the ad hoc process from the
Process Portal environment.

- Configuring activities for inline completion (deprecated)

Some activities in your process application can be completed with a single action, such as an approval, rejection, or a simple decision. Using the services provided in the system toolkit in Process Designer, you can configure these activities to be performed by the business user in Process Portal with a single click action that does not necessitate the user opening the coach interface.
- Optimizing process execution for latency

Select the optimization for latency to reduce thread context-switching for processes that require low latency responses. When enabled, this optimization causes the process instance to keep its execution thread rather than releasing it back to the pool of threads that are shared between activities.
- Automatically starting the user's next task

To help your business users be maximally efficient while they are using your application, consider places in your process where you expect the same user to be completing multiple tasks in sequence.
- Defining ad hoc actions (deprecated)

While a process is running, a user might need to launch a new activity or set of activities, such as updating a customer's contact information or canceling the process instance. The designer can define a set of these unplanned, or ad hoc, actions to be launched by the user fromProcess Portal.