# Adding MQCIH statically in a WebSphere MQ binding

There are various ways to add MQCIH header information to a message
(for example, by using the Header Setter mediation primitive). It
might be useful to add this header information statically, without
the use of an additional mediation module. Static header information,
including the CICS® program name, the transaction ID, and other
data format header details, can be defined and added as part of the
WebSphere MQ binding.

WebSphere® MQ, the MQ CICS Bridge,
and CICS must be configured for MQCIH header information
to be added statically.

You can use Integration Designer to
configure the WebSphere MQ import with the static values that are
required for the MQCIH header information.

When a message arrives and is processed by the WebSphere MQ import,
a check is made to see if MQCIH header information is already present
in the message. If the MQCIH is present, the static values defined
in the WebSphere MQ import are used to override the corresponding
dynamic values in the message. If the MQCIH is not present, one is
created in the message and the static values defined in the WebSphere
MQ import are added.

The static values defined in the WebSphere MQ import are specific
to a method. You can specify different static MQCIH values for different
methods within the same WebSphere MQ import.

This facility is not used to provide default values if the MQCIH
does not contain specific header information because a static value
defined in the WebSphere MQ import will override a corresponding value
provided in the incoming message.