# Event Emitter mediation primitive

## Introduction

You can use the Event Emitter
mediation primitive to send out events, during a mediation flow. Because
the events are generated to conform to the Common Base Event specification,
they have a standard XML-based format. The events are sent to a Common
Event Infrastructure (CEI) server. For information on CEI resources
and services refer to the runtime product documentation and runtime
online help.

You can decide whether generated events contain
the message being processed, or not.

- If you set the Root property, you can generate
events that contain all or part of the message being processed. The Root property
is an XPath expression that specifies the section of the Service Message
Object (SMO) that is included in the event. The Root property
can specify the complete SMO, a subtree or a leaf element. Note: At
run time, if the Root value does not match any of
the elements in the SMO, the message being processed is not included
in the generated event.
- If you do not set the Root property, any generated
events do not contain the message being processed.

The Event Emitter mediation primitive has one input terminal
(in), one output terminal (out)
and a fail terminal (fail). The in terminal
is wired to accept a message and the other terminals are wired to
propagate a message. The out terminal propagates
the original message. If an exception occurs during the processing
of the input message, the fail terminal propagates
the original message, together with any exception information contained
in the failInfo element.

## Details

If a generated event contains the
message being processed, the event format can be version 6.1 or later.
By default, Event Emitter mediation primitives emit events in version
6.1 format, when running on a version 6.1 system.

The version
6.1 format, stores the message as an XML element in the xsd:any slot
of an event. Because the message is stored in an xsd:any slot,
you can retrieve it as an XML instance and use existing XML technologies
to process it in an efficient way.

## 6.1 format

| Element   | Sub-elements    | Sub-elements      | Sub-elements      | Description                            |
|-----------|-----------------|-------------------|-------------------|----------------------------------------|
| event     | eventPointData  | ModuleName        | ModuleName        | The name of the module instance        |
| event     | eventPointData  | MediationName     | MediationName     | The name of the Event Emitter instance |
| event     | eventPointData  | EventEmitterLabel | EventEmitterLabel | The Label property value               |
| event     | eventPointData  | Root              | Root              | The Root property value                |
| event     | applicationData | content           | value             | Application data                       |

- If a generated event does not contain the message being processed,
the applicationData child element of the event element
is absent.
- If the Root property of the Event Emitter primitive
specifies a single leaf element, the applicationData element
contains the value of the leaf element. At run time this would generate
the following event element: event/applicationData/content/value.
- If the Root property of the Event Emitter primitive
specifies a business object, the applicationData element
stores the specified business object. For example, if the business
object contained an accountID and creditLimit,
at run time this would generate event elements: event/applicationData/content/value/accountID and event/applicationData/content/value/creditLimit.

## Usage

The Event Emitter mediation primitive
enhances your monitoring capability by allowing you to send business
events from a mediation flow component. You can then view the Event
Emitter events using the event browser, on the application server,
or other event consumer applications.

Use the Event Emitter
mediation primitive to indicate an unusual event. For example, notification
of a failure in the flow or an unusual path in the flow. When you
place event emitters in a flow you should consider the possible number
of events that can be generated, and the size of the message that
will be stored in the event. Placing an event emitter in the normal
flow path generates many events compared to placing it in an unusual
event or failure path. In addition, consider configuring the emitter
to store only significant message data, rather than the complete message,
to reduce the overall size of the event.

You can use the Event
Emitter mediation primitive to record a failure in another mediation
primitive, and then continue processing. To do this you wire the fail
terminal of the previous mediation primitive to the input terminal
of the Event Emitter mediation primitive; and wire the output terminal
of the Event Emitter mediation primitive to the next step in the flow.

You
can also use the Event Emitter mediation primitive, in combination
with the Message Filter mediation primitive, to generate business
events based on message content. To do this you wire one of the output
terminals of the Message Filter mediation primitive to the input terminal
of the Event Emitter mediation primitive; and wire the output terminal
of the Event Emitter mediation primitive to the next step in the flow.

## Detailed event contents

The
events emitted by the Event Emitter mediation primitive conform to
the Common Base Event specification 1.0.1 structure. The event specification
is part of the IBM® Autonomic
Computing Toolkit.

The following elements are common to all
Event Emitter events:

```
<esb:ModuleName>Test2</esb:ModuleName>
```

```
<esb:MediationName>EventEmitter1</esb:MediationName>
```

```
<esb:EventEmitterLabel>Test2\_EventEmitter1\_Req</esb:EventEmitterLabel>
```

```
<esb:Root>/body/operation1/input1/field1</esb:Root>
```

```
<wbi:content wbi:name="Message">
	 <wbi:value xsi:type="xsd:string">hello</wbi:value>
</wbi:content>
```

```
<xsd:complexType name="MyBO">
        <xsd:sequence>
                <xsd:element name="value1" type="xsd:string"/>
                <xsd:element name="value2" type="bons0:MySubBO"/>
        </xsd:sequence>
</xsd:complexType>

<xsd:complexType name="MySubBO">
        <xsd:sequence>
                <xsd:element name="value1" type="xsd:string"/>
                <xsd:element name="value2" type="xsd:int"/>
        </xsd:sequence>
</xsd:complexType>
```

```
<wbi:content wbi:name="Message" wbi:businessObjectName="MyBO" 
	wbi:targetNamespace="http://Test" >
        <wbi:value xsi:type="p:MyBO" >
                <value1>hello</value1>
                <value2>
                        <value1>world</value1>
                        <value2>1234</value2>
                </value2>
        </wbi:value>
</wbi:content>
```

- Event Emitter mediation primitive properties

You can specify values for mediation primitive properties either by using the property fields in the IBM Integration Designer user interface or by using an XML format. The property field names displayed in IBM Integration Designer are generally different from the property names used when building a mediation flow using XML code. In the following information, icons are used to identify each property name used in IBM Integration Designer and the corresponding XML name. (Where applicable, XML names that are required, but not shown in IBM Integration Designer, are also described.)