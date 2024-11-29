<!-- image -->

# Deleting process instances

## About this task

To delete a process instance, you need process administrator
rights and the process instance must be a top-level process instance.

The
following example shows how to delete all of the finished process
instances.

## Procedure

1. List the process instances that are finished. FilterOptions fo = new FilterOptions();
fo.setSelectedAttributes("PIID");
fo.setQueryCondition("STATE=STATE\_FINISHED");
EntityResultSet result = process.queryEntities("PROCESS\_INSTANCE", fo, null, null);
This action returns a query result set that lists process
instances that are finished.
2. Delete the process instances that are finished. for (int i = 0; i < result.getEntities().size(); i++) {
  PIID piid = (PIID) result.getEntities().get(i);
  process.delete(piid);
}This action deletes
the selected process instance and its inline tasks from the database.