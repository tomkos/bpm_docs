# Installing and configuring Workflow Center
with a new Db2 database
server

## Before you begin

## About this task

Using the typical installation option, you can install Db2 and configure the required databases for
IBM Business Automation Workflow. Select typical installation only if you
have administrative privileges (are an Administrator user) and do not have an existing Db2 database server on the system. If you are installing
Db2 as a Windows domain user, the domain
user name must exist and be added to the local Administrators group before you start the
launchpad.

From the product launchpad, the typical installation process installs the
software, configures the deployment manager and managed-node profiles, and configures a
single-cluster deployment environment that consists of one node and one server. It also installs IBM WebSphere SDK Java Technology Edition 8 (Java 8).

Only one IBM Installation Manager is required to install multiple instances
of IBM Business Automation Workflow.

## Procedure

1 Optional: If you are connected to the Internet, the typicalinstallation process automatically upgrades your product to the latest refresh pack and interim fixlevel. If you want these upgrades to be installed from a local directory instead, or if you want tospecify the fix level, you can modify a properties file to direct Installation Manager to theupgrades to install. Create the following file: where Note: Ensure that you have read/write access to the folders that are specifiedin the bpm\_updates.properties file. The file uses three prefixes: ifix , fixpack , andlaunchpad . Each prefix must be followed by a period. The name after the prefix andthe period can be anything you want, which enables you to point to multiple locations for interimfixes, fixpacks, and launchpad upgrades. The locations can be either local directories or URLs. Thefollowing code is an example of the prefixes and names in the propertiesfile:ifix.1=C:/bpmUpdatesfixpack.2=http://test/replaunchpad.1=C:/launchpad\_updatesfixpack.WAS\_REP=C:/WAS\_updatesfixpack.BPM\_REP=C:/BPM\_updates
    - C:/HOMEPATH/bpm\_updates.properties
    - The HOMEPATH environment variable points to
C:/Users/user\_name

```
ifix.1=C:/bpmUpdates
fixpack.2=http://test/rep
launchpad.1=C:/launchpad\_updates
fixpack.WAS\_REP=C:/WAS\_updates
fixpack.BPM\_REP=C:/BPM\_updates
```

2. Run Launchpad64.exe, which is in the root
directory of the extracted files.  You can run only one launchpad at a
time.
3. Optional: 
If you are prompted to update the launchpad, click Update. The updates
are installed and your launchpad is restarted automatically.
If you do not have access to the Internet and want the updates to be installed from a local
directory, you can modify a properties file with the appropriate launchpad prefix as described in
step 1 to direct Installation Manager to the updates to install.
4. On the Welcome page, click Typical
installation.
5. Select Install Workflow Center and click Next.
6. Click Next.
7 Optional: Change the location information. Restriction: Because you are installing Db2 , your installation location cannot containNational Language Strings (NLS).

- Host name: This field shows the name of your machine.Important: If a value of localhost or 127.0.0.1 is used for the host name, Workflow Server installations on a remote system will not be able
to connect to Workflow Center.To use an external
Content Platform Engine, the hostname property value must have a
domain name suffix, for example
MyDmgrHost.my\_domain.com.
- Location : Enter the installation location for Workflow Center , or click Browse to selectthe location.Notes:
    - The installation location must either be an empty directory or a directory that does not exist
and is created during installation.
    - The installation location cannot contain National Language Strings
(NLS).
8. Specify the User name and Password for the cell
administrative account.
The cell administrator is the primary WebSphere® Application
Server
administrator. A user who is assigned to this role can assign other administrator roles, and is
responsible for the administration of the cell and topology. A user who is assigned to this role is
not responsible for the administration of the IBM Business Automation
Workflow components. This role provides access to all
interfaces, enabling users to alter or delete all types of available library items and assets,
including process applications and toolkits. The user in this role also administers process servers,
Performance Data Warehouses, and internal users and groups. You must be a user assigned to this role
to deploy process applications on the Workflow Center
server.
9. Specify the User name and
Password for the deployment environment administrative
account. The deployment environment administrator is the primary IBM Business Automation
Workflow administrator. A user who is assigned to this
role has administrative access to Process Center and Process Admin Console. Having this role
provides access to all interfaces, enabling users to alter or delete all types of available library
items and assets, including process applications and toolkits. The user in this role also
administers Workflow Servers, Performance Data Warehouses,
and internal users and groups.
10. Click Next.
11. Select No. I need one installed for me. to install Db2.
12 Specify the User name and Password for theDb2 database. Restriction:

- If you use a Windows domain user ID, include the at sign (@) and the domain name:
userID@example.com. Confirm that the domain user ID already exists and was
added to the local Administrators group before the launchpad was started.
- User names must not contain National Language Strings (NLS)
- User names must be maximum 30 characters long
13. Click Next to continue. 

Note: If you are using a local properties file, you do not need to provide your IBMid and
password.
A connection to the service repositories is required to download and install fix packs and
required interim fixes from the Internet, including fixes for WebSphere Application
Server and IBM Business Automation Workflow. You can obtain an IBMid and password by
registering at http://www.ibm.com.
To continue installing without downloading the required fixes, click
Cancel or clear the Use your support account to include updates
with the installation option on the Installation summary page.
After successfully installing the product, you can use Installation Manager to install the
required fixes.
14. On the Installation summary page, verify that the
installation options and read the license agreements. If you agree to the terms of the license
agreements, click  I have read and accepted the license agreement and
notices.
15. Click Install Software.

## Results

After a successful installation, the Quick Start console starts
automatically.

## What to do next

1. Follow the steps listed in DB2 log file error: SQL1092N "USERID does not have the authority to perform the requested command or operation.".
2. Edit the file
install\_root\logs\config\BPMConfig\_timestamp.log.
(There should only be one log file with that file name.)
3. In the log file, search for the line that contains the following string:
com.ibm.bpm.config.BPMConfig.validateBPMConfigCommand(): ENTRY -create
-de
4. When you have located the string, copy the portion of the string that begins with the
-create parameter and paste it to a BPMConfig script
invocation in the install\_root\bin directory on the Windows
command line. For example:BPMConfig -create -de
C:\Users\jdoe\AppData\Local\Temp\IBM\_LaunchPad\_BPM\_1383510443100\SingleCluster.properties

To learn about security for the environment and applications, see Creating a secure environment.

After the server is started, if you want to use the case management features,
see the topic Configuring your system for case management.

## Related reference

- Warnings about GTK or ulimit on Linux or UNIX when installing or migrating

## Related information

- Messages and known issues during installation and profile creation
- Installation and profile creation log files
- Preparing to install and configure IBM Business Automation Workflow
- DB2 log file error: SQL1092N "USERID does not have the authority to perform the requested command or operation."