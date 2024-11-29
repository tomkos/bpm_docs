<!-- image -->

# Link Evaluation Order tab: BPEL process editor

When an activity in a generalized flow has more than one
outgoing link an outgoing gateway is created. This Link
Evaluation Order tab appears when you select an outgoing
split gateway. For a split gateway, the first link that evaluates
to true is the one that is followed, and since the default
condition for a link is true, it may then be necessary to adjust
the Evaluation position of the links to ensure
that the appropriate link is fired.

To adjust the evaluation
order, select a link in the table, and then click either the Up or Down buttons
to change its numeric position. Those links that are higher in the
list are preferentially followed.

## Related tasks

- Working with generalized flow activities