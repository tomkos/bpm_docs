# WebSphere eXtreme
Scale:
Store mediation primitive properties

## eXtreme Scale definition cacheName

The name of the eXtreme Scale definition used to store
data. The maximum length is 256 characters. If this definition is not set, the default eXtreme Scale definition as defined in
the AdminConfig of the server is used. This definition can be set in the runtime administrative
console or by using admin commands.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | Yes               |
| Valid values   | StringNote:       |

## Map Name mapName

The backing map where the cached data must be
stored.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | Yes               |
| Valid values   | StringNote:       |

## XPath of the key keyXPath

An XPath value that points to the key by which the
cached data is referenced.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | Yes               |
| Valid values   | StringXPathNote:  |

## XPath of data to store in the cache insertXPath

An XPath expression that points to the data to be
stored in the cache.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | Yes               |
| Valid values   | StringXPathNote:  |

## Time to live timeToLive

Use this field to specify the number of seconds for
which the data should be stored. The default value is -1, which indicates to
use the map default. A value of 0 indicates that the data will never
expire.

| Field detail   | Value and notes                                                                                                            |
|----------------|----------------------------------------------------------------------------------------------------------------------------|
| Required       | Yes                                                                                                                        |
| Valid values   | IntegerNote: When using the Time to live property the ttlEvictorType of the specified map must be set to LAST\_UPDATE\_TIME. |

## Considerations

## Sample XML code

```
<node name="WXSStore1" type="WXSStore">
          <property name="cacheName" value="MyDefinition"/>
          <property name="mapName" value="Map1"/>
          <property name="keyXPath" value="/body/getCustomerResponse/output1"/>
          <property name="insertXPath" value="/body/getCustomerResponse/output1"/>
          <property name="timeToLive" value="15"/>
          <inputTerminal/>
          <outputTerminal>
            <wire targetNode="GetCustomer\_getCustomer\_InputResponse"/>
          </outputTerminal>
          <failTerminal/>
        </node>
```