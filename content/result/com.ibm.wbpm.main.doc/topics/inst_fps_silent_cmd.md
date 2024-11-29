# Installing IBM Process Federation
Server silently
by using the command line

## Before you begin

- IBM Installation
Manager. If you
are installing Process Federation Server in group mode,
you must use an instance of Installation Manager that is installed in
group mode. For more information, see the Installation Manager IBM Docs topic Group mode roadmaps and silent installation.
- WebSphere® Application
Server Liberty
Network Deployment.
- IBM SDK Java Technology Edition, Version 8

## About this task

1. Optional: Installation Manager is installed or updated
to the appropriate level.
2. The required base products and Process Federation Server are installed.

## Procedure

1. Read and accept the license terms before you install the
product. Adding -acceptLicense to the
command line means that you accept all licenses.
2 Run the following command: extract\_directory \IM64\tools\imcl install list\_of\_package\_IDs -acceptLicense -installationDirectory location -repositories repository -showVerboseProgress -log log\_name .log extract\_directory /IM64/tools/imcl install list\_of\_package\_IDs -acceptLicense -installationDirectory location -repositories repository -showVerboseProgress -log log\_name .log Note: Ifyou already have 32-bit Installation Manager installed,you can run the command from the following directory: Where:

<!-- image -->

```
extract\_directory\IM64\tools\imcl install list\_of\_package\_IDs 
    -acceptLicense -installationDirectory location 
    -repositories repository 
    -showVerboseProgress -log log\_name.log
```

<!-- image -->

<!-- image -->

```
extract\_directory/IM64/tools/imcl install list\_of\_package\_IDs 
    -acceptLicense -installationDirectory location 
    -repositories repository
    -showVerboseProgress -log log\_name.log
```

    - extract\_directory\IM\tools
    - extract\_directory/IM/tools
    - list\_of\_package\_IDs is a list of the IDs forthe products and features that you want to install. You must includethe required features. The syntax is package\_ID ,feature ,feature .Separate multiple products by using spaces.Table 1. Package IDs Product Package ID Feature and description IBM Process FederationServer com.ibm.bpm.pfs.v85 Select the feature that matches the licensefor the Business Automation Workflow partthat you purchased. Important: Select only one feature. WebSphere ApplicationServer Liberty NetworkDeployment com.ibm.websphere.liberty.ND.v85 Draft comment: Steve: you've specifically calledout that liberty is requires...does that mean everything else is optional? IBM InstallationManager com.ibm.cic.agent IBM SDK, Java Technology Edition, Version 8 com.ibm.java.jdk.v8 com.ibm.sdk.8: Required. IBM SDK Java Technology Edition core content.

| Product                                                 | Package ID                       | Feature and description                                                                                                                                                                                                                                                                                                                        |
|---------------------------------------------------------|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IBM Process Federation Server                           | com.ibm.bpm.pfs.v85              | Select the feature that matches the license for the Business Automation Workflow part that you purchased. Important: Select only one feature.  ProcessFederationServerPFS: IBM Business Automation Workflow Server Production license ProcessFederationServerPFS.NonProduction: IBM Business Automation Workflow Server Non-Production license |
| WebSphere Application Server Liberty Network Deployment | com.ibm.websphere.liberty.ND.v85 | Draft comment:  Steve: you've specifically called out that liberty is requires...does that mean everything else is optional?  liberty: Required. WebSphere Application Server Liberty core content. embeddablecontainer: Embeddable EJB container.Important: Do not include  embeddablecontainer for V18.0.0.1 or later.                       |
| IBM Installation Manager                                | com.ibm.cic.agent                | agent\_core: Installation Manager core content. agent\_jre: Installation Manager Java Runtime Environment (JRE)                                                                                                                                                                                                                                  |
| IBM SDK, Java Technology Edition, Version 8             | com.ibm.java.jdk.v8              | com.ibm.sdk.8: Required. IBM SDK Java Technology Edition core content.                                                                                                                                                                                                                                                                         |

- location is the path to the directory where
you want to install the products. To install into an existing supported
instance of WebSphere Application
Server Liberty
Network Deployment, specify its directory. Restriction: Ensure
that the directory names in the path contain only the following characters: 0-9
A-Z a-z (space) & ( ) + - . \_
- repository is the path to the repository where
you extracted the files: extract\_directory\repository\repos\_64bitextract\_directory/repository/repos\_64bitFor
more than one repository, separate the repository locations with commas.
- log\_ name is the name of the log file that
records messages and results.

## Results

## Example

Installs IBM Process Federation
Server, WebSphere Application
Server, Liberty Network
Deployment, and IBM SDK Java Technology Edition Version 8.0 for Liberty on Linux.

```
imcl install com.ibm.bpm.pfs.v85,ProcessFederationServerPFS 
com.ibm.websphere.liberty.ND.v85,liberty com.ibm.java.jdk.v8 -acceptLicense -
installationDirectory /usr/IBM/PFS -repositories /usr/tmp/BPM/repository  -
showVerboseProgress -log silentinstall.log
```

## What to do next

1. Create the Process Federation Server database.
See Creating the Process Federation Server database.
2. Create a process federation server. See Creating a process federation server.