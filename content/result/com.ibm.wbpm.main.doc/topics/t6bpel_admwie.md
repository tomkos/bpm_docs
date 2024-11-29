<!-- image -->

# Managing work items

## About this task

A work item represents the assignment of an object to
a user or group of users for a particular reason. The object is typically
a human task activity instance, a process instance, or a task instance.
The reasons are derived from the role that the user has for the object.
An object can have multiple work items because a user can have different
roles in association with the object, and a work item is created for
each of these roles. For example, a to-do task instance can have an
administrator, reader, editor, and owner work item at the same time.

The
actions that can be taken to manage work items depend on the role
that the user has, for example, an administrator can create, delete
and transfer work items, but the task owner can transfer work items
only.

## Procedure

- Create a work item. FilterOptions fo = new FilterOptions();
fo.setSelectedAttributes("TKIID");
fo.setQueryCondition("NAME='CustomOrder'");
EntityResultSet result = task.queryEntities("TASK", fo, null, null);

if (result.getEntities().size() > 0)
{
  Entity entity = (Entity) result.getEntities().get(0);
  TKIID tkiid = (TKIID) entity.getAttributeValue("TKIID");
  // create the work item
  task.createWorkItem(tkiid, WorkItem.REASON\_ADMINISTRATOR,"Smith");
}This action creates a work item
for the user Smith who has the administrator role.
- Delete a work item. FilterOptions fo = new FilterOptions();
fo.setSelectedAttributes("TKIID");
fo.setQueryCondition("NAME='CustomOrder'");
EntityResultSet result = task.queryEntities("TASK", fo, null, null);

if (result.getEntities().size() > 0)
{
  Entity entity = (Entity) result.getEntities().get(0);
  TKIID tkiid = (TKIID) entity.getAttributeValue("TKIID");
  // delete the work item
  task.deleteWorkItem(tkiid, WorkItem.REASON\_READER,"Smith"); 
}This action deletes the work item
for the user Smith who has the reader role.
- Transfer a work item. FilterOptions fo = new FilterOptions();
fo.setSelectedAttributes("TKIID");
fo.setQueryCondition("NAME='CustomerOrder' AND
  STATE=STATE\_READY AND
  WI.REASON=REASON\_POTENTIAL\_OWNER AND
  WI.OWNER\_ID='Miller'");
EntityResultSet result = task.queryEntities("TASK", fo, null, null);

if (result.getEntities().size() > 0)
{
  Entity entity = (Entity) result.getEntities().get(0);
  TKIID tkiid = (TKIID) entity.getAttributeValue("TKIID");
  // transfer the work item from user Miller to user Smith 
  // so that Smith can work on the task
  task.transferWorkItem(tkiid, WorkItem.REASON\_POTENTIAL\_OWNER,"Miller","Smith");
}This action transfers
the work item to the user Smith so that he can work on it.