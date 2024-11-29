<!-- image -->

# Generic JMS binding event code example

## Generic JMS binding event

```
<wbi:event
xmlns:wbi="http://www.ibm.com/xmlns/prod/websphere/monitoring/6.1"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"
xmlns:binding="http://www.ibm.com/xmlns/prod/websphere/scdl/6.0.0:Binding">
<wbi:eventHeaderData>
<wbi:WBISESSION\_ID>9.115.71.147;TestGenJMSClt;Import1;operation3;1311156316324;520298243</wbi:WBISESSION\_ID>
<wbi:ECSCurrentID>9.115.71.147;TestGenJMSClt;TestIntfPartner;Import1;operation3;1311156316324;520298243
</wbi:ECSCurrentID>
<wbi:ECSParentID>9.115.71.147;TestGenJMSClt;Import1;operation3;1311156316324;520298243</wbi:ECSParentID>
<wbi:WBIEventVersion>6.1</wbi:WBIEventVersion>
</wbi:eventHeaderData>
<wbi:eventPointData xsi:type="binding:WBI.SCA.JMSBINDING.EXIT">
<wbi:eventNature>EXIT</wbi:eventNature>
<wbi:payloadType>bogus</wbi:payloadType>
<binding:MODULE\_NAME>TestGenJMSClt</binding:MODULE\_NAME>
<binding:BINDING\_NAME>Import1</binding:BINDING\_NAME>
<binding:OPERATION\_NAME>operation3</binding:OPERATION\_NAME>
<binding:BINDING\_TYPE>Import</binding:BINDING\_TYPE>
<binding:BINDING\_PROTOCOL>JMS</binding:BINDING\_PROTOCOL>
<binding:DESTINATION>queue:///BDRQ?version=6</binding:DESTINATION>
<binding:REPLY\_DESTINATION>queue:///BDSQ?version=6</binding:REPLY\_DESTINATION>
<binding:CALLBACK\_DESTINATION>queue://TestGenJMSClt.Import1\_GENJMS\_CALLBACK\_D\_SIB?busName
=SCA.SYSTEM.WIN-1OPBE8FWO28Node01Cell.Bus</binding:CALLBACK\_DESTINATION>
<binding:DIRECTION>REQUEST</binding:DIRECTION>
<binding:JMS\_TYPE>GenericJMS</binding:JMS\_TYPE>
<binding:DATABINDING\_NAME>com.ibm.wsspi.sca.jms.data.JMSDataHandlerBindingImpl</binding:DATABINDING\_NAME>
<binding:MESSAGE\_ID>ID:414d5120513238382020202020202020637c264e20034307</binding:MESSAGE\_ID>
<binding:CORRELATION\_ID>ID:414d5120513238382020202020202020637c264e20034307</binding:CORRELATION\_ID>
</wbi:eventPointData>
</wbi:event>
```