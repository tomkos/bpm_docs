<!-- image -->

# An activity has stopped because of an unhandled fault (Message:
CWWBE0057I)

## Reason

- A fault is raised by either the activity's implementation or during
the evaluation of a condition, timer, or counter value associated
with the activity, for example, its join condition or any of the transition
conditions of its outgoing links.
- The fault is not handled on the enclosing scope.
- For invoke activities, inline human tasks, and Java snippets,if either of the following happens:
    - The continueOnError attribute of the process is set to no and
the continueOnError attribute of the activity is set to inherit or no.
    - The continueOnError attribute of the process is set to yes and
the continueOnError attribute of the activity is set to no.
- For all other activities, the continueOnError attribute of the
process is set to no.

## Resolution

1. An administrator must repair the stopped activity instance manually.
For example, to force complete or force retry the stopped activity
instance.
2. The reason for the failure must be investigated. In some cases
the failure is caused by a modeling error that must be corrected in
the model.