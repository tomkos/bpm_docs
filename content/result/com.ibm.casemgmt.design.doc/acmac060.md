# Generating the object store data map by using the command line

## About this task

The object store data map XML file is in the same XML
format that IBM®
FileNet® Deployment Manager creates
and reads. You can change the destination object stores by using a
text editor.

## Procedure

To generate the object store data map:

1. Change the current directory to the
install\_root/CaseManagement/configure directory, where
install\_root is the location where Business Automation Workflow is
installed.
2. Generate the object store data map
by running the following command. Do not enter any line breaks when
you enter the command.

configmgr\_cl generateObjectStoreDataMap
 -solutionPackage package\_file
 -file datamap\_file
  [-help]

-solutionPackage package\_file
Specifies the full path and file name of the solution package for which you are creating the
data map. If the path includes spaces, put the entire path in double quotation marks. For example,
enter "C:\Solution Packages\Credit Dispute Solution.zip".
-file datamap\_file
Specifies the full path and file name for the data map file to create. The directory structure
in the path exists. You can use any valid file name, but the .xml extension is recommended. If the
path includes a directory name with spaces, put the entire path in double quotation marks. For
example, enter "C:\Solution Packages\datamap.xml".
-help
Optional and displays a brief message on the command syntax instead
of running the command.