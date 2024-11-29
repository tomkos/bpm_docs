<!-- image -->

# Applying an interim fix  or cumulative fix by swinging profiles

## Before you begin

To associate a profile with a different installation by following this procedure, your
environment must be configured for swinging profiles. For more information, see Installing and configuring a swinging profiles environment.

## About this task

The BPMEnablePostInstaller command for enabling the necessary post installation
script is only supported for IBM Business Automation
Workflow interim
fixes and cumulative fixes. This command is not supported for WebSphere® Application
Server or Java SDK interim fixes.

## Procedure

To apply the interim fix or cumulative fix, complete the following steps:

1 On the computer that holds the master product installation:
    1. Use IBM Installation
Manager to apply the Business Automation Workflow interim fix or cumulative fix as usual.
    2. Copy the contents of the master installation directory to another directory and compress to a
TAR file, for example:

mkdir CLONE\_18002\_iFixes
cp -R /opt/BPMInstall/MASTER/AppServer/* /opt/CLONE\_18002\_iFixes/
tar -cvf CLONE\_18002\_iFixes.tar CLONE\_18002\_iFixes/
2 On each computer where you created profiles:

1 Stop all the Java processes associated with the Business Automation Workflow products that are being upgraded. Note: If you are applying a cumulative fix, this step is done as part of the normal upgradinginstructions.
    1. Stop the single cluster or the three clusters in the following order: Support, Application, and
then Messaging.
    2. Stop any other servers, the node agents, and then the deployment manager.
    3. Stop any other associated JVMs, such as the Profile Management Tool or the Quick Start
console.
    4. If you have a Microsoft Windows service or another function that automatically restarts the
servers when they are down, ensure that the service or function is disabled until the upgrade
process is complete.Important: The product might not continue to run successfully if you
install the fix when a Java process related to WebSphere Application
Server is running.
2. Get the TAR file from the master computer and decompress the archive, for example:

tar -xvf CLONE\_18002\_iFixes.tar
3. Modify the following properties in the properties/wasprofile.properties
file to point to the common profile directories that you previously created on this computer in step
2c in Installing and configuring a swinging profiles environment.
For example, change the following
lines:WS\_CMT\_LOG\_HOME=${was\_install\_root}/logs/manageprofiles
WS\_PROFILE\_REGISTRY=${was\_install\_root}/properties/profileRegistry.xml
WS\_WSPROFILE\_DEFAULT\_PROFILE\_HOME=${was\_install\_root}/profiles
to:
WS\_CMT\_LOG\_HOME=/opt/BPMUserData/logs/manageprofiles
WS\_PROFILE\_REGISTRY=/opt/BPMUserData/properties/profileRegistry.xml
WS\_WSPROFILE\_DEFAULT\_PROFILE\_HOME=/opt/BPMUserData/profiles
4. Change the symbolic link that you created in step 2d in Installing and configuring a swinging profiles environment to point
to the installation directory that you just decompressed on this computer, for example:

rm /opt/BPMCommonArea/BPMLink
ln -s /opt/CLONE\_18002\_iFixes /opt/BPMCommonArea/BPMLink
5. Use the BPMConfig -update command to change the network shared directory to
the folder you set. If you didn't set this directory in the previous version, set the
bpm.de.caseManager.networkSharedDirectory to an existing folder that is outside
the IBM Business Automation
Workflow installation folder.
6 Run the BPMEnablePostInstaller command to enable the necessarypost-installation scripts for the cumulative fix or interim fixes that were installed. If you are installing a few interim fixes, you can specify the fix name as the input parameterand separate the names with commas, forexample:BPMEnablePostInstaller.sh -ifix 8.6.0.0-WS-BPM-IFJR00000,8.6.0.0-WS-BPM-IFJR11111 Ifyou are installing many interim fixes, you do not need to specify the file names, forexample:BPMEnablePostInstaller.sh -ifix If you are installing a cumulativefix, you do not need to specify the file name, forexample:BPMEnablePostInstaller.sh Note: For case management:

```
BPMEnablePostInstaller.sh -ifix 8.6.0.0-WS-BPM-IFJR00000,8.6.0.0-WS-BPM-IFJR11111
```

```
BPMEnablePostInstaller.sh -ifix
```

```
BPMEnablePostInstaller.sh
```

- Every time you update IBM Business Automation
Workflow, run the
BPMEnablePostInstaller command to update the INI files.
- If you are using an external Content Platform Engine, every
time you replace the IBM Business Automation
Workflow installation files
to update IBM Business Automation
Workflow or update the version of the
external Content Platform Engine, you must run the
updateBPMExternalECM command to download those Content Platform Engine libraries again as mentioned in the upgrading
instructions.
7. Follow the upgrading steps to upgrade the database and profile. When you are finished
upgrading, start the environment and verify that the interim fix or cumulative fix installation was
successful.

Important: When you are applying a cumulative fix, make sure you wait to start the
environment only when directed to do so by the upgrading instructions.

## Related information

- BPMEnablePostInstaller command-line utility
- BPMConfig command-line utility
- updateBPMExternalECM command