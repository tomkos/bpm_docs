# Installing IBM Integration
Designer silently using
the command line

## Before you begin

Operating system and software prerequisite levels are important. Although the
installation process automatically checks for prerequisite operating system patches, review the
system requirements if you have not done so. The system requirements link lists all supported
operating systems and the operating system fixes and patches that you must install to have a
compliant operating system. It also lists the required levels of all prerequisite
software.

## About this task

- Installation Manager
- WebSphere® Application
Server Network Deployment (if you are
installing the test environment)

- Installs Installation Manager if it is not already installed or updates it to the appropriate
level if it is installed.
- Installs the required base products and IBM Integration
Designer.

## Procedure

To silently install IBM Integration
Designer, complete the following steps:

1. Run the following command to generate encrypted passwords that use IBM Installation Manager to
securely connect to Db2.

Important: Start your command prompt by right-clicking and selecting
Run as administrator.
IM\_location\eclipse\tools\imutilsc -silent -nosplash encryptString password\_to\_encrypt
2. Before installing, read and accept the license terms. Adding -acceptLicense to
the command line means that you accept all licenses.
3 Run the following command: Important: Start your command prompt by right-clicking and selectingRun as administrator . extract\_directory \disk1\IM\_win64\tools\imcl install list\_of\_package\_IDs -acceptLicense -installationDirectory location -repositories repository -showVerboseProgress -log logName .log Note: If you installed the 32-bit Installation Manager, then you can run the commandfrom the extract\_directory \IM\_win32\tools directory. Where Running this command installs the product with the default features. If you want toinstall specific features or make other changes, see the reference link for the command-linearguments for imcl.

```
extract\_directory\disk1\IM\_win64\tools\imcl install list\_of\_package\_IDs -acceptLicense 
  -installationDirectory location -repositories repository -showVerboseProgress -log logName.log
```

    - list\_of\_package\_IDs is a list of the IDs for the products that you want to
install, separated by spaces. 
Table 1. Package IDs

Product
Package ID
Feature
Description

IBM Integration
Designer
com.ibm.integration.designer.v85
Required: com.ibm.wid, com.ibm.rad.jre, com.ibm.wid.product,
com.ibm.rad.jee5, com.ibm.rad.was80\_devtools, com.ibm.rad.was85\_devtools, com.ibm.rad.j2c,
com.ibm.rad.birt, com.ibm.rad.transform\_authoring, and com.ibm.rad.pde
Required features

Optional: com.ibm.wid.bpm.stubs
Tools for developing applications without a local server
installation

Optional: com.ibm.wid.adapters.file
Email, Flat File, FTP, and JDBC IBM WebSphere Adapters

Optional: com.ibm.wid.adapters.cics
CICS adapter

Optional: com.ibm.wid.adapters.domino
Domino adapter (deprecated)

Optional com.ibm.wid.adapters.ims
IMS adapter

Optional com.ibm.wid.adapters.jde
JD Edwards adapter

Optional com.ibm.wid.adapters.oracleebs
Oracle adapter

Optional com.ibm.wid.adapters.peoplesoft
PeopleSoft adapter

Optional com.ibm.wid.adapters.sap
SAP adapter

Optional com.ibm.wid.adapters.siebel
Siebel adapter

Optional com.ibm.wid.adapters.wat
WebSphere Adapter Toolkit

Optional com.ibm.wid.adapters.wola
WebSphere Optimized Local adapter

Optional com.ibm.rad.webtools\_core
Web development tools

Optional com.ibm.wid.dev\_tools
Additional development tools

Optional com.ibm.wid.bpmps.user
IBM Workflow
Server environment

Optional com.ibm.wid.bpmpc.user
IBM Business Automation
Workflow environment

Installation Manager
com.ibm.cic.agent
agent\_core
Installation Manager core content

agent\_jre
Installation Manager JRE
    - location is the path to the directory where you want to install the
products.
    - repository is the path to the repository where you have extracted the files,
one or more of the following directories:
extract\_directory/disk1/IM\_win64
extract\_directory/disk1/diskTag.inf For more than one repository,
separate the repository locations with commas.
    - logName is the name of the log file to record messages and results.
4 If you also want to install the test environment , run the same command again with adifferent installation directory and the required package IDs and keys: extract\_directory \disk1\IM\_win64\tools\imcl install list\_of\_package\_IDs -acceptLicense -installationDirectory test\_location -repositories repository -properties key=value,key=value -showVerboseProgress -log logName .log Note: If you installed the 32-bit Installation Manager, then you can run the command from theextract\_directory \IM\_win32\tools directory. Where Running this command installs the test environment with the default features. If youwant to install specific features or make other changes, see the reference link for the command-linearguments for imcl.

```
extract\_directory\disk1\IM\_win64\tools\imcl install list\_of\_package\_IDs 
    -acceptLicense -installationDirectory test\_location -repositories repository 
    -properties key=value,key=value -showVerboseProgress -log logName.log
```

- list\_of\_package\_IDs is a list of the IDs for the products that you want to
install, separated by spaces.
Table 2. Package IDs for test
environment

Product
Package ID
Feature
Description

IBM BPM
Server
com.ibm.bpm.ADV.v85
BPMServer. NonProduction
Development, test, or staging use

WebSphere Application
Server Network Deployment 
com.ibm.websphere.ND.v85
core.feature
Required WebSphere Application Server core content

ejbdeploy
pre-EJB 3.0 modules

thinclient
standalone thin clients and resource adapters

embeddablecontainer
embeddable EJB container

samples
sample applications feature

com.ibm.sdk.8\_64bit

64-bit SDK

Installation Manager
com.ibm.cic.agent
agent\_core
Installation Manager core content

agent\_jre
Installation Manager JRE

Db2 for Windows
com.ibm.ws.DB2EXP.winia64
N/A
Db2 must match the system OS

IBM
Cognos® Analytics
com.ibm.ws.cognos.v1021.winia64
N/A
Must match the system OS
- location is the path to the directory where you want to install the
products.
- repository is the path to the repository where you have extracted the files:
extract\_directory/repository/repos\_64bit For more than one
repository, separate the repository locations with commas.
- key=value is a list of the keys and values that you want to pass to the
installation, which is separated by commas. Do not put spaces between the commas.
Table 3. Keys
for test environment

Key
Description

user.db2.admin.username
Username with authority to access the Db2 database. The default value is
bpmadmin.

user.db2.admin.password
Password for the username above. Choose a password that complies with the
password policy of your system.

user.db2.port 
Port for the Db2 database. The default value is 50000.
- logName is the name of the log file to record messages and results.

## Results

Installation Manager installs the list of products and writes a log file to the directory that
you specified.

## What to do next