# Message Validator mediation primitive properties

## Enabled enabled

Defines whether runtime validation is performed.
If the Enabled property is true, the Message Validator mediation primitive performs runtime
validation. The validation includes all message fields and not just those that you have
overlaid.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | Yes               |
| Valid values   | BooleanNote:      |
| Default        | true              |

## Root root

An XPath 1.0 expression representing the validation
scope.

| Field detail   | Value and notes                                                                                                                                                                                                                                                               |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Required       | Yes                                                                                                                                                                                                                                                                           |
| Valid values   | XPathNote: You can specify: / Refers to the complete SMO /body Refers to the body section of the SMO /headers Refers to the headers of the SMO   Alternatively, you can specify your own XPath expression, in which case only the part of the SMO you specified is validated. |
| Default        | /body                                                                                                                                                                                                                                                                         |

## Considerations

- The Enable and Root properties
are both promotable properties of the Message Validator mediation
primitive and can be set at run time.

## Sample XML code

```
<node name="MessageValidator1" type="MessageValidator">
  <inputTerminal/>
  <outputTerminal>
    <wire targetNode="FlowOrder1"/>
  </outputTerminal>
  <failTerminal/>
</node>
```