<!-- image -->

# Processing to-do tasks or collaboration tasks

## About this task

One of the potential owners claims the task associated
with the work item. This person is responsible for providing the relevant
information and completing the task.

## Procedure

1. List the tasks belonging to a logged-on person that are
ready to be worked on. FilterOptions fo = new FilterOptions();
fo.setSelectedAttributes("TKIID");
fo.setQueryCondition("STATE=STATE\_READY AND (KIND=KIND\_PARTICIPATING OR KIND=KIND\_HUMAN)AND WI.REASON=REASON\_POTENTIAL\_OWNER");
EntityResultSet result = task.queryEntities("TASK", fo, null, null);
This action returns a query result set that contains
the tasks that can be worked on by the logged-on person.
2. Claim the task to be worked on. 
if (result.getEntities().size() > 0)
{
  Entity entity = (Entity) result.getEntities().get(0);
  TKIID tkiid = (TKIID) entity.getAttributeValue("TKIID");
  ClientObjectWrapper input = task.claim(tkiid);
  DataObject taskInput = null ;
  if ( input.getObject()!= null && input.getObject() instanceof DataObject )
  {
    taskInput = (DataObject)input.getObject();
    // read the values
    ...
  }  
}When the task
is claimed, the input message of the task is returned.
3 When work on the task is finished, complete the task. The task can be completed either successfully or with a faultmessage. If the task is successful, an output message is passed. Ifthe task is unsuccessful, a fault message is passed. You must createthe appropriate messages for these actions.

The task can be completed either successfully or with a fault
message. If the task is successful, an output message is passed. If
the task is unsuccessful, a fault message is passed. You must create
the appropriate messages for these actions.

    1. To complete the task successfully, create an output
message. ClientObjectWrapper output = 
      task.createOutputMessage(tkiid);
DataObject myMessage = null ;
if ( output.getObject()!= null && output.getObject() instanceof DataObject )
{
  myMessage = (DataObject)output.getObject();
  //set the parts in your message, for example, an order number
  myMessage.setInt("OrderNo", 4711);
}

//complete the task
task.complete(tkiid, output); This
action sets an output message that contains the order number. The
task is put into the finished state.
    2. To complete the task when a fault occurs, create a fault
message. //retrieve the faults modeled for the task
List faultNames = task.getFaultNames(tkiid);

//create a message of the appropriate type
ClientObjectWrapper myFault = 
      task.createFaultMessage(tkiid, (String)faultNames.get(0));

// set the parts in your fault message, for example, an error number
DataObject myMessage = null ;
if ( myFault.getObject()!= null && input.getObject() instanceof DataObject )
{
  myMessage = (DataObject)myFault.getObject();
  //set the parts in the message, for example, a customer name
  myMessage.setInt("error",1304);
}

task.complete(tkiid, (String)faultNames.get(0), myFault);
This action sets a fault message that contains the
error code. The task is put into the failed state.