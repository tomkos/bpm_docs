# Route validation rules for a workflow

In the following diagrams, each step is represented with a circle
and each route is represented with an arrow. The arrow indicates the
direction of the step processing. The diagrams are simplified versions
of how a workflow map looks in the editor.

The following route rules are enforced during workflow validation:

Figure 1. An invalid map with steps that cannot be reached

<!-- image -->

- The step at the lower left is not connected by any route
- The route from the last step on the right goes in the opposite
direction of the rest of the route flow, and the step can never be
reached.

- For each AND-split step, there must be one AND-join (collector)
step. The AND-join step can immediately follow the AND-split step,
or there can be one or more steps in between. 
The following
illustration shows a valid map with all routes from a split meeting
at a join step:
Figure 2. A valid map with all routes from
a split meeting at a join step

In the illustration, all three routes from the split
meet at the join step.
- All paths from the AND-split step can meet at the AND-join
step, or one or more paths can end, that is, stop without going to
the AND-join step. A path is defined as a sequence of contiguous routes
that can be followed between a set of steps.
The following illustration
shows a valid split with one path terminated before join step:
Figure 3. A valid split with one path terminated before the join step

In the illustration, one path from the split step ends
at step A, but the paths with steps B and C proceed to the collector
step (join). Note that at least one path from the split step must
go to the join step.
- A path that passes through an AND-split step cannot return
to that step without first passing through the corresponding AND-join
step. 
The following illustration shows an invalid route with
one path returning to the split step:
Figure 4. An invalid
route with one path returning to the split step

In the illustration, the cycle from step C back to the
split step is not valid. Any path from step C must pass through the
join step.
- A path that passes through an AND-join step cannot return to
that step without first passing through the corresponding AND-split
step. 
The following illustration shows an invalid route that
passes only through the join step:
Figure 5. An invalid route
from step D that passes only through the join step

In the illustration, the route from step D goes to the
join step without passing through the split step, and the cycle from
step D to the join step is not valid. To create a valid cycle, the
path must first pass through the split step.
- All paths that pass through an AND-join step must first pass
through the corresponding AND-split step. 
Figure 6. An invalid
route connecting directly to join step without passing through split
step

In the illustration, the path from step D is not valid
because it did not first pass through the split step.