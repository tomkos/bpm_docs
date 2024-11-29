<!-- image -->

# Repairing activities

## About this task

The Business Process Choreographer API provides the forceRetry and forceComplete methods
for repairing activities. Examples are provided that show how you might add
repair actions for activities to your applications.

- Forcing the completion of an activity

Activities in long-running processes can sometimes encounter faults. If these faults are not caught by a fault handler in the enclosing scope and the associated activity template specifies that the activity stops when an error occurs, the activity is put into the stopped state so that it can be repaired. In this state, you can force the completion of the activity.
- Retrying the execution of a stopped activity

If an activity in a long-running process encounters an uncaught fault in the enclosing scope and if the associated activity template specifies that the activity stops when an error occurs, the activity is put into the stopped state so that it can be repaired. You can retry the execution of the activity.
- Repairing activities that stopped because a join, loop, or counter evaluation failed

Activities can stop because an exception occurred when a join or loop condition, or a forEach counter value was evaluated. The administrator decides not to retry the execution of the activity, for example, because the evaluation might fail again. In such cases, the correct values for the expression can be supplied using the Business Process Choreographer EJB API so that the navigation of the process can continue.
- Updating correlation sets associated with stopped activities

Correlation sets are used to support stateful collaboration between web services. In such cases, the correct values for the expression can be supplied using the Business Process Choreographer EJB API so that the navigation of the process can continue.