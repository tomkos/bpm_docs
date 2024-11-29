- Overview
- Package
- Class
- Tree
- Deprecated
- Index
- Help

- Prev Class
- Next Class

- Frames
- No Frames

- All Classes

- Summary:
- Nested |
- Field |
- Constr |
- Method

- Detail:
- Field |
- Constr |
- Method

## Class JMSMessage

- java.lang.Object
    - teamworks.JMSMessage

- public class JMSMessage
extends java.lang.Object
The JMSMessage class can be used to add messages to a JMS queue and to receive messages from a JMS queue.
 
Use this class for all JMS providers except IBM MQ.
 
JMSMessage does not support the Secure Sockets Layer (SSL).

- ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Constructor Summary

Constructors 

Constructor and Description

JMSMessage()
Default constructor.
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getMessage (java.lang.String initialContext, java.lang.String providerUrl, java.lang.String connectionFactory, java.lang.String queueName, java.lang.Boolean lookup, java.lang.String filter) Retrieves the message from the JMS Queue. void putMessage (java.lang.String initialContext, java.lang.String providerUrl, java.lang.String messageContent, java.lang.String connectionFactory, java.lang.String queueName, java.lang.Boolean lookup, java.util.HashMap properties) Adds a message to a JMS Queue.

### Method Summary

| Modifier and Type   | Method and Description                                                                                                                                                                                                                                                                                                        |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| java.lang.String    | getMessage(java.lang.String initialContext,           java.lang.String providerUrl,           java.lang.String connectionFactory,           java.lang.String queueName,           java.lang.Boolean lookup,           java.lang.String filter) Retrieves the message from the JMS Queue.                                      |
| void                | putMessage(java.lang.String initialContext,           java.lang.String providerUrl,           java.lang.String messageContent,           java.lang.String connectionFactory,           java.lang.String queueName,           java.lang.Boolean lookup,           java.util.HashMap properties) Adds a message to a JMS Queue. |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait