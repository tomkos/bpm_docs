<!-- image -->

# JMS headers

## JMS system header

The JMS system header
is represented in the SMO by the JMSHeader element, which contains
all the fields typically found in a JMS header. Although these can
be modified in the mediation (or ContextService), some JMS system
header fields set in the SMO will not be propagated in the outbound
JMS message as they are overridden by system or static values.

- JMSType and JMSCorrelationID - values of the specific
predefined message header properties
- JMSDeliveryMode - values for delivery mode (persistent
or nonpersistent; default is persistent)
- JMSPriority - priority value (0 to 9; default is JMS\_Default\_Priority)

## JMS properties

JMS properties are represented
in the SMO as entries in the Properties list. The properties can be
added, updated, or deleted in a mediation or by using the ContextService
API.

Properties can also be set statically in the JMS binding. Properties
that are set statically override settings (with the same name) that
are set dynamically.

User properties propagated from other bindings (for example,
an HTTP binding) will be output in the JMS binding as JMS properties.

## Header propagation settings

The propagation
of the JMS system header and properties either from the inbound JMS
message to downstream components or from upstream components to the
outbound JMS message can be controlled by the Propagate Protocol Header
flag on the binding.

- JMS export requestThe JMS header received in the message will
be propagated to target components by way of the context service.
JMS properties received in the message will be propagated to target
components by way of the context service.
- JMS export responseAny JMS header fields set in the context
service will be used in the outbound message, if not overridden by
static properties set on the JMS export binding. Any properties set
in the context service will be used in the outbound message if not
overridden by static properties set on the JMS export binding.
- JMS import requestAny JMS header fields set in the context
service will be used in the outbound message, if not overridden by
static properties set on the JMS import binding. Any properties set
in the context service will be used in the outbound message if not
overridden by static properties set on the JMS import binding.
- JMS import responseThe JMS header received in the message will
be propagated to target components by way of the context service.
JMS properties received in the message will be propagated to target
components by way of the context service.