# Data Handler mediation primitive properties

## Data
handler configuration dataHandlerConfig

Specify the Data handler
configuration which the primitive should use, as created by the binding resource
configuration wizard. The Data handler configuration will be used at run time to
select the correct data handler to be invoked and pass in any associated parameter
values.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | Yes               |
| Valid values   | StringNote:       |

## Output message
field refinements typeMap

You can use the Output Message field
refinements property to specify which fields in the message are refined using more specific
type information. By default, this property is empty.

| Field detail                                                                                                                                                                     | Value and notes   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| Weakly typed field path Specify the XPath of the weakly-typed field you want to refine. Actual field type assertedType Specify the data type you want to use for the refinement. |                   |

## Action action

Convert from native data format to a business object
calls the transform method of the data handler to deserialize the data. Convert from a business
object to native data format calls the transformInto method of the data handler to serialize the
data.

| Field detail   | Value and notes                                                                                                        |
|----------------|------------------------------------------------------------------------------------------------------------------------|
| Required       | Yes                                                                                                                    |
| Valid values   | Convert from native data format to a business object 0  Convert from a business object to native data format 1   Note: |
| Default        | Convert from native data format to a business object                                                                   |

## Source
XPath sourceXPath

The location of the object, in the source SMO,
that should be passed into the data handler, for example,
/body/operation1/input1/value.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | Yes               |
| Valid values   | XPathNote:        |

## Target
XPath targetXPath

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | Yes               |
| Valid values   | XPathNote:        |

## Sample XML code

```
<node name="DataHandler1" type="DataHandler">
  <property name="dataHandlerConfig" value="{http://www.ibm.com/xmlns/prod/
  websphere/j2ca/configuration/6.1.0}UTF8XMLDataHandler"/>
  <property name="sourceXPath" value="/body/myRequestMsg/native"/>
  <property name="targetXPath" value="/body/myRequestMsg/inflated"/>
  <inputTerminal/>
  <outputTerminal/>
  <failTerminal/>
</node>
```