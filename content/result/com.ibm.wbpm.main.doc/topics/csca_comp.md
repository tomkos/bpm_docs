<!-- image -->

# Component definition

This figure provides a more detailed look at the service component definition. Each service
component must have a unique name within the SCA module and it must match the file path relative to
the module root. As noted on the previous slide, the service component definition is included in a
file called <SERVICE\_NAME>.component.

Figure 1. Service component definition including component name, implementation, interfaces, and
references

<!-- image -->

Each service component must have a unique name within the SCA module and it must match the file
path relative to the module root. Next, each service component can have one or more interfaces
associated with it, which can be either Java™ or WSDL port type
interface definitions. The interfaces associated with a service component can support either a
synchronous or asynchronous interaction style with clients calling the service.

Each service component can be implemented in various ways, specified by the implementation
definition. Finally, service components can invoke other service components or imports defined in
the current service module. In this case, the appropriate reference must be defined to indicate
which service is used. Often this type of reference is in lined in the service component definition,
although it may alternatively be placed in the stand-alone references file. Each service component
definition can have zero or more references to other services called by the service component being
defined.

```
<?xml version="1.0" encoding="UTF-8"?>
<scdl:component xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"      	
     xmlns:mfc="http://www.ibm.com/xmlns/prod/websphere/scdl/mfc/8.5.0"  	
     xmlns:ns1="http://Resources/StockQuoteService"  	
     xmlns:ns2="http://stockquote.samp.sibx.websphere.ibm.com/DelayedService/"  	
     xmlns:ns3="http://stockquote.samp.sibx.websphere.ibm.com/RealtimeService/"  	
     xmlns:scdl="http://www.ibm.com/xmlns/prod/websphere/scdl/8.5.0"  	
     xmlns:wsdl="http://www.ibm.com/xmlns/prod/websphere/scdl/wsdl/8.5.0"  	
     DisplayName="StockQuote\_MediationFlow" name="StockQuote\_MediationFlow">  
<interfaces>    
   <interface xsi:type="wsdl:WSDLPortType" portType="ns1:StockQuoteService"/>   
</interfaces>  
<references>    
   <reference name="DelayedServicePortTypePartner">       
     <interface xsi:type="wsdl:WSDLPortType" portType="ns2:DelayedServicePortType">        
        <method name="getQuote"/>      
     </interface>     
     <wire target="DelayedService"/>    
   </reference>     
   <reference name="RealtimeServicePortTypePartner">     
     <interface xsi:type="wsdl:WSDLPortType" portType="ns3:RealtimeServicePortType"> 
        <method name="getQuote"/>       
     </interface>      
     <wire target="RealtimeService"/>     
   </reference>  
</references>  
<implementation xsi:type="mfc:MediationFlowImplementation" mfcFile="StockQuote\_MediationFlow.mfc"/>
</Scdl:component>
```