<!-- image -->

# Releasing a claimed task

## About this task

## Procedure

1. List the claimed tasks owned by a specific person, for
example, Smith. FilterOptions fo = new FilterOptions();
fo.setSelectedAttributes("TKIID");
fo.setQueryCondition("STATE=STATE\_CLAIMED AND OWNER='Smith'");
EntityResultSet result = task.queryEntities("TASK", fo, null, null);
This action returns a query result set that lists the
tasks claimed by the specified person, Smith.
2. Release the claimed task. if (result.getEntities().size() > 0)
{
  Entity entity = (Entity) result.getEntities().get(0);
  TKIID tkiid = (TKIID) entity.getAttributeValue("TKIID");
  task.cancelClaim(tkiid, true);
}This action returns
the task to the ready state so that it can be claimed by one of the
other potential owners. Any output or fault data that is set by the
original owner is kept.