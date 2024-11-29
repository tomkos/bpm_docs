<!-- image -->

# Resolving communication problems with remote UTE servers

## About this task

Starting
the integration test client has encountered a problem. Cannot start
application application\_name.

In
many situations, communication problems with remote servers are caused
by an incorrect server connection setting in Integration Designer
or incorrect server settings or system settings on the remote machine.
For example, when you created a server connection in Integration Designer,
you may have specified an IP address instead of a host name. Or you
may have installed the remote server with a host name of localhost rather
than an actual host name. To ensure that these settings are correct,
complete the steps in the following procedure.

## Procedure

1. In the file system of the remote machine, open the file serverindex.xml that
is located in the installation path of your server profile. The
default installation path for a server profile is:C:\IBM\IID\PS\v8.5\profiles\profile\_name\config\cells\cell\_name\nodes\node\_name\serverindex.xml
For
example:
C:\IBM\IID\PS\v8.5\profiles\AppSrv01\config\cells\localhostNode01Cell\nodes\nlNode01\serverindex.xml
2. In the serverindex.xml file, ensure that the hostName parameter
is not set to localhost (which can cause problems
in publishing and reporting status for the server). If it is set to localhost,
change the value of the hostName parameter to
the actual host name. For example: <?xml version="1.0" encoding="UTF-8"?>
<serverindex:ServerIndex xmi:version="2.0"
 xmlns:xmi="http://www.omg.org/XMI"
 xmlns:serverindex="http://www.ibm.com/websphere/appserver/schemas/5.0/serverindex.xmi"
 xmi:id="ServerIndex\_1"
 hostName="MyHostName">
<serverEntries ...
Tip: You can change
the value of the hostName parameter to the actual
host name at the command line level or console. To change the value
of hostName, see  Changing the node host names.
3. Save your changes and restart the remote server.
4 If you continue to experience problems in communicatingwith the remote server, complete the following steps:
    1. In the file system of the local machine where IBM® Integration
Designer is
installed, open the file hosts that is located in the following
path: C:\WINDOWS\system32\drivers\etc
    2. In the hosts file, ensure that there is an entry to
map the IP address of the remote server to its host name. Any entry
that maps an IP address to a host name must be specified on a separate
line in the file. The IP address must be placed in the first column
followed by at least one space and then the corresponding host name.
For example:9.186.64.134  MyRemoteServerHostName
    3. Save your changes.
    4. Republish to the remote server. (If you are working
with the integration test client, you can click the Run icon
to republish.)