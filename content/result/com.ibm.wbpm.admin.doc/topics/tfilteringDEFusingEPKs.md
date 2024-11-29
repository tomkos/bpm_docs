# Filtering DEF events by using event point key values

## Procedure

1. To find the event point key value that you use to filter the events, in a development
environment use a wildcard for all the event point keys in defconfig.xml file,
for example 
<filter xmi:id="DefFilter\_1446210018100" appName="*" version="*" 
componentType="*" componentName="*" elementType="*" elementName="*" nature="*" 
filterId="ProducerFor\_jmsListenerSupplier\_0"/>
Using this wildcard will emit all the events.
2. Enable the following DEF trace and run your application: 
*=info:com.ibm.ws.monitoring.*=all:com.ibm.bpm.def.*=all
The trace should look similar to this
example[6/17/21 10:55:36:570 CEST] 0000021a EventPointImp > com.ibm.ws.monitoring.core.Entry isEnabled() ENTRY ESBMediation.testmediation.UNKNOWN.MEDIATION\_FLOW\_PRIMITIVE.TestMediation\_TestMediation\_MappingFaultValidation.ENTRY
...
[6/17/21 10:55:36:571 CEST] 0000021a AbstractFilte > com.ibm.bpm.def.impl.filters.ProcessAppFilterRegistry isEventPointKeyEnabled Entry: eventPointKey=EventPointKey [processAppName=TestMediation, version=, elementType=MEDIATION.FLOW.PRIMITIVE, elementName=TestMediation:TestMediation:MappingFaultValidation, componentType=http://www.ibm.com/xmlns/prod/websphere/esb/6.0.2:ESBEventMediation, componentName=TestMediation, nature=ENTRY]       // You can see the EventPointKey HERE
[6/17/21 10:55:36:571 CEST] 0000021a AbstractFilte < com.ibm.bpm.def.impl.filters.ProcessAppFilterRegistry isEventPointKeyEnabled Exit: true
[6/17/21 10:55:36:571 CEST] 0000021a EventPointImp 2   isEnabled: listener exists so return true immediately
// The DEF EventPointKey is Enabled
3. Check the trace for the different events that are emitted with the event point key
values. You can filter in the defconfig.xml file for the events you want to
review. In the previous example trace, event point key is
eventPointKey=EventPointKey [processAppName=TestMediation, version=, 
elementType=MEDIATION.FLOW.PRIMITIVE, 
elementName=TestMediation:TestMediation:MappingFaultValidation, 
componentType=http://www.ibm.com/xmlns/prod/websphere/esb/6.0.2:ESBEventMediation, 
componentName=TestMediation, nature=ENTRY]The corresponding
defconfig entry in this example
is<filter xmi:id="DefFilter\_1446210018100" appName="TestMediation" 
version="*" componentType="http://www.ibm.com/xmlns/prod/websphere/esb/6.0.2:ESBEventMediation" 
componentName="TestMediation" 
elementType="MEDIATION.FLOW.PRIMITIVE" 
elementName="TestMediation:TestMediation:MappingFaultValidation" 
nature="ENTRY" filterId="ProducerFor\_jmsListenerSupplier\_0"/>
This action emits an
entry event for the MappingFaultValidation mediation primitive of the
TestMediation mediation flow component.