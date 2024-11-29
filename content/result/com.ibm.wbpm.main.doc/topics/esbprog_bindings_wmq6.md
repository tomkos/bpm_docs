<!-- image -->

# Using a mediation flow component to access the WebSphere MQ header

## Limitations

For an MQ import, if you clear Override the reply to queue of the request
message you must handle the response message by using another MQ consumer to listen the
queue. You specify another queue name by using the ReplyToQ property in the MQ
message.

Figure 1. MQ Header Setter mediation primitive properties

<!-- image -->

If you need to change multiple headers, you can set multiple actions. Multiple actions are
processed sequentially, in the order you specify. The MQ Header Setter mediation primitive does not
provide control of the MQMD header, which you can change using the MessageElementSetter, and Mapping mediation
primitives.

- MsgType
- MsgID
- BackoutCount
- ReplyToQ
- ReplyToQMgr
- UserIdentifier
- AccountingToken
- ApplIdentityData
- PutApplType
- PutApplName
- PutDate
- PutTime
- ApplOriginData
- GroupId
- MsgSeqNumber
- Offset
- OriginalLength

- UserIdentifier
- AppIdentityData
- PutApplType
- PutApplName
- ApplOriginData

- MsgID - request Message ID options must be set to copy from a SCA
message.
- MsgType - Clear the check box for the property: Set the message
type to MQMT\_DATAGRAM or MQMT\_REQUEST for request-response operations.
- ReplyToQ - Select the check box for the property:  Override the
reply to queue of request message.
- ReplyToQMgr - Select the check box for the property: Override
the reply to the queue of the request message. You can optionally define a queue
manager.

- BackoutCount
- AccountingToken
- PutDate
- PutTime
- Offset
- OriginalLength