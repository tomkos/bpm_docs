# Preparing Linux systems for installation

## Before you begin

If you plan to install interactively, ensure that you have a supported version of Mozilla Firefox
installed.

## About this task

Because certain steps are specific to
a version of the operating system, all steps might not apply to your
environment. If no qualifier is provided for a particular step, complete
the step for all versions of the operating system.

Business Automation Workflow does not
support different operating systems in the same cell, for example Red Hat Enterprise Linux 7 on one
node and Red Hat Enterprise Linux 8 on another node. All nodes must use the same operating
system.

## Procedure

Complete the following steps on your Linux®
system before installing Business Automation Workflow:

1. Because WebSphere®
Application Server is a
prerequisite of Business Automation Workflow,
complete all the required preparation steps in the Preparing Linux systems for installation topic in the WebSphere
Application Server documentation. 

Note: Some X11 libraries (specified in the previous link) are required for WebSphere
Application Server whether you use GUI
interfaces in Linux or not.
2. Increase the allowable stack size, number of open files, number of processes, and file size.
Add the following lines to the end of the /etc/security/limits.conf file, or if
the lines already exist, change the values. In this example, user\_name is the
name of the user that runs WebSphere
Application Server: 

# - stack - maximum stack size (KB)
user\_name soft stack 32768
user\_name hard stack 32768
# - nofile - maximum number of open files
user\_name soft nofile 65536
user\_name hard nofile 65536
# - nproc - maximum number of processes
user\_name soft nproc 16384
user\_name hard nproc 16384
# - fsize - maximum file size
user\_name soft fsize 6291453
user\_name hard fsize 6291453 Save and close the file, and log off and
log in again. 
You can check the current maximum number of open files by using ulimit -n and
the current maximum file size by using ulimit -f. The ulimit
requirement is dynamically calculated at installation time and might need to be larger based on the
options you select.
For more information about this setting, run man limits.conf or see the topic
Preparing Linux systems for installation in the WebSphere
Application Server documentation.
3. Check for the existence of a file that is named
/etc/security/limits.d/90-nproc.conf or
/etc/security/limits.d/20-nproc.conf, which overrides the
nproc value set in the limits.conf file. If this file exists,
edit it and set the same nproc values that you specified in
limits.conf.
4. Check for the existence of a file name /etc/profile, which overrides the
nofile values set in the limits.conf file. If the
ulimit -n values exist in the /etc/profile file, edit it and
set the same nofile values that you specified in
limits.conf.
5. On Linux on System z, if you plan to use the
Installation Manager graphical interface to install IBM Business Automation Workflow, install the
libgtk-2\_0-0-32bit and libgthread-2\_0-0-32bit libraries. 
The following example shows how to install by using the zypper
command:zypper install libgtk-2\_0-0-32bit
zypper install libgthread-2\_0-0-32bit
For more information, see X
libraries required by IBM Installation Manager on Linux for System z
6 Set the umask value to077 using the following command: The value 077 is the most restrictive value that IBM Business Automation Workflow tolerates. You canchoose to set a less restrictive umask value for the following access levels.This is optional.
    - umask 077
    - 037 for read-only access for a group of human administrators and tools
    - 027 for read and write access for a group of human administrators and tools
    - 007 for read, write, and execute access for a group of human administrators and tools
7. Restart the computer.
8. Complete the steps in Tuning Linux systems.
9. Ensure all servers that are involved are set to the same time. Use the same network time
protocol for all servers on all cluster nodes, including application, support, and database
clusters. A time mismatch causes erratic behavior, including duplicate system tasks.
10. If you are using Db2, make sure that all your Db2 parameters meet the Db2 naming
rules.