# Type Filter mediation primitive properties

## Enabled enabled

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | Yes               |
| Valid values   | BooleanNote:      |
| Default        | true              |

## Filters filters

A list of XPaths, types, and associated terminal names,
that define the filtering performed by the mediation primitive.

| Field detail                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Value and notes   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| Element xpath An XPath 1.0 expression against which the message is tested. The expression is evaluated starting from the XPath expression /, which refers to the complete SMO. Type type The qualified type to be matched. Terminal name terminalName The name of an output terminal. There is one terminal name for each pattern XPath type pair. The terminal name must be a valid connection endpoint, and it must not be fail or default. The default value is empty, which is invalid. |                   |

## Considerations

- If there is a syntax error in an XPath it can cause an exception
at run time.
- If the XPath resolves to more than one element the Type Filter
mediation primitive will not recognize a match.
- The Type Filter primitive matches on either the exact type of
an element or its derived types. For example, if you try to match
against xsd:int but the actual element is of type xsd:short,
it will still match.

## Sample XML code

```
<node name="TypeFilter1" type="TypeFilter">
  <table name="filters">
    <row>
      <property name="xpath" value="/body/myRequestMsg/person"/>
      <property name="type" value="boolean"/>
      <property name="terminalName" value="match1"/>
    </row>
  </table>
  <inputTerminal/>
  <outputTerminal name="default"/>
  <outputTerminal name="match1" type="XMLSchema:anyType">
    <refinement path="/body/myRequestMsg/person" type="boolean"/>
    <wire targetNode="MessageValidator1"/>
  </outputTerminal>
  <failTerminal/>
</node>
```