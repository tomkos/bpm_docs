# Fan In mediation primitive properties

## Fan Out ID fanOutID

The identifier corresponding to the Fan Out mediation
primitive that is associated with the Fan In.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | Yes               |
| Valid values   | StringNote:       |

## Decision
Type decisionType

The out terminal is fired when a
decision point is reached.

| Field detail   | Value and notes                                                                                                                                                                                                                                                                            |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Required       | Yes                                                                                                                                                                                                                                                                                        |
| Valid values   | Count 0 A simple count. XPath 1 An XPath expression. Iterate 2 The Fan In mediation primitive waits to receive all the messages produced by the corresponding Fan Out mediation primitive, when the Fan Out primitive is in iterate mode. The valid type is Boolean: true or false.  Note: |
| Default        | Count                                                                                                                                                                                                                                                                                      |

## Enable timeout timeout

The time, in seconds, by which the decision point must be
reached. The timeout period starts when the associated Fan Out fires an output terminal for the
first time. If a message arrives at the Fan In in terminal after this timeout
period, it is considered as being late and the incomplete terminal is fired.

| Field detail   | Value and notes                                                                                  |
|----------------|--------------------------------------------------------------------------------------------------|
| Required       | Yes                                                                                              |
| Valid values   | IntegerNote:                                                                                     |
| Default        | -1The default value of -1 means there is no timeout, and no messages will be considered as late. |

## Count count

The number of messages to receive before firing the
out terminal.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | Yes               |
| Valid values   | IntegerNote:      |
| Default        | 1                 |

## XPath
Completion Expression xpathCompletionExpression

The XPath expression that must evaluate to
true before firing the out terminal.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | No                |
| Valid values   | XPathNote:        |

## Considerations

- The Async Timeout values for Service Invoke
mediation primitives should not exceed the value of the Timeout property
of the aggregation's Fan In.
- Certain properties are promotable; therefore, you can change theirvalue from the runtime administrative console. The following propertiescan be promoted:
    - Count
    - XPath
    - Timeout

## Sample XML code

```
<node name="endAggregation" type="FanIn>
  <property name="fanOutID" value="startAggregation"/>
  <property name="decisionType" value="2"/>
  <inputTerminal/>
  <inputTerminal name="stop"/>
  <outputTerminal/>
  <outputTerminal name="incomplete"/>
  <failTerminal/>
</node>
```