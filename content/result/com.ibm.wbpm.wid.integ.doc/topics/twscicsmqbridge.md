<!-- image -->

# Creating a WebSphere MQ data binding for the WebSphere MQ CICS
bridge

## Before you begin

Your system administrator must set up the WebSphere MQ
CICS bridge. Then, your system administrator must provide you with
the message queue names and other connection information that the
WebSphere MQ binding configuration requires.

## Procedure

1 Begin by using a utility that examines the data structuresfrom a source language file that your application is working with.Using this information, the utility generates a business object ofthe DFHCOMMAREA that CICS uses to transfer data between programs.The utility also generates the marshalling and unmarshalling code.This code handles the transformation of data between the XML representationof the data and the source language representation of the data.
    1. Right-click your module in the navigation and select New > Business Object from External
Data. Select the language that your application
is working with: COBOL, PL/I, or C. You can also select if your application
uses a channel or has multiple outputs. Then, select the source file.
    2. In the Select Data Structures dialog,
select the data structure that you want to use. You can also select
other options like the code page.
    3. Then, select the name and location of the new business
object and generate the business object. Repeat this process if you
need other business objects. The process is also contained
in Language support in non-EIS bindings.
2. Create an interface that uses the business object or business
objects as types for the input and output parameters.
3 Generate a WebSphere MQ import binding with the interfaceyou created and the information that is provided by your system administrator.

1. In the Assembly Diagram, drag a WebSphere MQ import
from the palette to the canvas. The WebSphere MQ import is found under Outbound
Imports.
2. On the next page, select the interface that you created
and click Next.
3. In the Configure MQ Import Binding page,
enter the information from your system administrator in the End-point
Configuration section. If you are specifying your own configuration,
then enter the queue names and host name in the fields provided. Were
JNDI names provided for the WebSphere MQ connection factory, send
queue, WebSphere MQ ActivationSpec, and receive queue? If so, then
select the option that uses JNDI names and enter the information in
the appropriate fields.
4. In the Data Format section, select MQ adapter
language data binding generator for the Default request
data format and the Default response data format. Click Finish.