# Activity monitoring events

## Monitoring activity lifecycle events

The ACTIVITY\_READY, ACTIVITY\_ACTIVE, ACTIVITY\_TERMINATED, and ACTIVITY\_COMPLETED event types
report the lifecycle states of an activity. Some of these events contain custom business data and
default key performance indicators (KPI) data. The following table describes the event types that
are emitted for activities.

| Event type                        | Event description                                                                                                                                                                                                                                                                                                          | Required elements                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| bpmnx:ACTIVITY\_READY              | An instance of an activity is in the ready state. An activity enters the ready state when a token has arrived.This event includes custom business data (KPIs and auto-tracked fields) in the applicationData element.                                                                                                      | The <mon:model mon:type="activity\_type"> element describes the activity that emitted the event.  The <mon:type> attribute indicates the type of the activity, as defined in the BPMN 2.0 schema. For example, <mon:model mon:type="bpmn:callActivity">, or <mon:model type="bpmn:userTask">. The <mon:model> element describing the activity must be followed by a <mon:model> element describing the process defining the activity and the process instance from which the event was sent. It is followed by <mon:model> elements for higher-level constructs, such as process applications. The ACTIVITY\_ACTIVE event also contains the name of the user performing the activity as part of the <mon:role> element: <mon:role mon:id="PERFORMER">  <mon:resource mon:id="1:User assigned to the DeAdmin role" >  <mon:name>User assigned to the DeAdmin role</mon:name>  </mon:resource>  </mon:role> |
| bpmnx:ACTIVITY\_ACTIVE             | An instance of an activity is in the active state; required input and resources are available, and work has started.                                                                                                                                                                                                       | The <mon:model mon:type="activity\_type"> element describes the activity that emitted the event.  The <mon:type> attribute indicates the type of the activity, as defined in the BPMN 2.0 schema. For example, <mon:model mon:type="bpmn:callActivity">, or <mon:model type="bpmn:userTask">. The <mon:model> element describing the activity must be followed by a <mon:model> element describing the process defining the activity and the process instance from which the event was sent. It is followed by <mon:model> elements for higher-level constructs, such as process applications. The ACTIVITY\_ACTIVE event also contains the name of the user performing the activity as part of the <mon:role> element: <mon:role mon:id="PERFORMER">  <mon:resource mon:id="1:User assigned to the DeAdmin role" >  <mon:name>User assigned to the DeAdmin role</mon:name>  </mon:resource>  </mon:role> |
| bpmnx:ACTIVITY\_TERMINATED         | An instance of an activity has been terminated.                                                                                                                                                                                                                                                                            | The <mon:model mon:type="activity\_type"> element describes the activity that emitted the event.  The <mon:type> attribute indicates the type of the activity, as defined in the BPMN 2.0 schema. For example, <mon:model mon:type="bpmn:callActivity">, or <mon:model type="bpmn:userTask">. The <mon:model> element describing the activity must be followed by a <mon:model> element describing the process defining the activity and the process instance from which the event was sent. It is followed by <mon:model> elements for higher-level constructs, such as process applications. The ACTIVITY\_ACTIVE event also contains the name of the user performing the activity as part of the <mon:role> element: <mon:role mon:id="PERFORMER">  <mon:resource mon:id="1:User assigned to the DeAdmin role" >  <mon:name>User assigned to the DeAdmin role</mon:name>  </mon:resource>  </mon:role> |
| bpmnx:ACTIVITY\_COMPLETED          | An instance of an activity is in the completed state.This event includes custom business data (KPIs and auto-tracked fields) in the applicationData element.                                                                                                                                                               | The <mon:model mon:type="activity\_type"> element describes the activity that emitted the event.  The <mon:type> attribute indicates the type of the activity, as defined in the BPMN 2.0 schema. For example, <mon:model mon:type="bpmn:callActivity">, or <mon:model type="bpmn:userTask">. The <mon:model> element describing the activity must be followed by a <mon:model> element describing the process defining the activity and the process instance from which the event was sent. It is followed by <mon:model> elements for higher-level constructs, such as process applications. The ACTIVITY\_ACTIVE event also contains the name of the user performing the activity as part of the <mon:role> element: <mon:role mon:id="PERFORMER">  <mon:resource mon:id="1:User assigned to the DeAdmin role" >  <mon:name>User assigned to the DeAdmin role</mon:name>  </mon:resource>  </mon:role> |
| bpmnx:ACTIVITY\_RESOURCE\_ ASSIGNED | A resource, such as a user, group, or organization, is associated with a task instance in a specific role. For example, the performer role designates the resource that is currently assigned to work on the task. This event includes custom business data (KPIs and auto-tracked fields) in the applicationData element. | The <mon:instance> element describes the task execution. The <mon:instance> element describing a task execution can contain one or more <mon:role> elements, which describe the resource roles used in the execution.  Nested <mon:resource> elements describe each of the resources. An example is shown in the XML fragment following the table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

- xmlns:mon="http://www.ibm.com/xmlns/prod/websphere/monitoring/7.5"
- xmlns:bpmn="http://schema.omg.org/spec/BPMN/2.0"

## ACTIVITY\_RESOURCE\_ ASSIGNED
example

```
<mon:model mon:type="bpmn:userTask" 
   mon:id="bpdid:af46278784e183e2:-44d4289d:12ba655e3ba:-7fc0" 
   mon:version="2064.69fdfcef-3900-47aa-817a-7960a182a48cT">
      <mon:name>assignOrderNumber</mon:name>
      <mon:instance mon:id="5">
        <mon:role mon:id="PERFORMER">
          <mon:resource mon:id="User assigned to the DeAdmin role">
            <mon:name>User assigned to the DeAdmin role</mon:name>
          </mon:resource>
        </mon:role>
      </mon:instance>
    </mon:model>
```

## Example ACTIVITY\_READY event

In every activity monitoring event, the <mon:model> element describing the
activity is followed by a <mon:model> element that describes the process
defining the activity, and the process instance from which the event was sent. An additional
<mon:model> element describes the process application defining the process. The
following event example shows three <mon:model> elements, one each for the
activity, the process, and the process application.

```
<mon:monitorEvent 
   xmlns:mon="http://www.ibm.com/xmlns/prod/websphere/monitoring/7.5" 
   mon:id="d12a887ef13ced21792162189" 
   xmlns:bpmn="http://schema.omg.org/spec/BPMN/2.0" 
   xmlns:bpmnx="http://www.ibm.com/xmlns/bpmnx/20100524/BusinessMonitoring" 
   xmlns:ibm="http://www.ibm.com/xmlns/prod/websphere/monitoring/7.5/extensions" 
   xmlns:wle="http://www.ibm.com/xmlns/prod/websphere/lombardi/7.5" 
   xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <mon:eventPointData>
    <mon:kind mon:version="2010-11-11">bpmnx:ACTIVITY\_READY</mon:kind>
    <mon:time mon:of="occurrence">2011-02-03T10:44:15.481-05:00</mon:time>
    <ibm:sequenceId>13</ibm:sequenceId>
    <mon:model mon:type="bpmn:subProcess" 
      mon:id="bpdid:571234bad276b9a1:-1448ee2a:12c08c263e4:-7fec" 
      mon:version="2064.9d926c59-6511-4ee9-a0d2-4015fb19cb55">
      <mon:name>Call Pong</mon:name>
      <mon:instance mon:id="5"/>
    </mon:model>
    <mon:model mon:type="bpmn:process" 
      mon:id="854325da-04ea-4ea6-8664-c701b4bf3d61" 
      mon:version="2064.9d926c59-6511-4ee9-a0d2-4015fb19cb55">
      <mon:name>Ping</mon:name>
      <mon:documentation>The "Ping" process definition.</mon:documentation>
      <mon:instance mon:id="754">
        <mon:state>Active</mon:state>
      </mon:instance>
    </mon:model>
    <mon:model 
     mon:type="wle:processApplication" 
     mon:id="b9e85db9-5c4d-40e7-9421-e53acb738f4e" 
     mon:version="2064.9d926c59-6511-4ee9-a0d2-4015fb19cb55">
      <mon:name>Oscillating Invocations</mon:name>
      <mon:documentation>Ping pong between two processes.</mon:documentation>
    </mon:model>
    <mon:correlation>
      <mon:ancestor mon:id="854325da-04ea-4ea6-8664-c701b4bf3d61.2064.9d926c59-6511-4ee9-a0d2-4015fb19cb55.754.5">
        <mon:ancestor mon:id="854325da-04ea-4ea6-8664-c701b4bf3d61.2064.9d926c59-6511-4ee9-a0d2-4015fb19cb55.754"/>
      </mon:ancestor>
      <wle:starting-process-instance>854325da-04ea-4ea6-8664-c701b4bf3d61.2064.9d926c59-6511-4ee9-a0d2-4015fb19cb55.754
      </wle:starting-process-instance>
    </mon:correlation>
  </mon:eventPointData>
  <mon:applicationData>
    <wle:tracking-point 
    wle:time="2011-02-03T10:44:15.481-05:00" 
    wle:name="Call Pong (PRE)" 
    wle:id="8c263e4-7ff2bpdid571234bad276b9a1-1448ee2a12c08c263e4-7fec (PRE)" 
    wle:version="2064.9d926c59-6511-4ee9-a0d2-4015fb19cb55" 
    wle:groupName="at1288664978829" 
    wle:groupId="guid:571234bad276b9a1:-1448ee2a:12c08c263e4:-7ff2" 
    wle:groupVersion="2064.9d926c59-6511-4ee9-a0d2-4015fb19cb55">
      <wle:tracked-field 
      wle:name="levelEnteringPing" 
      wle:id="bpdid:571234bad276b9a1:-1448ee2a:12c08c263e4:-7fc2" 
      wle:type="xs:integer">2</wle:tracked-field>
      <wle:tracked-field 
      wle:name="reportOfWhereInPing" 
      wle:id="bpdid:571234bad276b9a1:-1448ee2a:12c08c263e4:-7fc0" 
      wle:type="xs:string">About to call Pong with argument = 1.
      </wle:tracked-field>
      <wle:tracked-field 
      wle:name="argumentForPong" 
      wle:id="bpdid:571234bad276b9a1:-1448ee2a:12c08c263e4:-7fbe" 
      wle:type="xs:integer">1</wle:tracked-field>
    </wle:tracking-point>
  </mon:applicationData>
</mon:monitorEvent>
```

## User Task fields and activity events

```
<mon:instance mon:id="3" >
   <wle:taskInstanceId> 253</wle:taskInstanceId>
   <wle:taskRecord
      wle:taskDisplayName="Task: Create position request"
      wle:taskStatus="Closed"
      wle:taskDueDate="2017-09-25T14:04:48.015+05:30"
      wle:taskAtRiskTime="2017-09-25T13:58:48.024+05:30"
      wle:taskCompletionTime="2017-09-25T13:08:06.464+05:30"
      wle:taskDescription=“Create a full-time or part-time position request”
      wle:taskPriority="Normal"/>
</mon:instance>
```

```
<common>
  <monitor-event-emission>
    <task-record-enabled merge="replace">true</task-record-enabled>
  </monitor-event-emission>
</common>
```

```
<common>
  <monitor-event-emission>
    <task-narrative-record-enabled merge="replace">true</task-narrative-record-enabled>
  </monitor-event-emission>
</common>
```

| Event type               | Event description                  | Required elements                                                                                                           |
|--------------------------|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| wle:TASK\_SUBJECT\_CHANGED | The subject of a task has changed. | The <mon:instance> element that describes a task execution contains <wle:taskInstanceId> and <wle:taskRecord> for the task. |
| wle:TASK\_FIELD\_CHANGED   | The taskRecord field has changed.  | The <mon:instance> element that describes a task execution contains <wle:taskInstanceId> and <wle:taskRecord> for the task. |
| wle:TASK\_STATUS\_CHANGED  | The status of a task has changed.  | The <mon:instance> element that describes a task execution contains <wle:taskInstanceId> and <wle:taskRecord> for the task. |

```
<common>
  <monitor-event-emission>
    <enable-task-api-def merge="replace">false</enable-task-api-def>
  </monitor-event-emission>
</common>
```

## Looped activity monitoring events

You can configure simple and multi-instance loops for activities in a business process
definition. Loops allow an action to be repeated a specified number of times, or until a specific
condition is true. In a process definition, simple or multi-instance looped activities are
identified by an indicator in the activity icon. The event types that are emitted for looped
activities are described in the following table. These events are emitted in addition to the usual
activity monitoring events, which occur for every loop iteration.

| Event type                                                | Event description                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Required elements                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ACTIVITY\_LOOP\_ CONDITION\_TRUE(Simple loop)                | This event indicates that a loop condition evaluated to true. This means that the loop is not yet finished and another iteration will occur. The event is issued at each iteration of a loop if the loop condition is true. When an activity is modeled with simple loops, the required number of instances is dynamically created, up to the specified maximum number of loops. A simple-looped activity is started sequentially until the last instance of the activity has been performed. | The <mon:model mon:type="activity\_type"> element describes the activity that emitted the event.  The <mon:model> element describing the activity must be followed by a <mon:model> element describing the process defining the activity and the process instance from which the event was sent. It can be followed by <mon:model> elements for higher level constructs, such as process applications. These events include custom business data in the applicationData element.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ACTIVITY\_LOOP\_ CONDITION\_FALSE(Simple loop)               | This event indicates that a loop condition evaluated to false. This means that the loop is finished and will be exited. The event is issued after the last iteration of a loop, if the loop condition is false.                                                                                                                                                                                                                                                                               | The <mon:model mon:type="activity\_type"> element describes the activity that emitted the event.  The <mon:model> element describing the activity must be followed by a <mon:model> element describing the process defining the activity and the process instance from which the event was sent. It can be followed by <mon:model> elements for higher level constructs, such as process applications. These events include custom business data in the applicationData element.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ACTIVITY\_PARALLEL\_ INSTANCES\_STARTED(Multi-instance loop) | This event is issued when multiple instances of an activity are created in parallel. The event reports the number of activity instances that have been created.                                                                                                                                                                                                                                                                                                                               | The <mon:instance> element which corresponds to the multi-instance activity must contain a <mon:started> element. The mon:started element indicates the number of instances that have been created. The mon:started element can also contain <mon:startedId> elements, which include the identifiers of the activity instances.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ACTIVITY\_TERMINATED(Multi-instance parallel)              | A multi-instance, parallel activity can be configured to terminate all running instances when its flow condition evaluates to true. Each terminated instance emits an ACTIVITY\_TERMINATED event.                                                                                                                                                                                                                                                                                              | The <mon:model mon:type="activity\_type"> element describes the activity that emitted the event.  The <mon:type> attribute indicates the type of the activity, as defined in the BPMN 2.0 schema. For example, <mon:model mon:type="bpmn:callActivity">, or <mon:model type="bpmn:userTask">. The <mon:model> element describing the activity must be followed by a <mon:model> element describing the process defining the activity and the process instance from which the event was sent. It is followed by <mon:model> elements for higher level constructs, such as process applications. The ACTIVITY\_ACTIVE event also contains the name of the user performing the activity as part of the <mon:role> element: <mon:role mon:id="PERFORMER">  <mon:resource mon:id="1:User assigned to the DeAdmin role" >  <mon:name>User assigned to the DeAdmin role</mon:name>  </mon:resource>  </mon:role> |

```
ACTIVITY\_READY
ACTIVITY\_LOOP\_CONDITION\_FALSE
ACTIVITY\_LOOP\_CONDITION\_FALSE
ACTIVITY\_LOOP\_CONDITION\_FALSE
ACTIVITY\_LOOP\_CONDITION\_TRUE
ACTIVITY\_COMPLETED
```

## Example of a simple looped activity mon:model element

```
<mon:model mon:type="bpmn:process" 
   mon:id="70be5404-7f97-4d15-95c5-2e0a02357978" 
   mon:version="2064.cf17230d-0af1-4494-82e7-e0505356a502T">
      <mon:name>Loop: Simple Loop</mon:name>
      <mon:instance mon:id="612">
        <mon:state>Active</mon:state>
      </mon:instance>
</mon:model>
```

## Monitoring data visible in Process Portal

```
<common>
    <monitor-event-emission>
      <auto-track-data-visible-in-portal>true</auto-track-data-visible-in-portal>
    </monitor-event-emission>
  </common>
```

- Monitoring events contain the alias names and values of the variables that are selected as
Visible in Process Portal, regardless or whether they are selected as tracked
or not. These fields are associated with the autotracking name, even if auto-tracking is not
enabled.
- Monitoring events do not contain explicitly tracked fields.
- The tracked fields of the monitoring events are not sent to Performance Data Warehouse.