<!-- image -->

# Function selector

- One Operation Function Selector, returns the operation defined on the
interface.
- TargetFunctionName header, returns the value of the TargetFunctionName
property stored in the message header. This is used for module to module communication.
- Message Type Selector, uses the JMS or MQ message type property in the
inbound message to determine the function name.
- MQ message body format, uses the MQ message body format as the function
name.
- URL and HTTP method, uses the URL context path and HTTP method to
determine the function name.
- Web Service service gateway function selector, uses the web service
message to determine the operation name.

An API is provided for custom function selectors to be created. These are implemented with a Java
class that implements the commonj.connector.runtime.FunctionSelector interface.