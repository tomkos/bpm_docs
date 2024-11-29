# Message Filter mediation primitive properties

## Enabled enabled

Defines whether the message is mediated by the
Message Filter mediation primitive. By default the mediate action of the Message Filter mediation
primitive is enabled. You can suspend the mediate action by clearing the check box. If you suspend
the mediation, the message goes to the default terminal.

## Distribution mode distributionMode

Determines the behavior of the mediation
primitive when an inbound message matches multiple expressions.

If there is no matching output terminal, the default terminal is
invoked.

## Filters filters

A list of expressions, and associated terminal
names, that define the filtering performed by the mediation primitive.

## Considerations

If there is a syntax error in the XPath expression of a Pattern it
can cause an exception at run time.

## Sample XML code

```
<node name="MessageFilter1" type="MessageFilter">
  <table name="filters">
    <row>
      <property name="pattern" value="/body/myRequestMsg/person/name=&quot;Bob&quot;"/>
      <property name="terminalName" value="match1"/>
    </row>
  </table>
  <inputTerminal/>
  <outputTerminal name="default">
    <wire targetNode="MessageElementSetter1"/>
  </outputTerminal>
  <outputTerminal name="match1"/>
  <failTerminal/>
</node>
```