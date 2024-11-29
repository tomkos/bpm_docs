<!-- image -->

# Starting a long-running process that contains a non-unique
starting service

## Procedure

1. Optional: List the process templates to find
the name of the process you want to start. This step
is optional if you already know the name of the process.
FilterOptions fo = new FilterOptions();
fo.setSelectedAttributes("PTID");
fo.setQueryCondition("EXECUTION\_MODE=EXECUTION\_MODE\_LONG\_RUNNING");
EntityResultSet result = process.queryEntities("PROCESS\_TEMPLATE", fo, null, null);
The results are sorted by name. The query returns an array
containing the first 50 sorted templates that can be started as long-running
processes.
2. Determine the starting service to be called. Entity entity = (Entity) result.getEntities().get(0);
PTID ptid = (PTID) entity.getAttributeValue("PTID");
ActivityServiceTemplateData[] startActivities = process.getStartActivities(ptid);
3. Start the process with an input message of the appropriate
type. When you create the message, you must specify
its message type name so that the message definition is contained.
If you specify a process-instance name, it must not start with an
underscore. If a process-instance name is not specified, the process
instance ID (PIID) in String format is used as the name.
ActivityServiceTemplateData activity = startActivities[0];
//create a message for the service to be called
ClientObjectWrapper input = process.createMessage
                            (activity.getServiceTemplateID(),
                             activity.getActivityTemplateID(),
                             activity.getInputMessageTypeName()); 
DataObject myMessage = null;
if ( input.getObject()!= null && input.getObject() instanceof DataObject )
{
  myMessage = (DataObject)input.getObject();
  //set the strings in the message, for example, a customer name
  myMessage.setString("CustomerName", "Smith");
}
//start the process
PIID piid = process.sendMessage(activity.getServiceTemplateID(),
                             activity.getActivityTemplateID(),
                             input); 
This action creates an instance
and passes some customer data. When the process starts, the operation
returns the object ID of the new process instance to the caller.
The
starter of the process instance is set to the caller of the request
and receives a work item for the process instance. The process administrators,
readers, and editors of the process instance are determined and receive
work items for the process instance. The follow-on activity instances
are determined. These are started automatically or, if they are
human task, receive, or pick activities, work items are created for
the potential owners.