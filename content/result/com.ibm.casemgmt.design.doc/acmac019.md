# Converting a solution to a template by using the command line

## About this task

## Procedure

To convert a solution to a template:

1. Change the current directory to the
install\_root/CaseManagement/configure directory, where
install\_root is the location where Business Automation Workflow is
installed.
2. Generate the text input file by running the following command.
Do not enter any line breaks when you enter the command:

configmgr\_cl generate\_input\_sa -operation convertToTemplate 
 -file input\_file\_name
  [-help]

-file input\_file\_name
Specifies the full path to the text input file to create. The
directory structure in the path must exist. You can use any valid
file name, but the .txt extension is recommended.
For example, use -file C:\solutions\to\_template\_input.txt.

-help 
Optional: Shows a brief message on the command syntax instead of running the command.

For example, the following command
creates the C:\solutions\to\_template\_input.txt input
file:configmgr\_cl generate\_input\_sa -operation createFromTemplate 
 -file C:\solutions\to\_template\_input.txt
3 Edit the property values in the input\_file\_name file.
    1. Open the input\_file\_name file
in a text editor.
    2. Provide a value for each property in the file.
For
example, enter the Content Platform Engine server
WSI URL value: 

CEWS\_URI=http://myserver:9080/wsi/FNCEWS40MTOMYou
can specify whether unique identifiers are preserved by providing
a value for the preserveIdentifier property. The default setting is preserveIdentifier=false. 

Important: For most solutions, do not change the default setting.
However, if this solution contains assets that are not managed by Case Builder, such as forms or search
templates whose unique identifiers are referenced by non-IBM® Business Automation
Workflow programs, you might want
the identifiers to be preserved. If you enter preserveIdentifier=true,
do not deploy more than one solution that is made from this template
to the same target object store.
    3. Save and close the input file.
4. Apply the values in the text input file by running the
following command. Do not type any line breaks when you enter the
command:

configmgr\_cl execute\_sa -operation convertToTemplate 
 -file input\_file\_name