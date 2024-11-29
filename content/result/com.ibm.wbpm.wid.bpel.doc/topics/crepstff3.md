<!-- image -->

# Replacement variables in people assignment criteria and task
descriptions

- Using percent signs within variable names is not allowed.
- If you want to use a percent sign in a string within the replacement
variable, then you will need to use two percent signs ("%%") instead
of one.
- Variables can contain XPath expressions. If an XPath expression
contains a "%" sign, it must be escaped as specified by XML (using &#37;).

Replacement variables for people assignment criteria and descriptions
in human tasks can contain the contents of variables and messages.
In addition resolved people assignment criteria of sibling inline
tasks can be used from other inline tasks.

Available expressions differ depending on whether it is a stand-alone,
or an inline human task.

## Stand-alone human tasks

The following table
lists all expressions that are available for human tasks that are
not embedded inline in a process, or stand-alone. When
these expressions are used inside descriptions as well as people assignment
criteria, they must be enclosed in '%' characters.

| Type of variable     | Expression                                            | Description                                                                                                                                                                                                                                                                                           |
|----------------------|-------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Staff Variables      | htm:task.originator                                   | the user ID of the originator of this task instance                                                                                                                                                                                                                                                   |
|                      | htm:task.owner                                        | the user ID of the owner of this task instance                                                                                                                                                                                                                                                        |
|                      | htm:task.starter                                      | task starter name                                                                                                                                                                                                                                                                                     |
|                      | htm:task.administrators                               | list of task administrators                                                                                                                                                                                                                                                                           |
|                      | htm:task.potentialOwners                              | list of potential task owners                                                                                                                                                                                                                                                                         |
|                      | htm:task.editors                                      | list of task editors                                                                                                                                                                                                                                                                                  |
|                      | htm:task.readers                                      | list of task readers                                                                                                                                                                                                                                                                                  |
|                      | htm:task.potentialStarters                            | list of potential task starters                                                                                                                                                                                                                                                                       |
|                      | htm:task.potentialInstanceCreators                    | list of potential creators                                                                                                                                                                                                                                                                            |
|                      |                                                       |                                                                                                                                                                                                                                                                                                       |
| Task variables       | htm:task.property.customPropertyName                  | value of the task's custom propertiesNote that only the string value of properties can be evaluated. For binary custom properties, the query string will be evaluated.                                                                                                                                |
|                      | htm:task.displayName                                  | default task display name                                                                                                                                                                                                                                                                             |
|                      | htm:task.description                                  | default task description                                                                                                                                                                                                                                                                              |
|                      | htm:task.instanceID                                   | task instance ID                                                                                                                                                                                                                                                                                      |
|                      | htm:input.[part][\XPath](or htm:input.part[\XPath])   | data from task's input message is provided using XPath expressions(Workflow Server messages usually have a single part, in which case the part name does not have to be specified. When using messages with multiple parts then the syntax in parenthesis has to be used. Also see the notes below.)  |
|                      | htm:output.[part][\XPath](or htm:output.part[\XPath]) | data from task's output message is provided using XPath expressions(Workflow Server messages usually have a single part, in which case the part name does not have to be specified. When using messages with multiple parts then the syntax in parenthesis has to be used. Also see the notes below.) |
|                      | Note that task instances have no default message.     |                                                                                                                                                                                                                                                                                                       |
|                      |                                                       |                                                                                                                                                                                                                                                                                                       |
| Escalation variables | htm:escalation.description                            | default escalation description                                                                                                                                                                                                                                                                        |
|                      | htm:escalation.expectedTaskState                      | escalation's expected task state                                                                                                                                                                                                                                                                      |
|                      | htm:escalation.instanceID                             | a string representation of the escalation instance ID                                                                                                                                                                                                                                                 |
|                      | htm:escalation(escalationName).receivers              | escalation receivers                                                                                                                                                                                                                                                                                  |
|                      | htm:escalation.property.customPropertyName            | value of escalation's custom propertiesNote that only the string value of properties can be evaluated. For binary custom properties, the query string will be evaluated.                                                                                                                              |

You can use either %htm.input.\XPath% or %htm.output.\XPath% to
refer to input or output parameters of the operation defined for a
task interface.

```
<?xml version="1.0" encoding="UTF-8"?>
<wsdl:definitions xmlns:tns="http://variables/variablesInterface" xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="variablesInterface" targetNamespace="http://variables/variablesInterface">
  <wsdl:types>
    <xsd:schema targetNamespace="http://variables/variablesInterface" xmlns:tns="http://variables/variablesInterface" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
      <xsd:element name="operation1">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="input1" nillable="true" type="xsd:string"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="operation1Response">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="output1" nillable="true" type="xsd:string"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
    </xsd:schema>
  </wsdl:types>
  <wsdl:message name="operation1RequestMsg">
    <wsdl:part element="tns:operation1" name="operation1Parameters"/>
  </wsdl:message>
  <wsdl:message name="operation1ResponseMsg">
    <wsdl:part element="tns:operation1Response" name="operation1Result"/>
  </wsdl:message>
  <wsdl:portType name="variablesInterface">
    <wsdl:operation name="operation1">
      <wsdl:input message="tns:operation1RequestMsg" name="operation1Request"/>
      <wsdl:output message="tns:operation1ResponseMsg" name="operation1Response"/>
    </wsdl:operation>
  </wsdl:portType>
</wsdl:definitions>
```

In addition, expressions like %htm:input.part[\XPath]%,
and %htm:input.part[\XPath]% can be used to refer
to input and output parameters associated with the different WSDL
message parts defined for a task operation. Currently, only single-part
messages are generated, so it can only be used on expressions that
exclude message part names.

For example, the expressions %htm:input.operation1Parameters\input1%,
%htm:output.operation1Result\output1% are valid and equivalent
to %htm:input.\input1%, %htm:output.\output1% .

It
is expected that XPATH will point to objects of type String, or String
List. In general, and object will be replaced by what the toString()
method returns.

## Inline human tasks

In addition to the expressions
in the previous table, a human task that is embedded inline in a process
can also use the expressions listed in the following table for staff
resolution. Note, that the description of an inline human task is
resolved by the Business Flow Manager (BFM) and must therefore be
modeled to use the syntax described in the previous section.

| Type of variable       | Expression                                | Description                                                                           |
|------------------------|-------------------------------------------|---------------------------------------------------------------------------------------|
| Process variables      | wf:variable.VariableName\[part][\XPath]   | 'VariableName\[part][\XPath]' is passed to BFM to resolve the variable/expression.    |
|                        | wf:property.customPropertyName            | The 'customPropertyName' is passed to the BFM to resolve the custom property.         |
|                        |                                           |                                                                                       |
| Inline staff variables | wf:process.starter                        | The starter of the process.                                                           |
|                        | wf:process.administrators                 | The administrators of the process.                                                    |
|                        | wf:process.readers                        | The readers of the process.                                                           |
|                        | wf:activity(activityName).potentialOwners | The potential owners of either the current activity or the activity named in brackets |
|                        | wf:activity(activityName).owner           | The owner of the activity named in brackets                                           |
|                        | wf:activity(activityName).editors         | The editors of either the current activity or the activity named in brackets          |
|                        | wf:activity(activityName).readers         | The readers of either the current activity or the activity named in brackets          |

Note that inline staff variables which refer to sibling
activities can only be resolved if the referred activity is also an
inline human task and is already started at the point in time when
the staff resolution happens.

As with stand-alone tasks, it
is expected that XPATH will point to objects of type String, or String
List. In general, and object will be replaced by what the toString()
method returns.

## Related concepts

- Replacement variables in process and activity descriptions
- Replacement variables in staff emails
- Replacement variables for escalation duration expressions