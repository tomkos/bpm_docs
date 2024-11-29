# Events not being received by consumers (NameNotFoundException)

## Cause

This problem indicates that the event
group configuration specifies one or more JMS resources that do not
exist.

## Remedy

1. In the administrative console, click Service integration > Common
Event Infrastructure > Event service > Event services > event\_service > Event
groups > event\_group.Multiple event groups: An event might belong to more than one event group.
2. Check the values of the Topic JNDI name and Topic connection
factory JNDI name properties. Verify that the specified JMS resources
exist. If necessary, use the configuration interface of your JMS provider
to create the necessary resources.