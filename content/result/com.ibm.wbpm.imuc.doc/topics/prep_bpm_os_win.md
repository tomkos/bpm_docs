# Preparing Windows systems for installation

Before you can install IBM® Business Automation
Workflow,
you must prepare your Windows operating system.

## Before you begin

If you are planning to use Db2® Standard
Edition with your
Business Automation Workflow installation,
the user account must have administrative privileges (Administrator) on the machine where you
install.

## About this task

Because WebSphere®
Application Server is a prerequisite
product for Business Automation Workflow.
Complete all preparation tasks for WebSphere
Application Server before installing
Business Automation Workflow.

Business Automation Workflow does not
support different operating systems in the same cell, for example Windows Server 2019 Standard
Edition on one node and Windows Server 2022 Standard Edition on another node. All nodes must use the
same operating system.

## Procedure

Complete the following steps on your Windows system
before installing IBM Business Automation Workflow:

1. Complete the steps in the Preparing Windows systems for installation topic in the WebSphere
Application Server documentation.
2. Complete the steps in Tuning
Windows systems.
3. Check that all servers that are involved are set to the same time. Use the same network
time protocol for all servers on all cluster nodes, including application, support, and database
clusters. A time mismatch causes erratic behavior, including duplicate system tasks.
4 If you are using a Czech locale, you must change the systemsettings to prevent seeing corrupted characters in IBM Heritage ProcessPortal andIBM Process Designer. Change the Windows settings by completing thefollowing steps:
    1. Click Regional and Language Options,
and open the Administrative tab.
    2. In the Language for non-Unicode programs section, click
Change system locale . . . , to open the locale list.
    3. Select Czech from the list and
click OK.
5. If you are using Db2, make sure that all your Db2 parameters
meet the Db2 naming rules.
6. Install 7-Zip file archiving tool for extracting installation
files from downloaded compressed files and DVD images.
7. If you are installing off a network drive, and your network has a firewall or other
security restrictions. Work with your network administrator to check that permissions, trusted
sites, and security levels are sufficient for installing.

## Related tasks

- Preparing Windows systems for installation
- Tuning Windows systems

## Related information

- General naming rules for DB2