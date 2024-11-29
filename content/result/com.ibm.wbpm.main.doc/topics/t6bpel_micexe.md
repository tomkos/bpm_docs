<!-- image -->

# Running a microflow that contains a unique starting service

## About this task

If the microflow implements a request-response operation, that
is, the process contains a reply, you can use the call method to run the process
passing the process template name as a parameter in the call.

If the
microflow is a one-way operation, use the sendMessage method to run the process.
This method is not covered in this example.

## Procedure

1. Optional: List the process templates to find the name
of the process you want to run. This step is optional if you
already know the name of the process.
ProcessTemplateData[] processTemplates = process.queryProcessTemplates
("PROCESS\_TEMPLATE.EXECUTION\_MODE =
       PROCESS\_TEMPLATE.EXECUTION\_MODE.EXCECUTION\_MODE\_MICROFLOW",
 "PROCESS\_TEMPLATE.NAME",
  new Integer(50),
  (TimeZone)null);The results are sorted
by name. The query returns an array containing the first 50 sorted templates
that can be started by the call method.
2. Start the process with an input message of the appropriate type.
When you create the message, you must specify its message type name
so that the message definition is contained.
ProcessTemplateData template = processTemplates[0];
//create a message for the single starting receive activity
ClientObjectWrapper input = process.createMessage
                           (template.getID(),
                            template.getInputMessageTypeName());
DataObject myMessage = null;
if ( input.getObject()!= null && input.getObject() instanceof DataObject )
{
  myMessage = (DataObject)input.getObject();
  //set the strings in the message, for example, a customer name
  myMessage.setString("CustomerName", "Smith");
}

//run the process
ClientObjectWrapper output = process.call(template.getName(), input);
DataObject myOutput = null;
if ( output.getObject() != null && output.getObject() instanceof DataObject )
{
  myOutput  = (DataObject)output.getObject();
  int order = myOutput.getInt("OrderNo");
}
This action creates an instance of the process
template, CustomerTemplate, and passes some customer data. The operation returns
only when the process is complete. The result of the process, OrderNo, is
returned to the caller.