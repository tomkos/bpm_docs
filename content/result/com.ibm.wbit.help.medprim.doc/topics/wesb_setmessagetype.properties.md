# Set Message Type mediation primitive properties

## Message field refinements
typeMap

Use the Message field refinements
property to specify which fields in the message are refined by more specific typing information. By
default, this property is empty.

## Reset message type
resetMessageTypes

If true, causes the current mediation
primitive to reset Message field refinements information from previous Set Message
Type mediation primitives.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | Yes               |
| Valid values   | BooleanNote:      |
| Default        | false             |

## Validate
validateInput

If true, causes the Set Message Type
mediation primitive to perform runtime validation. The validation includes all message fields and
not just those that you have overlaid.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | Yes               |
| Valid values   | BooleanNote:      |
| Default        | false             |

## Considerations

- At run time, the Set Message Type mediation primitive does not
affect the real structure or content of a message. The Set Message
Type mediation primitive makes it easier for you to manipulate messages.
- The Validate property is the only promotable
property of the Set Message Type mediation primitive. Because the Validate property
is promotable the runtime administrator can turn validation on and
off.

## Sample XML code

```
<node name="SetMessageType" type="SetMessageType">
  <table name="typeMap">
    <row>
      <property name="path" value="/body"/>
      <property name="assertedType" value="{http://TestMod/myInterface}myRequestMsg"/>
    </row>
  </table>
  <inputTerminal/>
  <outputTerminal type="myInterface:myRequestMsg">
    <refinement path="/body" type="myInterface:myRequestMsg"/>
    <wire targetNode="BOMapper1"/>
  </outputTerminal>
  <failTerminal/>
</node>
```