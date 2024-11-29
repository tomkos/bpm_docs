# Service integration monitoring events

When a service flow has started, completed, or
failed, the state change is reported in a monitoring event. Intermediate
tracking events of a service flow are also reported as monitoring
events.

- Service flow events
- Service task events
- Decision task events
- Content integration tasks
- Script tasks events
- Tracking events
- Common fault elements for all FAILED events

- External Services events (RTC 291938)

## Service flow events

The
event types emitted for service flows are described in the following
table.

| Event type              | Event description                | Required elements                                                                                                                                                                                     |
|-------------------------|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| bpmnx:PROCESS\_STARTED   | A service flow has been started. | The <mon:model mon:type="wle:serviceFlow"> element describes the service flow model that emitted the event. The <mon:instance> element identifies the instance of the process that emitted the event. |
| bpmnx:PROCESS\_COMPLETED | A service flow has completed.    | The <mon:model mon:type="wle:serviceFlow"> element describes the service flow model that emitted the event. The <mon:instance> element identifies the instance of the process that emitted the event. |
| bpmnx:PROCESS\_FAILED    | A service flow has failed.       | In addition to the required elements described for the other process events, the <mon:instance> contain a <mon:fault> element, which is described in Common fault elements for all FAILED events.     |

## Service
task events

The event types emitted for service tasks
are described in the following table.

| Event type               | Event description             | Required elements                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|--------------------------|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| bpmnx:ACTIVITY\_ACTIVE    | A service task is active.     | The <mon:model mon:type="bpmn:serviceTask"> element describes the service flow model that emitted the event. The <mon:instance> element identifies the instance of the service task that emitted the event. The <wle:externalService> element identifies the name of the external service that is invoked. The <wle:binding> element identifies the binding type. Possible values are: Java, REST, Web Service The <wle:operation> element identifies the operation of the external service that is invoked. |
| bpmnx:ACTIVITY\_COMPLETED | A service task has completed. | The <mon:model mon:type="bpmn:serviceTask"> element describes the service flow model that emitted the event. The <mon:instance> element identifies the instance of the service task that emitted the event. The <wle:externalService> element identifies the name of the external service that is invoked. The <wle:binding> element identifies the binding type. Possible values are: Java, REST, Web Service The <wle:operation> element identifies the operation of the external service that is invoked. |
| bpmnx:ACTIVITY\_FAILED    | A service task has failed.    | In addition to the required elements described for the other service task events, the <mon:instance> contain a <mon:fault> element, which is described in Common fault elements for all FAILED events.                                                                                                                                                                                                                                                                                                       |

## Decision
task events

The event types emitted for decision tasks
are described in the following table.

| Event type               | Event description              | Required elements                                                                                                                                                                                             |
|--------------------------|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| bpmnx:ACTIVITY\_ACTIVE    | A decision task is active.     | The <mon:model mon:type="bpmn:decisionTask"> element describes the service flow model that emitted the event. The <mon:instance> element identifies the instance of the decision task that emitted the event. |
| bpmnx:ACTIVITY\_COMPLETED | A decision task has completed. | The <mon:model mon:type="bpmn:decisionTask"> element describes the service flow model that emitted the event. The <mon:instance> element identifies the instance of the decision task that emitted the event. |
| bpmnx:ACTIVITY\_FAILED    | A decision task has failed.    | In addition to the required elements described for the other decision task events, the <mon:instance> contain a <mon:fault> element, which is described in Common fault elements for all FAILED events.       |

| Event type               | Event description                  | Required elements                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|--------------------------|------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| bpmnx:ACTIVITY\_ACTIVE    | An external service is active.     | The <mon:model mon:type="wle:externalService"> element describes the service flow model that emitted the event. The <mon:instance> element identifies the instance of the external service invocation task that emitted the event. Depending on the type of the external service, the service subtype is indicated by one of the following: REST\_EXTERNAL\_SERVICE for a REST service WS\_EXTERNAL\_SERVICE for a web service JAVA\_EXTERNAL\_SERVICE for a java invocation |
| bpmnx:ACTIVITY\_COMPLETED | An external service has completed. | The <mon:model mon:type="wle:externalService"> element describes the service flow model that emitted the event. The <mon:instance> element identifies the instance of the external service invocation task that emitted the event. Depending on the type of the external service, the service subtype is indicated by one of the following: REST\_EXTERNAL\_SERVICE for a REST service WS\_EXTERNAL\_SERVICE for a web service JAVA\_EXTERNAL\_SERVICE for a java invocation |
| bpmnx:ACTIVITY\_FAILED    | An external service has failed.    | In addition to the required elements described for the other external service invocation events, the <mon:instance> contain a <mon:fault> element, which is described in Common fault elements for all FAILED events.                                                                                                                                                                                                                                                  |

## Content
integration tasks

| Event type               | Event description                         | Required elements                                                                                                                                                                                                                                                                                                                                                                                                               |
|--------------------------|-------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| bpmnx:ACTIVITY\_ACTIVE    | A content integration task is active.     | The <mon:model mon:type="wle:contentIntegrationTask"> element describes the service flow model that emitted the event. The <mon:instance> element identifies the instance of the content integration task that emitted the event. The <wle:operation> element describes the operation invoked by the content integration task. The <wle:server> element identifies that server that is invoked by the content integration task. |
| bpmnx:ACTIVITY\_COMPLETED | A content integration task has completed. | The <mon:model mon:type="wle:contentIntegrationTask"> element describes the service flow model that emitted the event. The <mon:instance> element identifies the instance of the content integration task that emitted the event. The <wle:operation> element describes the operation invoked by the content integration task. The <wle:server> element identifies that server that is invoked by the content integration task. |
| bpmnx:ACTIVITY\_FAILED    | A content integration task has failed.    | In addition to the required elements described for the other content integration task events, the <mon:instance> contain a <mon:fault> element, which is described in Common fault elements for all FAILED events.                                                                                                                                                                                                              |

```
<?xml version="1.0" encoding="UTF-8"?>
<mon:monitorEvent mon:id="m236b83ae56da161792162189"
	xmlns:bpmn="http://schema.omg.org/spec/BPMN/2.0"
	xmlns:bpmnx="http://www.ibm.com/xmlns/bpmnx/20100524/BusinessMonitoring"
	xmlns:mon="http://www.ibm.com/xmlns/prod/websphere/monitoring/7.5"
	xmlns:ibm="http://www.ibm.com/xmlns/prod/websphere/monitoring/7.5/extensions"
	xmlns:wle="http://www.ibm.com/xmlns/prod/websphere/lombardi/7.5"
	xmlns:xs="http://www.w3.org/2001/XMLSchema">
	<mon:eventPointData>
		<mon:kind mon:version="2010-11-11">bpmnx:ACTIVITY\_ACTIVE</mon:kind>
		<mon:time mon:of="occurrence">2018-02-19T10:29:52.951+01:00</mon:time>
		<ibm:sequenceId>0000000002</ibm:sequenceId>
		<mon:model mon:type="wle:contentIntegrationTask" mon:id="da52a37a-ad1c-407d-855a-7ae984a1c319" mon:version="2064.ad84e1f8-bfb8-4d92-98d8-658856eee0b4">
			<mon:name>Content Integration</mon:name>
			<wle:operation>getDocument</wle:operation>
			<wle:server>EMBEDDED\_ECM\_SERVER</wle:server>

			<mon:instance mon:id="763.0">
				<mon:state>STATUS\_ACTIVE</mon:state>
			</mon:instance>
		</mon:model>
		<mon:model mon:type="wle:serviceFlow" mon:id="10a71c8b-9693-4096-abca-abee63ac0f74" mon:version="2064.ad84e1f8-bfb8-4d92-98d8-658856eee0b4">
			<mon:name>af\_svc\_flw\_8\_content</mon:name>
			<mon:instance mon:id="763">
				<mon:state>STATUS\_RCVD</mon:state>
			</mon:instance>
		</mon:model>
		<mon:model mon:type="wle:processApplication" mon:id="7275f2b5-e875-4bdc-aecf-0f93ce6577ee" mon:version="2064.ad84e1f8-bfb8-4d92-98d8-658856eee0b4">
			<mon:name>AF\_DEF\_TEST\_1</mon:name>
			<mon:documentation></mon:documentation>
		</mon:model>
		<mon:correlation>
			<mon:ancestor mon:id="10a71c8b-9693-4096-abca-abee63ac0f74.87040f9e-0b1b-431b-a487-f2ce4f008dc1.763.0">
				<mon:ancestor mon:id="10a71c8b-9693-4096-abca-abee63ac0f74.87040f9e-0b1b-431b-a487-f2ce4f008dc1.763"></mon:ancestor>
			</mon:ancestor>
			<wle:starting-process-instance>10a71c8b-9693-4096-abca-abee63ac0f74.87040f9e-0b1b-431b-a487-f2ce4f008dc1.763</wle:starting-process-instance>
		</mon:correlation>
		<mon:source>
			<ibm:system ibm:systemID="87040f9e-0b1b-431b-a487-f2ce4f008dc1"/>
		</mon:source>
	</mon:eventPointData>
</mon:monitorEvent>
```

## Script tasks events

| Event type               | Event description            | Required elements                                                                                                                                                                                                  |
|--------------------------|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| bpmnx:ACTIVITY\_ACTIVE    | A script task is active.     | The <mon:model mon:type="bpmn:scriptTask"> element describes the service flow model that emitted the event. The <mon:instance> element identifies the instance of the service task that emitted the event.         |
| bpmnx:ACTIVITY\_COMPLETED | A script task has completed. | The <mon:model mon:type="bpmn:scriptTask"> element describes the service flow model that emitted the event. The <mon:instance> element identifies the instance of the service task that emitted the event.         |
| bpmnx:ACTIVITY\_FAILED    | A script task has failed.    | In addition to the required elements described for the other content integration task events, the <mon:instance> contain a <mon:fault> element, which is described in Common fault elements for all FAILED events. |

## Tracking events

The monitoring
event EVENT\_THROWN is used to report intermediate tracking events
of a service flow.

| Event type         | Event description                                                                     | Required elements                                                                                                                                                                                                                                                                                                                                                                      |
|--------------------|---------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| bpmnx:EVENT\_THROWN | Intermediate tracking events of a service flow emit an EVENT\_THROWN monitoring event. | The <mon:eventPointData> element contains a <mon:model mon:type="wle:intermediateTrackingEvent"> element that describes the tracking event in the service flow. This element is followed by a <mon:model mon:type="wle:serviceFlow">  element for the service flow which emitted the event. These events include custom business data (tracked fields) in the applicationData element. |

```
<?xml version="1.0" encoding="UTF-8"?>
<mon:monitorEvent mon:id="Q57c4a750d02061792162189"
	xmlns:bpmn="http://schema.omg.org/spec/BPMN/2.0"
	xmlns:bpmnx="http://www.ibm.com/xmlns/bpmnx/20100524/BusinessMonitoring"
	xmlns:mon="http://www.ibm.com/xmlns/prod/websphere/monitoring/7.5"
	xmlns:ibm="http://www.ibm.com/xmlns/prod/websphere/monitoring/7.5/extensions"
	xmlns:wle="http://www.ibm.com/xmlns/prod/websphere/lombardi/7.5"
	xmlns:xs="http://www.w3.org/2001/XMLSchema">
	<mon:eventPointData>
		<mon:kind mon:version="2010-11-11">bpmnx:EVENT\_THROWN</mon:kind>
		<mon:time mon:of="occurrence">2017-12-04T10:16:53.028+01:00</mon:time>
		<ibm:sequenceId>0000000002</ibm:sequenceId>
		<mon:model mon:type="wle:intermediateTrackingEvent" 
               mon:id="0167bd53-fc8e-4b75-80cf-4d531973e899" 
               mon:version="2064.c554a27b-4366-4932-b3c7-45a4c1f9c922">
			<mon:name>af\_send\_tracking</mon:name>
		</mon:model>
		<mon:model mon:type="wle:serviceFlow" 
               mon:id="1cb3dfce-24fe-486b-b0fc-ce458bd436a9" 
               mon:version="2064.c554a27b-4366-4932-b3c7-45a4c1f9c922">
			<mon:name>AF\_svc\_flw\_1</mon:name>
			<mon:instance mon:id="703"></mon:instance>
		</mon:model>
		<mon:model mon:type="wle:processApplication" 
               mon:id="7275f2b5-e875-4bdc-aecf-0f93ce6577ee" 
               mon:version="2064.c554a27b-4366-4932-b3c7-45a4c1f9c922">
			<mon:name>AF\_DEF\_TEST\_1</mon:name>
			<mon:documentation></mon:documentation>
		</mon:model>
		<mon:correlation>
			<mon:ancestor mon:id="1cb3dfce-24fe-486b-b0fc-ce458bd436a9.b668efb4-e746-430c-9ac2-c466435db1d2.703.2">
				<mon:ancestor mon:id="1cb3dfce-24fe-486b-b0fc-ce458bd436a9.b668efb4-e746-430c-9ac2-c466435db1d2.703">
         </mon:ancestor>
			</mon:ancestor>
			<wle:starting-process-instance>1cb3dfce-24fe-486b-b0fc-ce458bd436a9.b668efb4-e746-430c-9ac2-c466435db1d2.703
      </wle:starting-process-instance>
		</mon:correlation>
		<mon:source>
			<ibm:system ibm:systemID="b668efb4-e746-430c-9ac2-c466435db1d2"/>
		</mon:source>
	</mon:eventPointData>
	<mon:applicationData>
		<wle:tracking-point wle:time="2017-12-04T10:16:53.028+01:00" 
                        wle:name="af\_send\_tracking" 
                        wle:id="3039771d-5dda-4b8b-8bcd-4cff377207de" 
                        wle:version="2064.c554a27b-4366-4932-b3c7-45a4c1f9c922T" 
                        wle:groupName="AF\_BPD\_TG\_1" 
                        wle:groupId="b2d4a594-5e9f-44cc-a749-97c728c2aef4" 
                        wle:groupVersion="2064.c554a27b-4366-4932-b3c7-45a4c1f9c922T">
			<wle:tracked-field wle:name="local\_bpd\_var\_4\_tracking" 
                          wle:id="8db45ad3-c87a-40b4-830e-4a1021d406bc" 
                          wle:type="xs:string">s3s3s3</wle:tracked-field>
		</wle:tracking-point>
	</mon:applicationData>
</mon:monitorEvent>
```

## Common fault elements for all FAILED events

- In case of a business error, for example, that is raised by an
error event, the <mon:fault> element includes
a mon:name attribute which contains the error code.
The content of the <mon:fault> element contains
optional additional diagnostic information. For example:<mon:fault mon:name="ERR\_123">The customer ID is invalid.</mon:fault>
- In case of an unexpected or system error, the mon:name attribute
contains an IBM product error message. For example:<mon:fault mon:name="GXSD1037E: The required parameter value is missing."></mon:fault>