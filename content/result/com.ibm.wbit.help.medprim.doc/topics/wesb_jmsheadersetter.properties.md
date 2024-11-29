# JMS Header Setter mediation primitive properties

## JMS Header Elements headerElements

| Field detail                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Value and notes   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| Mode mode   If you want to create a new JMS header, the Mode property must be set to 'Create'. If you want to search for a JMS header and then modify the value of any header that is found, or create a new header if none are found, the Mode property must be set to 'Modify'. If you want to search for a JMS header and then copy the first found header to another location in the SMO, the Mode property must be set to 'Copy'. If you want to search for a JMS header and then delete any headers that are found, the Mode property must be set to 'Delete'.   Header Name headerName You can specify a JMS header field name; any JMS headers in the SMO that has a matching name can then be set, copied, or deleted. Type headerType Specify the JMS header type. This is only used for User Headers that are listed at /headers/properties and is a Java primitive type or String. Set Value using XPath valueIsXPath Determine whether the Value to set should be a literal value or an XPath expression that identifies a source value to copy into the JMS header at run time. This property is only used when the Mode property is set to 'Create' or 'Modify'. The valid type is Boolean: true or false (the default). Value value If the Mode property is set to 'Create' or 'Modify', the Value property should be set to a JMS header literal value or an XPath expression that identifies a value to copy into the JMS header at run time. When a new JMS header is created or a matching JMS header is found, this new value is set in the specified field.If the Mode property is set to 'Copy', the Value property should be an XPath 1.0 expression, identifying the target element to where the first found JMS header will be copied.  If the Mode property is set to 'Delete', the Value property should not be set. |                   |

## Validate input validateInput

If true, causes the input message to be
validated before the mediation is performed.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | Yes               |
| Valid values   | BooleanNote:      |
| Default        | false             |

## Considerations

- If the Mode property is "Modify" and a header cannot be found,
a new header will be created.
- If the XPath expression of the copy target resolves to more than
one element in the SMO, a runtime exception occurs.
- The location of the header within the SMO depends upon its type;
standard or user.
- If the Validate input property is true and the input message is
invalid, a runtime exception occurs.

## Sample XML code

```
<node displayName="addHeader" name="addHeader1" type="JMSHeaderSetter">
  <table name="headerElements">
    <row>
      <property name="mode" value="Create"/>
      <property name="headerName" value="JMSMessageID"/>
      <property name="headerType" value="String"/>
      <property name="valueIsXPath" value="false"/>
      <property name="value" value="1234567890"/>
    </row>
  </table>
  <inputTerminal/>
  <outputTerminal>
    <wire targetNode="nextNode"/>
  </outputTerminal>
  <failTerminal/>
</node>
```