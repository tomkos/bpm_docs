# Preparing AIX systems
for installation

## About this task

Business Automation Workflow does not support
different operating systems in the same cell, for example AIX 7.1 on one node and AIX 7.3 on another
node. All nodes must use the same operating system.

For more information on configuring
IBM Installation
Manager to run on
64-bit AIX systems, see IBM Installation Manager and WebSphere Application Server Installation Common
Issues.

## Procedure

Complete the following steps on your AIX system
before installing Business Automation Workflow:

1. Because WebSphere®
Application Server is a prerequisite of Business Automation Workflow, complete the required preparation steps in the
Preparing AIX systems for installation topic in the WebSphere
Application Server documentation. 
Note: Make sure the X Window System (X11) is installed.
2 Increase the maximum number of open files and the maximum file size. The default settings areusually not enough. You can check the current maximum number of open files by using ulimit-n and the current maximum file size by using ulimit -f . The followingexample shows the maximum number of open files being increased to 8800 and the maximum file size to6291453, which is large enough for most systems. The ulimit requirement is dynamically calculated atinstallation time and might need to be larger based on the options you select. Before installing, run the following commands: Alternatively, you can use the following steps to edit the resource limits file:

Before installing, run the following commands:

    - ulimit -n 8800
    - ulimit -f 6291453

Alternatively, you can use the following steps to edit the resource limits file:

    1. Open /etc/security/limits.
    2 Edit or add the default section and include these lines:
        - nofiles = 8800
        - fsize = 6291453
3. Save and close the file.
4. Log off from the operating system and log in again.
3 Set the umask value to 077 using thefollowing command: The value 077 is the most restrictive value that Business Automation Workflow tolerates. You canoptionally choose to set a less restrictive umask value for the followingaccess levels:

- umask 077

- 037 for read-only access for a group of human administrators and tools
- 027 for read and write access for a group of human administrators and tools
- 007 for read, write, and execute access for a group of human administrators and tools
4. If you plan to install interactively, ensure that you have a supported version of Mozilla
Firefox installed.
5 Before starting the data movement service, increase the number of processes that areconfigured in the AIX operating system to avoid a connection reset error. You can increase thenumber of processing by using a command, or by using the AIX interface.

- Run the command:chdev  -l sys0 -a maxuproc='256'
- In the AIX interface, enter smitty, then select System
Environments > Change / Show Characteristics of Operating
System > Number of processes allowed per user(Num.).
6. Complete the steps in Tuning AIX systems.
7. Ensure all servers that are involved are set to the same time. Use the same network time
protocol for all servers on all cluster nodes, including application, support, and database
clusters. A time mismatch causes erratic behavior, including duplicate system tasks.