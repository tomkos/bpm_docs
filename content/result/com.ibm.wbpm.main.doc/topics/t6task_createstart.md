<!-- image -->

# Creating and starting a task instance

## Procedure

1. Optional: List the task templates to find the
task template ID (TKTID) of the collaboration task you want to run.
This step is optional if you already know the task template
ID.
FilterOptions fo = new FilterOptions();
fo.setSelectedAttributes("TKTID, NAME, NAMESPACE");
fo.setSortAttributes("NAME");
EntityResultSet ers = task.queryEntities("TASK\_TEMPL", fo, null, null);
The results are sorted by name. The query returns an
array containing the first 50 sorted task templates.
2. Create an input message of the appropriate type. Entity entity = (Entity) ers.getEntities().get(0);

// create a message for the selected task
ClientObjectWrapper input = task.createInputMessage((TKTID) entity.getAttributeValue("TKTID"));                       
DataObject myMessage = null ;
if ( input.getObject()!= null && input.getObject() instanceof DataObject )
{
  myMessage = (DataObject)input.getObject();
  //set the parts in the message, for example, a customer name
  myMessage.setString("CustomerName", "Smith");
}
3. Create and start the collaboration task; a reply handler
is not specified in this example. The example uses the
createAndStartTask method to create and start the task. 
TKIID tkiid = task.createAndStartTask( entity.getAttributeValue("NAME"), 
                                       entity.getAttributeValue("NAMESPACE"),
                                       input,
                                       (ReplyHandlerWrapper)null);Work items are created for the people
concerned with the task instance. For example, a potential owner can
claim the new task instance.
4. Claim the task instance. ClientObjectWrapper input2 = task.claim(tkiid);
DataObject taskInput = null ;
if ( input2.getObject()!= null && input2.getObject() instanceof DataObject )
{
  taskInput = (DataObject)input2.getObject();
  // read the values
  ...
}  When the task instance is claimed,
the input message of the task is returned.