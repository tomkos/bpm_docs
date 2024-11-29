# Configuring the case development environment by using the command line

## About this task

Configuring the development domain includes configuring Case Builder and Case Client. You must
create a profile for each development environment instance that you are configuring.

## Procedure

To configure the development environment:

1. Run the BPMConfig command to create the profiles for your development
environment.
If you have already created the dmgr and node profiles for your development environment, skip
to the next step.
2. Change the current directory to the
dmgr\_profile\_root/CaseManagement/DE\_name/profiles/ICM\_dev
directory.
3 Referring to Development environment tasks and files , edit the property values in the configuration XML filesthat you generated:
    1. Use a text editor or XML editor to open one of the configuration XML files that you
generated.
    2. Replace each occurrence of ****INSERT VALUE**** with a value that is
appropriate for your site. 
To change the default value to a blank value, replace <value>****INSERT
VALUE****</value> with <value />. See the descriptions in the
file for more information. Important: You are not required to store values for passwords
in the file. You can run the storePasswords command later to add encrypted
passwords to the file before you run the task.
    3. Replace empty values that have the format <value /> with a value that is
appropriate for your site.
Use the format
<value>my\_value</value>.
    4. Verify that the default values for the remaining properties are correct for your site.
    5. Verify that the task is enabled for each required task. Set the enabled
attribute value in the <configuration> element to true in any
configuration XML file that you edit if you want to run the configuration task.
When a task is disabled, the execute command skips the task. For example,
the registerexternaldataurl.xml file has the enabled
attribute value in the <configuration> element set to false by default,
and the task will be skipped.
    6. Save your edits and close the XML file.
    7. Repeat as needed until you edit all the required files.

Important: You must provide values for all of the entries in the
websphereapplicationserver.xml file, the
contentengineserver.xml file, and the
contentnavigatorserver.xml file before you can run any of the tasks.
4. If you are running Linux on POWER Little Endian (LE), modify the
install\_root/CaseManagement/configure/comfigmgr.ini file to
point to JDK 1.8 by making the following change:

-vm
/opt/install\_root/java\_1.8\_64/bin
5. Optional: 
Add encrypted passwords to the XML files by running the storePasswords
command for the profile.

Tip: If you do not add passwords to the XML files, you are prompted for the passwords
when you run the task for each file.

For example, the following command stores all the passwords in the profile named
myprofile1: 
configmgr\_cl storepasswords -profile myprofile1
6. Change to the install\_root/CaseManagement/configure
directory and run all of the tasks in the development profile by using the following command:

configmgr\_cl execute -profile myprofile
 [-silent] [-force] For more information about the syntax, see execute command.Note: On AIX, if IBM SDK is updated to version 8.0.6.25 or later, the Eclipse launcher might be
unable to load libjgskit.so and libjgsk8iccs\_64.so. You must
export the LIBPATH variable before you run the configmgr\_cl
command. To export LIBPATH, use the following command, where
<baw\_install\_root> is your Business Automation Workflow installation path:
export
LIBPATH=$LIBPATH:<baw\_install\_root>/java/jre/lib/ppc64:<baw\_install\_root>/java/jre/lib/icc.
7. You can check the task status by running the checkStatus command. For
example configmgr\_cl checkStatus -profile myprofile For more
information, see checkStatus
command.
8. Restart the application server.

## What to do next

- Development environment tasks and files

The BPMConfig command creates a profile that consists of a set of files that contain information about your development environment. You can edit the component files and the task files to update or add information before you run the tasks.