<!-- image -->

# Installing and configuring a swinging profiles environment

## Procedure

To install and configure an environment for swinging profiles, complete the following
steps:

1 On the computer that will hold the master product installation:
    1. Create a directory for the master installation, for example:

mkdir -p /opt/BPMInstall/MASTER/AppServer
    2. Create a common profile directory, for example:

mkdir -p /opt/BPMCommonArea
    3. Create a symbolic link for the master installation directory under the common profile
directory, for example:

ln -s /opt/BPMInstall/MASTER/AppServer /opt/BPMCommonArea/BPMLink
    4. Install IBM® Installation
Manager, WebSphere® Application
Server, and Business Automation Workflow on the master server. 
Use the symbolic link as the installation directory in Installation Manager. In the example, the installation directory is
/opt/BPMCommonArea/BPMLink.Important: Use custom installation to
install Business Automation Workflow. Do not create any profiles on
the master server.

As a result of the symbolic link, the product is installed to the master installation
directory, BPMInstall/MASTER/AppServer in the example. All fix packs and
interim fixes are applied to this installation, but it is not used to create profiles.
    5. Copy the contents of the master installation directory
(BPMInstall/MASTER/AppServer in the example) to another directory and compress
it to a TAR file, for example:

mkdir /opt/CLONE\_18002
cp -R /opt/BPMInstall/MASTER/AppServer/* /opt/CLONE\_18002/
tar -cvf CLONE\_18002.tar CLONE\_18002/
2 On the first computer where you intend to create profiles:

1. Get the TAR file from the master computer and decompress the archive, for example:

tar -xvf CLONE\_18002.tar
2 Create the common profile directories and subdirectories that are required. You can create theprofile directories anywhere outside the decompressed installation directory. Forexample:mkdir -p /opt/BPMUserData/logs/manageprofilesmkdir /opt/BPMUserData/propertiesmkdir /opt/BPMUserData/profiles
    - Main common profile directory, for example /opt/BPMUserData, referred to
as common\_profile\_dir
    - Common profile subdirectories:
        - common\_profile\_dir/logs
        - common\_profile\_dir/logs/manageprofiles
        - common\_profile\_dir/properties
        - common\_profile\_dir/profiles

```
mkdir -p /opt/BPMUserData/logs/manageprofiles
mkdir /opt/BPMUserData/properties
mkdir /opt/BPMUserData/profiles
```

3. Modify the following properties in the properties/wasprofile.properties
file to point to the common profile directories that you defined in the previous substep.
In this example, change the following
lines:WS\_CMT\_LOG\_HOME=${was.install.root}/logs/manageprofiles
WS\_PROFILE\_REGISTRY=${was.install.root}/properties/profileRegistry.xml
WS\_WSPROFILE\_DEFAULT\_PROFILE\_HOME=${was.install.root}/profiles
to:
WS\_CMT\_LOG\_HOME=/opt/BPMUserData/logs/manageprofiles
WS\_PROFILE\_REGISTRY=/opt/BPMUserData/properties/profileRegistry.xml
WS\_WSPROFILE\_DEFAULT\_PROFILE\_HOME=/opt/BPMUserData/profiles
4. Create a symbolic link to point to the installation directory that you decompressed on this
computer, for example:

ln -s /opt/CLONE\_18002 /opt/BPMCommonArea/BPMLinkJust as the
BPMLink link on the master computer points to the installation directory on the
master computer, the  BPMLink link on the cloned computer points to the
installation directory on the cloned computer.
5. Make sure that the following Business Automation Workflow
directories have write permission, especially for non-root users.

install\_root/configuration
install\_root/profileTemplates
install\_root/properties
install\_root/temp
install\_root/logs
6. Using the symbolic link, run the BPMConfig command to create the profiles
and deployment environment, for example:

/opt/BPMCommonArea/BPMLink/bin/BPMConfig.sh -create -de /opt/Advanced-PCSingleCluster-
DB2.properties

All profile artifacts, such as the updated profile registry, logs, and the profile
itself, are created in the common profile directories.
7 If you want to use case management, check that your directories are set up correctly and havethe right permissions.

- Make sure that the network shared directory is set to an existing folder that is outside the
IBM Business Automation
Workflow installation folder. If you used the
default property for the bpm.de.caseManager.networkSharedDirectory when you
created your deployment environment, use the BPMConfig -update command to change
the network directory.
- When you set up the Business Rules and Forms directories, make sure that they point to folders
outside the IBM Business Automation
Workflow installation folder.
- If you want to keep case configuration tool logs, the logs folder must be outside the IBM Business Automation
Workflow installation folder. You can change the log
folder in the CaseManagement/configure/log4j.properties file.
- Make sure that the following folders have read and write
permissions:install\_root/BPM/FileNet/lib
install\_root/BPM/Case/lib
install\_root/CaseManagement
8. Complete the remainder of the installation steps, following the instructions for your operating
system and database. 
For example, if you are using Linux and DB2, start at step 6 in Configuring profiles and creating a network deployment environment using BPMConfig on Linux. If the bpm.de.deferSchemaCreation property in
the configuration properties file was set to true, you must run the SQL scripts to create the
database tables and, if your environment includes Workflow Server, run the
bootstrapProcessServerDatabase command to finish configuring Business Automation Workflow before you can start the deployment
environment.

When you finish all installation and configuration steps, test to make sure that the installation
was successful and Business Automation Workflow is running
correctly.
3. Repeat Step 2 on all other computers where you want to install Business Automation Workflow and be able to swing the profiles.

## Results

After you configure your environment for swinging profiles, you can update or roll back the
product service level by applying service to the master installation and swinging profiles to an
updated application server copy.

## Related information

- BPMConfig command-line utility