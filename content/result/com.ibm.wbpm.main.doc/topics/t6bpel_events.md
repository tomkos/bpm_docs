<!-- image -->

# Handling events

## About this task

You can invoke an event handler any number of times as
long as the corresponding scope is running. In addition, multiple
instances of an event handler can be activated concurrently.

The
following code snippet shows how to get the active event handlers
for a given process instance and how to send an input message.

## Procedure

1. Determine the data of the process instance ID and list
the active event handlers for the process.  ProcessInstanceData processInstance = 
       process.getProcessInstance( "CustomerOrder2711");
EventHandlerTemplateData[] events = process.getActiveEventHandlers(
                                      processInstance.getID() );
2. Send the input message. This example uses
the first event handler that is found.
EventHandlerTemplateData event = null;
if ( events.length > 0 )
{
    event = events[0];

    // create a message for the service to be called
    ClientObjectWrapper input = process.createMessage(
    event.getID(), event.getInputMessageTypeName());
             
    if (input.getObject() != null && input.getObject() instanceof DataObject )
    {
      	DataObject inputMessage = (DataObject)input.getObject();
       // set content of the message, for example, a customer name, order number                              
       inputMessage.setString("CustomerName", "Smith");
       inputMessage.setString("OrderNo", "2711");
     
	       // send the message
       process.sendMessage( event.getProcessTemplateName(),
                            event.getPortTypeNamespace(),
                            event.getPortTypeName(),
                            event.getOperationName(),
				 input );
     }
 }
This action sends the specified
message to the active event handler for the process.