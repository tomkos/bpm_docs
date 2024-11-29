# HTTP Header Setter mediation primitive properties

## HTTP Header Elements headerElements

HTTP Header elements on an SMO
node.

- If you want to create a new HTTP header, the Mode property must be set to 'Create'.
- If you want to search for a HTTP header and then modify the value of any header that is found,
or create a new header if none are found, the Mode property must be set to 'Modify'.
- If you want to search for a HTTP header and then copy the first found header to another location
in the SMO, the Mode property must be set to 'Copy'.
- If you want to search for a HTTP header and then delete any headers that are found, the Mode
property must be set to 'Delete'.

If the Mode
property is set to 'Copy', the Value property should be an XPath 1.0 expression, identifying the
target element to where the first found HTTP header will be copied.

If the Mode property is
set to 'Delete', the Value property should not be set.

## Validate input validateInput

If true, causes the input message to be
validated before the mediation is performed.

## Considerations

- If the Mode property is "Modify" and a header cannot be found,
a new header will be created.
- If the XPath expression of the copy target resolves to more than
one element in the SMO, a runtime exception occurs.
- The location of the header within the SMO depends upon its type;
control, spec or user.
- If the Validate input property is true and the input message is
invalid, a runtime exception occurs.

## Sample XML code

```
<node displayName="addHeader" name="addHeader2" type="HTTPHeaderSetter">
  <table name="headerElements">
    <row>
      <property name="mode" value="Create"/>
      <property name="headerName" value="Method"/>
      <property name="valueIsXPath" value="false"/>
      <property name="value" value="POST"/>
    </row>
  </table>
  <inputTerminal/>
  <outputTerminal>
    <wire targetNode="nextNode"/>
  </outputTerminal>
  <failTerminal/>
</node>
```