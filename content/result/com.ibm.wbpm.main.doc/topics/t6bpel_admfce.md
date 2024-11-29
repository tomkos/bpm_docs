<!-- image -->

# Forcing the completion of an activity

## About this task

You can also force the completion of activities in the
running state if, for example, an activity is not responding.

## Procedure

1. List the stopped activities in the stopped state. FilterOptions fo = new FilterOptions();
fo.setSelectedAttributes("AIID");
fo.setQueryCondition("STATE=STATE\_STOPPED AND NAME='CustomOrder'");
EntityResultSet result = process.queryEntities("ACTIVITY", fo, null, null);
This action returns the stopped activities for the
CustomerOrder process instance.
2. Complete the activity, for example, a stopped human task
activity. In this example, an output message is passed.
if (result.getEntities().size() > 0)
{
   Entity activityEntity = (Entity) result.getEntities().get(0);
   AIID aiid = (AIID) activityEntity.getAttributeValue("AIID");
	  ActivityInstanceData activity = process.getActivityInstance(aiid);
  ClientObjectWrapper output = 
        process.createMessage(aiid, activity.getOutputMessageTypeName());
  DataObject myMessage = null;
  if ( output.getObject()!= null && output.getObject() instanceof DataObject )
   {
     myMessage = (DataObject)output.getObject();
     //set the parts in your message, for example, an order number
     myMessage.setInt("OrderNo", 4711);
   }

   boolean continueOnError = true;
   process.forceComplete(aiid, output, continueOnError);
}This action completes
the activity. If an error occurs, the continueOnError parameter
determines the action to be taken if a fault is provided with the
forceComplete request. 
In the example, continueOnError is
true. This value means that if a fault is provided, the activity is
put into the failed state. The fault is propagated to the enclosing
scopes of the activity until it is either handled or the process scope
is reached. The process is then put into the failing state and it
eventually reaches the failed state.