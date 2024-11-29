<!-- image -->

# Service Message Objects

- Context information (data other than the message payload and headers).
- Header information associated with the message. For example, Java™ Message Service (JMS) headers if a message has been conveyed using the JMS API, or MQ
headers if the messages has come from WebSphere® MQ.
- The body of the message: the message payload, is the application data exchanged between service
endpoints.
- Message attachments

The SMO is a DataObject and its content can be accessed via the Service Data Object API (SDO
API). SDO is a standard for representing structured business data. The body of the SMO contains a
business object representing the application payload.

- SMO structure

All SMOs have the same basic structure. The structure consists of a data object called a ServiceMessageObject, which contains other data objects representing the header, body, attachments, and context data.
- Data representation of SMO

A SMO has an SDO and XML nature and behaves like a business object. This means that you can always obtain XML representations of the SMO. A SMO can also be treated as a business object.