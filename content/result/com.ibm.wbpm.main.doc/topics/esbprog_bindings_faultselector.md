<!-- image -->

# Fault handling

## Fault selector

- Header Based, uses the message properties FaultType and FaultName to
determine the fault name.
- SOAP, checks for a SOAP fault in the body of the message and uses the
SOAP header to determine the fault name.

An API is provided for custom fault selectors to be written. These are implemented with a Java
class that implements the commonj.connector.runtime.FaultSelector interface.

## Fault handler

A fault handler is a type of data handler that is designed to handle fault message data. A fault
handler processes fault data and transforms it into the correct format to be sent by the export or
import binding. Fault handlers are defined in combination with the response data handler, so that an
import can handle runtime exceptions and business faults returned to it. They are only defined on
imports. They default to the data handler defined for the response data. Similarly to data handlers,
they can be defined at the binding, interface and operation level. Any of the data handlers provided
by Workflow Server can be used as a fault handler.