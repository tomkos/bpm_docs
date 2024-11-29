# Uninstalling IBM Process Federation
Server silently

## Before you begin

## About this task

## Procedure

1. Open a command prompt, and change the directory to the /eclipse/tools directory
under Installation Manager.
 Important: If you are running Windows,
start your command prompt by right-clicking and selecting Run
as administrator.
2 Make the appropriate replacements and run the followingcommand: imcl uninstall list\_of\_package\_IDs -installationDirectory installation\_directory -log log\_location -properties optionalProperties

```
imcl uninstall list\_of\_package\_IDs -installationDirectory installation\_directory -log log\_location -properties optionalProperties
```

    1. Replace list\_of\_package\_IDs with
a list of the IDs for the products you want to uninstall, separated
by spaces.  
Table 1. Package IDs

Product
Package ID

 IBM Process Federation
Server
com.ibm.bpm.pfs.v85

WebSphere® Application
Server Liberty
Network Deployment
com.ibm.websphere.liberty.ND.v85

IBM Installation
Manager 
com.ibm.cic.agent

WebSphere SDK Java Technology Edition Version 8.0 for Liberty
com.ibm.websphere.liberty.IBMJAVA.v80
    2. Replace installation\_directory with
the location where you installed the product.
    3. Replace log\_location with
the location and file name to log the information.

## Results

## Example

The following example uninstalls IBM Process Federation
Server, WebSphere Application
Server Liberty Network Deployment, and WebSphere SDK
Java Technology Edition Version 8.0 for Liberty on Linux.

```
C:\Program Files\IBM\Installation Manager\eclipse\tools>imcl uninstall com.ibm.bpm.pfs.v85 com.ibm.websphere.liberty.ND.v85 com.ibm.websphere.liberty.IBMJAVA.v80 -installationDirectory C:\IBM\PFS86 -log uninstalllog.txt
```

## What to do next