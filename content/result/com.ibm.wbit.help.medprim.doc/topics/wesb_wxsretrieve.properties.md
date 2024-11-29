# WebSphere eXtreme
Scale:
Retrieve mediation primitive properties

## eXtreme Scale definition cacheName

The name of the eXtreme Scale definition used to
retrieve data. The maximum length is 256 characters. If this definition is not set, the default
eXtreme Scale definition as
defined in the AdminConfig of the server is used. This definition can be set in the runtime
administrative console or by using admin commands.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | Yes               |
| Valid values   | StringNote:       |

### Map Name mapName

The backing map where the cached data must be
stored.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | Yes               |
| Valid values   | StringNote:       |

### XPath of the key keyXPath

An XPath expression that refers to the key used to
retrieve information from the cache.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | Yes               |
| Valid values   | String XPathNote: |

### XPath of data to store the result
from the cache replaceXPath

An XPath expression that refers to the root
Object where the result is placed. The information obtained from the cache should be of the same
type specified by the XPath of the data to store the result from the cache property. If the data
type obtained from the cache is assigned to a string then a string representation of that
information will be used, where possible.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | Yes               |
| Valid values   | String XPathNote: |

## Considerations

## Sample XML code

```
<node name="WXSRetrieve1" type="WXSRetrieve">
          <property name="cacheName" value="MyDefinition"/>
          <property name="mapName" value="Map1"/>
          <property name="keyXPath" value="/body/getCustomer/input1"/>
          <property name="replaceXPath" value="/body/getCustomer/input1"/>
          <inputTerminal/>
          <outputTerminal>
            <wire targetNode="XSLTransformation1"/>
          </outputTerminal>
          <outputTerminal name="notFound">
            <wire targetNode="XSLTransformation2"/>
          </outputTerminal>
          <failTerminal/>
        </node>
```