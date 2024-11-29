# Event Emitter mediation primitive properties

## Enabled enabled

By default, the mediate action of this mediation
primitive is enabled. You can suspend the mediate action by clearing the check box.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | Yes               |
| Valid values   | BooleanNote:      |
| Default        | true              |

## Label label

Allows you to define a unique identifier for the event.

The unique identifier maps to the extension name of the event that conforms to the Common Base
Event specification. IBM Integration
Designer provides a default
label, but it is strongly recommended that you provide a more meaningful event label for your
particular event type. Events are emitted to the CEI server, which can be accessed by many different
event consumer applications; therefore, event names should be unique across the system in order to
distinguish different event types. If two Event Emitter mediation primitives generate exactly the
same event type, it might be acceptable to have the same Label name.

The default is a combination of module name, flow name, and flow type. The flow type indicates
whether the flow is a request or a response.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | Yes               |
| Valid values   | StringNote:       |

## Root root

An XPath 1.0 expression representing the part of the
message to be included in the event.

| Field detail   | Value and notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Required       | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Valid values   | XPathNote: You can specify: <exclude message content from event data>, /, /headers, /context, /body, or your own XPath expression. <exclude message content from event data> indicates that no data will be included within the event body, / refers to the complete SMO, /headers refers to the headers of the SMO, /context refers to the context of the SMO, and /body refers to the body section of the SMO. If you specify your own XPath expression, the part of the SMO that you specify is processed. |

## Transaction mode transactionMode

Lets you override the transaction mode set on
the emitter. (An event source, such as an Event Emitter mediation primitive, does not interact
directly with the event server; instead it interacts with an object called an emitter.) The
transaction mode can be configured in the CEI infrastructure or overridden at the Event Emitter
mediation primitive level.

| Field detail   | Value and notes                                                                                                                                                                                                                                   |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Required       | Yes                                                                                                                                                                                                                                               |
| Valid values   | Default 0 Events are sent to the CEI server using the default setting in the CEI emitter.  Existing 1 Events are sent to the CEI server in the flow's transaction. New 2 Events are sent to the CEI server outside the flow's transaction.  Note: |
| Default        | Default                                                                                                                                                                                                                                           |

## Considerations

- If a problem occurs when an event is sent to the CEI server, a
runtime exception occurs and the fail terminal
of the mediation primitive is triggered.
- If you use the Event Emitter mediation primitive to record a failure
in another mediation primitive, and then explicitly cause the flow
to fail (by wiring the Event Emitter out terminal
to the Fail mediation primitive), you must consider the runtime implications.
If the mediation module is configured to run inside a global transaction,
the Event Emitter mediation primitive must be configured to send events
in a New transaction. Otherwise, the event
created by the Event Emitter mediation primitive could be rolled back
(and lost).

## Sample XML code

```
<node name="EventEmitter1" type="EventEmitter">
  <property name="label" value="TestMod\_TestMod\_EventEmitter1\_Req"/>
  <property name="root" value="/body"/>
  <inputTerminal/>
  <outputTerminal/>
  <failTerminal/>
</node>
```