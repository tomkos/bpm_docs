<!-- image -->

# Retrying the execution of a stopped activity

## About this task

You can set variables that are used by the activity. With
the exception of script activities, you can also pass parameters in
the force-retry call, such as the message that was expected by the
activity.

## Procedure

1. List the stopped activities. FilterOptions fo = new FilterOptions();
fo.setSelectedAttributes("AIID");
fo.setQueryCondition("STATE=STATE\_STOPPED AND NAME='CustomOrder'");
EntityResultSet result = process.queryEntities("ACTIVITY", fo, null, null);
This action returns the stopped activities for the
CustomerOrder process instance.
2. Retry the execution of the activity, for example, a stopped
human task activity. if (result.getEntities().size() > 0)
{
  Entity activityEntity = (Entity) result.getEntities().get(0);
  AIID aiid = (AIID) activityEntity.getAttributeValue("AIID");
  ActivityInstanceData activity = process.getActivityInstance(aiid);
  ClientObjectWrapper input = 
        process.createMessage(aiid, activity.getOutputMessageTypeName());
  DataObject myMessage = null;
  if ( input.getObject()!= null && input.getObject() instanceof DataObject )
    {
      myMessage = (DataObject)input.getObject();
      //set the strings in your message, for example, chocolate is to be ordered
      myMessage.setString("OrderNo", "chocolate");
    }

   boolean continueOnError = true;
   process.forceRetry(aiid, input, continueOnError); 
}This action retries
the activity. If an error occurs, the continueOnError parameter
determines the action to be taken if an error occurs during processing
of the forceRetry request. 
In the example, continueOnError is
true. This means that if an error occurs during processing of the
forceRetry request, the activity is put into the failed state. The
fault is propagated to the enclosing scopes of the activity until
it is either handled or the process scope is reached. The process
is then put into the failing state and a fault handler on the process
level is run before the process state ends in the failed state.