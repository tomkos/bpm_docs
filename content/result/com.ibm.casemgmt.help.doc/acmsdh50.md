# Activity preconditions

If the preconditions for an activity are not fully satisfied and the activity has a trigger, such
as updating a case property or a filing a document. The activity remains in waiting state until the
next trigger occurs to reevaluate the preconditions.

An activity with preconditions is complete after all preconditions are met. However, the trigger
you defined starts only if all its preconditions are met, such as when a second document is
added.

You can join the conditions by using the Boolean ALL or ANY
operators.

Depending on the property type, the operators in the expression
change.

Optionally, you can specify more property conditions. If you specify more property
conditions, the property conditions must also be met for an activity to start.

You can also
mark the activity as repeatable when the precondition is satisfied.

Optionally, you can specify more property
conditions. If you specify more property conditions, the conditions must also be met for an activity
to start.

You can mark the activity to repeat when the precondition is satisfied. For example,
if your activity is to review an accident claim estimate, you can define the activity to repeat. A
new activity is created and work is added to the in-basket of the case worker. The claim estimate is
reviewed each time that a repair estimate document is added to the case.

For example, you can include
several activities into an activity group, and use the completion of the activity group to trigger
an activity. You can also mark the activity to repeat when the precondition is satisfied.

You can update the preconditions for an activity at any time, including on deployed solutions. If
you change the expression of a property condition for a deployed solution, for activity types that
have the A property condition is met precondition, run the precondition
checker utility after you redeploy the solution.