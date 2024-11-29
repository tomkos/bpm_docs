# Converging and diverging process flows with gateways

## About this task

In a service
flow diagram, you can use only exclusive gateways. For examples of exclusive
gateways, see the Hiring Sample Overview.

In a process
diagram, you can model any of the following types of
gateways:

| Component icon    | Gateway type    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-------------------|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                   | Parallel (AND)  | Use a parallel, diverging gateway when you want the process to follow all available paths. Use a parallel, converging gateway when you want to converge all available paths.                                                                                                                                                                                                                                                                                    |
|                   | Inclusive (OR)  | Use inclusive, diverging gateway when you want to follow one or more available paths based on conditions that you specify. Use downstream of an inclusive diverging gateway to converge multiple paths into a single path after all the active paths completed their runtime execution. The inclusive join looks upstream at each path to determine whether the path is active, in which case it waits. Otherwise, it passes the token through without waiting. |
|                   | Exclusive (XOR) | Use to model a point in the process or service flow execution where only one of several paths can be followed, depending on a condition, or to model a point in process execution when the token for one of several incoming paths is passed through the gateway. Note:  The exclusive gateways are the only gateways that can be implemented in human services. For more information, see Implementing exclusive gateways.                                     |
|                   | Event           | Use to model a point in the process execution where only one of several paths can be followed, depending on events that occur. A specific event, such as the receipt of a message or timer event, determines the path to be taken. An event gateway must be modeled a certain way as described in Modeling event gateways.                                                                                                                                      |

When you model inclusive and exclusive gateways, if all conditions evaluate to
false, the process follows the default sequence flow. The default sequence
flow is the first sequence flow that you create from the gateway to a following activity, but you
can change the default sequence flow at any time, as described in the following procedure.

To
add gateways to a process or human service diagram:

## Procedure

1. Drag a gateway from the palette onto the diagram.
2. Create the necessary sequence flow to and from the gateway.
The default sequence flow is the first sequence that you create from the gateway to a
following activity. For a gateway, you can change the default flow by reordering the sequence flow
in the implementation properties.
3. In the General section of the general properties, select
a gateway type.
4. Optional: For an exclusive or inclusive gateway, if the decision
is complex, you can designate a service flow or decision service as the main logic of the decision.
To do so, in the Decision tab of the properties, select a service flow or
decision service and define the required input mapping.
5 Configure the implementation for the gateway.
    1. Each outgoing sequence line in an inclusive or exclusive gateway (except the default
line) requires a condition (in JavaScript) that controls whether the path is followed.
 Ensure that the sequence flow shown as the Default Sequence Flow is the
one that you want the process or service flow to follow if all conditions evaluate to
false. If not, reorder the lines until the one that you want is designated the
default.
Note:
Gateway decision expressions are evaluated as the last operation in executing a gateway after the
post expression is run.
A default sequence flow does not have a condition.

Tip:  If the gateway is implemented by a service, as described in step 4, then you can access
the output of the service by using the namespace tw.decision.
    2. For event gateways, see Modeling event gateways.
6. Click Save or Finish Editing.