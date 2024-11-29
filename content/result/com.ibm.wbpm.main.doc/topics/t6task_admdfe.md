<!-- image -->

# Deleting task instances

## Procedure

1. List the task instances that are finished. FilterOptions fo = new FilterOptions();
fo.setSelectedAttributes("TKIID");
fo.setQueryCondition("STATE=STATE\_FINISHED");
EntityResultSet result = task.queryEntities("TASK", fo, null, null);
This action returns a query result set that lists task
instances that are finished.
2. Delete the task instances that are finished. for (int i = 0; i < result.getEntities().size(); i++) {
  Entity entity = (Entity) result.getEntities().get(i);
  TKIID tkiid = (TKIID) entity.getAttributeValue("TKIID");
  task.delete(tkiid);
}