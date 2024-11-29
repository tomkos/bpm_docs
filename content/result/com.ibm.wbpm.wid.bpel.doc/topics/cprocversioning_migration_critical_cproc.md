<!-- image -->

# BPEL process migration: Changes to the business logic of a
process instance

The following business logic changes are supported.

## Basic activities

- Assign
- Empty
- Human task
- Invoke
- Java snippet
- Reply
- Rethrow
- Terminate
- Throw
- Wait

## Structured activities

To migrate an existing process instance, the process
navigation can have reached the source activity of the link, but this
activity must not yet be complete. In addition, if the new version
of the process contains a new link, the process navigation must also
not have reached the target activity.

If
the new version of the process contains any changes that affect the
business logic of the generalized flow, then the entire generalized
flow must be after the current position of the process navigation
for existing process instances to be migrated.

An existing process instance
can be migrated as long as the current navigation position is before
other business logic changes in the current branch. In addition, if
the scope, switch, or pick activity that contains the branch has been
navigated, the process instance cannot be migrated.