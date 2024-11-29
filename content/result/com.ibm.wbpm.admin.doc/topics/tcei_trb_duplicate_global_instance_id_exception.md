# Error when sending event (message CEIEM0025E)

## Cause

This problem indicates that the emitter
submitted the event, but the event service rejected it because another
event already exists with the same global instance identifier. Each
event must have a unique global instance identifier, specified by
the globalInstanceId property.

## Remedy

- Make sure your event source application generates a unique global
instance identifier for each event.
- Leave the globalInstanceId property of your submitted events empty.
The emitter then automatically generates a unique identifier for each
event.