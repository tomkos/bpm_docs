# Installing silently using the command line

## Before you begin

- IBM Installation
Manager. If you
are installing IBM Business Automation Workflow in group mode, you must use an instance of IBM Installation
Manager that is installed in
group mode. For more information, see the Installation Manager documentation topic Administrator, nonadministrator, and group mode.
- WebSphere® Application
Server Network Deployment, including the
ejbdeploy and thinclient features.

To extract files on AIX, use the GNU tar program instead of the AIX tar program. The AIX tar
program might truncate long file names, which can cause installation errors. To install the GNU tar
program, see Use GNU tar to extract server installation images on AIX.

<!-- image -->

Extract the installation files to a directory that does not contain spaces or special
characters.

## About this task

- Installation Manager is installed or updated to the appropriate level.
- The required base products and IBM Business Automation
Workflow are
installed.

Only one IBM Installation Manager is required to install multiple instances
of IBM Business Automation Workflow.

## Procedure

1. Optional: Run the following command to generate
encrypted passwords using IBM Installation Manager to securely connect to Db2® and the administrative console. 
extract\_directory/IM64/tools/imutilsc -silent -nosplash encryptString password\_to\_encrypt
Note: If you already have 32-bit Installation Manager installed, you can run the command from the
extract\_directory/IM/tools directory.
2. Read and accept the license terms before installing. Adding
-acceptLicense to the command line means that you accept all licenses.
3 Run the following command: Note: If you already have 32-bit Installation Manager installed, you can run the command from theextract\_directory /IM/tools directory. where: Running this command installs the product with the default features. To installspecific features or make other changes, see the reference link for the command-line arguments forimcl.
    - extract\_directory/IM64/tools/imcl install list\_of\_package\_IDs -acceptLicense -installationDirectory location -repositories repository -properties key=value,key=value -showVerboseProgress -log logName.log
    - extract\_directory/IM64/tools/imcl install list\_of\_package\_IDs -acceptLicense -installationDirectory location -repositories repository -showVerboseProgress -log logName.log
    - list\_of\_package\_IDs is a list of the IDs for the products and features thatyou want to install. You must include the required features. The syntax ispackageID ,feature ,feature . Separatemultiple products by using spaces.Table 1. Package IDs Product Package ID Feature and Description IBM Business Automation WorkflowEnterprise com.ibm.bpm.ADV.v85 Important: Do not mix production and non-production servers in the same cell. IBM Business Automation WorkflowExpress com.ibm.bpm.EXP.v85 Important: Do not mix production and non-production servers in thesame cell. IBM Business AutomationWorkflow Enterprise Service Bus com.ibm.bpm.ESB.v85 Important: Do not mix production and non-production servers in thesame cell. WebSphere ApplicationServer Network Deployment com.ibm.websphere.ND.v85 On Linux on Power LE:com.ibm.websphere.ND.le.v85 Installation Manager com.ibm.cic.agent Db2 for Linux on Intel systems com.ibm.ws.DB2EXP.linuxia64 Db2 must match theoperating system.

| Product                                                 | Package ID                                                                 | Feature and Description                                                                                                                                                                                                                                                                                                                                                                |
|---------------------------------------------------------|----------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IBM Business Automation Workflow Enterprise             | com.ibm.bpm.ADV.v85                                                        | WorkflowEnterprise.NonProduction - Test, staging, or development use WorkflowEnterprise.Production - Production use  Important: Do not mix production and non-production servers in the same cell.                                                                                                                                                                                     |
| IBM Business Automation Workflow Express                | com.ibm.bpm.EXP.v85                                                        | WorkflowExpress.NonProduction - Test, staging, or development use WorkflowExpress.Production - Production use  Important: Do not mix production and non-production servers in the same cell.                                                                                                                                                                                           |
| IBM Business Automation Workflow Enterprise Service Bus | com.ibm.bpm.ESB.v85                                                        | EnterpriseServiceBus.NonProduction - Test, staging, or development use EnterpriseServiceBus.Production - Production use  Important: Do not mix production and non-production servers in the same cell.                                                                                                                                                                                 |
| WebSphere Application Server Network Deployment         | com.ibm.websphere.ND.v85 On Linux on Power LE: com.ibm.websphere.ND.le.v85 | core.feature: Required. WebSphere Application Server core content. ejbdeploy: Required. Pre-Enterprise JavaBeans (EJB) 3.0 modules. thinclient: Required. Stand-alone thin clients and resource adapters. embeddablecontainer: Embeddable EJB container. samples: Sample applications feature. com.ibm.sdk.8\_64bit: 64-bit SDK. com.ibm.sdk.71\_64bit: 64-bit SDK on Linux on Power LE. |
| Installation Manager                                    | com.ibm.cic.agent                                                          | agent\_core: Installation Manager core content. agent\_jre: Installation Manager Java Runtime Environment (JRE).                                                                                                                                                                                                                                                                         |
| Db2 for Linux on Intel  systems                         | com.ibm.ws.DB2EXP.linuxia64                                                | Db2 must match the operating system.                                                                                                                                                                                                                                                                                                                                                   |

- location is the path to the directory where you want to install the products.
To install into an existing supported instance of WebSphere Application
Server Network Deployment, specify its directory.
- repository is the path to the repository where you have extracted the files:
extract\_directory/repository/repos\_64bitFor more than
one repository, separate the repository locations with commas.
- key=value is a list of the keys and values that you want to pass to the
installation, separated by commas. Do not put spaces between the commas. 
Create encrypted passwords using the IBM Installation Manager.Important: You must include the user.wasjava=java8
property.
If you are installing Db2, you can include the following
properties:
Table 2. Keys for AIX and Linux

Key
Description

user.db2.port 
Port for the Db2 database.
The default value is 50000.

Table 3. Keys for Linux only

Key
Description

user.db2.instance.username
Db2 instance user name

user.db2.instance.password
Encrypted password for the Db2 instance user name. For an encrypted password, use quotation marks. For example,
user.db2.instance.password="the\_encrypted\_password"

user.db2.fenced.newuser
The value true is for a new user. The value
false is for an existing user. If the value is false, the
user.db2.fenced.password is not needed.

user.db2.fenced.username
Fenced user name. The fenced user is used to run user defined functions (UDFs)
and stored procedures outside of the address space used by the Db2 database. The default user is db2fenc1
and the default group is db2fadm1. 

user.db2.fenced.password
Encrypted password for the fenced user name. For an encrypted password, use
quotation marks. For example, user.db2.fenced.password="the\_encrypted\_password"

user.db2.das.newuser
The value true is for a new user. The value
false is for an existing user. If the value is false, the
user.db2.das.password is not needed.

user.db2.das.username
Db2 administration server
(DAS) user name. The user ID for the Db2
administration server user is used to run the Db2
administration server on your system. The default user is dasusr1 and the default
group is dasadm1. This user ID is also used by the Db2 GUI tools to perform administration tasks against the
local server database instances and databases. 

user.db2.das.password
Encrypted password for the administration server user name. For an encrypted
password, use quotation marks. For example,
user.db2.das.password="the\_encrypted\_password"
- logName is the name of the log file that records messages and results.

## Results

Installation Manager installs the list of products and writes a log file to
the directory that you specified. The log file is empty if there are no errors or warnings.

## Example

- imcl install com.ibm.bpm.ADV.v85,WorkflowEnterprise.NonProduction com.ibm.websphere.ND.v85,core.feature,ejbdeploy,thinclient,embeddablecontainer,samples,com.ibm.sdk.8\_64bit com.ibm.ws.DB2EXP.linuxia64 -acceptLicense -installationDirectory /opt/IBM/BPM -repositories /usr/tmp/BPM/repository/repos\_64bit -properties user.wasjava=java8,user.db2.instance.username=bpmadmin,user.db2.instance.password="Vvrs88V/a9BUdxwodz0nUg==" -showVerboseProgress -log silentinstall.log
- imcl install com.ibm.bpm.ADV.v85,WorkflowEnterprise.Production com.ibm.websphere.ND.v85,core.feature,ejbdeploy,thinclient,embeddablecontainer,samples,com.ibm.sdk.8\_64bit -acceptLicense -installationDirectory /opt/IBM/BPM -repositories /usr/tmp/BPM/repository/repos\_64bit -showVerboseProgress -log silentinstall.log

- imcl install com.ibm.bpm.ESB.v85,EnterpriseServiceBus.NonProduction com.ibm.websphere.ND.v85,core.feature,ejbdeploy,thinclient,embeddablecontainer,samples,com.ibm.sdk.8\_64bit -acceptLicense -installationDirectory /opt/IBM/BPM -repositories /usr/tmp/BPM/repository/repos\_64bit-showVerboseProgress -log silentinstall.log
- imcl install com.ibm.bpm.ESB.v85,EnterpriseServiceBus.Production com.ibm.websphere.ND.v85,core.feature,ejbdeploy,thinclient,embeddablecontainer,samples,com.ibm.sdk.8\_64bit -acceptLicense -installationDirectory /opt/IBM/BPM -repositories /usr/tmp/BPM/repository/repos\_64bit-showVerboseProgress -log silentinstall.log

- imcl install com.ibm.bpm.ADV.v85,WorkflowEnterprise.Production com.ibm.websphere.ND.v85,core.feature,ejbdeploy,thinclient,embeddablecontainer,samples,com.ibm.sdk.8\_64bit com.ibm.ws.DB2EXP.linuxia64 -acceptLicense -installationDirectory /opt/IBM/BPM -repositories /usr/tmp/BPM/repository/repos\_64bit,/usr/tmp/BPMCF -properties user.wasjava=java8,user.db2.instance.username=bpmadmin,user.db2.instance.password="Vvrs88V/a9BUdxwodz0nUg==" -showVerboseProgress -log silentinstall.log
- imcl install com.ibm.bpm.ADV.v85,WorkflowEnterprise.NonProduction com.ibm.websphere.ND.v85,core.feature,ejbdeploy,thinclient,embeddablecontainer,samples,com.ibm.sdk.8\_64bit -acceptLicense -installationDirectory /opt/IBM/BPM -repositories /usr/tmp/BPM/repository/repos\_64bit,/usr/tmp/BPMCF -showVerboseProgress -log silentinstall.log

- imcl install com.ibm.bpm.ESB.v85,EnterpriseServiceBus.Production com.ibm.websphere.ND.v85,core.feature,ejbdeploy,thinclient,embeddablecontainer,samples,com.ibm.sdk.8\_64bit -acceptLicense -installationDirectory /opt/IBM/BPM -repositories /usr/tmp/BPM/repository/repos\_64bit,/usr/tmp/BPMCF -showVerboseProgress -log silentinstall.log
- imcl install com.ibm.bpm.ESB.v85,EnterpriseServiceBus.NonProduction com.ibm.websphere.ND.v85,core.feature,ejbdeploy,thinclient,embeddablecontainer,samples,com.ibm.sdk.8\_64bit -acceptLicense -installationDirectory /opt/IBM/BPM -repositories /usr/tmp/BPM/repository/repos\_64bit,/usr/tmp/BPMCF  -showVerboseProgress -log silentinstall.log

```
imcl install com.ibm.bpm.ADV.v85,WorkflowEnterprise.NonProduction -acceptLicense -installationDirectory /opt/IBM/BPM -repositories /usr/tmp/BPM/repository/repos\_64bit -showVerboseProgress -log silentinstall.log
```

```
imcl install com.ibm.bpm.ESB.v85,EnterpriseServiceBus.NonProduction -acceptLicense -installationDirectory /opt/IBM/BPM -repositories /usr/tmp/BPM/repository/repos\_64bit -showVerboseProgress -log silentinstall.log
```

## What to do next

## Related reference

- Warnings about GTK or ulimit on Linux or UNIX when installing or migrating

## Related information

- Messages and known issues during installation and profile creation
- Installation and profile creation log files
- Preparing to install and configure IBM Business Automation Workflow