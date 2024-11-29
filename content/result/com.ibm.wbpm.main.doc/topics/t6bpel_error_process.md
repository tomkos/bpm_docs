<!-- image -->

# Checking which unhandled exception or fault occurred for a
failed process instance

## About this task

## Procedure

1. List the process instances that are in the failed state.
QueryResultSet result = 
     process.query("PROCESS\_INSTANCE.PIID", 
                   "PROCESS\_INSTANCE.STATE = 
                       PROCESS\_INSTANCE.STATE.STATE\_FAILED", 
                    (String)null, (Integer)null, (TimeZone)null); 
This action returns a query result
set that contains the failed process instances.
2. Read the information for the unhandled exception. if (result.getEntities().size() > 0)
{
  Entity entity = (Entity) result.getEntities().get(0);
  PIID piid = (PIID) entity.getAttributeValue("PIID");
  ProcessInstanceData pInstance = process.getProcessInstance(piid);
  
  ProcessException excp = pInstance.getUnhandledException();
  if ( excp instanceof RuntimeFaultException )
  {
   RuntimeFaultException xcp = (RuntimeFaultException)excp;
   Throwable cause = xcp.getRootCause();
  }
  else if ( excp instanceof StandardFaultException )
  {
   StandardFaultException xcp = (StandardFaultException)excp;
   String faultName = xcp.getFaultName();
  }
  else if ( excp instanceof ApplicationFaultException )
  {
   ApplicationFaultException xcp = (ApplicationFaultException)excp;
   String faultName = xcp.getFaultName();
  }     
}

## Results

Use this information to look up the fault name or the root
cause of the problem.