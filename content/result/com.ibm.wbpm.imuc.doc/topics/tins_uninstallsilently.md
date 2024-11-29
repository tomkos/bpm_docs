# Uninstalling IBM Business Automation Workflow silently

## Before you begin

## About this task

## Procedure

To silently uninstall IBM Business Automation Workflow, complete
the following steps:

1. Open a command prompt, and change directories
to the /eclipse/tools directory under Installation
Manager.  Important: If you are
running Windows, start your command prompt by right-clicking and selecting Run
as administrator.
2 Make the appropriate replacements andrun the following command: imcl uninstall list\_of\_package\_IDs -installationDirectory installationDirectory -log logLocation -properties optionalProperties

```
imcl uninstall list\_of\_package\_IDs -installationDirectory installationDirectory -log logLocation -properties optionalProperties
```

    1. Replace list\_of\_package\_IDs with a list of the IDs for the
products you want to uninstall, separated by spaces. 

Important: The Db2® Standard
Edition
installation might be used by multiple products, including products on a remote system. If you
uninstall Db2, all Db2 databases and database assets are
deleted. 
Table 1. Package IDs

Product
Package ID

IBM Business Automation Workflow
Enterprise
com.ibm.bpm.ADV.v85

IBM Business Automation Workflow
Express
com.ibm.bpm.EXP.v85

IBM Business Automation
Workflow Enterprise Service Bus
com.ibm.bpm.ESB.v85

IBM Process
Designer
com.ibm.bpm.pdesigner.v85 

WebSphere® Application
Server Network
Deployment
com.ibm.websphere.ND.v85

WebSphere Application
Server Network Deployment Linux on POWER
Little Endian (LE)
com.ibm.websphere.ND.le.v85 

Installation Manager
com.ibm.cic.agent

DB2 for Linux 64-bit
com.ibm.ws.DB2EXP.linuxia64

DB2 for Windows 64-bit
com.ibm.ws.DB2EXP.winia64
    2. Replace installationDirectory with
the location where you installed the product.
    3. Replace logLocation with
the location and file name to log the information.

## Results

## Example

The following example uninstalls IBM Business Process Manager
Advanced, WebSphere Application
Server ND, and Db2 from Windows.

```
C:\Program Files\IBM\Installation Manager\eclipse\tools>imcl uninstall com.ibm.bpm.ADV.v85 com.ibm.websphere.ND.v85 com.ibm.ws.DB2EXP.winia64 -installationDirectory C:\IBM\BPM -log uninstalllog.txt
```

## What to do next

## Related reference

- Command-line arguments for the imcl command