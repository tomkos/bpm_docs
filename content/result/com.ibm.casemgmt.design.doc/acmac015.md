# Creating a list of object store properties and document classes by using the command
line

## About this task

When you create the list of properties and document classes, the information data is stored in
the PropertyTemplates.csv and DocumentTypes.csv files.
These files are comma-separated value text files that you can open in a spreadsheet program or text
editor.

- Property Template Display Name
- Symbolic Name
- Data Type
- Description
- Cardinality (single value or multi-value choice list)
- Default Value
- Min Value
- Max Value
- Max Length
- Choice List
- Required
- Hidden

- Display Name,
- Symbolic Name
- Descriptive Text
- Is Hidden
- Is Persistent
- Properties (symbolic names of properties associated with this document class)

## Procedure

To create a list of the object store properties and document classes in an object
store:

1. Change the current directory to the
install\_root/CaseManagement/configure directory, where
install\_root is the location where Business Automation Workflow is
installed.
2. Generate the text input file by running the following command.
Do not enter any line breaks when you enter the command:

configmgr\_cl generate\_input\_sa -operation list 
 -file input\_file\_name
  [-silent] [-force] [-help]

-file input\_file\_name
Specifies the full path to the XML input file to create. Restriction: The directory structure in the path must exist.
You can use any valid file name, but the .txt extension
is recommended. For example, use -file C:\propertylist\propertylist.txt.

-silent
Optional: When you specify the -silent parameter, no prompts or
informational messages are shown in the console, but the errors are written to the log. Failure
messages and validation error messages are shown as needed, such as messages about missing passwords
or invalid port numbers. If you run the execute command to run all the activities
in a profile and you specify the -silent parameter, you must also specify the
-force parameter.
-force 
Optional and applies only when the -silent parameter is used. When you
specify the -force parameter, the activity is run without pausing for required
responses to validation error messages, such as messages about missing passwords or invalid port
numbers. 
-help 
Optional: Shows a brief message on the command syntax instead of running the command.

For example, the following command
creates the C:\propertylist\propertylist.XML input
file:configmgr\_cl generate\_input\_sa -operation list 
 -file "C:\propertylist\propertylist.txt" 

The input\_file\_name file
is created.
3 Edit the property values in the input\_file\_name file.
    1. Open the input\_file\_name file
in a text editor.
    2. Provide a value for each property in the file.
For
example, enter the Content Platform Engine server
WSI URL value: 

CEWS\_URI=http://myserver:9080/wsi/FNCEWS40MTOM
    3. Save and close the input file.
4. Apply the values in the text input file by running the
following command. Do not enter any line breaks when you enter the
command:

configmgr\_cl execute\_sa -operation list 
 -file "C:\propertylist\propertylist.txt" 
The two CSV files are created.
5. Provide copies of the CSV files to your business analysts who design solutions in Case Builder.
You can open the CSV files in a text editor, a spreadsheet, or other program to review the
list of available document classes or property templates and their settings.