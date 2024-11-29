<!-- image -->

# Create an outbound service

## About this task

To create the outbound service using the adapter pattern
wizard, follow these steps:

## Procedure

1. Right-click SeparateCustomers and
from the context menu, select New > External Service.
The External Service window opens. Expand Adapters
> Flat File. Select Simple: Create an outbound
Flat File service to write to a local file and click Next.
Alternately, switch to SeparateCustomers - Assembly
Diagram and from the palette in the assembly editor, expand Outbound
Adapters.  Select the Flat File adapter
and then click the assembly editor canvas. The External
Service window opens. Expand Adapters > Flat
File. Select Simple: Create an outbound Flat
File service to write to a local file and click Next.
2. The New Outbound Flat File Service page
opens. Change the name to SeparateCustomerOut and
click Next.
3. The Business object and output directory page
opens. Using Browse, navigate to and select
the business object, Customer, you created
earlier. For the directory entry, select the flatfiles\outputdir output
directory you created earlier in Create the directories and input file. Click Next.
4. The Output file name page opens. A
variety of ways can be used to create an output file name. Accept
the defaults, which will result in output files for each customer
record in the format Customer.<number of customer record>.txt.
The Customer.seq file will contain the number
of customer records processed.  Generating a random
file name is useful if your application requires unique generated
output file names. If your application will specify the business object
name then select Use a wrapper business object to specify
the output file name. In that case, you can also select
an append operation for writing all business objects to a single file
rather than multiple files. 
Click Next.
5. The Output file format page opens.
Accept the default, XML, and click Finish. 
As discussed in Create an inbound service,
XML is a standard file format in SOA applications. However, there
can be cases where the native data is in another format such as a
stream of bytes, delimited data (such as comma separated values),
fixed width data or JavaScript Object
Notation (JSON). In these cases, you can browse to select the data
handler. Data handlers are discussed in "Working with data handlers,
faults and registries" in the information center and a sample is provided
to show how to create one.

## Results

The following artifacts are created.

| Artifact                            | Name                                                                                      | Description                                                                                                                                                                                                                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Import                              | SeparateCustomerOut                                                                       | The import lets your service use the WebSphere Adapter for Flat Files to output files.                                                                                                                                                                                                          |
| Business objects                    | CreateResponse, UnstructuredContent                                                       | CreateResponse, which will be used in creating the output of the application, uses the Customer business object as its input. The UnstructuredContent business object can be used for generic input types.                                                                                      |
| Business objects for fault handling | DuplicateRecordFault, MissingDataFault, PrimaryKeyPairType, RecordNotFoundFault, WBIFault | These business objects can be used to handle exceptions. When a business exception is thrown, the adapter throws a fault exception and passes the fault information to the calling component. If you want to use this information, you will need to create a fault selector configuration file. |
| Interface                           | SeparateCustomerOut                                                                       | This interface contains the operation that can be invoked.                                                                                                                                                                                                                                      |
| Operation                           | create                                                                                    | This operation creates the files in the output directory.                                                                                                                                                                                                                                       |

For our particular application, we will only be using
a one-way inbound request and do not require fault handling. In the
following steps, we will remove the faults from the import binding
and the interface.

1. Select SeparateCustomerOut in the assembly
editor and then select the Faults Configuration tab
in the Properties view.
2. Select Default Fault Configuration.  In
the panel to the right, click Clear.
3. Expand Default Fault Configuration and
the create operation beneath it. Select MISSING\_DATA.
In the panel to the right, click Clear.
4. Repeat the previous step for DUPLICATE\_RECORD and RECORD\_NOT\_FOUND.
5. Save your changes. From the menu, select File > Save.
Close the assembly editor.

1. Expand Interfaces in the Business
Integration view. Double-click SeparateCustomerOut to
open the interface editor.
2. Click MISSING\_DATA fault. Then select the Delete icon.
It is on the top of the editor on the right.
3. Similarly, delete DUPLICATE\_RECORD and RECORD\_NOT\_FOUND faults.
4. Save your changes. From the menu, select File > Save.Close
the interface editor.