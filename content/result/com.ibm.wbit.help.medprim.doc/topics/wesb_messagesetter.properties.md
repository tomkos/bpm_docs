# Message Element Setter mediation primitive properties

## Message Elements messageElements

Elements of the message that you want to
add, change, or delete.

In IBM Integration
Designer, click
Add to specify a message element update. After you have defined an update, it
appears in the Message Elements table. You can change the order in which message element updates
occur, by moving the Message Elements up and down in the table.

- Using Set, you can set a target element to a constant value (specified in
the Value property).
- Using Copy, you can copy from a source element to a target element.
Note: You must ensure that the source data type is compatible with the target data type, or a
runtime exception occurs.
- Using Append, you can copy from a source element to a new element
instance, by appending to a repeating element in the output. You can only append to a repeating
element in the output. Note: You must ensure that the source data type is compatible with the target
data type, or a runtime exception occurs.
- Using Delete, you can delete an element instance from the SMO. Note: You
should only attempt to delete optional or repeating elements.

| Field detail                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Value and notes   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| Target target An XPath 1.0 expression that describes the location of the element to set, create or delete. You can specify: /, /headers, /context or /body. / refers to the complete SMO, /headers refers to the headers of the SMO, /context refers to the context of the SMO and /body refers to the body of the SMO.If you want to set a target element to a constant value, the target XPath expression must resolve to a single leaf element. If you want to copy from a source element to a target element, both the source and target must specify an XPath expression that resolves to a single message element (a single leaf or subtree). If you set multiple targets, the elements are set sequentially. Therefore, if you set element X from value 13 to value 14, and then set element Y to the value of element X, the mediation sets element X to value 14 and element Y to value 14. If you specify the same target element more than once, the last operation performed on the target element takes precedence.  Type type The type of the element value. If you want to set the Target to a constant value, the Type must be a simple XML schema type, or an XML schema type that extends a simple XML schema type.  If you want to set the Target to a value copied from somewhere in the input SMO, the Type must be the keyword copy. When you copy a value from somewhere in the input SMO, the target type is assumed to be the same as the source type. A copy operation always takes its source value from the unmodified input SMO (that is, the SMO instance received by the primitive on its in terminal). If the same target element is specified more than once in a particular primitive, the last operation performed on that target element wins. If you want to copy a value from the input SMO to a new element instance, appended to a repeating element in the output, the Type must be the keyword append. You can only append to a repeating element in the output, and the target type is assumed to be the same as the source type. If you want to delete an element instance, the Type must be the keyword delete. You can only delete optional or repeating elements.   Value value An XPath expression or a value compatible with the Type property. Only used with Set.If the Type property is set to copy or append, the Value property should be an XPath 1.0 expression, identifying the source element. (In IBM Integration Designer, the XPath 1.0 expression for the Value property is displayed in a field titled Source.) The copy and append operations always take their source value from the unmodified input SMO.  If the Type property is set to delete, the Value property should not be set.  If the Type property is not copy, append or delete, the Value and Type properties must be compatible. For example, if the Type is the XML schema type int, the Value could validly be 14, but not GoldAccount. |                   |

## Validate input validateInput

If true, causes the
input message to be validated before the mediation is performed.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | Yes               |
| Valid values   | BooleanNote:      |
| Default        | false             |

## Considerations

Consider the following when using the Message Element Setter mediation
primitive:

- If the XPath expression of the source resolves to more than one
element in the SMO, a runtime exception occurs.
- If you attempt to set a target element to a value of incompatible
type, a runtime exception occurs.
- If the Validate input property is true and
the input message is invalid, a runtime exception occurs.

## Sample XML code

```
<node name="MessageElementSetter1" type="MessageElementSetter">
  <table name="messageElements">
    <row>
      <property name="target" value="/body/myRequestMsg/person/message"/>
      <property name="type" value="{http://www.w3.org/2001/XMLSchema}string"/>
      <property name="value" value="HelloWorld"/>
    </row>
  </table>
  <inputTerminal/>
  <outputTerminal>
    <wire targetNode="DatabaseLookup1"/>
  </outputTerminal>
  <failTerminal/>
</node>
```