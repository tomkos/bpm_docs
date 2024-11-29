# Custom mediation primitive properties

## javaCode

Specify the Java code that will be run by the Custom
mediation. This is the same information that is specified within the details section of the Custom
mediation primitive panel. Either this property or the javaClass property must be
specified.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | No                |
| Valid values   | StringNote:       |

## Operation operation

This property is deprecated.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | No                |
| Valid values   | StringNote:       |

## Reference serviceReferenceName

This property is deprecated.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | No                |
| Valid values   | StringNote:       |

## javaClass

Specify the Java class that will be run by the Custom
mediation. Either this property or the javaCode property must be
specified.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | No                |
| Valid values   | StringNote:       |

## version

Set the version as 6.1.0.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | No                |
| Valid values   | StringNote:       |

## User Properties userProperties

You can define User Properties for
your Custom Mediation. A user property must have a name, type and value. After you have created a
user property you can promote it, so that the runtime administrator can change the value.

| Field detail                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Value and notes   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| Name name The name of your property. The valid type is String. Type type The data type of your property. The valid types are: String, Boolean, Integer, Float, and XPath. Value value The value of your property. Whether a value is valid, depends on the data type you assign to the user property. Required required If a property is marked as Required, the runtime environment checks to see if the property is set. The valid type is Boolean, with a value of true or false. The default is false. |                   |

## javaImports

Specify a semi-colon delimited list of Java complete
class names that need to be imported for running the code specified for the
javaCode property; for example:

javaImports="java.utils.List;java.utils.ArrayList".

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | No                |
| Valid values   | StringNote:       |

## Considerations

If you copy and paste a Custom Mediation primitive, the terminals,
properties and implementation are cloned.

## Sample XML code

```
<node name="CustomMediation1" type="CustomMediation">
  <property name="javaCode" value="out.fire(smo); // propagate the service message 
  object to the primitive that is wired to the 'out' terminal"/>
  <property name="javaClass" value="sca.component.mediation.java.Custom1290618010468"/>
  <property name="version" value="6.1.0"/>
  <table name="userProperties">
    <row>
      <property name="name" value="name1"/>
      <property name="type" value="String"/>
      <property name="value" value="value1"/>
        <property name="required" value="false"/>
    </row>
  </table>
  <property name="javaImports" value="java.util.ArrayList"/>
  <inputTerminal/>
  <outputTerminal>
    <wire targetNode="BOMapper1"/>
  </outputTerminal>
  <failTerminal/>
</node>
```