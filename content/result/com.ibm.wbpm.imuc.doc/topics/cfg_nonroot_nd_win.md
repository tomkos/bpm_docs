# Granting write permission of files and directories to nonadministrative
users for profile creation or augmentation

## About this task

The
product installer (who can be an administrative or nonadministrative
user) can grant write permission to the appropriate IBM Business Automation Workflow files
and directories to nonadministrative users. The nonadministrative
users can then create profiles. Alternatively, the product installer
can create a group for users who are authorized to create profiles
or give individual users the authority to create profiles.

Nonadministrative
users create their own profiles to manage their own environments.
Typically, they manage environments for development purposes.

Nonadministrative
users must store their profiles in their private directory structure,
not in the installation\_root\profiles directory
of the product.

- IBM Business Automation Workflow does
not support changing ownership of existing profiles from the product
installer to nonadministrative users. A nonadministrative user cannot
augment profiles owned by another user.
- Mechanisms within the Profile Management Tool that suggest unique
names and port values are disabled for nonadministrative users. The
nonadministrative user must change the default field values in the
Profile Management Tool for the profile name, node name, cell name,
and port assignments. The product installer can assign nonadministrative
users a range of values for each of the fields, and assign responsibility
to the users for adhering to their assigned value ranges and for maintaining
the integrity of their own definitions.

If you already created at least
one profile, certain directories and files were created. You can skip
the steps in this topic that create these directories and files. If
no profile was previously created, you must complete the steps to
create the required directories and files.

The
following example task shows how to create a group that is authorized
to create profiles. The terms "installer" and "product installer"
refer to the user ID that installed IBM Business Automation Workflow. The
installer can perform the following steps to create the profilers group
and give the group appropriate permissions to create a profile.

## Procedure

1. Log in to the IBM Business Automation Workflow system
as the product installer. The product installer can be
a administrative or nonadministrative user.
2 Using operating system commands, performthe following steps:
    1. Create a group named profilers, which
will contain all users who can create profiles.
    2. Create a user named user1, who can
create profiles.
    3. Add users product\_installer and user1 to
the profilers group.
3. Log off and log back on as the installer to
pick up the new group.
4 If no profile exists, create the followingdirectories as the installer:

- Create the install\_root\logs\manageprofiles directory
by following instructions in the Windows documentation.
For this example procedure, the directory is:install\_root\logs\manageprofiles
- Create the install\_root\properties\fsdb directory
by following instructions in the Windows documentation.
For this example procedure, the directory is:install\_root\properties\fsdb
5. If no profile exists, create the profileRegistry.xml file
as the installer. For this example, the file path is: install\_root\properties\profileRegistry.xmlAdd
the following information to the profileRegistry.xml file.
The file must be encoded as UTF-8.<?xml version="1.0" encoding="UTF-8"?>
<profiles/>
6 Check if the directory install\_root \logs\config exists. Ifit does not exist, create the directory as the installer:

- Create the install\_root\logs\config directory by following
instructions in the Windows documentation. For this
example procedure, the directory
is:install\_root\logs\config
7. As the product installer, use operating
system tools to change directory and file permissions.   The following example assumes that the variable $WASHOME is the IBM Business Automation Workflow root installation directory C:\Program Files\IBM\WebSphere\AppServer. Follow instructions in the Windows documentation to give the profilers group read and write permission
to the following directories and their
files:@WASHOME\logs\manageprofiles
@WASHOME\properties
@WASHOME\properties\fsdb
@WASHOME\properties\profileRegistry.xml
@WASHOME\logs\config
@WASHOME\configurationYou
might have to change the permissions on additional files if the nonadministrative user encounters
permission errors. For example, if the product installer authorizes a nonadministrative user to
delete a profile, then the product installer might have to delete the following file:
install\_root\properties\profileRegistry.xml\_LOCKGive write
access to the nonadministrative user for the file to authorize the user to delete the file. If the
nonadministrative user still cannot delete the profile, then the product installer can delete the
profile.

## Results

The installer created the profilers group
and gave the group the correct permissions to the directories and
files required for a nonadministrative user to create profiles.

## What to do next

The nonadministrative user that belongs
to the profilers group can create profiles in a directory
that the nonadministrative user owns and to which the nonadministrative
user has write permission. However, the nonadministrative user cannot
create profiles in the installation root directory of the product.

The
administrative user and the nonadministrative user can use the same
tasks to manage profiles.