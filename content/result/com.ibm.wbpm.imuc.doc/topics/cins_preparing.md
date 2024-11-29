# Preparing to install and configure the software

1. Review hardware and software requirements. Visit Detailed system requirements for a specific product.
2. Prepare the operating system on each computer that you plan to use for product installation. See
Preparing operating systems for product installation.
3 Make sure that you have installed your database management system. Consult your databasedocumentation for information about installing and administering your database managementsystem.IBM Business Automation Workflow embeds the Db2® database. If you want to use Db2 as your database, you can select it asa feature from the installer and it is installed and configured automatically. The user must haveadministrative privileges (root or Administrator) to install Db2 . Important:

IBM Business Automation Workflow embeds the Db2® database. If you want to use Db2 as your database, you can select it as
a feature from the installer and it is installed and configured automatically. The user must have
administrative privileges (root or Administrator) to install Db2.

    - If you already have a version of Db2 installed and you want to install Db2, you must uninstall Db2 before running
the IBM Business Automation Workflow installer. If the installer
detects a version of Db2 installed and you have selected to install Db2 from the installer, you will receive a
warning message and will not be able to install Db2.
    - If you already have a version of Db2 installed
and you create the deployment environment without deferring schema creation, you must have Db2 10.5.0.0 or later. Otherwise, the
database version validation will fail with an error; for example CWMCB0316E: Your database
system is not the required version. The minimum supported version is 10.5.0.0 but the current
version is 10.1.0.2.
    - If you are installing Db2 as a root user, you must ensure that all
kernel requirements are met before the Db2 installation begins. See Kernel parameter requirements (Linux) for a list of the kernel requirements. You can locate
the current values by parsing the output of the ipcs -l command.
    - You will not be able to properly install and use Db2 if the password that is specified does
not meet operating system or company restrictions, because an operating system user is created on
install.

- System requirements

Before you install, ensure that your system meets all system requirements.
- Preparing operating systems for product installation

Before you can install IBM Business Automation Workflow, you must prepare your operating system. The configuration depends on the type of operating system you are using.
- Considerations for HADR setup and configuration

Review the following considerations while you plan to set up and configure DB2 for High Availability and Disaster Recovery (HADR).
- Configuring Oracle Data Guard for IBM Business Automation Workflow

You can configure Oracle Data Guard to be used with IBM Business Automation Workflow. Oracle Data Guard provides high availability, disaster recovery, and data protection and is used to create, manage, and monitor one or more standby databases so that production Oracle databases can survive disasters and data corruptions.