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

## Class MQMessages

- java.lang.Object
    - teamworks.MQMessages

- public class MQMessages
extends java.lang.Object
This MQMessages class can be used to add messages using the MQQueueManager class.
 
Use this class only if using IBM MQ.
 
MQMessages does not support the Secure Sockets Layer (SSL).

- ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Constructor Summary

Constructors 

Constructor and Description

MQMessages()
Default constructor.
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getMessage (java.lang.String hostname, java.lang.String queueManagerName, java.lang.String channel, java.lang.Integer port, java.lang.String queueName) Retrieves the message from the MQQueueManager. void putMessage (java.lang.String messageContent, java.lang.String hostname, java.lang.String queueManagerName, java.lang.String channel, java.lang.Integer port, java.lang.String queueName) Adds a message to the MQQueueManager.

### Method Summary

| Modifier and Type   | Method and Description                                                                                                                                                                                                                                                          |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| java.lang.String    | getMessage(java.lang.String hostname,           java.lang.String queueManagerName,           java.lang.String channel,           java.lang.Integer port,           java.lang.String queueName) Retrieves the message from the MQQueueManager.                                   |
| void                | putMessage(java.lang.String messageContent,           java.lang.String hostname,           java.lang.String queueManagerName,           java.lang.String channel,           java.lang.Integer port,           java.lang.String queueName) Adds a message to the MQQueueManager. |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait