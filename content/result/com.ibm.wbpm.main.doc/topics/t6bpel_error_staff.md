<!-- image -->

# Checking which fault is set for a human task activity

## About this task

## Procedure

1. List the task activities that are in a failed or stopped
state. FilterOptions fo = new FilterOptions();
fo.setSelectedAttributes("AIID");
fo.setQueryCondition("(STATE=STATE\_FAILED OR STATE=STATE\_STOPPED) AND KIND=KIND\_STAFF");
EntityResultSet result = process.queryEntities("ACTIVITY", fo, null, null);
This action returns a query result set that contains failed
or stopped activities.
2. Read the name of the fault. if (result.getEntities().size() > 0)
{
  Entity entity = (Entity) result.getEntities().get(0);
  AIID aiid = (AIID) entity.getAttributeValue("AIID");
  ClientObjectWrapper faultMessage = process.getFaultMessage(aiid);
  DataObject fault = null ;
  if ( faultMessage.getObject() != null && faultMessage.getObject() 
       instanceof DataObject )
  {
    fault = (DataObject)faultMessage.getObject();
    Type type = fault.getType();
    String name = type.getName();
    String uri = type.getURI();
  }
}This returns the
fault name. You can also analyze the unhandled exception for a stopped
activity instead of retrieving the fault name.