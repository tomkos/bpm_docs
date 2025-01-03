# Sample routes for a workflow

Figure 1. Route with no conditions

<!-- image -->

Figure 2. Route with an OR condition

<!-- image -->

Most
workflows require branching at various points as the result of a response
made by a participant. In the illustration about the route condition,
the route from the launch step is always true. The route from the
Eval step depends on the value of a response by the participant at
the Eval step. Only one of the routes is taken.

For example,
if the Eval step requires the participant to respond by choosing either
"OK" or "No," you can define two routes from the step: one route for
the OK response and one for the No response. This type of step is
called an OR-split.

Figure 3. Route with an AND condition

<!-- image -->

When
there are multiple routes from a step and more than one of those routes
can evaluate to true, then work can continue down multiple paths simultaneously.
The work proceeds along all true routes.

In the illustration
about AND conditions, the Write step uses an AND-split. The route
to Graphics is always true, and the Start review path and the Request
graphics path are both processed. The Start review step is an OR-split
that processes either Review A or Review B. The case worker sees that
there are two separate work items: one for Graphics and one for either
A or B.

To create a valid map, you must define a collector
step that brings the work back into a single path at the end of all
the true routes. In this illustration, the Edit step is the collector
step and is an AND-join.

The processing waits just before the
collector step (Edit) until all of the child processes reach this
stage.