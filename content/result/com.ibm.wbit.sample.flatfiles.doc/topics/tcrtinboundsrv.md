<!-- image -->

# Create an inbound service

## About this task

To create the inbound service using the adapter
pattern wizard, follow these steps:

## Procedure

1. Right-click SeparateCustomers and
from the context menu, select New > External Service.
The External Service window opens. Expand Adapters
> Flat File. Select Simple: Create an inbound
Flat File service to read from a local file and click Next.
Alternately, switch to SeparateCustomers - Assembly
Diagram and from the palette in the assembly editor, expand Inbound
Adapters.  Select the Flat File adapter
and then click the assembly editor canvas. The External
Service window opens. Expand Adapters > Flat
File. Select Simple: Create an inbound Flat
File service to read from a local file and click Next.
2. The New Inbound Flat File Service page
opens. Change the name to CustomersIn and click Next.
3. The Business object and directory page
opens. Using Browse, navigate to and select
the business object, Customer, you created
earlier. For the directory entry, select the flatfiles\inboundevents directory
where you placed the input file earlier in Create the directories and input file. Click Next.
4. The Input file format and file content split
option page opens. Accept the default input file format,
XML. XML file format is the standard file format used in service-oriented
architecture (SOA) applications to contain a business object. However,
you may also use a custom data handler, which you could have created
earlier or one of the supplied data handlers. A data handler lets
you transform a native input data format, for example, a stream of
bytes, delimited data (such as comma separated values), fixed width
data or JavaScript Object
Notation (JSON) into a business object. Data handlers are discussed
in "Working with data handlers, faults and registries" the information
center and a sample is provided to show how to create one.  Select Split
file content by delimiter. In the field, enter ####;\r\n.
The delimiter is ####. The semi-colon (;) indicates there are more
delimiters after the ####. The \r\n, in the Windows environment, indicates a new line. Linux® users: use ####;\n. Click Next. 
Refer
to the Flat Files documentation on file splitting for more information
and examples.
5. The Archive directory and wrapper business object page
opens. Navigate to the flatfiles\inboundarchive directory
you created earlier. Click Finish. The inbound
service is created. The optional archive directory is
used if you want a record of your processed files. The collection
of files will grow over time so an administrator or an application
would need to regularly move them to auxiliary storage. The wrapper
business object would be used if you need to access the input file
name or event directory.

Some warnings are created. They
will be corrected by completing future steps in this sample.

## Results

The following artifacts are created.

| Artifact   | Name        | Description                                                                                      |
|------------|-------------|--------------------------------------------------------------------------------------------------|
| Export     | CustomersIn | The export exposes the module externally, in this case, to the WebSphere Adapter for Flat Files. |
| Interface  | CustomersIn | This interface contains the operation that can be invoked.                                       |
| Operation  | emit        | emit is the only operation in the interface.                                                     |

Other generated artifacts allow data to be passed transparently
between a service operating in a service-component architecture environment
and another environment. They are the data binding (FlatFileXMLDataBinding)
and the data handler (UTF8XMLDataHandler).