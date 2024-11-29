# Creating an IMS import

## Before you begin

- You must have access to an IMS host
system.
- You must have the COBOL, C, or PL/I program for the IMS application that you want to invoke.
- You should have an existing module to work with. If not, in the
Business Integration perspective, create one from File > New > Module.

## About this task

## Procedure

1. In the Business Integration perspective, right-click the
module that you want to create an import for and select New >  External Service.  The New External Service window
opens.
2. Select IMS as the type of service
to access and click Next.
3. Select the version of the IMS TM
resource adapter you want to use and click Next.
4. Select IMS COBOL, PL/I or C based application,
and click Next.
5 Specify your security configuration properties setting: For more information about connection properties, see the TM resource adapter information . After you made your selection, clickNext . The Add, Edit, or Remove Operations page opens. It is initiallyempty.
    - If you choose Use predefined connection properties, the JNDI name and
the J2C authentication data entry that you specified do not need to exist on the target server at
this time. They can be created in a later step.
    - If you choose Specify connection properties, you must provide the
TCP/IP host name and port number and the IMS data store
name.

After you made your selection, click
Next.

6 Define the operations and the input and output for eachoperation on the Operations page. For each operationthat you want to create:

1. Click Add to define an operation.
2 Specify the input and output types for the operation.The first time you use this page, there are no input types to choosefrom.
    1. Click New next to the Input type field.
You are asked to provide details for the mapping.
    2. Select the mapping for the Choose mapping field
based on your program.
    3. Click Browse and navigate to your program
file.
    4. Click Next.
3 In the Select Data Structures page,specify the data structure. Tip:

1. For Platform, you must select z/OS for
an import component that runs an IMS transaction.
2. Code page is already completed for you.  You can change it if
your IMS data is in a code page
other than US English (037).
3 Click Advanced to reveal the default settingsfor the z/OS® platform.
    - Most of the values can be accepted without change. However, because
most IMS programs are compiled
with the TRUNC(BIN) option, it is recommended that you change the
value of the Trunc field to BIN.
    - The value for the Quote field might also differ, depending on
your source file.
4. In the Data Structures field, click Find.
The wizard analyzes the data structures in the source program file
and returns them to the pane.
5 Select the data structure you want to work on and click Next .The Generate Business Objects page opens.

- Specifying a folder is recommended because all generated files
will be put in the specified folder rather than the root module folder.
Having a specific folder makes it easier to manage the files.
- The name for the XSD file by default is the data structure name
if you do not change it.
- Generation style lets you specify a variation of generated names,
as indicated by the hover help.
6. Click Finish to complete the specification
of your operation.
7. Repeat the steps for the other data structure, such as the output
message, in this operation if necessary.

- You can specify multiple output messages.
- You can add more operations by repeating step 6.
7 After an operation is created, you can view and set theinteraction properties in the Operations page:

1. Click an operation in the Operations pane. 
The interaction, request type, execution timeout, and
commit mode properties display.
2. Click Advanced if you need to specify other properties. For a
complete description of the properties of IMSInteractionSpec, see the IMS TM resource adapter information in the TM resource adapter information.
3. Click Next when you are finished
specifying the properties.  The Generate Service
page opens.
8 In the Generate Service page, you can specify a folderto contain the generated files. Your service is created and added to the module.

1. Enter the name of the folder.
2. Enter a name in the Name field for the service you are
creating.
3. Click Finish.