# Installing fix packs silently

## Before you begin

Visit the IBM
Support website to check for available fix packs and interim
fixes.

1. Read the fix pack documentation thoroughly. The documentation
lists dependencies, such as WebSphere® Application
Server fix pack levels or other IBM product
fixes that you must install before you apply the fix pack.
2. To ensure that your implementation is performing the same way
that it did before you applied the fix pack, prepare a regression
test plan.
3. Back up your databases and profiles.
4. Before you deploy the fix pack to a production environment, install
the fix pack in a development or quality-assurance environment.
5. You must perform the installation
using the same user account that you used to install the product packages.

## About this task

You cannot use this procedure to install updates on the
underlying IBM Db2® Standard
Edition. You must update
Db2 by following its normal update
process.

## Procedure

To add a fix pack to Business Automation Workflow silently,
complete the following steps:

1. Read the license terms before updating.
Adding -acceptLicense to the command line means that
you accept all license terms. If you do not accept the
license, you cannot perform the installation.
2 Run the following command: Important: On Windows, start your command prompt by right-clickingand selecting Run as administrator . extract\_directory \IM64\tools\imcl install list\_of\_package\_IDs -acceptLicense -installationDirectory location -repositories repository -showVerboseProgress -log logName .log extract\_directory /IM64/tools/imcl install list\_of\_package\_IDs -acceptLicense -installationDirectory location -repositories repository -showVerboseProgress -log logName .log where:

<!-- image -->

```
extract\_directory\IM64\tools\imcl install list\_of\_package\_IDs -acceptLicense -installationDirectory location -repositories repository -showVerboseProgress -log logName.log
```

<!-- image -->

<!-- image -->

```
extract\_directory/IM64/tools/imcl install list\_of\_package\_IDs -acceptLicense -installationDirectory location -repositories repository -showVerboseProgress -log logName.log
```

    - list\_of\_package\_IDs is a list of the IDs for the products you want to update,
separated by spaces.
Table 1. Package IDs

Product
Package ID

IBM Business Automation Workflow
Enterprise
com.ibm.bpm.ADV.v85

IBM Business Automation
Workflow Enterprise Service Bus
com.ibm.bpm.ESB.v85

WebSphere Application
Server Network
Deployment
com.ibm.websphere.ND.v85

WebSphere Application
Server Network Deployment Linux on POWER
Little Endian (LE)
com.ibm.websphere.ND.le.v85
    - extract\_directory is the path to where you extracted the fix pack files.
    - location is the path to the directory where you want to update the
products.
    - repository is the path to the repository where you have extracted the fix
pack files. For more than one repository, separate the repository locations with commas.
    - logName is the name of the log file to record messages and results.

## Results

Installation Manager updates the list of products
and writes a log file to the directory that you specified.

## Example

The following example updates IBM Business Automation Workflow on
Windows.

```
imcl install com.ibm.bpm.ADV.v85 com.ibm.websphere.ND.v85 -acceptLicense -installationDirectory C:\IBM\BPM -repositories D:\temp\BPM856\repository,D:\temp\WAS8552\repository showVerboseProgress -log silentinstall.log
```

## Related information

- IBM Installation Manager documentation
- Command-line arguments for the imcl command