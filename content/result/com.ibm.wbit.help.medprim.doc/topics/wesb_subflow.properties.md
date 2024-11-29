# Subflow mediation primitive properties

## Subflow file

The name of the file containing the subflow
implementation. For example, TestSubflow.subflow.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | No                |
| Valid values   | StringNote:       |

## Subflow name

The qualified name specified in the subflow
implementation of the format {namespace}localpart. For example,
{http://TestModule}TestSubflow

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | No                |
| Valid values   | StringNote:       |

## Subflow properties

These properties correspond to the properties promoted
from primitives within the subflow implementation.

| Field detail                                                                                                                                                                                       | Value and notes   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| Name name The name of the property, which corresponds to the alias name of the promoted property. Type type The type of the property. For example, STRING. Value value  The value of the property. |                   |

## Subflow references

This represents the mapping between a reference defined
on the subflow implementation and a reference defined on the parent flow.

| Field detail                                                                                                                                                                                                                     | Value and notes   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| Name name The name of the reference in the subflow implementation. Interface interface The interface of the reference. Value value The name of the reference in the parent flow to which the reference in the subflow is mapped. |                   |

## Considerations

- You cannot use a Policy Resolution primitive in a subflow.
- You cannot specify a context element within a subflow. Context
elements that are available in the parent flow are also available
to mediation primitives in the subflow.

## Sample XML code

```
<node name="mySubflow" type="Subflow" >
  <property name="subflowFile" value="mySubflow.subflow"/>
  <property name="subflowName" value="{http://TestMod}mySubflow"/>
  <inputTerminal description="The In node is the starting point for the subflow."/>
  <outputTerminal description="The Out node is the end point for the subflow.">
    <wire targetNode="Fail1"/>
  </outputTerminal>
  <failTerminal/>
</node>
```