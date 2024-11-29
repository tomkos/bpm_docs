# Events not being stored in the persistent data store

## Cause

- The persistent data store not enabled for the event service.
- The events do not belong to an event group that is configured
for event persistence.
- The events are being filtered out by the emitter.

## Remedy

1. In the administrative console, click Service integration > Common
Event Infrastructure > Event service > Event services > event\_service.
2. Make sure the Enable event data store check box is selected.
3. Click OK to save any changes.

1. In the administrative console, click Service integration > Common
Event Infrastructure > Event service > Event services > event\_service > Event
groups > event\_group.
2. Make sure the Persist events to event data store check
box is selected.
3. Click OK to save any changes.

1. In the administrative console, click Service integration > Common
Event Infrastructure > Event emitter factories > emitter\_factory > Event
filter. (Make sure you are viewing the settings for the emitter
factory your event source application is using.)
2. Check to see whether the filter configuration string excludes
the events you are trying to send to consumers. If so, you can either
modify the filter configuration string or modify the event data so
the events are not filtered out.
3. Click OK to save any changes.