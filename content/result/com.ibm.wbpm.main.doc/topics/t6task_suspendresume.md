<!-- image -->

# Suspending and resuming a task instance

## Before you begin

## About this task

You can suspend a task instance while it is running. You
might want to do this, for example, so that you can gather information
that is needed to complete the task. When the information is available,
you can resume the task instance.

## Procedure

1. Get a list of tasks that are claimed by the logged-on user.
FilterOptions fo = new FilterOptions();
fo.setSelectedAttributes("TKIID");
fo.setQueryCondition("STATE=STATE\_CLAIMED");
EntityResultSet result = task.queryEntities("TASK", fo, null, null);
This action returns a query result set that contains
a list of the tasks that are claimed by the logged-on user.
2. Suspend the task instance. if (result.getEntities().size() > 0)
{
  Entity entity = (Entity) result.getEntities().get(0);
  TKIID tkiid = (TKIID) entity.getAttributeValue("TKIID");
  task.suspend(tkiid);
}This action suspends
the specified task instance. The task instance is put into the suspended
state.
3. Resume the process instance. task.resume( tkiid );
This action puts the task instance into the state it
had before it was suspended.