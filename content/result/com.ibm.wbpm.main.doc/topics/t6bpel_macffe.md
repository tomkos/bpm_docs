<!-- image -->

# Analyzing the results of a process

## About this task

## Procedure

```
FilterOptions fo = new FilterOptions();
fo.setSelectedAttributes("PIID");
fo.setQueryCondition("NAME='CustomerOrder' AND STATE=STATE\_FINISHED");
EntityResultSet ers = process.queryEntities("PROCESS\_INSTANCE", fo, null, null);
if (ers.getEntities().size() > 0)
{
  Entity processEntity = (Entity) ers.getEntities().get(0);
  PIID piid = (PIID) processEntity.getAttributeValue("PIID");
  ClientObjectWrapper output = process.getOutputMessage(piid);
  DataObject myOutput = null;
  if ( output.getObject() != null && output.getObject() instanceof DataObject )
  {
     myOutput = (DataObject)output.getObject();
     int order = myOutput.getInt("OrderNo");
  }
}
```