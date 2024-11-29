<!-- image -->

# Create the mediation flow implementation

## About this task

## Procedure

1. In the assembly editor, double-click the HelloWorldMediation component
and click Yes in the Open window, then click OK in the
Generate Implementation window. The mediation flow editor opens.
Note: At some points in your development activities, a Tip window
may open to help guide you in making development decisions. For the
purposes of this sample, you can simply close the Tip windowes and
adhere to the sample instructions.
2. At the top of the mediation flow editor, you see callHello on
the left and getHello  on the right. This is the single operation
from this component's interface and the single operation from
this component's reference. (Note that it is valid to have multiple
interfaces and references for each component, and multiple operations
for each interface and reference. But this is Hello World.)
Select the callHello interface operation. You
will now need to select whether you want to create a mediation flow
that performs a simple map between operations. Note, however, that
you can make any change that you want in the mediation flow editor,
so you are not locked into your choice. In this sample, you will perform
a simple map between operations, so you should select the Operation
Map link shown in the following screen cap:
3. When the Select Reference Operation window opens, select
the getHello operation (as shown below), then
click OK.  What you have
indicated here is that you will be invoking the getHello operation
as part of implementing the callHello operation for this component.
4. Next you want to finish the implementation of the flow for
the callHello operation. Because this is a request response
operation, there is one flow for the request and another for the response,
but you start first with the request. At the top of the canvas, click
the callHello Request tab, as shown here:    In the flow area, you see an input node
on the left, which represents control reaching your request flow by
way of the callHello operation being invoked. The flow then invokes
the input\_map XSL transform that maps between the input business object
of the callHello and getHello operations. The flow then calls the
getHello reference operation, which in this case is an external web
service. In the flow area of the request, there is a sticky note that
contains the tasks that you must perform to fully implement the flow.
5. Double-click the input\_map primitive
to create its map. The New XML Map  window opens. Click Finish.
The XML map editor opens.
6. In the XML map editor, fully expand the left and right
trees.
7. Wire title on the left to name on the right.
This creates a transform of type Move.
8. Wire firstName on the left to the Move transform
in the middle. A Connection Selection Helper is shown.
9. Select Primary Connection. This
changes the operation into a Concat operation.
10. Wire lastName on the left to the Concat operation
in the middle. A Connection Selection Helper is shown again. Select Primary
Connection. You now see three wires coming in, and one
going out, as shown here:
11. Select the Concat operation and then go to the Properties 
view and click the General tab.
12. When the fields are concatenated you want spaces between
the title, given name and family name. Use the delimiter settings
in the General tab of the Properties view
to create these spaces. For the default delimiter, select Space
character. The delimiter is reported as (Space
character) in the table, as shown in the following figure:
13. Save and close the XML map editor.
14. Save the mediation flow editor.
15. Now you must finish the implementation of the mediation response 
flow, to process the response from the web service you invoked in
the request flow and turn it into a response to the caller of this
component. Select the Response  tab at the top of the flow
editor, as shown here:
16. Double-click the output\_map primitive.
In the New XML Map wizard, click Finish to
create the new map.
17. Map the incoming output1 field to the outgoing result 
field, as shown in the following figure:
18. Save and close the XML map editor.
19. Save the mediation flow editor.
20. Finally, you want to get rid of the warning that you have
not wired the fail terminal for the callout response node, as shown
in the following figure: 
The warning occurs because you have not accounted for a situation
where a call to the web service fails.
21. To capture any unhandled errors that might occur in the
request or response flow, implement the Error flow. Click the Error
tab at the top of the flow editor, as shown here:
22 For encapsulation of error handling and to more easilyadd logging, complete the following steps to add a subflow:
    1. In the palette, click Mediation Subflow and
then click Subflow, as shown in the following
figure:
    2. Drag Subflow from the palette to the canvas. The Subflow
Selection window opens.
    3. Click the New button. The New
Mediation Subflow wizard opens.
    4. In the Name field, type ErrorHandling,
as shown in the following figure:
    5. Click Finish.
    6. In the Subflow Selection window, select ErrorHandling,
as shown in the following figure:
    7. Click OK to close the Subflow
Selection window. The ErrorHandling subflow opens.
    8. In the palette of the new subflow, click the Error
Handling folder and then click the Fail primitive,
as shown in the following figure:
    9. Drag the Fail primitive from
the palette to the canvas.
    10. Wire the right edge of the in terminal
to the Fail primitive, as shown in the following
figure:
    11. Since no messages will exit the flow, right-click the out terminal
and select Delete.
    12. Now you must change the input message type to Any
message type. Hover the cursor over the in terminal
and then click the i icon that appears at the
top edge of the terminal. The in window opens.
    13. In the window, expand Service Message Object
Details and click Change. The Change
Message Type window opens.
    14. Select Any message type, as shown
in the following figure:
    15. Click OK to close the Change
Message Type window and then close the in window.
    16. Press Ctrl-S to save the subflow
and then close the subflow. A File Changed window is displayed, as
shown in the following figure:
    17. Select Save and Reload. This
reloads the changes that you made to the ErrorHandling subflow in
the HelloWorldMediation flow.
    18. Switch to the Error tab. Wire the out terminal of Error
Input to the ErrorHandling subflow.
    19. The Input Response is used to send messages back to
the service requester. Since the Input Response is not used here,
you can choose to hide it. Right-click the canvas, and select Hide
Input Response.
23. Now that you have completed your TODO on the request and
response flows, right-click the TODO windowes on the canvas of both
the Request and Response tabs and then select Delete to
remove them.
24. Save and close the mediation flow editor and the assembly
editor.

## Results