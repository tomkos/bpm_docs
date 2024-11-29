# Processing a search case operation result (deprecated)

## About this task

Follow these steps to make multiple updates using a search
case result.

Although this topic is about a search case, it
could also be applied to a retrieve case. For example, you could search
for a case and for each case reference returned perform a retrieve
to get the properties of each case instance. You could look upon this
example as a pattern that can be used any time multiple case references
need to be processed.

## Procedure

1. In the IBM® Business Automation
Workflow Integration
Service editor, create a flow of operations similar to the following
screen capture.
2. In the Loop Case References component,
add JavaScript similar to the following in the Implementation section of the Properties view. It will let
the loop run until there are no more cases in the array to process. 
/* Assumes that the counter variable will always be reset to -1 at the end of the loop */
tw.local.counter ++; /* Increase the counter by one */
tw.local.currentReference = null; /* Reset the current reference */

/* If the counter is within the length of the array, get the next case reference */
if(tw.local.counter <= tw.local.references.listLength){
    tw.local.currentReference = tw.local.references[tw.local.counter];
}else{
    /* Else, reset the counter.  The Reference is 
       already null so the decision node should continue */
    tw.local.counter = -1;
    
}
3. In the Implementation section of
the Properties view for the Decision
Gateway, return the flow to the Update Case service when the currentReference variable
from the JavaScript shown previously is not equal to a null value.
4. Create a query to run against your IBM Business Automation
Workflow solution
as shown in Building a query for a search case operation.
5. Run the business process that invokes this service.
A different situation to the one described in the previous
steps is if you update a case instance in IBM Workflow
Center that originated on the IBM Business Automation
Workflow server.
When you return that case instance to the IBM Business Automation
Workflow server,
use the tw.system.enclosingCaseInstance system variable
as the reference to the case instance running on the IBM Business Automation
Workflow server.
This variable is only available at the business process definition
level.