<!-- image -->

# Language support in non-EIS bindings

Follow these steps to create business objects from source code, which can be used in your
applications with non-EIS bindings:

1. Right-click your module. Select New > Business Object from External Data.
On the subsequent page, expand Languages and choose a language like COBOL.
Proceed through the wizard, selecting a source file and the data structure that will form the basis
of your business objects. Then generate the business objects.
2. You can see your business objects by using the business object editor. To use them in the
context of a non-EIS binding like JMS, add an import or export to the assembly editor and create an
interface for it. When you create the input and output parameters for an operation on the interface,
use the business objects you just created as types.
3. Add a binding to the import or export, such as JMS, and select the appropriate data format
transformation.

You can use a similar process to create a WebSphere MQ data binding to interact with a CICS
system that was set up with a WebSphere MQ CICS bridge. See Creating a WebSphere MQ data binding for the WebSphere MQ CICS bridge.

## Related concepts

- Java Message Service (JMS)
- WebSphere MQ Java Message Service (MQ JMS)
- Generic JMS
- WebSphere MQ (WMQ)

## Related reference

- Mapping a message to an SCA interface
- Recommendations when using messaging bindings