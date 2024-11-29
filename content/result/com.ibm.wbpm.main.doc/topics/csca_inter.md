<!-- image -->

# Interfaces

All components have interfaces of the WSDL type. Only Java components support Java-type
interfaces. If a component, import or export, has more than one interface, all interfaces must be
the same type.

```
<?xml version="1.0" encoding="UTF-8"?>
<scdl:component xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  	
     xmlns:mfc="http://www.ibm.com/xmlns/prod/websphere/scdl/mfc/7.0.0"  	
     xmlns:ns1="http://HelloWorldLibrary/HelloWorld" 
     xmlns:ns2="http://HelloService/HelloService"  	
     xmlns:scdl="http://www.ibm.com/xmlns/prod/websphere/scdl/7.0.0"  	
     Xmlns:wsdl="http://www.ibm.com/xmlns/prod/websphere/scdl/wsdl/7.0.0"  	
     displayName="HelloWorldMediation" name="HelloWorldMediation">   
<Interfaces>    
   <interface xsi:type="wsdl:WSDLPortType" portType="ns1:HelloWorld">      
     <scdl:interfaceQualifier xsi:type="scdl:JoinTransaction" value="true"/>  
   </interface>  
</Interfaces> 
<references>     
   <reference name="HelloServicePartner">      
     <interface xsi:type="wsdl:WSDLPortType" portType="ns2:HelloService"/>   
       <scdl:referenceQualifier xsi:type="scdl:SuspendTransaction" value="false"/>       
       <scdl:referenceQualifier xsi:type="scdl:Reliability"/>     
       <scdl:referenceQualifier xsi:type="scdl:DeliverAsyncAt" value="commit"/>       
     <wire target="HelloServiceImport"/>    
   </reference>   
</references>  
<implementation xsi:type="mfc:MediationFlowImplementation" mfcFile="HelloWorldMediation.mfc">     
<scdl:implementationQualifier xsi:type="scdl:Transaction" value="global"/>
```

These interfaces can be specified as either Java interfaces or WSDL port type interfaces.
However, you cannot mix Java and WSDL port type interfaces on the same service component definition.
The arguments and return types for these interfaces are specified as simple Java types, Java
classes, Service DataObjects, or XML Schema (for WSDL port type interfaces).

A component can be called synchronously or asynchronously; this is independent of whether the
implementation is synchronous or asynchronous. The component interfaces are defined in the
synchronous form and asynchronous support is also generated for them. You can specify a preferred
interaction style as synchronous or asynchronous. The asynchronous type advertises to users of the
interface that it contains at least one operation that can take a significant amount of time to
complete. As a consequence, the calling service must avoid keeping a transaction open while waiting
for the operation to complete and send its response. The interaction style applies to all the
operations in the interface.

Components in different modules can be wired together by publishing the services as exports that
have their interfaces and dragging the exports into the required assembly diagram to create imports.
When wiring components, you can also specify quality of service qualifiers on the implementations,
partner references, and interfaces of the component.

Imports have interfaces that are the same as or a subset of the interfaces of the remote service
that they are associated with so that those remote services can be called. Imports are used in an
application in exactly the same way as local components. This provides a uniform assembly model for
all functions, regardless of their locations or implementations. The import binding does not have to
be defined at development time; it can be done at deployment time.

Exports have interfaces that are the same as or a subset of the interfaces of the component that
they are associated with so that the published service can be called. An export dragged from another
module into an assembly diagram automatically creates an import.