<!-- image -->

# Checking which fault occurred for a stopped invoke activity

## About this task

## Procedure

1. List the human task activities that are in a stopped state.
FilterOptions fo = new FilterOptions();
fo.setSelectedAttributes("AIID");
fo.setQueryCondition("STATE=STATE\_STOPPED AND KIND=KIND\_INVOKE");
EntityResultSet result = process.queryEntities("ACTIVITY", fo, null, null);This action returns
a query result set that contains stopped invoke activities.
2. Read the name of the fault. if (result.getEntities().size() > 0)
{
  Entity entity = (Entity) result.getEntities().get(0);
  AIID aiid = (AIID) entity.getAttributeValue("AIID");
  ActivityInstanceData activity = process.getActivityInstance(aiid);
  
  ProcessException excp = activity.getUnhandledException();
  if ( excp instanceof ApplicationFaultException )
  {
   ApplicationFaultException fault = (ApplicationFaultException)excp;
   String faultName = fault.getFaultName();
  }
}