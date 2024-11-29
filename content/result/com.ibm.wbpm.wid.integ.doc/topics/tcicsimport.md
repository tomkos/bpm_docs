<!-- image -->

# Creating a CICS import

## Before you begin

## About this task

## Procedure

1. Right-click the module and from the menu select New
> External Service. (Alternately, you could begin by opening
the assembly editor and dragging a CICS outbound
icon on to the canvas.) The External Service window
opens. Select Adapters > CICS from the available
types and click Next.
2. The Select an Adapter page opens.
Select ECIResourceAdapter with the RAR file
version you want to use and click Next. The Adapter
Import page opens with a connector project name, which
you can change. The RAR file has already been discovered and is listed
along with the runtime environment. Click Next.
3. The Service Configuration Properties page
opens. You can use a predefined JNDI name or specify the connection
properties to the CICS server
at this time. Click Next.
4 The Operations page opens where youwill define the operations for the import. Click Add todefine an operation. In the Add Operation wizard,specify an operation name, an input type and, optionally, an outputtype. An input type can be an available one or a new one. In our case,we selected New . This opens the ExternalData Discovery window to the Business ObjectMapping Details page. The different typesof mappings available are listed as follows: Note that each language (C, COBOL or PL/I) has two choicesfor an input mapping. For an output mapping, there are three choices.The differences in these selections are as follows: In our example, we chose COBOL to BusinessObject (CICS Channel) . Then we clicked New andnavigated to a COBOL file. Click Next .
    - C to business object
    - C to business object (CICS Channel)
    - COBOL to business object
    - COBOL to business object (CICS Channel)
    - PL/I to business object
    - PL/I to business object (CICS Channel)
    - A language which will have one output value at run time
    - A language with CICS channel
support. Traditionally, CICS programs
have used communication areas (COMMAREAs) to exchange data. Channels
and containers provide an improved method for transferring data between
programs, in amounts that exceed the 32KB limit that applies to COMMAREAs.
A container is a named block of data that is used to pass information
between programs (it can be thought of as a named COMMAREA). Any number
of containers can be passed between programs through the use of a
channel.
    - For an output mapping only, there can be a language with multiple
outputs, which means at run time one of the outputs will be selected
to return a value.

In our example, we chose COBOL to Business
Object (CICS Channel). Then we clicked New and
navigated to a COBOL file.

Click Next.

5. The Select Data Structures page opens.
Platform and code page are already completed for you, but you can
change them. The platform and properties specified here must be those
of the target platform where the CICS transaction
is running (z/OS®, Windows, and so on). The defaults shown are
taken from the preferences set for the COBOL importer in the preferences
page. To see these preferences, from the menu select Window
> Preferences > Importer > COBOL.  Clicking Advanced reveals
other fields you can change such as the floating-point format. Click Find beside
the Data structures pane. The wizard returns the data structures in
the COBOL file. Select the one you want. Click Finish.
6. You are returned to the Business Object Mapping
Details page. Our selection was in the Containers pane
as we had selected CICS channel
support. Click Next.
7. The Generate Business Objects page
opens. You can choose to change or create a new module at this point.
The name of the generated business object will be the data structure
name if you do not change it. Specifying a folder is recommended since
otherwise all generated files will be in the root module folder, which
will make them difficult to manage. Generation style, which in this
case you will see if you select the container name, lets you choose
several options that can shorten the length of the generated file
names. A CICS channel name
and container name must be specified. Click Finish to
complete the generation of your business objects.
8. The Operation page will let you add
an output type at this point or let you choose to use the input type
for output. In the case of a CICS channel
selection like ours, the input and output must be the same. Click Finish when
your operations have been defined.
9. You are about to complete your service. In the Operations page
of the External Service wizard, you may add more
operations. The function name must be specified. It is the name of
the program that will be run on the CICS server.
You may also specify a maximum length for the commarea. Clicking Advanced provides
other properties for you to override such as the timeout value. Click Next.
10. The Generate Service page opens. You
are at the point where you are about to generate your service. You
can add a folder to contain the generated files. You must enter a
service name. If you want to have the RAR file deployed with the module,
you can select a check box to do so. However, the preferred deployment
method is to configure one instance on the application server. Click Finish.
11. Your service is generated and added to the module. If you
see a message asking if you want to overwrite changes, click Yes.