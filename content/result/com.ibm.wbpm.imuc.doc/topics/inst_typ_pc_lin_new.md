# Installing and configuring Workflow Center
with a new Db2 database
server

## Before you begin

- Extract the installation files to a directory that does not contain spaces or special
characters. The launchpad cannot be started from a directory path that contains spaces or special
characters.
- Linux on Power LE does not support typical installation.

## About this task

Using the typical installation option, you can install Db2 on Linux on Intel systems, and configure the
required databases for IBM Business Automation Workflow. Select typical
installation only if you are installing on Linux on Intel, have administrative privileges (are a
root user), and do not have an existing Db2
database server on the system. If you are installing on Linux for z or Linux on Power, use the
instructions for installing onto and configuring an existing database.

From the product launchpad, the typical installation process installs the
software, configures the deployment manager and managed-node profiles, and configures a
single-cluster deployment environment that consists of one node and one server. It also installs IBM WebSphere SDK Java Technology Edition 8 (Java 8).

Only one IBM Installation Manager is required to install multiple instances
of IBM Business Automation Workflow.

## Procedure

1 Optional: If you are connected to the Internet, the typical installation process automatically upgradesyour product to the latest fix pack or refresh pack level and recommended interim fixes. If you wantthese upgrades to be installed from a local directory instead, or if you want to specify the fixlevel, you can modify a properties file to direct Installation Manager to the upgrades toinstall. Create the following file: Note: Ensure that you have read/write access to the folders that are specifiedin the bpm\_updates.properties file. The file uses three prefixes: ifix , fixpack , andlaunchpad . Each prefix must be followed by a period. The name after the prefix andthe period can be anything you want, which enables you to point to multiple locations for interimfixes, fix packs, and launchpad upgrades. The locations can be either local directories or URLs. Thefollowing code is an example of the prefixes and names in the propertiesfile:ifix.1=/bpmUpdatesfixpack.2=http://test/replaunchpad.1=/launchpad\_updatesfixpack.WAS\_REP=/WAS\_updatesfixpack.BPM\_REP=/BPM\_updates
    - /user\_home\_directory/bpm\_updates.properties

```
ifix.1=/bpmUpdates
fixpack.2=http://test/rep
launchpad.1=/launchpad\_updates
fixpack.WAS\_REP=/WAS\_updates
fixpack.BPM\_REP=/BPM\_updates
```

2. Run launchpad.sh, which is in the root directory of
the extracted files.  You can run only one launchpad at a time.
3. Optional: 
If you are prompted to update the launchpad, click Update. The updates
are installed and your launchpad is restarted automatically.
If you do not have access to the Internet and want the updates to be installed from a local
directory, you can modify a properties file with the appropriate launchpad prefix as described in
step 1 to direct Installation Manager to the updates to install.
4. On the Welcome page, click Typical
installation.
5. Select Install Workflow Center and click Next.
6 Optional: Change the location information:

- Host name: This field shows the name of your machine.Important: If a value of localhost or 127.0.0.1 is used for the host name, Workflow Server installations on a remote system will not be able
to connect to the Workflow Center. Do not use localhost
for environments that are spread across multiple computers. To use an external Content Platform Engine, the hostname property value must have a domain name
suffix, for example
MyDmgrHost.my\_domain.com.
- Location : Enter the installation location for Workflow Center , or click Browse to selectthe location.Notes:
    - The installation location must either be an empty directory or a directory that does not exist
and is created during installation.
    - The installation location cannot contain National Language Strings
(NLS).
7. Specify the User name and Password for the cell
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
8. Specify the User name and
Password for the deployment environment administrative
account. The deployment environment administrator is the primary IBM Business Automation
Workflow administrator. A user who is assigned to this
role has administrative access to Process Center and Process Admin Console. Having this role
provides access to all interfaces, enabling users to alter or delete all types of available library
items and assets, including process applications and toolkits. The user in this role also
administers Workflow Servers, Performance Data Warehouses,
and internal users and groups.
9. Click Next.
10. Select No. I need one installed for me. to install Db2.
11 Specify the following Db2 administrative user names and passwords: If the fenced user or administration (DAS) server user name exists, clear the NewUser option. Restriction:

- Db2 instance user
- Db2 fenced user. The fenced user is used to
run user defined functions (UDFs) and stored procedures outside of the address space used by the
Db2 database. The default user is
db2fenc1 and the default group is db2fadm1.
- Db2 administration server (DAS) user. The user
ID for the Db2 administration server user is used
to run the Db2 administration server (DAS) on your
system. The default user is dasusr1 and the default group is
dasadm1. This user ID is also used by the Db2 GUI tools to perform administration tasks against the
local server database instances and databases.

- User names must not contain National Language Strings (NLS)
- User names must be maximum eight characters long
12. Click Next to continue. 

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
13. On the Installation summary page, verify that the
installation options and read the license agreements. If you agree to the terms of the license
agreements, click  I have read and accepted the license agreement and
notices.
14. Click Install Software.

## Results

After a successful installation, the Quick Start console starts
automatically.

## What to do next

To learn about security for the environment and applications, see Creating a secure environment.

After the server is started, if you want to use the case management features,
see the topic Configuring your system for case management.

## Related reference

- Warnings about GTK or ulimit on Linux or UNIX when installing or migrating

## Related information

- Messages and known issues during installation and profile creation
- Installation and profile creation log files
- Preparing to install and configure IBM Business Automation Workflow