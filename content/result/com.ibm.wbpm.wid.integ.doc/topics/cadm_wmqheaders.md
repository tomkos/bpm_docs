<!-- image -->

# WebSphere MQ headers

WebSphere MQ messages
consist of a system header (the MQMD), zero or more other MQ headers
(system or custom), and a message body. If multiple message headers
exist in the message, the order of the headers is significant.

Each header contains information describing the structure of the
following header. The MQMD describes the first header.

## Limitations

For an MQ import, if you clear Override the reply to queue of the request
message you must handle the response message by using another MQ consumer to listen the
queue. You specify another queue name by using the ReplyToQ property in the MQ
message.

## How MQ headers are parsed

- MQRFH
- MQRFH2
- MQCIH
- MQIIH

Headers that start with MQH are handled
differently. Specific fields of the header are not parsed; they remain
as unparsed bytes.

For other MQ headers, you can write custom
MQ header data bindings to parse those headers.

## How MQ headers are accessed

- Through the service message object (SMO) in a mediation
- Through the ContextService API

- MQMD represents the contents of the WebSphere MQ message description, except
for information determining the structure and encoding of the body.
- MQControl contains information determining the structure and encoding
of a message body.
- MQHeaders contain a list of MQHeader objects.

The MQ header chain is unwound so that, inside the SMO,
each MQ header carries its own control information (CCSID, Encoding,
and Format). Headers can be added or deleted easily, without altering
other header data.

## Setting fields in the MQMD

- Encoding
- CodedCharacterSet
- Format
- Report
- Expiry
- Feedback
- Priority
- Persistence
- CorrelId
- MsgFlags

- UserIdentifier
- AppIdentityData

- UserIdentifier
- AppIdentityData
- PutApplType
- PutApplName
- ApplOriginData

- BackoutCount
- AccountingToken
- PutDate
- PutTime
- Offset
- OriginalLength