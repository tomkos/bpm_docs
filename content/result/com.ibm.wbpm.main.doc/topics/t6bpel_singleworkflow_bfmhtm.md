<!-- image -->

# Processing a page flow that is started by a to-do task

## Before you begin

- Because the next activity in the page flow is made available in
the transaction of the activity that completed, the transactional
behavior of all the human task activities must be set to participates.
- To ensure that the next human task in the page flow can be found at run time, transaction
boundaries are not introduced between tasks. To do this, for example, make sure that any invoke
activities between two human task activities also have the transactional behavior set to
participates, and that they do not use services, such as wait activities, that
require a transaction boundary.Note: Business Process Choreographer dynamically introduces
non-modeled transaction boundaries as required, for example as deadlock prevention, which affect the
behavior of the completeAndClaimSuccessor API. Normally, the API claims the next
human task in the page flow, if it is available in the transaction of the activity that completed.
However, if a transaction boundary exists, the API request returns without claiming the next
task.Moreover, where and how transaction boundaries are added can change in the future, for
example after a product update, or after a fix is installed. Therefore, even though you model
transaction boundaries by setting the transactional behavior property on activities, adherence to
these boundaries is not guaranteed.
- If the page flow is to be used in Business Space, each of the
human tasks in the page flow must have the htm.hasNext custom
property set to true, except the last human
task in the sequence. This task must have the htm.hasNext custom
property set to false.

## About this task

- Client-side page flows, where the navigation between the different
pages is realized using client-side technology, such as a multi-page Lotus Forms form.
- Server-side page flows are realized using a BPEL process and a
set of human tasks that are modeled so that subsequent tasks are assigned
to the same person.

- You need to invoke services between steps carried out in a user
interface, for example, to retrieve or update data.
- You have auditing requirements that require CEI events to be written
after a user interface interaction completes.

In
an online bookstore, the purchaser completes a sequence of actions
to order a book. This sequence of actions can be implemented as a
series of human task activities (to-do tasks). If the purchaser decides
to order several books, this is equivalent to claiming the next human
task activity. Information about the sequence of tasks is maintained
by Business Flow Manager, while the tasks themselves are maintained
by Human Task Manager.

Compare this example with the example
of a page flow that starts with the BPEL process.

## Procedure

1. Use the Business Flow Manager API to get the process instance
that you want to work on. In this example, an instance
of the CustomerOrder process.
ProcessInstanceData processInstance = 
   process.getProcessInstance("CustomerOrder");
String piid = processInstance.getID().toString();
2. Use the Human Task Manager API to query the ready to-do
tasks (kind participating) that are part of the specified process
instance.  Use the containment context ID of the task
to specify the containing process instance. For a page flow, the query
returns the to-do task that is associated with the first human task
activity in the sequence of human task activities.
//
 // Query the list of to-do tasks that can be claimed by the logged-on user 
 // for the specified process instance
//
FilterOptions fo = new FilterOptions();
fo.setSelectedAttributes("TKIID");
fo.setQueryCondition("CONTAINMENT\_CTX\_ID = ID('" + piid + "') AND STATE = STATE\_READY AND KIND = KIND\_PARTICIPATING AND WI.REASON = REASON\_POTENTIAL\_OWNER");
EntityResultSet result = task.queryEntities("TASK", fo, null, null);
3. Claim the to-do task that is returned. if (result.getEntities().size() > 0)
{
  Entity entity = (Entity) result.getEntities().get(0);
  TKIID tkiid = (TKIID) entity.getAttributeValue("TKIID");
  ClientObjectWrapper input = task.claim(tkiid);
  DataObject activityInput = null ;
  if ( input.getObject()!= null && input.getObject() instanceof DataObject )
  {
    taskInput = (DataObject)input.getObject();
    // read the values
    ...
  }  
}
When the task is claimed,
the input message of the task is returned.
4 Determine the human task activity that is associated withthe to-do task. You can use one of the following methodsto correlate activities to their tasks.
    - The task.getActivityID method:AIID aiid = task.getActivityID(tkiid);
    - The parent context ID that is part of the task object:AIID aiid = null;
Task taskInstance = task.getTask(tkiid);

OID oid = taskInstance.getParentContextID();
if ( oid != null and oid instanceof AIID )
{
  aiid = (AIID)oid;
}
5. When work on the task is finished, use the Business Flow
Manager API to complete the task and its associated human task activity,
and claim the next human task activity in the process instance.
To complete the human task activity, an output message is
passed. When you create the output message, you must specify the message
type name so that the message definition is contained. 
ActivityInstanceData activity = process.getActivityInstance(aiid);
ClientObjectWrapper output = 
      process.createMessage(aiid, activity.getOutputMessageTypeName());
DataObject myMessage = null ;
if ( output.getObject()!= null && output.getObject() instanceof DataObject )
{
  myMessage = (DataObject)output.getObject();
  //set the parts in your message, for example, an order number
  myMessage.setInt("OrderNo", 4711);
}

//complete the human task activity and its associated to-do task,
// and claim the next human task activity
CompleteAndClaimSuccessorResult successor = 
   process.completeAndClaimSuccessor(aiid, output);
This action sets an output message that contains the order
number and claims the next human task activity in the sequence. If AutoClaim is
set for successor activities and if there are multiple paths that
can be followed, all of the successor activities are claimed and a
random activity is returned as the next activity. If there are no
more successor activities that can be assigned to this user, Null is
returned.If the process contains parallel paths that can be followed
and these paths contain human task activities for which the logged-on
user is a potential owner of more than one of these activities, a
random activity is claimed automatically and returned as the next
activity.
6. Work on the next human task activity. ClientObjectWrapper nextInput = successor.getInputMessage();
if ( nextInput.getObject()!= 
               null && nextInput.getObject() instanceof DataObject )
{
  activityInput = (DataObject)input.getObject();
  // read the values
  ...
}  

aiid = successor.getAIID();
7. Continue with step 5 to complete the human task activity
and to retrieve the next human task activity.