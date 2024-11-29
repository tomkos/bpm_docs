<!-- image -->

# Analyzing the results of a task

## About this task

The results of the task are stored in the database only
if the task template from which the task instance was derived does
not specify automatic deletion of the derived task instances.

## Procedure

The example
shows how to check the order number of a successfully completed task.

```
FilterOptions fo = new FilterOptions();
fo.setSelectedAttributes("TKIID");
fo.setQueryCondition("NAME='CustomerOrder' AND STATE=STATE\_FINISHED");
EntityResultSet result = task.queryEntities("TASK", fo, null, null);

if (result.getEntities().size() > 0)
{
  Entity entity = (Entity) result.getEntities().get(0);
  TKIID tkiid = (TKIID) entity.getAttributeValue("TKIID");
  ClientObjectWrapper output = task.getOutputMessage(tkiid);
  DataObject myOutput = null;
  if ( output.getObject() != null && output.getObject() instanceof DataObject)
  {
     myOutput  = (DataObject)output.getObject();
     int order = myOutput.getInt("OrderNo");
  }
}
```

## Related concepts

- Business Process Choreographer EJB query API