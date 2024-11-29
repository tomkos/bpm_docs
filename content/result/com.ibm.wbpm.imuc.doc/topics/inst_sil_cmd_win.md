# Installing silently using the command line

## Before you begin

- IBM Installation
Manager
- WebSphere® Application
Server Network Deployment, including the
ejbdeploy and thinclient features.

## About this task

- Installation Manager is installed or updated to the appropriate level.
- The required base products and IBM Business Automation
Workflow are
installed.

Only one IBM Installation Manager is required to install multiple instances
of IBM Business Automation Workflow.

## Procedure

1. Run the following command to generate
encrypted passwords using Installation Manager to securely connect to Db2® and the administrative console. 
Important: On Windows, start your command prompt by right-clicking and selecting
Run as administrator.
extract\_directory/IM64/tools/imutilsc -silent -nosplash encryptString password\_to\_encrypt
Note: If you already have 32-bit Installation Manager installed, you can run the command from the
extract\_directory\IM\tools directory.
2. Read and accept the license terms before installing. Adding
-acceptLicense to the command line means that you accept all licenses.
3 Run the following command: Important: On Windows, start your command prompt by right-clicking and selectingRun as administrator . extract\_directory /IM64/tools/imcl install list\_of\_package\_IDs -acceptLicense -installationDirectory location -repositories repository -properties key=value,key=value -showVerboseProgress -log logName .log where: Running this command installs the product with the default features. To installany specific features or make other changes, see the reference link for the command-line argumentsfor imcl.

```
extract\_directory/IM64/tools/imcl install list\_of\_package\_IDs -acceptLicense -installationDirectory location -repositories repository -properties key=value,key=value -showVerboseProgress -log logName.log
```

    - list\_of\_package\_IDs is a list of the IDs for the products and features thatyou want to install. You must include the required features. The syntax ispackageID ,feature ,feature , with multipleproducts separated by spaces.Table 1. Package IDs Product Package ID Feature and Description IBM Business Automation WorkflowEnterprise com.ibm.bpm.ADV.v85 Important: Do not mix production and non-production servers in thesame cell. IBM Business Automation WorkflowExpress com.ibm.bpm.EXP.v85 Important: Do not mix production and non-production servers in thesame cell. IBM Business AutomationWorkflow Enterprise Service Bus com.ibm.bpm.ESB.v85 Important: Do not mix production and non-production servers in thesame cell. WebSphere ApplicationServer Network Deployment com.ibm.websphere.ND.v85 Installation Manager com.ibm.cic.agent Db2 for Windows64-bit com.ibm.ws.DB2EXP.winia64 Db2 must match theoperating system

| Product                                                 | Package ID                | Feature and Description                                                                                                                                                                                                                                                                                                         |
|---------------------------------------------------------|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IBM Business Automation Workflow Enterprise             | com.ibm.bpm.ADV.v85       | WorkflowEnterprise.NonProduction - Test, staging, or development use WorkflowEnterprise.Production - Production use  Important: Do not mix production and non-production servers in the same cell.                                                                                                                              |
| IBM Business Automation Workflow Express                | com.ibm.bpm.EXP.v85       | WorkflowExpress.NonProduction - Test, staging, or development use WorkflowExpress.Production - Production use  Important: Do not mix production and non-production servers in the same cell.                                                                                                                                    |
| IBM Business Automation Workflow Enterprise Service Bus | com.ibm.bpm.ESB.v85       | EnterpriseServiceBus.NonProduction - Test, staging, or development use EnterpriseServiceBus.Production - Production use  Important: Do not mix production and non-production servers in the same cell.                                                                                                                          |
| WebSphere Application Server Network Deployment         | com.ibm.websphere.ND.v85  | core.feature: Required. WebSphere Application Server core content. ejbdeploy: Required. Pre-Enterprise JavaBeans (EJB) 3.0 modules. thinclient: Required. Stand-alone thin clients and resource adapters. embeddablecontainer: Embeddable EJB container. samples: Sample applications feature. com.ibm.sdk.8\_64bit: 64-bit SDK. |
| Installation Manager                                    | com.ibm.cic.agent         | agent\_core: Installation Manager core content. agent\_jre: Installation Manager Java Runtime Environment (JRE).                                                                                                                                                                                                                  |
| Db2 for Windows 64-bit                                  | com.ibm.ws.DB2EXP.winia64 | Db2 must match the operating system                                                                                                                                                                                                                                                                                             |

- location is the path to the directory where you want to install the products.
To install into an existing supported instance of WebSphere Application
Server Network Deployment, specify its directory.Tip: Keep the
installation path as short as possible. Otherwise, you might run into problems later when the paths
of other components, when added to this path, exceed the 255-character path limit.
- repository is the path to the repository where you have extracted the files:
extract\_directory/repository/repos\_64bitFor more than
one repository, separate the repository locations with commas.
- key=value is a list of the keys and values you want to pass to the
installation, separated by commas. Do not put spaces between the commas. 
Create encrypted passwords using the IBM Installation Manager.Important: You must include the user.wasjava=java8
property.
If you are installing Db2, you can include the following
properties:
Table 2. Keys

Key
Description

user.db2.admin.username
User name with authority to access the Db2 database

user.db2.admin.password
Encrypted password for the user name with authority to access the Db2 database. Choose a password that complies with the
password policy of your system.

user.db2.port
Port for the Db2 database.
The default value is 50000.
- logName is the name of the log file to record messages and results.

## Results

Installation Manager installs the list of products and writes a log file to
the directory that you specified. The log file is empty if there are no errors or warnings.

## Example

```
imcl install com.ibm.bpm.ADV.v85,WorkflowEnterprise.NonProduction com.ibm.websphere.ND.v85,core.feature,ejbdeploy,thinclient,embeddablecontainer,samples,com.ibm.sdk.8\_64bit com.ibm.ws.DB2EXP.winia64 -acceptLicense -installationDirectory C:/IBM/BPM -repositories D:/temp/BPM/repository/repos\_64bit -properties user.wasjava=java8,user.db2.admin.username=bpmadmin,user.db2.admin.password="Vvrs88V/a9BUdxwodz0nUg==" -showVerboseProgress -log silentinstall.log
```

```
imcl install com.ibm.bpm.ESB.v85,EnterpriseServiceBus.NonProduction com.ibm.websphere.ND.v85,core.feature,ejbdeploy,thinclient,embeddablecontainer,samples,com.ibm.sdk.8\_64bit -acceptLicense -installationDirectory C:/IBM/BPM -repositories D:/temp/BPM/repository/repos\_64bit -showVerboseProgress -log silentinstall.log
```

```
imcl install com.ibm.bpm.ADV.v85,WorkflowEnterprise.NonProduction com.ibm.websphere.ND.v85,core.feature,ejbdeploy,thinclient,embeddablecontainer,samples,com.ibm.sdk.8\_64bit com.ibm.ws.DB2EXP.winia64 -acceptLicense -installationDirectory C:/IBM/BPM -repositories D:/temp/BPM/repository/repos\_64bit,/usr/tmp/BPMCF -properties user.wasjava=java8,user.db2.admin.username=bpmadmin,user.db2.admin.password="Vvrs88V/a9BUdxwodz0nUg==" -showVerboseProgress -log silentinstall.log
```

```
imcl install com.ibm.bpm.ESB.v85,EnterpriseServiceBus.NonProduction com.ibm.websphere.ND.v85,core.feature,ejbdeploy,thinclient,embeddablecontainer,samples,com.ibm.sdk.8\_64bit -acceptLicense -installationDirectory C:/IBM/BPM -repositories D:/temp/BPM/repository/repos\_64bit,/usr/tmp/BPMCF -showVerboseProgress -log silentinstall.log
```

```
imcl install com.ibm.bpm.ADV.v85,WorkflowEnterprise.NonProduction -acceptLicense -installationDirectory /opt/IBM/BPM -repositories /usr/tmp/BPM/repository/repos\_64bit -showVerboseProgress -log silentinstall.log
```

```
imcl install com.ibm.bpm.ESB.v85,EnterpriseServiceBus.NonProduction -acceptLicense -installationDirectory /opt/IBM/BPM -repositories /usr/tmp/BPM/repository/repos\_64bit -showVerboseProgress -log silentinstall.log
```

## What to do next

## Related reference

- Command-line arguments for imcl
- IBM Business Process Manager system requirements
- Warnings about GTK or ulimit on Linux or UNIX when installing or migrating

## Related information

- IBM WebSphere Application Server documentation
- Messages and known issues during installation and profile creation
- Installation and profile creation log files
- Preparing to install and configure IBM Business Automation Workflow