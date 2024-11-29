<!-- image -->

# Generic JMS bindings

The service provided through a JMS binding allows a Service Component
Architecture (SCA) module to make calls or receive messages from external
systems. The system can be an external JMS system.

The Generic JMS binding provides integration with non-JCA
1.5-compliant JMS providers that support JMS 1.1 and implement the
optional JMS Application Server Facility. The Generic JMS
binding supports those JMS providers (including Oracle AQ, TIBCO,
SonicMQ, WebMethods, and BEA WebLogic) that do not support JCA 1.5
but do support the Application Server Facility of the JMS 1.1 specification.
The WebSphere® embedded
JMS provider (SIBJMS), which is a JCA 1.5 JMS provider, is not supported
by this binding; when using that provider, use the JMS bindings.

Use this Generic binding when integrating with a non-JCA
1.5-compliant JMS-based system within an SCA environment. The target
external applications can then receive messages and send messages
to integrate with an SCA component.

- Generic JMS bindings overview

Generic JMS bindings are non-JCA JMS bindings that provide connectivity between the Service Component Architecture (SCA) environment and JMS systems that are compliant with JMS 1.1 and that implement the optional JMS Application Server Facility.
- Key features of Generic JMS bindings

The features of the Generic JMS import and export binding are consistent with those of the WebSphere embedded JMS and MQ JMS import bindings. Key features include header definitions and access to existing Java EE resources. However, because of its generic nature, there are no JMS provider-specific connectivity options, and this binding has limited capability to generate resources at deployment and installation.
- Generic JMS headers

Generic JMS headers are Service Data Objects (SDO) that contain all the properties of the Generic JMS message properties. These properties can be from the inbound message or they can be the properties that will be applied to the outbound message.
- Troubleshooting Generic JMS bindings

You can diagnose and fix problems with Generic JMS binding.
- Handling exceptions

The way in which the binding is configured determines how exceptions that are raised by data handlers or data bindings are handled. Additionally, the nature of the mediation flow dictates the behavior of the system when such an exception is thrown.