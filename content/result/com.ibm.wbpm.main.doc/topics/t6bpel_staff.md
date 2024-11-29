<!-- image -->

# Processing human task activities

## About this task

When a human task activity is activated, both an activity
instance and an associated to-do task are created. Handling of the
human task activity and the work item management is delegated to Human
Task Manager. Any state change of the activity instance is reflected
in the task instance and vice versa.

A potential owner claims
the activity. This person is responsible for providing the relevant
information and completing the activity.

## Procedure

1. List the activities belonging to a logged-on person that
are ready to be worked on: FilterOptions fo = new FilterOptions();
fo.setSelectedAttributes("AIID");
fo.setQueryCondition("STATE=STATE\_READY AND KIND=KIND\_STAFF AND WI.REASON=REASON\_POTENTIAL\_OWNER");
EntityResultSet ers = process.queryEntities("ACTIVITY", fo, null, null);
This action returns a query result set that contains the
activities that can be worked on by the logged-on person.
2. Claim the activity to be worked on: if (ers.getEntities().size() > 0)
{
  Entity activity = (Entity) ers.getEntities().get(0);
  AIID aiid = (AIID) activity.getAttributeValue("AIID");
  ClientObjectWrapper input = process.claim(aiid);
  DataObject activityInput = null ;
  if ( input.getObject() != null && (input.getObject() instanceof DataObject) )
    {
    activityInput = (DataObject)input.getObject();
    // read the values
    ...
    }  
}When the activity
is claimed, the input message of the activity is returned.
3 When work on the activity is finished, complete the activity. The activity can be completed either successfully or with afault message. If the activity is successful, an output message ispassed. If the activity is unsuccessful, the activity is put intothe failed or stopped state and a fault message is passed. You mustcreate the appropriate messages for these actions. When you createthe message, you must specify the message type name so that the messagedefinition is contained.
    1. To complete the activity successfully, create an output
message. ActivityInstanceData activity = process.getActivityInstance(aiid);
ClientObjectWrapper output = 
      process.createMessage(aiid, activity.getOutputMessageTypeName());
DataObject myMessage = null ;
if ( output.getObject()!= null && output.getObject() instanceof DataObject )
{
  myMessage = (DataObject)output.getObject();
  //set the parts in your message, for example, an order number
  myMessage.setInt("OrderNo", 4711);
}

//complete the activity
process.complete(aiid, output);This
action sets an output message that contains the order number.
    2. To complete the activity when a fault occurs, create
a fault message. //retrieve the faults modeled for the human task activity
List faultNames = process.getFaultNames(aiid);

//create a message of the appropriate type
ClientObjectWrapper myFault = 
      process.createMessage(aiid, faultNames.get(0) );

// set the parts in your fault message, for example, an error number
DataObject myMessage = null ;
if ( myFault.getObject()!= null && input.getObject() instanceof DataObject )
{
  myMessage = (DataObject)myFault.getObject();
  //set the parts in the message, for example, a customer name
  myMessage.setInt("error",1304);
}

process.complete(aiid, myFault,(String)faultNames.get(0) );
This action sets the activity in either the failed or
the stopped state. If the continueOnError parameter
for the activity in the process model is set to true, the activity
is put into the failed state and the navigation continues. If the continueOnError parameter
is set to false and the fault is not caught on the surrounding scope,
the activity is put into the stopped state. In this state the activity
can be repaired using force complete or force retry.