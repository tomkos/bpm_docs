<!-- image -->

# Reference definition

Each reference has a name, used to look up the appropriate service by a client using the client
programming model. In addition to the name, a reference also includes an interface element. The
multiplicity for a reference indicates how many wire definitions can name this reference as the
source. Finally, the wire definition specifies the name of the target service component or import
that resolves the reference.

There are two ways to define references. The first way is to inline the reference in the service
component definition. Using this approach, the references are only available to the service
component in which the references are included. Another approach is to include reference definitions
within the stand-alone references file. For this approach, the references can be used by a non-SCA
client or by another component within the module. For example, a user interface component such as a
JSP might need the ability to invoke a particular service. The client needs a reference so that it
can use the SCA run time to look up the appropriate service to invoke.

Figure 1. Clients can call a service component using either stand-alone or inline references

<!-- image -->

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
       <Method name="getQuote"/>      
     </interface>       
     <wire target="RealtimeService"/>     
   </reference>   
</references>   
<implementation xsi:type="mfc:MediationFlowImplementation" mfcFile="StockQuote\_MediationFlow.mfc"/>
</scdl:component>
```