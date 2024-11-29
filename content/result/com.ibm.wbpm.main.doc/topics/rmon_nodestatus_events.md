# Event monitoring events

## Monitoring events

The event monitoring events
are described in the following table.

| Event type           | Event description                                                                                                                                                                                                                                                                                                                                                                                                               | Required elements                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| bpmnx:EVENT\_EXPECTED | An Intermediate Timer Event in a process definition emits an EVENT\_EXPECTED monitoring event when a token arrives and starts the timer. When time is up and the flow continues, an EVENT\_CAUGHT monitoring event is emitted.                                                                                                                                                                                                    | The <mon:eventPointData> element contains a <mon:model mon:type="event\_type"> element describing the process event in the process definition, such as a Start Event, where the mon:type attribute indicates the type of process event. For example, mon:type="bpmn:startEvent", or mon:type="bpmn:endEvent". This element is followed by a <mon:model mon:type="bpmn:process"> element for the process which emitted the event. These events include custom business data (KPIs and auto-tracked fields or tracked fields for an Intermediate Tracking Event) in the applicationData element. |
| bpmnx:EVENT\_CAUGHT   | A BPMN process is started by a Start Event, Start Message Event, or Start Ad Hoc Event. These occurrences are reported by an EVENT\_CAUGHT monitoring event.An Intermediate Timer Event can also emit an EVENT\_CAUGHT monitoring event to report that the timer has started.                                                                                                                                                     | The <mon:eventPointData> element contains a <mon:model mon:type="event\_type"> element describing the process event in the process definition, such as a Start Event, where the mon:type attribute indicates the type of process event. For example, mon:type="bpmn:startEvent", or mon:type="bpmn:endEvent". This element is followed by a <mon:model mon:type="bpmn:process"> element for the process which emitted the event. These events include custom business data (KPIs and auto-tracked fields or tracked fields for an Intermediate Tracking Event) in the applicationData element. |
| bpmnx:EVENT\_THROWN   | A BPMN process is ended by an End Event, Terminate Event, or End Exception Event. These occurrences are reported by an EVENT\_THROWN monitoring event. Some Intermediate Events, including Intermediate Message Event, Intermediate Exception Event, and Intermediate Tracking Event, also emit an EVENT\_THROWN monitoring event. The event reports that a message was sent, or an exception error or tracking data was created. | The <mon:eventPointData> element contains a <mon:model mon:type="event\_type"> element describing the process event in the process definition, such as a Start Event, where the mon:type attribute indicates the type of process event. For example, mon:type="bpmn:startEvent", or mon:type="bpmn:endEvent". This element is followed by a <mon:model mon:type="bpmn:process"> element for the process which emitted the event. These events include custom business data (KPIs and auto-tracked fields or tracked fields for an Intermediate Tracking Event) in the applicationData element. |

Additional information about Start, End and Intermediate
events is provided in the Business Process Model and Notation (BPMN)
2.0 specification document, which you can download from the Object Management Group website. Sections
10.4.1 through 10.4.4 in the specification document discuss these
process model elements.

## Example EVENT\_CAUGHT event

```
<mon:monitorEvent 
  xmlns:mon="http://www.ibm.com/xmlns/prod/websphere/monitoring/7.5" 
  mon:id="Y129bea9f13ced21792162189" 
  xmlns:bpmn="http://schema.omg.org/spec/BPMN/2.0" 
  xmlns:bpmnx="http://www.ibm.com/xmlns/bpmnx/20100524/BusinessMonitoring" 
  xmlns:ibm="http://www.ibm.com/xmlns/prod/websphere/monitoring/7.5/extensions" 
  xmlns:wle="http://www.ibm.com/xmlns/prod/websphere/lombardi/7.5" 
  xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <mon:eventPointData>
    <mon:kind mon:version="2010-11-11">bpmnx:EVENT\_CAUGHT</mon:kind>
    <mon:time mon:of="occurrence">2011-02-03T10:44:14.255-05:00</mon:time>
    <ibm:sequenceId>4</ibm:sequenceId>
    <mon:model 
     mon:type="bpmn:startEvent" 
     mon:id="bpdid:571234bad276b9a1:-1448ee2a:12c08c263e4:-7fee" 
     mon:version="2064.9d926c59-6511-4ee9-a0d2-4015fb19cb55">
      <mon:name>Start</mon:name>
      <mon:instance mon:id="2"/>
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
      <mon:ancestor 
       mon:id="854325da-04ea-4ea6-8664-c701b4bf3d61.2064.9d926c59-6511-4ee9-a0d2-4015fb19cb55.754.2">
        <mon:ancestor 
         mon:id="854325da-04ea-4ea6-8664-c701b4bf3d61.2064.9d926c59-6511-4ee9-a0d2-4015fb19cb55.754"/>
      </mon:ancestor>
      <wle:starting-process-instance>854325da-04ea-4ea6-8664-c701b4bf3d61.2064.9d926c59-6511-4ee9-a0d2-4015fb19cb55.754
      </wle:starting-process-instance>
    </mon:correlation>
  </mon:eventPointData>
  <mon:applicationData>
    <wle:tracking-point 
     wle:time="2011-02-03T10:44:14.255-05:00" 
     wle:name="Start (POST)" wle:id="c263e4-7ff2bpdid571234bad276b9a1-1448ee2a12c08c263e4-7fee (POST)" 
     wle:version="2064.9d926c59-6511-4ee9-a0d2-4015fb19cb55" wle:groupName="at1288664978829" 
     wle:groupId="guid:571234bad276b9a1:-1448ee2a:12c08c263e4:-7ff2" 
     wle:groupVersion="2064.9d926c59-6511-4ee9-a0d2-4015fb19cb55">
      <wle:tracked-field wle:name="levelEnteringPing" 
       wle:id="bpdid:571234bad276b9a1:-1448ee2a:12c08c263e4:-7fc2" 
       wle:type="xs:integer">2</wle:tracked-field>
      <wle:tracked-field wle:name="reportOfWhereInPing" 
       wle:id="bpdid:571234bad276b9a1:-1448ee2a:12c08c263e4:-7fc0" 
       wle:type="xs:string">This is Ping. Called with level = 2.</wle:tracked-field>
      <wle:tracked-field 
       wle:name="argumentForPong" 
       wle:id="bpdid:571234bad276b9a1:-1448ee2a:12c08c263e4:-7fbe" 
       wle:type="xs:integer"/>
    </wle:tracking-point>
  </mon:applicationData>
</mon:monitorEvent>
```