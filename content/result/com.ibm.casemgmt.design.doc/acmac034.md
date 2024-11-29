# Configuring additional object stores for the production environment
by using the command line

## Before you begin

Be sure to have your completed configuration checklist available.

## About this task

You must edit and run the configuration XML
file for each object store. The configcmos.xml XML
file was created when you generated the development environment profile
files. You must create and run one additional configcmos.n.xml file
for each object store in your production environment.

## Procedure

To configure multiple object stores:

1. Change the current directory to the
install\_root/CaseManagement/configure directory, where
install\_root is the location where Business Automation Workflow is
installed.
2 If you have more than one objectstore in your production environment, generate an additional configcmos.n .xml fileby running the following command. Do not type any line breaks whenyou enter the command: configmgr\_cl generateConfig -task configcmos -profile myprofile [-silent] [-force] where -profile myprofile Specifies the profile to use. The myprofile value can be one of the following items: -silent Optional: When you specify the -silent parameter, no prompts orinformational messages are shown in the console, but the errors are written to the log. Failuremessages and validation error messages are shown as needed, such as messages about missing passwordsor invalid port numbers. If you run the execute command to run all the activitiesin a profile and you specify the -silent parameter, you must also specify the-force parameter. -force Optional and applies only when the -silent parameter is used. When youspecify the -force parameter, the activity is run without pausing for requiredresponses to validation error messages, such as messages about missing passwords or invalid portnumbers. For example, the following commandgenerates one configcmos.n .xml filefor the existing production environment profile that is named Production1: configmgr\_cl generateConfig -task configcmos -profile Production1

```
configmgr\_cl generateConfig 
 -task configcmos
 -profile myprofile
 [-silent] [-force]
```

where

    - The name of the profile, such as develop1. The profile is located in the
install\_root/CaseManagement/configure/profiles directory.
install\_root is the location where IBM® Business Automation
Workflow is installed.
    - The full path to the profile directory, such as
"install\_root\CaseManagement\configure\profiles\develop1" or
/install\_root/CaseManagement/configure/profiles/develop1.
    - The full path to the profile input file, such as
"install\_root\CaseManagement\configure\profiles\develop1\develop1.cfgp"
or
/install\_root/CaseManagement/configure/profiles/develop1/develop1.cfgp.

```
configmgr\_cl generateConfig 
 -task configcmos
 -profile Production1
```

3. Repeat 2 as
needed for each object store.
The file name increments
for each new file that you generate.
4 Edit the property values in the configcmos.n .xml filesthat you generated:

1. Use a text editor or XML editor
to open one of the configuration XML files that you generated.
2. Replace each occurrence of  ****INSERT VALUE**** with
a value appropriate for your site. 
See the descriptions
in the file for more information and use your configuration checklists.
      

Important: You are not required to store values
for passwords in the file. You can run the storePasswords command
later to add encrypted passwords to the file.
3. Replace empty values that have the format <value
/> with a value appropriate for your site.
Use
the format <value>my\_value</value>.
4. Verify that the default values for the remaining properties
are correct for your site.
5. Set the enabled attribute value
in the <configuration> tag to true in any
configuration XML file that you edit if you want to run the configuration
task.
When a task is disabled, the execute command
skips the task.
6. Save your edits and close the XML
file.
7. Repeat as needed until you edit all the configcmos.n.xml files
for your profile.
5. Run the configcmos tasks
in the profile one at a time by running the following command. Do
not type any line breaks when you enter the command:

configmgr\_cl execute -taskfile task\_file\_name
 -profile myprofile [-silent] [-force]
task\_file\_name is the name of the task file, configcmos.n.xml,
and n is a number larger than 2.
6. Repeat 5 as
needed for each object store that you generated a task file for.

## What to do next