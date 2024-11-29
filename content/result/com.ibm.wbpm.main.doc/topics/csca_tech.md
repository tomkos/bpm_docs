<!-- image -->

# SCA programming techniques

- Runtime rules used for Java to Service Data Objects conversion

To correctly override generated code, or to determine possible runtime exceptions related to Java™ to Service Data Object (SDO) conversions, an understanding of the rules involved is important. The majority of the conversions are straightforward, but there are some complex cases where the runtime provides the best possibility when it converts the generated code.
- Overriding a Service Data Object to Java conversion

Sometimes, the conversion the system creates between a Service Data Object (SDO) and a Java type object may not meet your needs. Use this procedure to replace the default implementation with your own.
- Overriding the generated Service Component Architecture implementation

Sometimes, the conversion the system creates between a Java code and a Service Data Object (SDO) may not meet your needs. Use this procedure to replace the default Service Component Architecture (SCA) implementation with your own.
- Protocol header propagation from non-SCA export bindings

The context service is responsible for propagating the context (including the protocol headers, such as the JMS header, and the user context, such as account ID) along a Service Component Architecture (SCA) invocation path. The context service offers a set of APIs and configurable settings.

<!-- image -->