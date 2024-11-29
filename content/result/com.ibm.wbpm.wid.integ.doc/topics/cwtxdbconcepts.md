<!-- image -->

# WTX data handler concepts

## WTX data handler and IBM Integration
Designer servers

The WTX data handler communicates with Websphere Transformation Extender over JNI since Websphere Transformation Extender is a C++ product. As a result, the WTX data handler runs in the same process space as Websphere Business Automation Workflow or WebSphere® Enterprise
Service Bus.

## WTX maps

The WebSphere Transformation
Extender Data Binding invokes a WebSphere Transformation
Extender map in order to perform the transformation. The map provides
the system with the details of conversion from one format to another.
The WTX data handler determines what map to call based
on the configuration properties on the data binding or the data binding
descriptor which is described in the runtime documentation. When converting
native data like Electronic Data Interchange (EDI), for example, to
data object, the map must be built with the input card from EDI and
the output card based on XML Schema.  When converting data object
to native data, the map must be built with the input card based on
XML Schema and output card based on native data.