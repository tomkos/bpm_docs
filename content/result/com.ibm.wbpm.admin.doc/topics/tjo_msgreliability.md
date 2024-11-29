# Changing message reliability for a bus destination

## About this task

The administrator can specify the reliability setting
on bus destinations, or the reliability can be specified by individual
producers (typically under application control through an API call).
The administrator can specify whether the default reliability for
the destination can be overridden by a producer, and the maximum reliability
that attached producers can request.

To browse or change the
message reliability setting of a destination, use the administrative
console to complete the following steps:

## Procedure

1. Click Service integration > Buses in the navigation pane.
2. Click the name of the bus on which the destination exists
in the content pane.
3. Click Destinations
4. Click the destination name. This displays
the details page for the destination.
5. Review the reliability properties. The following
properties control the message reliability for the destination:
Default reliability
The reliability assigned to a message produced to this destination
when an explicit reliability has not been set by the producer.
Maximum reliability
The maximum reliability of messages accepted by this destination.

These properties can have values from the following
list:
Best effort nonpersistent
Messages are discarded when a messaging engine stops or fails.
Messages may also be discarded if a connection used to send them becomes
unavailable and as a result of constrained system resources.
Express nonpersistent
Messages are discarded when a messaging engine stops or fails.
Messages may also be discarded if a connection used to send them becomes
unavailable.
Reliable nonpersistent
Messages are discarded when a messaging engine stops or fails.
Reliable persistent
Messages may be discarded when a messaging engine fails.
Assured persistent
Messages are not discarded.

For more information about using these properties
to control message reliability, see Message reliability levels.
6. Review whether producers can override the default reliability
setting. 
Enable producers to override default reliability
Select this option to enable producers to override the default
reliability that is set on the destination.
7. Optional: Change the destination properties
to suit your needs. You can further refine the configuration
of a destination by setting other properties to suit your needs, as
described in Configuring bus destinations.
8. Click OK.
9. Save your changes to the master configuration.