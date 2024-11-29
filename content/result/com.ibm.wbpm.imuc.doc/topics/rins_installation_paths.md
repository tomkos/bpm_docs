# Installation directories for the product and profiles

- install\_root default
directory
- profile\_root default
directory
- Db2® Standard
Edition default directory
- IBM Business Automation Workflow and WebSphere® Application
Server default
installation directory
- Default installation
directory for a profile named profile\_name
- Process Designer
default directory
- Installation Manager default
installation directories
- Installation Manager default
agent data directories

## Variables used
in the documentation

Several variables representing specific
default directories are used throughout the documentation. These file
paths are default locations. You can install the product and other
components and create profiles in any directory for which you have
write access. Multiple installations of IBM Business Automation Workflow products
or components require multiple locations.

Here are the main
variables used in the documentation:

## How variable
meanings can differ

The meaning of variables used to represent
installation directories can differ based on whether you are installing
the product on a clean workstation or on a workstation that has an
existing installation of WebSphere Application
Server or WebSphere Application Server
Network Deployment. The variables can also differ depending on whether
you are performing the installation as a root (Administrator on a Windows system) or nonroot user.

## Limitations
of nonroot installers

Root, Administrator, and nonroot users
can install the product. The default directories the installation
program provides differ based on whether the user has root (Administrator)
privileges. Root and Administrator users can register shared products
and install into system-owned directories (globally shared resources
that are available to all users), while nonroot users cannot. Nonroot
users can install only into directories they own.

Alternatively, you can use IBM Installation
Manager group mode to install Installation Manager and IBM Business Automation Workflow so that a group of nonroot users can install
and manage the installation packages. You can install in group mode only with custom command line or
response file installation methods, not typical or custom with the graphical interface methods.

## Default directories for Typical Installation

The
following tables show the default installation locations of the IBM Business Automation Workflow base
installation and its profiles during a typical installation.

| Default install\_root for root or Administrator users   | Default install\_root for nonroot users   |
|--------------------------------------------------------|------------------------------------------|
| /opt/IBM/Workflow/v18.0/                               | user\_home/IBM/Workflow/v18.0/            |
| /opt/ibm/Workflow/v18.0/                               | user\_home/ibm/Workflow/v18.0/            |
| C:\IBM\Workflow\v18.0                                  | C:\IBM\Workflow\v18.0                    |

| Default profile\_root for root or Administrator users   | Default profile\_root for nonroot users             |
|--------------------------------------------------------|----------------------------------------------------|
| /opt/IBM/Workflow/v18.0/profiles/profile\_name          | user\_home/IBM/Workflow/v18.0/profiles/profile\_name |
| /opt/ibm/Workflow/v18.0/profiles/profile\_name          | user\_home/ibm/Workflow/v18.0/profiles/profile\_name |
| C:\IBM\Workflow\v18.0\profiles\profile\_name            | C:\IBM\Workflow\v18.0\profiles\profile\_name        |

| Default Db2 binary location   | Database Instance location                                                                                                                                                                                                                       |
|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| /opt/ibm/Workflow/v18.0/DB2   | Database instance is created under the bpminst user. For example: user\_home/bpminst                                                                                                                                                              |
| C:\IBM\Workflow\v18.0\DB2     | The BPMINST database instance is created under the root (\) of the drive where IBM Business Automation Workflow is installed. For example, if IBM Business Automation Workflow is installed under C:\IBM\BPM\v8.5\ then you will see C:\BPMINST. |

## Default directories for Custom Installation
or existing installation of WebSphere Application
Server or WebSphere
Application Server Network Deployment

| Default install\_root for root or Administrator users   | Default install\_root for nonroot and group users   |
|--------------------------------------------------------|----------------------------------------------------|
| /usr/IBM/WebSphere/AppServer                           | user\_home/IBM/WebSphere/AppServer                  |
| /opt/IBM/WebSphere/AppServer                           | user\_home/IBM/WebSphere/AppServer                  |
| C:\Program Files\IBM\WebSphere\AppServer               | user\_home\IBM\WebSphere\AppServer                  |

| Default profile\_root for root or Administrator users           | Default profile\_root for nonroot and group users        |
|----------------------------------------------------------------|---------------------------------------------------------|
| /usr/IBM/WebSphere/AppServer/profiles/profile\_name             | user\_home/IBM/WebSphere/AppServer/profiles/profile\_name |
| /opt/IBM/WebSphere/AppServer/profiles/profile\_name             | user\_home/IBM/WebSphere/AppServer/profiles/profile\_name |
| C:\Program Files\IBM\WebSphere\AppServer\profiles\profile\_name | user\_home\IBM\WebSphere\AppServer\profiles\profile\_name |

| Default Process Designer installation location for root or Administrator users   | Default Process Designer installation location for nonroot users   |
|----------------------------------------------------------------------------------|--------------------------------------------------------------------|
| C:\IBM\ProcessDesigner\v8.5                                                      | C:\IBM\ProcessDesigner\v8.5                                        |

## Default installation directories
for IBM Installation
Manager

- The directories in Table 7 are the defaults (per
operating system) into which Installation Manager is installed. For more
information about other defaults for Installation Manager, see Installing as an administrator, nonadministrator, or group in the Installation Manager documentation.
- The agent data directories in Table 8 are the
defaults (per operating system) used by Installation Manager for data associated with
the application, such as the state and history of operations performed by Installation Manager. For more information
about the agent data location, see Agent data location in the Installation Manager documentation.

Installation Manager also uses
another directory to store shared program objects and cached files that are generated when you
install a product. You can specify this shared resources directory when you install WebSphere Application
Server and IBM Business Automation Workflow. This value is set the
first time that a product is installed with a particular Installation Manager instance. For further
information about the shared resources directory, see Overview of package groups and the shared resources directory. For
information about how to locate the shared resources directory, see Backing up and restoring Installation Manager.

| Defaults for root or Administrator users                                                        | Defaults for nonroot or non-administrator users                                     | Defaults for group mode users            |
|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|------------------------------------------|
| /opt/IBM/InstallationManager                                                                    | /user\_home/IBM/InstallationManager                                                  | /user\_home/IBM/InstallationManager\_Group |
| /opt/IBM/InstallationManager                                                                    | /user\_home/IBM/InstallationManager                                                  | /user\_home/IBM/InstallationManager\_Group |
| Windows 8, Windows Server 2012:   C:\Program Files [(x86)]\IBM\Installation Manager             | Windows 8, Windows Server 2012: C:\Users\user\IBM\Installation Manager              | Not available.                           |
| (deprecated)  Windows Server 2008, Windows 7: C:\Program Files [(x86)]\IBM\Installation Manager | (deprecated) Windows Server 2008, Windows 7: C:\Users\user\IBM\Installation Manager | Not available.                           |
|                                                                                                 |                                                                                     |                                          |

| Defaults for root or Administrator users                                                       | Defaults for nonroot or non-administrator users                                        | Defaults for group mode users                |
|------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|----------------------------------------------|
| /var/ibm/InstallationManager                                                                   | /user\_home/var/ibm/InstallationManager                                                 | /user\_home/var/ibm/InstallationManager\_Group |
| /var/ibm/InstallationManager                                                                   | /user\_home/var/ibm/InstallationManager                                                 | /user\_home/var/ibm/InstallationManager\_Group |
| Windows 8, Windows Server 2012:   C:\ProgramData\IBM\Installation Manager                      | Windows 8, Windows Server 2012: C:\Users\user\AppData\Roaming\IBM\Installation Manager | Not available.                               |
| (deprecated) Windows Server 2008, Windows 7: C:\Program Files [(x86)]\IBM\Installation Manager | (deprecated) Windows Server 2008, Windows 7: C:\Users\user\IBM\Installation Manager    | Not available.                               |
|                                                                                                |                                                                                        |                                              |

## Related concepts

- Process and process application considerations
- Resource considerations
- Development and deployment version levels
- Naming considerations for profiles, nodes, servers, hosts, and cells

## Related tasks

- Preparing necessary security authorizations