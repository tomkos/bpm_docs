# Monitoring events

Monitoring events are emitted by process executions in support of monitoring and should not be
confused with process events, which are one-way messages that are part of the behavior of a
process.

## Parts of a monitoring event

The following table describes the significant parts of a monitoring event. Refer to the XML
schema for the detailed event format.

Event parts are referenced using standard XPath notation. When elements are nested, this is
indicated by a slash (/) separating the element part names. The @ symbol indicates that the part is
an attribute of the element. The table also indicates if an event part is optional or required.

A copy of the XML schema is provided for reference in Event schema extensions.

| Event part                                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Optional or required   | Type      |
|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|-----------|
| mon:monitorEvent                                                            | The root element of an event.There is one root element per event.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Required               | complex   |
| <mon:model mon:name="<name>">                                               | Identifies the instance of the script task that emitted the event.Note: This element is not part of the schema definition.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Required               | xs:string |
| mon:monitorEvent/@mon:id                                                    | The unique identifier of an event.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Optional               | xs:string |
| mon:monitorEvent/mon:eventPointData                                         | Describes the nature, the time, and the source of the occurrence reported by the event. There is one mon:eventPointData element per event.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Required               | complex   |
| mon:monitorEvent/    mon:eventPointData/mon:kind                            | Defines the kind of the event (for example, bpmnx:PROCESS\_STARTED). There is one mon:kind element per event.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Required               | xs:Qname  |
| mon:monitorEvent/    mon:eventPointData/mon:model                           | Describes an executable model element defining the event emission point (for example, a human task such as Review Claim). There is at least one mon:model element per event, but there can be multiple mon:model elements when the event emission point is part of a model-defined hierarchy (for example, a human task, which is defined within a process that is part of a process application).                                                                                                                                                                                                                                                                                                                                                                                       | Required               | complex   |
| mon:monitorEvent/    mon:eventPointData/mon:model/@mon:type                 | Specifies the type of the process model element from which the event originated. The value of the mon:type attribute refers to elements defined in the BPMN 2.0 schema (for example, bpmn:process or bpmn:userTask).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Required               | xs:QName  |
| mon:monitorEvent/    mon:eventPointData/    mon:model/mon:instance          | References or describes the instance of the executable model element that emitted the event (for example, a specific execution of a task). The instance is typically running in an execution environment such as a process engine, but is referenced by the mon:instance element. There is at most one mon:instance element per mon:model element. In some cases, a mon:model element can occur without a mon:instance element (for example, when a top-level mon:model element refers to a grouping construct, such as a process application or solution, which does not have runtime instances).                                                                                                                                                                                       | Required               | complex   |
| mon:monitorEvent/    mon:eventPointData/mon:correlation/mon:ancestor        | Contains a hierarchy of correlation identifiers, which can be auto-generated and created by the process engine or which can be user-defined. For events that originate from IBM Business Automation Workflow, the <mon:ancestor> tree is populated by the process engine. The <mon:ancestor> elements contain instance identifiers that identify the following items:  The process step emitting the event (for example, a human task) The process execution (for example, a claims process) Any callers   Additional correlation identifiers, such as customer order numbers, or claim identifiers, can be added in the mon:correlation section following the <mon:ancestor> tree. The additional identifiers can be used to facilitate correlation across multiple business processes. | Optional               | complex   |
| mon:monitorEvent/    mon:eventPointData/mon:source                          | Describes the source location where the event originated (or example, a specific server).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Optional               | complex   |
| mon:monitorEvent/    mon:eventPointData/    mon:source/mon:server           | Identifies the server on which the event emitter is running.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Optional               | complex   |
| mon:monitorEvent/    mon:eventPointData/    mon:source/mon:server/@mon:type | Indicates the syntax of the server identification (for example, a URL or an IP address). If a mon:server element is present, a mon:type attribute must be specified to qualify the server identification.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Required               | xs:QName  |
| mon:monitorEvent/mon:applicationData                                        | Contains well-formed XML that is reported by the event-emitting application. This element contains the custom business data in the event, such as tracked field data, tracking point information, or KPI data. Some events do not include the applicationData element. For more information about the structure of the applicationData, see Event schema extensions and the example applicationData provided at the end of this topic.                                                                                                                                                                                                                                                                                                                                                   | Optional               | complex   |

The monitoring event part names begin with the mon namespace prefix, which is
bound to the namespace http://www.ibm.com/xmlns/prod/websphere/monitoring/7.5.

The namespace prefix xs, used to designate XML schema types, is bound to
http://www.w3.org/2001/XMLSchema.

```
<mon:correlation>
    <mon:ancestor mon:id="3e888eb2-9c18-4cd5-a9de-3991aeb4f40e.2064.33692aa7-cb0e-4f0a-ac90-b85a5a5687ffT.161.6">
<mon:ancestor mon:id="3e888eb2-9c18-4cd5-a9de-3991aeb4f40e.2064.33692aa7-cb0e-4f0a-ac90-b85a5a5687ffT.161">
        </mon:ancestor>
            
    </mon:ancestor>
    <wle:starting-process-instance>3e888eb2-9c18-4cd5-a9de-3991aeb4f40e.2064.33692aa7-cb0e-4f0a-ac90-b85a5a5687ffT.161
<mon:correlation>
```

In the following monitoring event example, namespace prefixes are bound by the
xmlns attributes in the root element.

## Monitoring event example

```
<mon:monitorEvent xmlns:mon="http://www.ibm.com/xmlns/prod/websphere/monitoring/7.5" 
   mon:id="C1299df7f13ced21792162189" 
   xmlns:bpmn="http://schema.omg.org/spec/BPMN/2.0" 
   xmlns:bpmnx="http://www.ibm.com/xmlns/bpmnx/20100524/BusinessMonitoring" 
   xmlns:ibm="http://www.ibm.com/xmlns/prod/websphere/monitoring/7.5/extensions" 
   xmlns:wle="http://www.ibm.com/xmlns/prod/websphere/lombardi/7.5" 
   xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <mon:eventPointData>
    <mon:kind mon:version="2010-11-11">bpmnx:PROCESS\_STARTED</mon:kind>
    <mon:time mon:of="occurrence">2011-02-03T10:44:13.829-05:00</mon:time>
    <ibm:sequenceId>2</ibm:sequenceId>
    <mon:model mon:type="bpmn:process" mon:id="854325da-04ea-4ea6-8664-c701b4bf3d61" 
    mon:version="2064.9d926c59-6511-4ee9-a0d2-4015fb19cb55">
      <mon:name>Ping</mon:name>
      <mon:documentation>The "Ping" process definition.</mon:documentation>
      <mon:instance mon:id="754">
        <mon:state>Active</mon:state>
      </mon:instance>
    </mon:model>
    <mon:model mon:type="wle:processApplication" mon:id="b9e85db9-5c4d-40e7-9421-e53acb738f4e" 
    mon:version="2064.9d926c59-6511-4ee9-a0d2-4015fb19cb55">
      <mon:name>Oscillating Invocations</mon:name>
      <mon:documentation>Ping pong between two processes.</mon:documentation>
    </mon:model>
    <mon:correlation>
      <mon:ancestor mon:id="854325da-04ea-4ea6-8664-c701b4bf3d61.2064.9d926c59-6511-4ee9-a0d2-4015fb19cb55.754"/>
      <wle:starting-process-instance>854325da-04ea-4ea6-8664-c701b4bf3d61.2064.9d926c59-6511-4ee9-a0d2-4015fb19cb55.754
      </wle:starting-process-instance>
    </mon:correlation>
  </mon:eventPointData>
</mon:monitorEvent>
```

## applicationData element example

```
<mon:applicationData>
    <wle:tracking-point wle:time="2011-02-03T10:44:16.054-05:00" wle:name="Call Ping ? (PRE)" 
     wle:id="8bfe448-7ceebpdid571234bad276b9a1-4cb5676012c08bfe448-7cd0 (PRE)" 
     wle:version="2064.9d926c59-6511-4ee9-a0d2-4015fb19cb55" 
     wle:groupName="at12886649788291288665594539" 
     wle:groupId="guid:571234bad276b9a1:-4cb56760:12c08bfe448:-7cee" 
     wle:groupVersion="2064.9d926c59-6511-4ee9-a0d2-4015fb19cb55">
      <wle:tracked-field wle:name="levelEnteringPong" 
        wle:id="bpdid:571234bad276b9a1:-1448ee2a:12c08c263e4:-7fbc" 
        wle:type="xs:integer">1</wle:tracked-field>
      <wle:tracked-field wle:name="reportOfWhereInPong" 
        wle:id="bpdid:571234bad276b9a1:-1448ee2a:12c08c263e4:-7fba" 
        wle:type="xs:string">This is Pong. Called with level = 1.</wle:tracked-field>
      <wle:tracked-field wle:name="argumentForPing" 
        wle:id="bpdid:571234bad276b9a1:-1448ee2a:12c08c263e4:-7fb8" 
        wle:type="xs:integer"/>
      <wle:kpi-data wle:name="Labor Cost" 
         wle:id="fbec4968-5e4c-4f2b-b11b-f3c9ef63d09b" 
         wle:version="2064.8d7ade38-7307-4894-a633-9903b7fc69d6" 
         wle:type="xs:decimal">0</wle:kpi-data>
      <wle:kpi-data wle:name="Total Time (Clock)" 
         wle:id="67cbb213-0032-4f14-be44-7e9c7a1a146f" 
         wle:version="2064.8d7ade38-7307-4894-a633-9903b7fc69d6" 
         wle:type="xs:dayTimeDuration">P0DT0H0M0S</wle:kpi-data>
      <wle:kpi-data wle:name="Wait Time (Clock)" 
         wle:id="43b503bd-63e7-4c42-8268-92d1033e0997" 
         wle:version="2064.8d7ade38-7307-4894-a633-9903b7fc69d6" 
         wle:type="xs:dayTimeDuration">P0DT0H0M0S</wle:kpi-data>
      <wle:kpi-data wle:name="Resource Cost" 
         wle:id="d5da2c80-b2af-40a6-981d-9de4df12ed12" 
         wle:version="2064.8d7ade38-7307-4894-a633-9903b7fc69d6" 
         wle:type="xs:decimal">0</wle:kpi-data>
      <wle:kpi-data wle:name="Value Add" 
         wle:id="e30cf309-a884-4a7b-a2db-16e8a371a4c1" 
         wle:version="2064.8d7ade38-7307-4894-a633-9903b7fc69d6" 
         wle:type="xs:decimal">1</wle:kpi-data>
      <wle:kpi-data wle:name="Execution Time (Clock)" 
         wle:id="8601bb6b-9c9d-4cba-936e-16350a036de3" 
         wle:version="2064.8d7ade38-7307-4894-a633-9903b7fc69d6" 
         wle:type="xs:dayTimeDuration">P0DT0H0M0S</wle:kpi-data>
      <wle:kpi-data wle:name="Cost" 
         wle:id="995ba3fc-e786-45eb-b356-47acb3d3ebbc" 
         wle:version="2064.8d7ade38-7307-4894-a633-9903b7fc69d6" 
         wle:type="xs:decimal">0.00000000</wle:kpi-data>
      <wle:kpi-data wle:name="Rework" 
         wle:id="0f650e6c-a9d7-4355-90bd-06530fa3eeec" 
         wle:version="2064.8d7ade38-7307-4894-a633-9903b7fc69d6" 
         wle:type="xs:decimal">0</wle:kpi-data>
    </wle:tracking-point>
  </mon:applicationData>
```

## Consideration when monitoring events emitted by Business Automation Workflow processes

```
<?xml version="1.0" encoding="UTF-8" ?>
<properties>
    <common>
        <monitor-event-emission merge="replace">
          <enabled>true</enabled>
          <use-system-id-for-correlation>true</use-system-id-for-correlation>
        </monitor-event-emission>
    </common>
</properties>"
```

- Process components and monitoring events

IBM Business Automation Workflow emits monitoring events for tracking purposes. Monitoring events are separate from start, end and intermediate process components that are defined in a process model, and are part of the modeled process logic. Use monitoring events for tracking or to capture information when you want to report what a process execution is doing without interfering with the process.
- Process monitoring events

When the execution, or instance, of a process has started, completed or failed, or if the process instance has been terminated or deleted, the process state change is reported in a monitoring event.
- Service integration monitoring events

When a service flow has started, completed, or failed, the state change is reported in a monitoring event. Intermediate tracking events of a service flow are also reported as monitoring events.
- Exposed automation service events

When an exposed automation service (REST) is active, completed or failed, the state change is reported in a monitoring event.
- Activity monitoring events

When an execution, or instance, of an activity has entered a specific state such as ready, active, or completed, the activity state is reported in a monitoring event. In addition, you can configure process activities with simple and multi-instance loops.
- Event monitoring events

The monitoring events EVENT\_EXPECTED, EVENT\_CAUGHT and EVENT\_THROWN are used to monitor the execution behavior of the BPMN Start, End and Intermediate events.
- Gateway events

Gateways are process modeling elements that control how a process diverges or converges.
- Event schema extensions

The XML schema for monitoring events is included in this section for reference purposes. Also included are IBM-specific extensions to the XML schema that define how tracking fields and key performance indicators (KPI) data values are reported.
- Advanced events

IBM Business Automation Workflow advanced content includes service components, and each of these components has its own set of event points that can be monitored. This event catalog contains the specifications for all the events that can be monitored for each service component type, and the associated Common Base Event extended data elements produced by each event.