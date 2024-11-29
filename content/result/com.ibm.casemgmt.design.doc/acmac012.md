# Configuring the production environment by using the command line

## About this task

Configuring the production domain includes configuring Case Client.

## Procedure

To configure the production environment:

1. Run the BPMConfig command to create the profiles for your production
environment.
If you already created the dmgr and node profiles for your production environment, skip to the
next step.
2. Change the current directory to the
dmgr\_profile\_root/CaseManagement\_DE\_name/profiles/ICM\_prod
directory.
3 Referring to Production environment tasks and files , edit the property values in the configuration XML filesthat you generated:
    1. Use a text editor or XML editor to open one of the configuration XML files that you
generated.
    2. Replace each occurrence of ****INSERT VALUE**** with a value that is
appropriate for your site. 
To change the default value to a blank value, replace <value>****INSERT
VALUE****</value> with <value />. For more information, see
the descriptions in the file. Important: You are not required to store values for
passwords in the file. You can run the storePasswords command later to add
encrypted passwords to the file before you run the task.
    3. Replace empty values that have the format <value /> with a value
appropriate for your site.
Use the format
<value>my\_value</value>.
    4. Verify that the default values for the remaining properties are correct for your
site.
    5. Verify that the task is enabled for each required task. Set the enabled
attribute value in the <configuration> element to true in any
configuration XML file that you edit if you want to run the configuration task.
When a task is disabled, the execute command skips the task. For example,
the registerexternaldatauri.xml file has the enabled
attribute value in the <configuration> element set to false by default,
and the task is skipped.
    6. Save your edits and close the XML file.
    7. Repeat as needed until you edit all the required files.

Important: You must provide values for all the entries in the
websphereapplicationserver.xml file, the
contentengineserver.xml file, and the
contentnavigatorserver.xml file before you can run any of the tasks.
4. Optional: 
Add encrypted passwords to the XML files by running the storePasswords
command for the profile.

Tip: If you do not add passwords to the XML files, you are prompted for the passwords
when you run the task for each file.

For example, the following command stores all the passwords in the profile named
myprofile1: configmgr\_cl storePasswords -profile myprofile1
5. Change to the install\_root/CaseManagement/configure
directory and run the tasks in the development profile by using the following command:

configmgr\_cl execute -profile myprofile
 [-silent] [-force] For more information about the syntax, see execute command.
6. You can check the task status by running the checkStatus command. For
example configmgr\_cl checkStatus -profile myprofile For more
information, see checkStatus
command.
7. Restart the application server.

## What to do next

- Production environment tasks and files

The BPMConfig command creates a profile that consists of a set of files that contain information about your production environment. You can edit the component files and the task files to update or add information before you run the tasks.
- Configuring additional object stores for the production environment by using the command line

You must configure the case management object store for each object store in your production environment. You can create a new configuration XML file for each object store and use the command line to run the task.