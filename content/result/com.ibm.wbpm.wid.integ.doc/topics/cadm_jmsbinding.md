<!-- image -->

# JMS bindings

JMS bindings can be used when you interact with the Service Integration
Bus (SIB) provider binding, and are compliant with JMS and JCA 1.5.

You can use the JMS export and import bindings  a Service
Component Architecture (SCA) module to make calls to, and receive
messages from, external JMS systems.

The JMS import and export bindings provide integration with JMS
applications using the JCA 1.5-based SIB JMS provider that is part
of WebSphere® Application
Server. Other JCA 1.5-based JMS resource adapters are not supported

- JMS bindings overview

JMS bindings provide connectivity between the Service Component Architecture (SCA) environment and JMS systems.
- JMS integration and resource adapters

 The Java Message Service (JMS) provides integration through an available JMS JCA 1.5-based resource adapter. Complete support for JMS integration is provided for the Service Integration Bus (SIB) JMS resource adapter.
- JMS import and export bindings

You can make SCA modules interact with services provided by external JMS applications using JMS import and export bindings.
- JMS headers

A JMS message contains two types of headers-the JMS system header and multiple JMS properties. Both types of headers can be accessed either in a mediation module in the Service Message Object (SMO) or by using the ContextService API.
- JMS temporary dynamic response destination correlation scheme

The temporary dynamic response destination correlation scheme causes a unique dynamic queue or topic to be created for each request sent.
- External clients

The server can send messages to, or receive messages from, external clients using JMS bindings.
- Troubleshooting JMS bindings

You can diagnose and fix problems with JMS bindings.
- Handling exceptions

The way in which the binding is configured determines how exceptions that are raised by data handlers or data bindings are handled. Additionally, the nature of the mediation flow dictates the behavior of the system when such an exception is thrown.