# Copying an existing case solution by using the command line

## About this task

You can create a copy of an existing solution in the same
object store. You must specify a new name and solution prefix for
the new solution because these values must be unique.

You can either reuse the existing properties or document classes from the original solution, or
you can select the option to create new properties or document classes when you deploy the new
solution. When you reuse existing properties or document classes in a solution, you cannot redefine
them in Case Builder. You can remove the property or document class
from the solution in Case Builder, but you cannot change any of the
attributes, such as data type.

## Procedure

To copy a solution:

1. Change the current directory to the
install\_root/CaseManagement/configure directory, where
install\_root is the location where Business Automation Workflow is
installed.
2. Generate the text input file by running the following command.
Do not type any line breaks when you enter the command:

configmgr\_cl generate\_input\_sa -operation copy 
 -file input\_file\_name
[-help]

-file input\_file\_name
Specifies the full path to the text input file to create. The
directory structure in the path must exist. You can use any valid
file name, but the .txt extension is recommended.
For example, use -file C:\solutions\copy\_input.txt.

-help 
Optional: Shows a brief message on the command syntax instead of running the command.

For example, the following command creates the C:\solutions\copy\_input.txt
input
file:configmgr\_cl generate\_input\_sa -operation copy 
 -file C:\solutions\copy\_input.txt
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
following command. Do not type any line breaks when you enter the
command:

configmgr\_cl execute\_sa -operation copy 
 -file input\_file\_name