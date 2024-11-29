# Deploying a legacy case solution to a production target object store by using the command
line

## Before you begin

Ensure that you exported the solution package from the
development environment design object store and imported it to the
production environment staging object store.

Be sure to have
your completed configuration checklists available.

## About this task

The IBM® Business Automation
Workflow Case
configuration tool stores your settings for the case deployment profile in a set of XML
configuration files that is called a profile. The XML files contain the properties and values that
describe the associated configuration and deployment tasks. You must provide values for the profile
properties that are specific to each configuration at your site, such as the application server
name.

| Configuration and task information                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | XML file                                                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| Settings for deploying an IBM Business Automation Workflow solution into a production target object store. You need one configuration file for each production environment target object store that you deploy a solution to. You can create additional task files in the same profile, or you can create a separate profile for the additional settings. When you generate a second solution deployment configuration file in a profile, it is named deploysolution.2.xml. The file name increments for each new file that you generate. You cannot change the file name, but you can edit the value in the file for the name of the task. | deploysolution.xml deploysolution.n.xml. n is an integer starting with 2. |

## Procedure

To deploy a solution:

1. Change the current directory to the
install\_root/CaseManagement/configure directory, where
install\_root is the location where Business Automation Workflow is
installed.
2 If you want to create additionaldeployment configuration files in the same profile, generate an additional deploysolution.n .xml fileby running the following command. Do not type any line breaks whenyou enter the command: configmgr\_cl generateConfig -task deploysolution -profile myprofile -profileType prodenv [-silent] [-force] -profile myprofile Specifies the profile to use. The myprofile value can be one of the following items: -profileType prodenv Specifies the type of profile and must be prodenv for WebSphere® ApplicationServer . -silent Optional: When you specify the -silent parameter, no prompts orinformational messages are shown in the console, but the errors are written to the log. Failuremessages and validation error messages are shown as needed, such as messages about missing passwordsor invalid port numbers. If you run the execute command to run all the activitiesin a profile and you specify the -silent parameter, you must also specify the-force parameter. -force Optional and applies only when the -silent parameter is used. When youspecify the -force parameter, the activity is run without pausing for requiredresponses to validation error messages, such as messages about missing passwords or invalid portnumbers. For example, the following commandgenerates one deploysolution.n .xml filesfor the existing case deployment profile that is named deploy\_solution: configmgr\_cl generateConfig -task deploysolution -profile deploy\_solution

```
configmgr\_cl generateConfig 
 -task deploysolution
 -profile myprofile
 -profileType prodenv
 [-silent] [-force]
```

    - The name of the profile, such as develop1. The profile is located in the
install\_root/CaseManagement/configure/profiles directory.
install\_root is the location where IBM Business Automation
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
 -task deploysolution
 -profile deploy\_solution
```

3 Edit the property values in the deploysolution.xml filesthat you generated in the case deployment profile:

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
in the <configuration> tag to true in
any configuration XML file that you edit if you want to run the configuration
task.
When a task is disabled, the execute command
skips the task.
6. Save your edits and close the XML
file.
7. Repeat as needed until you edit all the deploysolution.n.xml files
for your profile.
4. Run the deploysolution tasks
in the profile one at a time by running the following command. Do
not type any line breaks when you enter the command:

configmgr\_cl execute -taskfile task\_file\_name
 -profile myprofile [-silent] [-force]
Where task\_file\_name is the name of the task
file: deploysolution.xml or deploysolution.n.xml and n is
a number larger than 2.
5. Repeat 4 as
needed for each deploy solution task file that you generated in this
profile.
6 Optional: Assign users to the roles for thiscase:

1. Run the test command to assign users by running the
following command. Do not type any line breaks when you enter the
command:

configmgr\_cl test -taskfile task\_file\_name
 -profile myprofile [-silent][-force][-help]
Where task\_file\_name is
the name of the task file: deploysolution.xml or deploysolution.n.xml and n is
a number larger than 2.

The Case Client opens for you to assign
users to the roles for this solution.
2. Add users to the roles.
3. Repeat as needed for each deploy solution task file
that you generated in this profile.