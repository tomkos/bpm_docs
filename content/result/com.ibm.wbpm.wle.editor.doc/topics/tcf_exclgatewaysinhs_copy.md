# Implementing exclusive gateways

## About this task

## Procedure

To add an exclusive gateway to a human service or service flow:

1. Open the service.
2. In the Diagram view, add an exclusive gateway  to the canvas, and wire it to create the required sequence flow. 
The default sequence flow, which is marked with a forward slash (/) sign on the diagram, is
the first sequence that you create from the gateway to a following activity.
3. Click the gateway in the diagram. In the General common properties,
specify a name and a description for the gateway.
4. Switch to Implementation. Under Decisions, specify
a condition (in JavaScript) for each outgoing sequence line to control which path is followed.
5. Ensure that the default sequence flow under Default Flow is the
one that you want the flow to follow if all conditions evaluate to false. If not, in the list select
the sequence flow that you want to designate as the default sequence flow.
Note that the default sequence flow does not have a condition.
6. Click a sequence line and verify its implementation in the General
properties. If you do not want the sequence line name to be displayed in the diagram, clear
Name Visible.
7. Click Save or Finish Editing.