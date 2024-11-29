<!-- image -->

# Overview of the MQ function selectors

There has to be some mechanism that can be used to determine
which SCA operation the message corresponds with. An MQ message contains
only data and carries no indication about the target operation for
which it is intended. Therefore, we need to map an MQ message to an
operation of the targeted service interface. The MQ export listens
to a particular destination. When a message arrives to that destination,
the function selector determines the target operation.

- Set of MQ function selectors
- Implementing your own function selector

## Set of MQ function selectors

Several
function selectors are provided for your selection at binding generation
time. The function selector choices you will see on the user interface
are as follows:

- Use handleMessage as the native function (default)
returns handleMessage as a value. The value is mapped using the export's
method bindings to the name of an operation on the interface. The
native method is assumed to be handleMessage from the SCA application's
perspective. The SCA application does not need to understand the internal
representation of the MQ message, but only how it drives the current
operation on the interface. It is the recommended selection for most
applications. It may be necessary to edit one of the method bindings
to bind an operation to the handleMessage native function.
- Use messagebody's format as the native function finds
the Format field of the last header and returns that field as a String.
- Use Type information as the native function creates
a method in your export binding by retrieving a URL containing the
Msd, Set, Type and Format properties found in the MQRFH2 header. The
name of the method will be the interface operation name. This selector
can by used to interoperate with messages coming from MQ JMS clients
and WebSphere® Business
Integration Message Broker flows.
- Use JMS default function selector means
that the JMS function selector is used to create a method in your
export binding (see Overview of JMS function selectors). The name
of the method will be the interface operation name. This function
selector reads the native operation from the TargetFunctionName property
of the folder of an MQRFH2 header.
- Service Gateway function selector should
be used in conjunction with an HTTP binding using the Service Gateway
interface. It determines if the request is a one-way or two-way operation
based on the message type field within the message.
- User supplied means you create your own
function selector by implementing the com.ibm.websphere.sca.mq.selector.MQFunctionSelector class.
Implementing your own function selector is discussed in the following
section.

## Implementing your own function selector

The
easiest, and recommended, way to build an MQ function selector is
to extend the MQFunctionSelector class implementing
an abstract method. The function selector's generateEISFunctionName() method
has a single argument with an array of type Object.
The MQFunctionSelector class unmarshalls these parameters
and calls an overloaded generateEISFunctionName() method
with a more intuitive argument list, as shown in the following code.
The array of four parameters represents different parts of the MQ
message.

```
public abstract class MQFunctionSelector implements
		commonj.connector.runtime.FunctionSelector {
	public final String generateEISFunctionName(Object[] args)
			throws SelectorException;

	public abstract String generateEISFunctionName(MQMD md, String bodyFormat,
			List headers, MQDataInputStream input) throws IOException,
			SelectorException;
}
```

You may alternately provide an implementation of the commonj.connector.runtime.FunctionSelector interface
to create your own function selector. If you are implementing your
own function selector, you will need to understand the header data
binding and body data binding framework as the function selector is
given a list of parsed header objects and an unparsed body in an MQDataInputStream input.

## Related concepts

- Prepackaged MQ data format transformations
- Prepackaged MQ function selectors

## Related reference

- Overview of MQ data format transformations
- Data handlers
- Prepackaged JMS and MQ fault selectors