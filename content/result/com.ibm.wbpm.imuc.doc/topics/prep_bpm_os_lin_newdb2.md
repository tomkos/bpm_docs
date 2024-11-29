# Preparing Linux systems for installation with a new Db2® database

## Before you begin

If you plan to install interactively, ensure that you have a supported version of Mozilla Firefox
installed.

## About this task

Because certain steps are specific to a version of the operating system, all steps might not
apply to your environment. If no qualifier is provided for a particular step, complete the step for
all versions of the operating system.

Business Automation Workflow does not
support different operating systems in the same cell, for example Red Hat Enterprise Linux 7 on one
node and Red Hat Enterprise Linux 8 on another node. All nodes must use the same operating
system.

## Procedure

Complete the following steps on your Linux
system before installing Business Automation Workflow:

1. Because WebSphere®
Application Server is a prerequisite of Business Automation Workflow, complete all the required preparation steps in
the Preparing Linux systems for installation topic in the WebSphere
Application Server documentation. 

Note: Some X11 libraries (specified in the previous link) are required for WebSphere
Application Server whether you use GUI
interfaces in Linux or not.
2. Check that you have administrative (root) privileges.
3. Increase the allowable stack size, number of open files, number of processes, and file size.
Add the following lines to the end of the /etc/security/limits.conf file or if
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
Preparing the operating system for product installation in the WebSphere
Application Server documentation.
4. Check for the existence of a file that is named
/etc/security/limits.d/90-nproc.conf or
/etc/security/limits.d/20-nproc.conf, which overrides the
nproc value set in the limits.conf file. If this file exists,
edit it and set the same nproc values that you specified in
limits.conf.
5. Check for the existence of a file name /etc/profile, which overrides the
nofile values set in the limits.conf file. If the
ulimit -n values exist in the /etc/profile file, edit it and
set the same nofile values that you specified in
limits.conf.
6. If you have previously installed and uninstalled Db2, check that the previous database entries
in the /etc/services file are deleted. For example, if the previous entry
DB2\_instance-name\_suffix 50000/tcp still exists, the new installation uses the
next available port, 50001, which might not work with your configuration. For more information, see
Verifying port range availability in the Db2
documentation
7. Restart the system.
8 Set the umask value to 077 using the following command: The value 077 is the most restrictive value that Business Automation Workflow tolerates. You can chooseto set a less restrictive umask value for the following access levels. Thisstep is optional.
    - umask 077
    - 037 for read-only access for a group of human administrators and tools
    - 027 for read and write access for a group of human administrators and tools
    - 007 for read, write, and execute access for a group of human administrators and tools
9. Restart the computer.
10. Complete the steps in Tuning Linux systems.
11. Check whether all servers that are involved are set to the same time. Use the same network time
protocol for all servers on all cluster nodes, including application, support, and database
clusters. A time mismatch causes erratic behavior, including duplicate system tasks.