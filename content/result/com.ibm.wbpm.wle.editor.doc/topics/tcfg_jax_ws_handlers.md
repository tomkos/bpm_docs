# Registering custom JAX-WS handlers

## Procedure

To register a custom JAX-WS handler for SSO or technical
user scenarios, complete the following steps:

1. Create a class that implements the javax.xml.ws.handler.soap.SOAPHandler interface
and, optionally, implements the com.ibm.bpm.integration.client.interfaces.handler.BPMHandler interface,
which is in APPSERVER\_ROOT\plugins\com.ibm.bpm.integration.client.interfaces.jar.
The com.ibm.bpm.integration.client.interfaces.handler.BPMHandler interface
defines the single public void init(Properties p) method.
If a handler implements both interfaces, IBM Business Automation
Workflow calls
the init(...) method and passes custom properties
that are configured as part of the BPMCustomCmisHandler WCCM
configuration object (see step 3).  Creating this class
allows cluster-wide consistent configuration for custom JAX-WS handlers,
including scripting support, without the need to maintain numerous
property files. Your custom JAX-WS handler implementation gives you
access to the following context parameters:String userId = (String) messageContext.get(BindingProvider.USERNAME\_PROPERTY);
String password = (String) messageContext.get(BindingProvider.PASSWORD\_PROPERTY);
String endpointAdress = (String) messageContext.get(BindingProvider.ENDPOINT\_ADDRESS\_PROPERTY);
String repositoryId = (String) messageContext.get(BPMHandler.REPOSITORY\_ID\_PROPERTY);
String uniqueRepositoryId = (String) messageContext.get(BPMHandler.UNIQUE\_REPOSITORY\_ID\_PROPERTY);Tip: You can find sample implementations of a JAX-WS handler
at APPSERVER\_ROOT/BPM/samples/integration-clients-samples-src.jar.
2. Create a Java Archive (JAR) file that contains your JAX-WS
handler implementation. Copy this JAR file into the APPSERVER\_ROOT/lib/ext directory
on all nodes of your Business Automation Workflow system.
3. Create a BPMCustomCmisHandler configuration
object in either cmisSsoJaxWsHandlers or cmisTechnicalUserJaxWsHandlers.
The following attributes are relevant to this object type:

Attribute name
Description

className
Fully qualified class name of your JAX-WS handler
implementation

weight
A weight to define the sequence in which the
JAX-WS handlers are started. The default weight is 0.

Note: IBM Business Automation
Workflow handlers
start first. During outbound processing (request), the sequence is
low to high. During inbound processing (response), the sequence is
high to low.
4. On the deployment manager, start the wsadmin tool:
wsadmin -lang jython -conntype NONE
5 Locate the parent configuration object.
    - IBM Workflow
Center (where
application\_cluster\_name is the name of the application cluster in the deployment
environment):
bpdServer = AdminConfig.getid("/Cell:/ServerCluster:application\_cluster\_name
/BPMClusterConfigExtension:/BPMProcessCenter:/")
    - IBM Workflow
Server (where
application\_cluster\_name is the name of the application cluster in the deployment
environment):bpdServer = AdminConfig.getid("/Cell:/ServerCluster:application\_cluster\_name
/BPMClusterConfigExtension:/BPMProcessServer:/")
6 Optionally, create a handler object in the cmisSsoJaxWsHandlers listfor SSO scenarios: ssoHandler0=AdminConfig.create('BPMCustomCmisHandler',bpdServer,[['className','com.ibm.bpm.samples.CustomBPMHandlerSample'],['weight',0]],'cmisSsoJaxWsHandlers')

```
ssoHandler0=AdminConfig.create('BPMCustomCmisHandler',bpdServer,[['className','com.ibm.bpm.samples.CustomBPMHandlerSample'],
['weight',0]],'cmisSsoJaxWsHandlers')
```

1. Add custom properties. ssoProperty0=AdminConfig.create('BPMProperty',ssoHandler0,[['name','name0'],['value','value0']],'customProperties')
ssoProperty00=AdminConfig.create('BPMProperty',ssoHandler0,[['name','name00'],['value','value00']],'customProperties')
2. Repeat step 3a if you are registering multiple
handlers, for examplessoHandler1=AdminConfig.create('BPMCustomCmisHandler',bpdServer,[['className','com.ibm.bpm.samples.CustomHandlerSample'],
['weight',1]],'cmisSsoJaxWsHandlers')
ssoHandler2=AdminConfig.create('BPMCustomCmisHandler',bpdServer,[['className','com.ibm.bpm.samples.CustomBPMHandlerPerformanceSample'],
['weight',1]],'cmisSsoJaxWsHandlers')
ssoProperty2=AdminConfig.create('BPMProperty',ssoHandler2,[['name','Logfile'],['value','C:\performanceLog1.log']],'customProperties')
ssoHandler3=AdminConfig.create('BPMCustomCmisHandler',bpdServer,[['className','com.ibm.bpm.samples.CustomBPMHandlerCmisSSO'],
['weight',2]],'cmisSsoJaxWsHandlers')
ssoProperty3=AdminConfig.create('BPMProperty',ssoHandler3,[['name','Logfile'],['value','C:\CmisSSO1.log']],'customProperties')
7 Create a handler object in the cmisTechnicalUserJaxWsHandlers listfor technical scenarios: techUserHandler0=AdminConfig.create('BPMCustomCmisHandler',bpdServer,[['className','com.ibm.bpm.samples.CustomBPMHandlerSample'],['weight',0]],'cmisTechnicalUserJaxWsHandlers')

```
techUserHandler0=AdminConfig.create('BPMCustomCmisHandler',bpdServer,[['className','com.ibm.bpm.samples.CustomBPMHandlerSample'],
['weight',0]],'cmisTechnicalUserJaxWsHandlers')
```

1. Add custom properties.techProperty0=AdminConfig.create('BPMProperty',techUserHandler0,[['name','name0'],['value','value0']],'customProperties')
techProperty00=AdminConfig.create('BPMProperty',techUserHandler0,[['name','name00'],['value','value00']],'customProperties')
2. Repeat step 4a if you are registering multiple
handlers, for example techUserHandler1=AdminConfig.create('BPMCustomCmisHandler',bpdServer,[['className','com.ibm.bpm.samples.CustomHandlerSample'],
['weight',1]],'cmisTechnicalUserJaxWsHandlers')
techUserHandler2=AdminConfig.create('BPMCustomCmisHandler',bpdServer,[['className','com.ibm.bpm.samples.
CustomBPMHandlerPerformanceSample'],['weight',2]],'cmisTechnicalUserJaxWsHandlers')
techProperty2=AdminConfig.create('BPMProperty',techUserHandler2,[['name','Logfile'],['value','C:\performanceLog2.log']],
'customProperties')
techUserHandler3=AdminConfig.create('BPMCustomCmisHandler',bpdServer,[['className','com.ibm.bpm.samples.
CustomBPMHandlerCmisTechnicalUser'],['weight',3]],'cmisTechnicalUserJaxWsHandlers')
techProperty3=AdminConfig.create('BPMProperty',techUserHandler3,[['name','Logfile'],['value','C:\CmisTechUser.log']],
'customProperties')
8. Save your changes by running the following command: AdminConfig.save().
9. Synchronize the changes and restart the application servers.