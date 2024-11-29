<!-- image -->

# Uninstalling IBM Integration
Designer silently
using the command line

## Before you begin

## About this task

## Procedure

To uninstall IBM Integration
Designer using
the command line, complete the following steps:

1. Open a command prompt, and change directories
to the /eclipse/tools directory under Installation
Manager.  Important: If you are
running Windows, start your command prompt by right-clicking and selecting Run
as administrator.
2 Make the appropriate replacements andrun the following command: imcl uninstall list\_of\_package\_IDs -installationDirectory installationDirectory -log logLocation

```
imcl uninstall list\_of\_package\_IDs -installationDirectory installationDirectory -log logLocation
```

    1. Replace list\_of\_package\_IDs with a list of the IDs for the
products you want to uninstall, separated by spaces. 

Table 1. Package IDs

Product
Package ID

IBM Integration
Designer
com.ibm.integration.designer.v85

Installation Manager
com.ibm.cic.agent
    2. Replace installationDirectory with
the location where you installed the product.
    3. Replace logLocation with
the location and file name to log the information.
3 If you also want to uninstall the testenvironment , make the appropriate replacements and run the samecommand again: imcl uninstall list\_of\_package\_IDs -installationDirectory testInstallationDirectory -log logLocation

```
imcl uninstall list\_of\_package\_IDs -installationDirectory testInstallationDirectory -log logLocation
```

1. Replace list\_of\_package\_IDs with a list of the IDs for the
products you want to uninstall, separated by spaces. 

Important: The Db2®
installation might be used by multiple products, including products on a remote system. If you
uninstall Db2, all Db2 databases and database assets are
deleted. 
Table 2. Package IDs for test environment

Product
Package ID

Business Automation Workflow
com.ibm.bpm.ADV.v85

WebSphere® Application
Server Network
Deployment
com.ibm.websphere.ND.v85

Db2 for Linux 64-bit
com.ibm.ws.DB2EXP.linuxia64

Db2 for Windows 64-bit
com.ibm.ws.DB2EXP.winia64

IBM
Cognos® Analytics for
Windows
com.ibm.ws.cognos.v1021.winia64
2. Replace installationDirectory with
the location where you installed the product.
3. Replace logLocation with
the location and file name to log the information.

## Results