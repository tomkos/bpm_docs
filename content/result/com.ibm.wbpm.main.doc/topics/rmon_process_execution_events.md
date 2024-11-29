# Process monitoring events

The event types emitted for process executions are described
in the following table.

| Event type               | Event description                            | Required elements                                                                                                                                                                                                                                                                                                                                                                            |
|--------------------------|----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| bpmnx:PROCESS\_STARTED    | An instance of a process has been started.   | The <mon:model mon:type="bpmn:process"> element describes the process model and the type of process which emitted the event. The <mon:instance> element identifies the instance of the process that emitted the event.                                                                                                                                                                       |
| bpmnx:PROCESS\_COMPLETED  | An instance of a process has been completed. | The <mon:model mon:type="bpmn:process"> element describes the process model and the type of process which emitted the event. The <mon:instance> element identifies the instance of the process that emitted the event.                                                                                                                                                                       |
| bpmnx:PROCESS\_TERMINATED | An instance of a process has terminated.     | The <mon:model mon:type="bpmn:process"> element describes the process model and the type of process which emitted the event. The <mon:instance> element identifies the instance of the process that emitted the event.                                                                                                                                                                       |
| bpmnx:PROCESS\_DELETED    | An instance of a process has been deleted.   | The <mon:model mon:type="bpmn:process"> element describes the process model and the type of process which emitted the event. The <mon:instance> element identifies the instance of the process that emitted the event.                                                                                                                                                                       |
| bpmnx:PROCESS\_FAILED     | An instance of a process has failed.         | In addition to the required elements described for the other process events, the PROCESS\_FAILED event includes these elements: The <mon:instance> element must contain a <mon:fault> element. The content of the mon:fault element provides diagnostic information such as an error message or stack trace. The mon:name attribute on the mon:fault element indicates the name of the fault. |

Although a monitoring event must contain at least one <mon:model>
element describing the process model and a corresponding <mon:instance>
element describing the process execution, in some cases, more than
one of these elements can exist in an event. For example, when the
deployed process model is part of a higher-level construct, such as
a module, application or solution, then the event can include additional <mon:model>
elements that describe the construct.

## Example PROCESS\_STARTED event

```
<mon:monitorEvent xmlns:mon="http://www.ibm.com/xmlns/prod/websphere/monitoring/7.5" 
   mon:id="C1299df7f13ced21792162189" xmlns:bpmn="http://schema.omg.org/spec/BPMN/2.0" 
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
    <mon:model mon:type="wle:processApplication" 
     mon:id="b9e85db9-5c4d-40e7-9421-e53acb738f4e" 
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