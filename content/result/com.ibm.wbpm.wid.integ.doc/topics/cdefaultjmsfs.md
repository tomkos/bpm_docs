<!-- image -->

# Default JMS function selector

## Default function selector

There
has to be some mechanism that can be used to determine which of the
possible JMS or MQ JMS export components the message should be delivered
to, and which SCA operation the message corresponds with. A JMS or
MQ JMS message contains only data, and the message may contain an
indication about the target operation, but there is not a standard
way to retrieve this information. Therefore, we need to map a certain
message to a certain operation of the targeted service interface.
The JMS or MQ JMS export listens to a particular destination. When
a message arrives to that destination, the function selector determines
the target operation.

In the export binding, the method binding
has a native method , which contains an identifier representing
a JMS or MQ JMS message.  Use of the native method allows for a level
of indirection, which enables rename of an operation, without affecting
the mapping.

By default, the value of native method is set to
the interface operation name when the export is created.  The export
utilizes a function selector to inspect an incoming message in the
message header or the message body. The export provides a default
function selector that returns the value of JMS String Property TargetFunctionName from
the header.  So to identify the JMS or MQ JMS messages, the default
behavior is for the import to set the JMS header property TargetFunctionName to
the name of the interface operation name, and the default function
selector used by the export will extract the TargetFunctionName property
from the JMS header to correctly identify the incoming message.  If
the manner in which the native method name is to be found does not
use the TargetFunctionName property, then a FunctionSelector implementation
must be provided to correctly map the incoming JMS message to its
intended SCA operation.

The commonj.connector.runtime.FunctionSelector interface
presented below is used to extract the native function name or identifier
(event ID) from the native data flowing inbound from the resource
adapter using an EIS export.

```
public interface FunctionSelector {

	public String generateEISFunctionName(Object[] argObjects)
			throws SelectorException;

}
```

The implementation of this interface has to be provided
by a resource adapter or third party who understands how to locate
in the native data the appropriate identifier.

The implementation
for the default JMS function selector basically looks like the following:

```
public class JMSFunctionSelectorImpl implements FunctionSelector {

	public String generateEISFunctionName(Object[] argObjects)
			throws SelectorException {

		try {
			Message message = (Message) argObjects[0];
			String functionName = message
					.getStringProperty("TargetFunctionName");
			return functionName;
		} catch (Throwable e) {
			throw new SelectorException(e);
		}
	}
}
```

Some other possible implementations for a FunctionSelector could
use the JMSType header property or hard code the
name of the method on the interface. Why would you hard code the name
of the method on the interface? You would only hard code the name
of the method if there were only one target SCA operation and that
operation had a single input or output. Using the header property
would typically be done for routing the message, performing some parsing
and applying some logic to the parsed message. But suppose your application
does not require any routing? A hard coded value in this case would
make sense.

```
public class JMSFunctionSelectorImpl implements FunctionSelector {

    public String generateEISFunctionName(Object[] argObjects) throws SelectorException {
		
	return "handleMessage";
}
```

Another possible implementation is to have the SCA
application handle the routing. The mapped SCA operation would decide
how to dispatch the message and then another part of the application
would parse the message contents represented by its Service Data Object
(SDO).

The following method demonstrates how a JMSType function
selector could be used to create a name for the function:

```
public String generateEISFunctionName(Object[] arg)
			throws SelectorException {

		try {
			Message message = (Message) arg[0];
			String type = message.getJMSType();
			return type;
		} catch (JMSException e) {
			// Todo - Auto-generated catch block
			throw new SelectorException(e);
		}
	}
```