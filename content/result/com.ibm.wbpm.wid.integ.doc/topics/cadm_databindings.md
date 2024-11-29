<!-- image -->

# Data bindings

You use IBM® Integration
Designer to
specify which data binding you want to use or to create your own data
binding. A discussion of creating data bindings can be found in the Overview
of JMS, MQ JMS and generic JMS bindings section of the IBM Integration
Designer information
center.

## JMS bindings

- JMS bindings
- Generic JMS bindings
- WebSphere® MQ JMS bindings

The table also includes a description of the tasks that
the data bindings perform.

| Data binding            | Native data to business object                                                                                                                                                                             | Business object to native data                                                                                                                                                 |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Serialized Java™ object | Transforms the Java serialized object into a business object (which is mapped as the input or output type in the WSDL).                                                                                    | Serializes a business object to the Java serialized object in the JMS object message.                                                                                          |
| Wrapped bytes           | Extracts the bytes from the incoming JMS bytes message and wraps them into the JMSBytesBody business object.                                                                                               | Extracts the bytes from the JMSBytesBody business object and wraps them into the outgoing JMS bytes message                                                                    |
| Wrapped map entry       | Extracts the name, value, and type information for every entry in the incoming JMS map message and creates a list of MapEntry business objects. It then wraps the list into the JMSMapBody business object | Extracts the name, value, and type information from the MapEntry list in the JMSMapBody business object and creates the corresponding entries in the outgoing JMS map message. |
| Wrapped object          | Extracts the object from the incoming JMS object message and wraps it into the JMSObjectBody business object.                                                                                              | Extracts the object from the JMSObjectBody business object and wraps it into the outgoing JMS object message.                                                                  |
| Wrapped text            | Extracts the text from the incoming JMS text message and wraps it into the JMSTextBody business object.                                                                                                    | Extracts the text from the JMSTextBody business object and wraps it into the outgoing JMS text message.                                                                        |

## WebSphere MQ
bindings

The following table lists the data bindings that
can be used with WebSphere MQ
and describes the tasks that the data bindings perform.

| Data binding           | Native data to business object                                                                                                                                                                                   | Business object to native data                                                                                                                                            |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Serialized Java object | Transforms the Java serialized object from the incoming message into a business object (which is mapped as the input or output type in the WSDL).                                                                | Transforms a business object to the Java serialized object in the outgoing message                                                                                        |
| Wrapped bytes          | Extracts the bytes from the unstructured MQ bytes message and wraps them into the JMSBytesBody business object.                                                                                                  | Extracts the bytes from a JMSBytesBody business object and wraps the bytes into the outgoing unstructured MQ bytes message.                                               |
| Wrapped text           | Extracts the text from an unstructured MQ text message and wraps it into a JMSTextBody business object.                                                                                                          | Extracts text from a JMSTextBody business object and wraps it in an unstructured MQ text message.                                                                         |
| Wrapped stream entry   | Extracts the name and type information for every entry in the incoming JMS stream message and creates a list of the StreamEntry business objects. It then wraps the list into the JMSStreamBody business object. | Extracts the name and type information from the StreamEntry list in the JMSStreamBody business object and creates corresponding entries in the outgoing JMSStreamMessage. |

In addition to the data bindings listed in Table 2, WebSphere MQ also uses header
data bindings. See the IBM Integration
Designer information
center for details.

## HTTP bindings

The following table lists
the data bindings that can be used with
HTTP and describes the tasks that the data bindings
perform.

| Data binding   | Native data to business object                                                                                   | Business object to native data                                                                                |
|----------------|------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Wrapped bytes  | Extracts the bytes from the body of the incoming HTTP message and wraps them into the HTTPBytes business object. | Extracts the bytes from the HTTPBytes business object and adds them to the body of the outgoing HTTP message. |
| Wrapped text   | Extracts the text from the body of the incoming HTTP message and wraps it into the HTTPText business object.     | Extracts the text from the HTTPText business object and adds it to the body of the outgoing HTTP message.     |