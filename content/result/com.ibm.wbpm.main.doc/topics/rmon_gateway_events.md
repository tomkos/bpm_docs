# Gateway events

| Event type              | Event description                                                  | Required elements                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-------------------------|--------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| bpmnx:GATEWAY\_ACTIVATED | The gateway is activated by the inbound sequence flow.             | The <mon:eventPointData> element must contain a <mon:model mon:type="gateway-type"> element for the gateway definition. The mon:type attribute indicates the type of the gateway that was activated, for example, mon:type="bpmn:exclusiveGateway", or mon:type="bpmn:parallelGateway". The <mon:eventPointData> element is followed by a <mon:model mon:type="bpmn:process"> element for the process definition which emitted the event. The <mon:model> elements describing the gateway and the process must each contain a <mon:instance> element describing the specific instance. These events include custom business data (KPIs and auto-tracked fields) in the applicationData element. |
| bpmnx:GATEWAY\_COMPLETED | The gateway is completed and the outbound sequence flow continues. | The <mon:eventPointData> element must contain a <mon:model mon:type="gateway-type"> element for the gateway definition. The mon:type attribute indicates the type of the gateway that was activated, for example, mon:type="bpmn:exclusiveGateway", or mon:type="bpmn:parallelGateway". The <mon:eventPointData> element is followed by a <mon:model mon:type="bpmn:process"> element for the process definition which emitted the event. The <mon:model> elements describing the gateway and the process must each contain a <mon:instance> element describing the specific instance. These events include custom business data (KPIs and auto-tracked fields) in the applicationData element. |

## Example GATEWAY\_COMPLETED event

```
<mon:monitorEvent 
  xmlns:mon="http://www.ibm.com/xmlns/prod/websphere/monitoring/7.5" 
  mon:id="c12a558cf13ced21792162189" 
  xmlns:bpmn="http://schema.omg.org/spec/BPMN/2.0" 
  xmlns:bpmnx="http://www.ibm.com/xmlns/bpmnx/20100524/BusinessMonitoring" 
  xmlns:ibm="http://www.ibm.com/xmlns/prod/websphere/monitoring/7.5/extensions" 
  xmlns:wle="http://www.ibm.com/xmlns/prod/websphere/lombardi/7.5" 
  xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <mon:eventPointData>
    <mon:kind mon:version="2010-11-11">bpmnx:GATEWAY\_COMPLETED</mon:kind>
    <mon:time mon:of="occurrence">2011-02-03T10:44:14.982-05:00</mon:time>
    <ibm:sequenceId>11</ibm:sequenceId>
    <mon:model mon:type="bpmn:exclusiveGateway" 
     mon:id="bpdid:571234bad276b9a1:-1448ee2a:12c08c263e4:-7fe7" 
     mon:version="2064.9d926c59-6511-4ee9-a0d2-4015fb19cb55">
      <mon:name>Call Pong ?</mon:name>
      <mon:instance mon:id="4"/>
    </mon:model>
    <mon:model mon:type="bpmn:process" 
     mon:id="854325da-04ea-4ea6-8664-c701b4bf3d61" mon:version="2064.9d926c59-6511-4ee9-a0d2-4015fb19cb55">
      <mon:name>Ping</mon:name>
      <mon:documentation>The "Ping" process definition.</mon:documentation>
      <mon:instance mon:id="754">
        <mon:state>Active</mon:state>
      </mon:instance>
    </mon:model>
    <mon:model mon:type="wle:processApplication" 
     mon:id="b9e85db9-5c4d-40e7-9421-e53acb738f4e" 
     mon:version="2064.9d926c59-6511-4ee9-a0d2-4015fb19cb55">
      <mon:name>Oscillating Invocations</mon:name>
      <mon:documentation>Ping pong between two processes.</mon:documentation>
    </mon:model>
    <mon:correlation>
      <mon:ancestor mon:id="854325da-04ea-4ea6-8664-c701b4bf3d61.2064.9d926c59-6511-4ee9-a0d2-4015fb19cb55.754.4">
        <mon:ancestor mon:id="854325da-04ea-4ea6-8664-c701b4bf3d61.2064.9d926c59-6511-4ee9-a0d2-4015fb19cb55.754"/>
      </mon:ancestor>
      <wle:starting-process-instance>854325da-04ea-4ea6-8664-c701b4bf3d61.2064.9d926c59-6511-4ee9-a0d2-4015fb19cb55.754
      </wle:starting-process-instance>
    </mon:correlation>
  </mon:eventPointData>
  <mon:applicationData>
    <wle:tracking-point 
     wle:time="2011-02-03T10:44:14.982-05:00" 
     wle:name="Call Pong ? (POST)" 
     wle:id="c263e4-7ff2bpdid571234bad276b9a1-1448ee2a12c08c263e4-7fe7 (POST)" 
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
       wle:type="xs:string">This is Ping. Called with level = 2.</wle:tracked-field>
      <wle:tracked-field 
       wle:name="argumentForPong" 
       wle:id="bpdid:571234bad276b9a1:-1448ee2a:12c08c263e4:-7fbe" 
       wle:type="xs:integer"/>
      <wle:kpi-data 
       wle:name="Labor Cost" 
       wle:id="fbec4968-5e4c-4f2b-b11b-f3c9ef63d09b" 
       wle:version="2064.8d7ade38-7307-4894-a633-9903b7fc69d6" 
       wle:type="xs:decimal">0</wle:kpi-data>
      <wle:kpi-data 
       wle:name="Total Time (Clock)" 
       wle:id="67cbb213-0032-4f14-be44-7e9c7a1a146f" 
       wle:version="2064.8d7ade38-7307-4894-a633-9903b7fc69d6" 
       wle:type="xs:dayTimeDuration">P0DT0H0M0S</wle:kpi-data>
      <wle:kpi-data 
       wle:name="Wait Time (Clock)" 
       wle:id="43b503bd-63e7-4c42-8268-92d1033e0997" 
       wle:version="2064.8d7ade38-7307-4894-a633-9903b7fc69d6" 
       wle:type="xs:dayTimeDuration">P0DT0H0M0S</wle:kpi-data>
      <wle:kpi-data 
       wle:name="Resource Cost" 
       wle:id="d5da2c80-b2af-40a6-981d-9de4df12ed12" 
       wle:version="2064.8d7ade38-7307-4894-a633-9903b7fc69d6" 
       wle:type="xs:decimal">0</wle:kpi-data>
      <wle:kpi-data 
       wle:name="Value Add" 
       wle:id="e30cf309-a884-4a7b-a2db-16e8a371a4c1" 
       wle:version="2064.8d7ade38-7307-4894-a633-9903b7fc69d6" 
       wle:type="xs:decimal">1</wle:kpi-data>
      <wle:kpi-data 
       wle:name="Execution Time (Clock)" 
       wle:id="8601bb6b-9c9d-4cba-936e-16350a036de3" 
       wle:version="2064.8d7ade38-7307-4894-a633-9903b7fc69d6" 
       wle:type="xs:dayTimeDuration">P0DT0H0M0S</wle:kpi-data>
      <wle:kpi-data 
       wle:name="Cost" wle:id="995ba3fc-e786-45eb-b356-47acb3d3ebbc" 
       wle:version="2064.8d7ade38-7307-4894-a633-9903b7fc69d6" 
       wle:type="xs:decimal">0.00000000</wle:kpi-data>
      <wle:kpi-data 
       wle:name="Rework" 
       wle:id="0f650e6c-a9d7-4355-90bd-06530fa3eeec" 
       wle:version="2064.8d7ade38-7307-4894-a633-9903b7fc69d6" 
       wle:type="xs:decimal">0</wle:kpi-data>
    </wle:tracking-point>
  </mon:applicationData>
</mon:monitorEvent>
```