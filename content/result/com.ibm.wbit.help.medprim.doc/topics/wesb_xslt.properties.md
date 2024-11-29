# Mapping mediation primitive properties

## Root root

An XPath 1.0 expression that specifies the root of the mapping.
This property is used for both the input message and the transformed message. When you create a new
XML map, you can specify the following message roots: /,
/headers, /context or /body.

| Field detail   | Value and notes                                                                                                                                                                |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Required       | Yes                                                                                                                                                                            |
| Valid values   | XPathNote: / refers to the complete SMO, /headers refers to the headers of the SMO, /context refers to the context of the SMO and /body refers to the body section of the SMO. |
| Default        | /                                                                                                                                                                              |

## XSLTransform

Specifies the XSLT stylesheet used during the
transformation. This is required when the Target engine property in the XML Map
is set to XSLT 1.0 or XSLT 2.0.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | No                |
| Valid values   | StringNote:       |

## Mapping file XMXMap

Specifies the name of the XML mapping file, or the XSL
stylesheet, that the mediation primitive uses. You can choose either an XML mapping file, with an
associated XSL stylesheet or Business Object Map, or an XSL stylesheet on its own.

You can browse existing XML mapping files or create a new mapping file. An XML mapping file has a
generated XSL stylesheet or Business Object Map that performs the transformation at run time.

You can browse existing XSL stylesheets, if they exist in the same project as the mediation
module.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | No                |
| Valid values   | StringNote:       |

## Validate input validateInput

If true, the input message is
validated at run time, before the mediation is performed.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | Yes               |
| Valid values   | BooleanNote:      |
| Default        | false             |

## SMOVersion

This value is always defined as
SMO61.

| Field detail   | Value and notes                  |
|----------------|----------------------------------|
| Required       | Yes                              |
| Valid values   | SMO61 SMO61  SMO60 SMO60   Note: |
| Default        | SMO60                            |

## Considerations

- If the Mapping file property is not valid, it
causes an exception at run time.
- If Validate input property is true,
the input message is validated against its schema, at run time. If
the input message does not match its schema, an exception occurs.

## Sample XML code

```
<node name="Mapping1" type="XSLTransformation">
  <property name="root" value="/"/>
  <property name="XSLTransform" value="xslt/Mapping1\_req\_1.xsl"/>
  <property name="XMXMap" value="xslt/Mapping1\_req\_1.map"/>
  <property name="SMOVersion" value="SMO61"/>
  <inputTerminal type="XMLSchema:anyType"/>
  <outputTerminal type="XMLSchema:anyType">
    <wire targetNode="TypeFilter1"/>
  </outputTerminal>
  <failTerminal/>
</node>
```