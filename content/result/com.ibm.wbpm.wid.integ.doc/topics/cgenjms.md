<!-- image -->

# Generic JMS

A generic JMS provider provides a product that supports the Application
Server Facilities (ASF) in the JMS 1.1 specification but does not
support Java Platform, Enterprise Edition Connector Architecture (JCA)
1.5. Some generic JMS products are BEA WebLogic, Oracle Advanced Queuing
(AQ), SonicMQ, TIBCO and webMethods. The generic JMS binding can also
be used with WebSphere® MQ
though not with WebSphere MQ
applications using the Service Integration Bus (SIB) as SIB is a JCA
1.5 JMS provider.

In IBM® Integration
Designer,
the generic JMS binding can be used on imports and exports. In both
cases, an initial binding configuration is required. At run time,
the behavior differs between an import and an export.

An import with a generic JMS binding at run time sends data from
the service-component architecture application to the messaging provider;
that is, the request is made from the service-component architecture
application to the messaging provider. Optionally, the import with
the generic JMS binding may receive data back from the messaging provider
in a response to the request.

An export with an JMS binding at run time listens for a request
from the messaging provider; that is, the request is made from the
messaging provider to the service-component architecture application.
Optionally, the export may send data to the messaging provider in
response to the request.

- Generating a generic JMS import binding

Generating a generic JMS import binding with either a one-way operation or request-response operation is shown in this section. Once generated, the binding properties are discussed.
- Generating a generic JMS export binding

Generating a generic JMS export binding with either a one-way operation or request-response operation is shown. When generated, the binding properties are discussed.
- Limitations of the JMS, MQ JMS and generic JMS bindings

The JMS and MQ JMS bindings have some limitations.

## Related concepts

- Java Message Service (JMS)
- WebSphere MQ Java Message Service (MQ JMS)
- WebSphere MQ (WMQ)

## Related reference

- Mapping a message to an SCA interface
- Recommendations when using messaging bindings
- Language support in non-EIS bindings