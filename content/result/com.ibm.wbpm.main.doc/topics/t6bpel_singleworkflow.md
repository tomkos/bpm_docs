<!-- image -->

# Processing a page flow that starts with the BPEL process

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

A typical example of a page flow is the ordering process
in an online bookstore, where the purchaser completes a sequence of
actions to order a book. This sequence of actions can be implemented
as a series of human task activities (to-do tasks). If the purchaser
decides to order several books, this is equivalent to starting an
order process, and claiming the next human task activity.

The initiateAndClaimFirst API
starts the page flow, that is, it starts the specified process and
claims the first human task activity in the sequence of activities.
It returns information about the claimed activity, including the input
message to be worked on.

The completeAndClaimSuccessor API
then completes the human task activity and claims the next one in
the same process instance for the logged-on person. The API returns
information about the next claimed activity, including the input message
to be worked on.

Compare this example with the example of a
page flow that is started by a to-do task.

## Procedure

1 Start the book ordering process and claim the first activityin the sequence of activities. Start the process with aninput message of the appropriate type. When you create the message,you must specify its message type name so that the message definitionis contained. If you specify a process instance name, it must notstart with an underscore. If a process instance name is not specified,the process instance ID (PIID) in String format is used as the name. When the first activity is claimed, the input messageand the ID of the claimed activity is returned.
    1. Retrieve the process template to create an input message
of the appropriate type. ProcessTemplateData template = process.getProcessTemplate("CustomerOrder");
ClientObjectWrapper input = process.createMessage(template.getID(),
                            template.getInputMessageTypeName());
DataObject myMessage = null;
if ( input.getObject()!= null && input.getObject() instanceof DataObject )
{
  myMessage = (DataObject)input.getObject();
  //set the strings in the message, for example, a customer name
  myMessage.setString("CustomerName", "Smith");
}
    2. Start the process and claim the first human task activity.
InitiateAndClaimFirstResult result = 
  process.initiateAndClaimFirst("CustomerOrder", "MyOrderProcess", input);
AIID aiid = result.getAIID(); 
ClientObjectWrapper input = result.getInputMessage();
2. When work on the activity is finished, complete the activity,
and claim the next activity. To complete the activity,
an output message is passed. When you create the output message, you
must specify the message type name so that the message definition
is contained. 
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

//complete the activity and claim the next one
CompleteAndClaimSuccessorResult successor = 
   process.completeAndClaimSuccessor(aiid, output);
This action sets an output message that contains the order
number and claims the next activity in the sequence. If AutoClaim is
set for successor activities and if there are multiple paths that
can be followed, all of the successor activities are claimed and a
random activity is returned as the next activity. If there are no
more successor activities that can be assigned to this user, Null is
returned. If the process contains parallel paths that can be followed
and these paths contain human task activities for which the logged-on
user is a potential owner of more than one of these activities, a
random activity is claimed automatically and returned as the next
activity.
3. Work on the next activity. String name = successor.getActivityName();

ClientObjectWrapper nextInput = successor.getInputMessage();
if ( nextInput.getObject()!= 
               null && nextInput.getObject() instanceof DataObject )
{
  activityInput = (DataObject)input.getObject();
  // read the values
  ...
}  

aiid = successor.getAIID();
4. Continue with step 2 to complete the activity.