# Using the BPMConfig command to export system data for performance
analysis

## Before you begin

You can use the BPMConfig command to
export system data on machines that are running Linux or one of the
supported Unix operating systems. However, you cannot use the BPMConfig command
to export system data on machines that are running the Windows operating
system.

When you run the BPMConfig command
to export system data, it uses an input file to invoke four commands
that are specific to Linux and Unix. Although three of the commands
are installed by default in the operating systems, the iostat command
is not installed by default. If your operating system supports the
use of the iostat command, you should install it
from the sysstat install package. You can export
system data without the use of the iostat command,
but the exported data will not include storage input and output statistics
for the operating system.

The BPMConfig command
uses the existing Tivoli Remote Execution and Access (RXA) toolkit
to run specific local commands on remote machines. However, the RXA
toolkit requires Secure Shell (SSH) to be installed and enabled on
your machines. To enable SSH, configure OpenSSH 3.6.1, OpenSSH 4.7
(on AIX), or Oracle SSH 1.1 to support RXA connections. (OpenSSH 3.7.1
or later contains security enhancements that are not available in
earlier releases and it is recommended.) For more information about
enabling SSH, refer to the SSH documentation for your corresponding
operating system.

## About this task

When you run the BPMConfig command
to export system data, it uses an input file to invoke the following
four commands:

## Procedure

To use the BPMConfig command to export
system data for performance analysis:

1. Ensure that your local user account has sufficient privileges
to run the BPMConfig command with the –export parameter.
Information about the BPMConfig command is found
in the topic BPMConfig command-line utility.
2. Ensure that your input user (root user or common user)
has sufficient privileges to run the top, vmstat, iostat,
and uname commands. If you do not have sufficient
privileges for running these commands, an error message will be issued.
3. In the file system, navigate to the following sample input
file (which will be passed to the BPMConfig command):
install\_root/BPM/samples/config/performanceanalysis/PerformanceAnalysis.properties
4. Open the PerformanceAnalysis.properties input
file in a text editor. The input file contains properties
that are similar to the ones shown in the following example:machine.1.hostname=
machine.1.username=
machine.1.password=
#optional, in seconds
machine.1.commandsTimeout=
#optional
machine.1.vmstat.commandOptions=
#optional
machine.1.iostat.commandOptions=
#optional
machine.1.top.commandOptions=

machine.2.hostname=
machine.2.username=
machine.2.password=
#optional, in seconds
machine.2.commandsTimeout=
#optional
machine.2.vmstat.commandOptions=
#optional
machine.2.iostat.commandOptions=
#optional
machine.2.top.commandOptions=
5. For the machine.#.hostname properties,
specify an IP address for both the node machine and the database machine.
6. For the machine.#.username and machine.#.password properties,
specify a user name and password for both the node machine and the
database machine.
7. For the optional machine.#.command\_name.commandOptions properties,
you can specify a value for one or more of the four Linux/Unix commands
on both the node machine and the database machine. For
example, for the machine.1.vmstat.commandOptions property,
you could specify the following value:machine.1.vmstat.commandOptions=vmstat 2 5If
a value is not specified for the machine.#.command\_name.commandOptions properties,
the following default values are used:
iostat 2 10
vmstat 2 10
top -d 10 -n 2 -b
uname -a
8. For the optional machine.#.commandsTimeout properties,
you can specify a value (in seconds) for both the node machine and
the database machine to control how long all of the Linux/Unix commands
can run together in total before they automatically time out. If you
don't specify a value for this property, the default value of 300 seconds
is used. Without this property, you could potentially
specify a value for a machine.#.command\_name.commandOptions property
that would cause the command to run indefinitely. For example, if
you specified the value iostat -d 2 for the machine.1.iostat.commandOptions property,
the command would return a continuous device report at two-second
intervals and would run indefinitely until it was manually terminated.
9. Ensure that you can connect to the node and database machines
using the specified host names, user names, and passwords, then save
and close the PerformanceAnalysis.properties input
file.
10. Run the following command (where ProfileName is
the name of a deployment manager profile or stand-alone profile and outputDir is
the full path to the configuration output directory where you want
the results to be generated): BPMConfig.sh -export -profile ProfileName [-de deName] -system inputFile.properties [-outputDir outputDir]For
example:
BPMConfig.sh -export -profile DmgrProfile -de De1 -system /home/user/performanceAnalysis.properties -outputDir /home/user/outputNote: If
there is only one deployment environment in the WebSphere cell, you
can omit the -de option.
When you run the command using this syntax, the output is returned to the deployment manager
machine and it is grouped by machine name as part of the command output. If you specify the optional
-outputDir option and an output directory name, a new directory named
systemPerformanceResult is generated under the specified output directory. If
you do not specify the -outputDir parameter, the
systemPerformanceResult directory is generated under the default output
directory install\_root/temp/deName.
Note: If
you intend to run the command more than once because you have more
than one deployment environment, remember to specify different output
directory names whenever you use the -outputDir parameter.
11. After you run the command, switch to the underlying systemPerformanceResult directory,
which is either under the output directory that you specified with
the -outputDir parameter or under the default
output directory (if you did not specify the -outputDir parameter).
The systemPerformanceResult directory
contains a subdirectory for each machine. And in each machine subdirectory,
there is a summary.txt file as well as a text
file for each Linux/Unix command that was run. The following example
shows the directory structure under the systemPerformanceResult directory:
outputDir/systemPerformanceResult/machine1/iostat.txt
                                          /vmstat.txt
                                          /top.txt
                                          /uname.txt
                                          /summary.txt
                                 /machine2/iostat.txt
                                          /vmstat.txt
                                          /top.txt
                                          /uname.txt
                                          /summary.txt
                                 .
                                 .
                                 .The content of the
text files for the commands is exactly the same as the content that
you would get from running each command in the shell environment.
12. Navigate to the subdirectory for each machine, then use
a text editor to open the text files and read and analyze the system
data.