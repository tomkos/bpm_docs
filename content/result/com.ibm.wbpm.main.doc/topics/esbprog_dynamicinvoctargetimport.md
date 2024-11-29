# Dynamic invocation with a target import

Dynamic invocation with a target import allows the configuration
and protocol used to call a service to be dynamically selected at
run time by identifying a supported import binding. The import and
its binding must already be available within the module and is selected
at run time according to information contained in the message.

You
can use Integration Designer to create
a mediation module that selects the target service dynamically at
run time. The target services might use different protocols, different
formats or different quality-of-service values. Each combination must
be known at the time the mediation module is developed. This means
that for each combination of protocol, format, and quality-of-service
value, Integration Designer includes
an import in the mediation module with an appropriate configuration.

- Gold customers receive a reliable real-time stock quote, which
is mapped within the mediation flow component using a JMS binding.
- Standard customers receive a delayed stock quote, which is mapped
with a WebServices binding.

Figure 1. Dynamic invocation
with a target import

<!-- image -->

In
addition to dynamically selecting an import, a new target address
can also be set using the incoming message content and routing information.
The mediation flow component sets the new address by changing the
SMO values using the Endpoint Lookup mediation primitive, and registering
the Gold and Standard Services in WSRR. The choice between the target
service destinations is made dynamically at run time using available
metadata provided by the message or by WSRR. The name of the target
import is placed in the SMO Header by the Endpoint Lookup mediation
primitive. If an import is targeted that does not support the target
endpoint, a ServiceRuntimeException will occur.