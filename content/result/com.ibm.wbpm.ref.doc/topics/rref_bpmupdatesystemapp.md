# BPMUpdateSystemApp command

The BPMUpdateSystemApp command is run
using the AdminTask object of the wsadmin scripting client.

## Prerequisites

The following conditions must be met:

- Run the command in disconnected mode; that is,
with the server stopped. Use the -conntype none option.
- Run the command on the deployment manager node.
- To avoid out-of-memory problems, add the following options when
you start the wsadmin command: -javaoption -Xms256m -javaoption
-Xmx1024m. The default Java virtual machine settings for
the memory allocation pool (-Xmx) and maximum heap
size (-Xms) are sometimes not large enough for running
the BPMUpdateSystemApp command.

## Location

Start the wsadmin scripting client from the install\_root/profiles/deployment\_manager\_profile/bin directory.

## Syntax

```
BPMUpdateSystemApp 
-twxFile full\_path\_of\_the\_updated\_system\_.twx\_file
-clusterName cluster\_name
[-purge]
```

## Parameters

## Example for a network deployment environment

In
this example, you apply an interim fix to the database for a network
deployment environment. After you use Installation Manager to install
an interim fix, the .twx file in this path is updated: install\_root/BPM/Lombardi/imports.
The following commands show you how to use that updated file to apply
the interim fix to the database.

```
wsadmin -lang jython -conntype none -javaoption -Xms256m -javaoption -Xmx1024m

wsadmin>AdminTask.BPMUpdateSystemApp( [ '-twxFile', 'install\_root/BPM/Lombardi/imports/system-toolkit.twx', '-clusterName', 'PC\_clusterName' ] )
```

## Applying an interim fix

1. Use Installation Manager to install an interim fix into the install\_root path.
2. If under one installation you created multiple application clusters
that point to a different Process database server, use the command
to apply the interim fix to those clusters one by one. To apply an
interim fix to a cluster, you can use one member of the cluster.
3. If the interim fix requires a profile upgrade (as stated in the
post-IM installation steps section of the interim fix readme file),
you must run the profile upgrade command before you run the BPMUpdateSystemApp command
to update the toolkits or process apps.
4. Switch to the /bin directory of a profile.
5. Run the wsadmin command and pass the path of the .twx file
that was changed by the interim fix. See the interim fix readme for
the name of the .twx file to use for the -twxFile parameter.

## Rolling back an interim fix

1. Use Installation Manager to uninstall an interim fix from the install\_root.
2. If under one installation you created multiple profiles, use the
wsadmin command to roll back the interim fix against those profiles
one by one.
3. If the interim fix requires a profile upgrade (as stated in the
post-IM installation steps section of the interim fix readme file)
as part of the uninstallation procedure, you must run the profile
upgrade command before you run the BPMUpdateSystemApp command
to roll back the toolkits or process apps.
4. Switch to the /bin directory of a profile.
5. Run the wsadmin command and pass the path of the .twx file
that was changed by the interim fix. See the interim fix readme for
the name of the .twx file to use for the -twxFile parameter.