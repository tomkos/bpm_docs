# Creating a master archive of a Process Federation Server configuration

## Before you begin

## Procedure

1. Stop Process Federation Server.
2. Open a command prompt, then change the directory to the pfs\_install\_root/bin directory.
3. Package the Process Federation Server installation.
Both .zip and .jar archive formats are supported. To preserve
file permissions, use the .jar format.Enter the following
command.server package server\_name --archive=package\_file\_name.jar --include=all
Where:
server\_name
The Process Federation Server name.
If you do not specify a server name, defaultServer is
used.Restriction: Ensure that the server name contains
only the following characters. In addition, the server name cannot
start with a period (.) or a dash (-).0-9 A-Z a-z + - . \_

--archive package\_file\_name
The target file for the package operation. The file name can include
a full path name. If the full path is omitted, a compressed file called package\_file\_name.jar
is created in the pfs\_install\_root/usr/servers/server\_name directory.
If you do not specify the --archive parameter,
the value of server\_name is used for package\_file\_name,
and the compressed file is created in the pfs\_install\_root/usr/servers/server\_name directory.
--include all
Packages the runtime binaries and the relevant files in the pfs\_install\_root directory.