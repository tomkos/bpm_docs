<!-- image -->

# WebSphere MQ (WMQ)

This section examines the WMQ programming model. The section then
shows how a WMQ message maps to Service Component Architecture (SCA)
artifacts; that is, how a message maps to a business object and how
input and output from a WMQ client maps to an interface's operations.
Data bindings and an important function called the function selector
as applied to WMQ are discussed. You are then led through the generation
of an MQ import and export binding.

- WebSphere MQ programming model

The WebSphere MQ programming model is discussed in this section.
- MQ and MQ JMS features

Several features of MQ and MQ JMS bindings and how SCA artifacts work with them are discussed.
- Working with MQ bindings

MQ bindings can be generated for imports and exports with either a one-way type of operation or request-response type of operation. All cases are discussed in this section.
- MQ data bindings

The MQ data bindings are discussed in this section.
- Creating a WebSphere MQ data binding for the WebSphere MQ CICS bridge

You can use a WebSphere MQ data binding to interact with a CICS system that was set up with a WebSphere MQ CICS bridge. This WebSphere MQ data binding saves you from hand-coding your own binding.
- Example of custom MQ data bindings

Data bindings convert a message to or from an Service Data Object (SDO) or business object data format to or from a native format. For example, a data binding could convert a business object used to represent making a credit to a bank account to a Java data structure containing the same information but in a Java context. IBM Integration Designer offers many data bindings which are documented in the sections, generating an import or export. In many cases, these standard bindings will be sufficient but in some cases you may want to write your own custom data binding to suit the needs of a particular application. In this section, we show you how to create custom MQ data bindings.
- Configuration for CICS programs

For the MQ binding to invoke a Customer Information Control System (CICS®) program, you will need to configure some header fields specific to CICS.
- Configuration for IMS programs

For the MQ binding to invoke an Information Management (IMS) program, you will need to configure some header fields specific to IMS.
- MQ imports and exports at run time

The sequence of the methods used at run time is discussed.
- Limitations of the MQ binding

The MQ binding has a limitation in its use that is listed here.

## Related concepts

- Java Message Service (JMS)
- WebSphere MQ Java Message Service (MQ JMS)
- Generic JMS

## Related reference

- Mapping a message to an SCA interface
- Recommendations when using messaging bindings
- Language support in non-EIS bindings