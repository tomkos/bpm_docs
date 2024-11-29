# Business Object Map mediation primitive properties

## Root root

An XPath 1.0 expression that specifies the root of the
transformation. This property is used for both the input message and the transformed
message.

| Field detail   | Value and notes                                                                                                                                                                                                                 |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Required       | Yes                                                                                                                                                                                                                             |
| Valid values   | XPathNote: You can specify: /, /headers, /context or /body. / refers to the complete SMO, /headers refers to the headers of the SMO, /context refers to the context of the SMO and /body refers to the body section of the SMO. |

## Mapping File mappingFile

Specifies the name of the business object map that
the mediation primitive uses. The business object map is used to transform data between the input
and output business objects.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | Yes               |
| Valid values   | StringNote:       |

## containsRelationships

Specifies whether the Business Object Map
mediation primitive uses a Business Object map that uses the relationship capability.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | Yes               |
| Valid values   | BooleanNote:      |
| Default        | false             |

## Considerations

- If the Mapping File property is not valid it
causes an exception at run time.
- The order of transformations can be important.
- The business object map associated with the Business Object Map
mediation primitive can be stored in the mediation module, or in a
library project that you declare as a dependency of the mediation
module.
- If you use dynamic relationships in the Business Object Map mediation
primitive across request and response flows, the display name of the
primitive in the response flow must match the corresponding primitive
name in the request flow.

## Sample XML code

```
<node name="BOMapper1" type="BOMapper>
  <property name="root" value="/"/>
  <property name="mappingFile" value="myBOMap.map"/>
  <inputTerminal type="myInterface:myRequestMsg"/>
  <outputTerminal type="myInterface:myRequestMsg"/>
  <failTerminal/>
</node>
```