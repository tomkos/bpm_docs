<!-- image -->

# Installing fix packs for IBM Integration
Designer silently

## Procedure

To update IBM Integration
Designer silently,
complete the following steps:

1. Read and accept the license terms before
updating. Adding -acceptLicense to the command line
means that you accept all licenses.
2 Start your command prompt by right-clicking and selecting Run asadministrator : extract\_directory \disk1\IM\_win64\tools\imcl install com.ibm.integration.designer.v85 -acceptLicense -installationDirectory location -repositories repository -showVerboseProgress -log logName .log where

```
extract\_directory\disk1\IM\_win64\tools\imcl install com.ibm.integration.designer.v85
    -acceptLicense -installationDirectory location -repositories repository 
    -showVerboseProgress -log logName.log
```

    - location is the path to the directory where you want to update the
products.
    - repository is the path to the repository where you have extracted the fix
pack files. For more than one repository, separate the repository locations with commas.
    - logName is the name of the log file to record messages and results.
3 If you also want to update the test environment, run the same command again with the correctinstallation directory and the required package IDs: extract\_directory \disk1\IM\_win64\tools\imcl install list\_of\_package\_IDs -acceptLicense -installationDirectory test\_location -repositories repository -showVerboseProgress -log logName .log where

```
extract\_directory\disk1\IM\_win64\tools\imcl install list\_of\_package\_IDs -acceptLicense 
    -installationDirectory test\_location -repositories repository -showVerboseProgress 
    -log logName.log
```

- list\_of\_package\_IDs is a list of the IDs for the products you want to update,
separated by spaces.
Table 1. Package IDs for test environment

Product
Package ID

IBM Business Automation Workflow
Enterprise
com.ibm.bpm.PS.v85

WebSphere® Application
Server Network
Deployment
com.ibm.websphere.ND.v85
- location is the path to the directory where you want to update the
products.
- repository is the path to the repository where you have extracted the fix
pack files. For more than one repository, separate the repository locations with commas.
- logName is the name of the log file to record messages and results.

## Results

IBM Installation
Manager updates the list of products
and writes a log file to the directory that you specified.

## Example

The following example updates IBM Integration
Designer:

```
imcl install com.ibm.integration.designer.v85 -acceptLicense 
    -installationDirectory C:\IBM\IID\v18.0 -repositories D:\temp\IID\Fixpack1 
    -showVerboseProgress -log update.log
```