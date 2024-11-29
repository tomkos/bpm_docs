# Flow Order mediation primitive properties

## terminals

Specify a caret-delimited (^) list of the order
terminals to be fired. For example, terminals="out1^out2" will cause terminal
out1 to be fired followed by out2.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | Yes               |
| Valid values   | StringNote:       |
| Default        | out1^out2         |

## Sample XML code

```
<node name="FlowOrder1" type="FlowOrder">
  <property name="terminals" value="out1^out2^out3"/>
  <inputTerminal/>
  <outputTerminal name="out1">
    <wire targetNode="CustomMediation1"/>
  </outputTerminal>
  <outputTerminal name="out2">
    <wire targetNode="MessageElementSetter1"/>
  </outputTerminal>
  <outputTerminal name="out3">
    <wire targetNode="MessageFilter1"/>
  </outputTerminal>
</node>
```