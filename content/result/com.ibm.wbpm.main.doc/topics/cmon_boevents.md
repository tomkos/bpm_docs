<!-- image -->

# Business objects in events

You specify the level of business object detail that will be captured in service component
events. This level of detail affects only the amount of business object code that will be passed to
the event; all the other Common Base Event elements (both standard and event-specific) will be
published to the event.

The names of the detail levels applicable to service component events differ depending on whether
you created a static monitor using IBM® Integration
Designer
or a dynamic monitor on the administrative console, but they correspond as shown in the following
table:

| Administrative console detail level   | Common Base Event/Integration Designer detail level   | Payload information published   |
|---------------------------------------|-------------------------------------------------------|---------------------------------|
| FINE                                  | EMPTY                                                 | None.                           |
| FINER                                 | DIGEST                                                | Payload description only.       |
| FINEST                                | FULL                                                  | All of the payload.             |

The detail level is specified by the PayloadType element, which is part of the
event instance data. The actual business object data is included in the event only if the monitor is
set to record FULL/FINEST detail.

The business object data itself is included in the Common Base Event under an
xsd:any schema. You can see the process server business object payloads with the
root element named wbi:event.

If you are publishing the event output to the logger, you will see the output when you view the
log files.