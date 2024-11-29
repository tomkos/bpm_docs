<!-- image -->

# Sending a message to a waiting activity

## About this task

## Procedure

1. List the activity service templates that are waiting for
a message from the logged-on user in a process instance with a specific
process instance ID. ActivityServiceTemplateData[] services = process.getWaitingActivities(piid);
2. Send a message to the first waiting service. It
is assumed that the first service is the one that you want serve.
The caller must be a potential starter of the activity that receives
the message, or an administrator of the process instance.
VTID vtid = services[0].getServiceTemplateID();
ATID atid = services[0].getActivityTemplateID();
String inputType = services[0].getInputMessageTypeName(); 
  
// create a message for the service to be called
  ClientObjectWrapper message = 
        process.createMessage(vtid,atid,inputMessageTypeName);  
  DataObject myMessage = null;
  if ( message.getObject()!= null && message.getObject() instanceof DataObject )
  {
    myMessage = (DataObject)message.getObject();
    //set the strings in the message, for example, chocolate is to be ordered
    myMessage.setString("Order", "chocolate");
  }

  // send the message to the waiting activity 
  process.sendMessage(vtid, atid, message);  
}This action sends the specified
message to the waiting activity service and passes some order data.
You
can also specify the process instance ID to ensure that the message
is sent to the specified process instance. If the process instance
ID is not specified, the message is sent to the activity service,
and the process instance that is identified by the correlation values
in the message. If the process instance ID is specified, the process
instance that is found using the correlation values is checked to
ensure that it has the specified process instance ID.