# Error when querying an event group (message CEIES0048E)

## Cause

This problem indicates that the event
consumer application performed a query using the EventAccess bean,
but the consumer specified an event group name that does not correspond
to any existing event group.

## Remedy

1. In the administrative console, click Service integration > Common
Event Infrastructure > Event service > Event services > event\_service > Event
groups. The table shows a list of all event groups defined for
the event service.
2. Make sure the event source specifies a defined event group name
in the parameters of the query method call.