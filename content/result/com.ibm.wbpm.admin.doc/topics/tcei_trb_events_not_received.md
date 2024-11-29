# Events not being received by consumers (no error message)

## Cause

- Event distribution is not enabled for the event service.
- The events are being filtered out by the emitter.
- The events are being filtered out by the notification helper.
- The event consumer is not specifying the correct event group.
- The JMS connection is not started.

## Remedy

The remedy for this problem depends
upon the underlying cause.

- To verify that event distribution is enabled for the eventservice:
    1. In the administrative console, click Service integration > Common
Event Infrastructure > Event service > Event services > event\_service.
    2. If the Enable event distribution property is not selected,
select the check box.
    3. Click OK to save any changes.
- To check the event filter settings for the emitter:

1. In the administrative console, click Service integration > Common
Event Infrastructure > Event emitter factories > emitter\_factory > Event
filter. (Make sure you are viewing the settings for the emitter
factory your event source application is using.)
2. Check to see whether the filter configuration string excludes
the events you are trying to send to consumers. If so, you can either
modify the filter configuration string or modify the event data so
the events are not filtered out.
3. Click OK to save any changes.
- To check the event filter settings for the notificationhelper:

1. Check your event consumer application to see if an event selector
is specified for the notification helper using the NotificationHelper.setEventSelector
method.
2. If an event selector is specified, make sure it does not exclude
the event you are trying to receive. (A null event selector passes
all events.)
- To check the event group specified by the event consumer:

1. In the administrative console, click Service integration > Common
Event Infrastructure > Event service > Event services > event\_service > Event
groups. The table shows a list of all event groups defined for
the event service.
2. Select the event group your event consumer subscribes to.
3. Find the Event selector string property.
4 Make sure the specified event selector matches the content ofthe event you are trying to receive. If it does not match, you mightwant to make one of the following changes:
    - Modify the event selector so the event is included in the event
group.
    - Modify the event data so the event matches the event group.
    - Modify your event consumer to subscribe to a different event group
that includes the event.
- To start the JMS connection:In your event consumer,
use the QueueConnection.start() method or the TopicConnection.start()
method before attempting to receive events.