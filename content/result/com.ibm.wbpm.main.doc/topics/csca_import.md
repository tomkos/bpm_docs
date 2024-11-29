<!-- image -->

# Import definition

Like service components, imports have a name and a set of 1..N interfaces with which they are
associated. Imports also have a binding attribute, which is used to describe how the external
service is bound to the current module.

Imports can be thought of as a special type of service component in an SCA module. Imports are
valid targets in a wire definition for a service reference. This means that to a client invoking a
target service, the client programming model is the same whether the reference points to an import
or another service component.

```
<?xml version="1.0" encoding="UTF-8"?>
<scdl:import xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  	
     xmlns:ns1="http://stockquote.samp.sibx.websphere.ibm.com/DelayedService/"  	
     xmlns:scdl="http://www.ibm.com/xmlns/prod/websphere/scdl/8.5.0"  	
     xmlns:webservice="http://www.ibm.com/xmlns/prod/websphere/scdl/webservice/8.5.0"  	
     xmlns:wsdl="http://www.ibm.com/xmlns/prod/websphere/scdl/wsdl/8.5.0"  	
     displayName="DelayedService" name="DelayedService">   
<interfaces>     
   <interface xsi:type="wsdl:WSDLPortType" portType="ns1:DelayedServicePortType">       
     <method name="getQuote"/>     
   </interface>  
</interfaces>   
<esbBinding xsi:type="webservice:WebServiceImportBinding"    	
   endpoint="http://localhost:9080/DelayedService/services/DelayedServiceSOAP"    	
   port="ns1:DelayedServiceSOAP" service="ns1:DelayedService"/>
</scdl:import>
```