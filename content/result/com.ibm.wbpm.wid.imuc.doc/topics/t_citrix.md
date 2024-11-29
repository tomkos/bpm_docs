<!-- image -->

# Installing on Citrix Presentation Server

## About this task

## Procedure

1. When you install IBM Integration
Designer on
the server, ensure that you are logged on as a user with administrator
access.
2. After installing, ensure that the installation directory
is read-only. This is the product directory, not the shared install
directory. This step will ensure that the configuration information
is written in the home directory. If this measure is not taken, all
users will end up using the same location for their configuration
area, which is not supported. Note: Ensure that client users are granted write permission to the following directory, or the
integrated test environment server status can't be detected:
install\_root\runtimes\bi\_version\_stub\
3. When launching IBM Integration
Designer from
a client, the workspace is created in a directory specified by the
user.
4. To use the servers in the test environment, a profile is required for each
non-administrator user. The product installer can grant write permission to the appropriate IBM Business Automation
Workflow files and
directories to other non-administrator users. The non-administrator users can then create profiles.
Alternatively, the product installer can create a group for users who are authorized to create
profiles or give individual users the authority to create profiles. The following example task shows
how to create a group that is authorized to create profiles.

## Configuring the Citrix Presentation Server

### About this task

### Procedure

1. Log on to the IBM Integration
Designer system as the product
installer (the product installer can be an administrator or non-administrator user).
2 Using operating system commands, do the following tasks:
    1. Create a group named profilers, which will contain all users who can create
profiles.
    2. Create a user named user1, who can create profiles.
    3. Add users product\_installer and user1 to the
profilers group.
3. As the product installer, set access control to grant profilers read and write permission
to these directories and files under the install\_root
(C:\IBM\IID\Workflow\v2103). Follow instructions in the Citrix and Windows
documentation to give the profilers group read and write permission to the following directories and
their files: 
C:\IBM\IID\Workflow\v2103\logs\manageprofiles
C:\IBM\IID\Workflow\v2103\logs\config
C:\IBM\IID\Workflow\v2103\properties
C:\IBM\IID\Workflow\v2103\properties\fsdb
C:\IBM\IID\Workflow\v2103\properties\profileRegistry.xmlYou might have to change the
permissions on additional files if the non administrative user encounters permission errors. For
example, if the product installer authorizes a non administrative user to delete a profile, then
product installer might have to delete the following file:
install\_root\properties\profileRegistry.xml\_LOCKGive write access to the
non-administrator user for the file to authorize the user to delete the file. If the
non-administrator user still cannot delete the profile, then the product installer can delete the
profile.

### Results