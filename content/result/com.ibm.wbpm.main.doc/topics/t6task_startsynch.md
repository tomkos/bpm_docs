<!-- image -->

# Starting an invocation task that invokes a synchronous interface

## About this task

Such an SCA component can, for example, be implemented
as a microflow or as a simple Java™ class.

This
scenario creates an instance of a task template and passes some customer
data. The task remains in the running state until the two-way operation
returns. The result of the task, OrderNo, is returned to the caller.

## Procedure

1. Optional: List the task templates to find the
name of the invocation task you want to run. This step
is optional if you already know the name of the task.
TaskTemplate[] taskTemplates = task.queryTaskTemplates
("TASK\_TEMPL.KIND=TASK\_TEMPL.KIND.KIND\_ORIGINATING",
 "TASK\_TEMPL.NAME",
  new Integer(50),
  (TimeZone)null);The results are
sorted by name. The query returns an array containing the first 50
sorted originating templates.
2. Create an input message of the appropriate type. 
Entity entity = (Entity) ers.getEntities().get(0);
// create a message for the selected task
ClientObjectWrapper input = task.createInputMessage(
  entity.getAttributeValue("TKTID"));                    
DataObject myMessage = null ;
if ( input.getObject()!= null && input.getObject() instanceof DataObject )
{
  myMessage = (DataObject)input.getObject();
  //set the parts in the message, for example, a customer name
  myMessage.setString("CustomerName", "Smith");
}
3. Create the task and run the task synchronously. For
a task to run synchronously, it must be a two-way operation. The example
uses the createAndCallTask method to create and run the task. 
ClientObjectWrapper output = task.createAndCallTask( entity.getAttributeValue("NAME"), 
                                                     entity.getAttributeValue("NAMESPACE"),
                                                     input);
4. Analyze the result of the task. DataObject myOutput = null;
if ( output.getObject() != null && output.getObject() instanceof DataObject )
{
  myOutput  = (DataObject)output.getObject();
  int order = myOutput.getInt("OrderNo");
}