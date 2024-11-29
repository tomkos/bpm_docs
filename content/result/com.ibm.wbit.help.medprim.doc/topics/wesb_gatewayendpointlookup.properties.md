# Gateway Endpoint Lookup mediation primitive properties

## Lookup Method

| Field detail   | Value and notes                                                                                                                                                                                                                                                                                                                                                                                                                   |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Required       | Yes                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Valid values   | URL 0 Query the built-in configuration store, using the input URL as the virtual service name. A proxy gateway can use a Lookup Method of URL or XPath.  Action 1 Query WSRR, for all endpoints with the action value specified by the message.  XPath 2 Query the built-in configuration store, using a virtual service name located using an XPath expression. A proxy gateway can use a Lookup Method of URL or XPath.   Note: |
| Default        | URL                                                                                                                                                                                                                                                                                                                                                                                                                               |

## Proxy Group Names

## Lookup XPath

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | No                |
| Valid values   | XPathNote:        |

## Registry Name

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | No                |
| Valid values   | StringNote:       |

## Classification URIs

To
extract endpoint information about web services then, in WSRR, you
 must specify any classifications on the appropriate WSDL Port objects.

- Account
    - Identifier
    - Name
        - First name
        - Second name
- Address

- First line of address
- Second line of address

## User Properties

| Field detail                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Value and notes   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| Name name The name of the user-defined property. The valid type is String. Type type The type of the user-defined property. If the type is String, then what you specify as the Value is used as a literal, in the search query. If the type is XPath, then what you specify as theValue must be an XPath expression. The XPath expression must resolve to a unique leaf node in the inbound SMO. The value of the leaf node is used in the search query. Value value The value of the user-defined property. This can be either a literal value or an XPath expression, depending upon the Type property. |                   |

## Considerations

- If the Use dynamic endpoint if set in the message header property
is not set in the callout node, the runtime environment does not use
the dynamic endpoint in /headers/SMOHeader/Target/address.
In this case, the runtime environment uses the default endpoint if
there is one, or throws an error.
- If the Lookup XPath expression resolves
to more than one element in the SMO, a runtime exception occurs.
- All Classification or User Properties specified
for a Gateway Endpoint Lookup mediation primitive result in a query
that combines all of these properties using a logical AND.
- If you want to use Classification URIs
that include white space characters, the correct URI encoding should
be used. For example, a single character space should be represented
as %20.
- White space characters provided in any of the Gateway Endpoint
Lookup mediation primitive properties are treated as literal characters.
They are not removed by the Gateway Endpoint Lookup mediation primitive
when querying the registry. For example, if you specify a Classification property
and the expected results are not returned from a query, ensure there
is no white space before or after the Classification URI.

## Sample
XML code

```
<node name="GatewayEndpointLookup1" type="GatewayEndpointLookup" >
  <table name="proxyGroupNames">
    <row>
      <property name="name" value="myProxyGateway"/>
    </row>
  </table>
  <inputTerminal/>
  <outputTerminal>
    <wire targetNode="PolicyResolution"/>
  </outputTerminal>
  <outputTerminal name="noMatch"/>
  <failTerminal/>
</node>
```