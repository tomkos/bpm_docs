<!-- image -->

# Prepackaged JMS and MQ fault selectors

You can configure your import and export
bindings to handle faults (for example, business exceptions) that
occur during processing. A fault handler can be set up at three levels:
you can associate a fault handler with a fault, with an operation,
or with a binding. For import bindings, you can also set up a fault
selector to determine whether a response is a fault and, if so, the
name of the fault. See Handling faults in bindings for
more information.

| Fault selectors             | Description                                                                                                                                                                                                                                                        |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header-based fault selector | A header-based fault selector examines the headers in the incoming response message to determine if the response message is a business fault, a runtime exception or a normal message. See Header-based fault selector.                                            |
| SOAP fault selector         | A SOAP fault selector examines the body of the incoming response message for the fault message and examines the SOAP header to determine if the fault is a business or runtime fault, and the fault name in the case of a business fault. See SOAP fault selector. |

If you want to create and use a new data transformation
binding resource, see Creating a data format transformation resource configuration .

## Related concepts

- Prepackaged JMS data format transformations
- JMS function selectors
- Prepackaged MQ data format transformations
- Prepackaged MQ function selectors

## Related reference

- Overview of JMS, MQ JMS and generic JMS bindings
- Data handlers
- Working with the simple JMS data bindings
- Business object XML using JMS text message serialization
- Overview of MQ data format transformations
- Overview of the MQ function selectors