# Runtime states for activities in process applications

- If an automatic activity has no precondition or if it has a precondition
that evaluated to true, the activity is put into the WORKING state.
- If a manual activity has no precondition or if it has a precondition
that evaluated to true, the activity is put into the READY state.
- For both automatic and manual activities, if the activity has
a precondition that evaluated to false, the activity is put into the WAITING state.

<!-- image -->

For each non-end state, a set of events or actions cause the activity to go into another
state.

- When the precondition evaluates to true:
    - If it is an automatic activity, the activity changes to the LAUNCHING
state.
    - If it is a manual activity, the activity changes to the READY state.
- If the user clicks Disable or the corresponding REST API is
invoked, the activity changes to the DISABLED state.
- If the activity is optional and the enclosing scope ends, the activity changes
to the NOT USED state.

- If the user clicks Start or the corresponding REST API is invoked, the
activity changes to the WORKING state.
- If the user clicks Disable or the corresponding REST API is
invoked, the activity changes to the DISABLED state.
- If the activity is optional and the enclosing scope ends, the activity changes
to the NOT USED state.

- If the activity completes successfully, it changes to the COMPLETED state.
- If the activity completes unsuccessfully, it changes to the FAILED state.

- The administrator repairs the activity and restarts it. The activity is put into the
WORKING state.
- The administrator determines that the activity cannot be repaired puts it into the
SKIPPED state. The processing of the instance continues without the activity.

- If the user clicks Enable or the corresponding REST API is invoked, the
activity returns to the state that the activity was in when it was disabled:
WAITING or READY. Remember: If the activity was in the
WAITING state when it was disabled and the precondition now evaluates to true, the
activity changes to the READY state.
- If the activity is optional and the enclosing scope ends, the activity changes
to the NOT USED state.

- Ready shows manual activities that are in READY or
WAITING state.
- In progress shows all activities that are in WORKING
state or automatic activities that are in WAITING state.
- Complete shows activities that are in COMPLETED,
FAILED, and DISABLED states.
- In Process Inspector, All shows all activities regardless of their state.
In Process Portal, All shows activities in READY,
WAITING, WORKING, COMPLETED,
FAILED, and DISABLED states. It does not show activities in the
NOT USED or SKIPPED state.