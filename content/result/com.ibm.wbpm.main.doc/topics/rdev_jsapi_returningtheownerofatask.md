# Returning the owner of a task

```
var user = tw.system.currentTask.assignedTo;
```

It
returns a TWUser object.

The name property
can be used to determine the userid of the user that claimed the task.