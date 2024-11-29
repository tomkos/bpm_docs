# Modifying an existing configuration

## About this task

You can use the Case configuration tool to create a profile and edit a few properties in the profile and its tasks, and then save the
profile without entering values for each of the properties. You can then open the profile later and
edit the values to replace the default values or to change your previous values. If you did not run
any of the tasks successfully yet, you can make unlimited modifications to the property values.

Editing some task values and running
the task again on a working system can significantly affect your development
environment or production environment. For example, if you change
the name of the case management design object store after you create
solutions, you lose access to your solution templates, to any existing
connection definitions, and to related data in the previous design
object store. To restore access, you must set the name of the case
management design object store back to the original value.

## Procedure

To modify an existing configuration profile:

1 If your configuration profile is not open in the Case configuration tool , open the profile:
    1. Click File > Open Profile.
    2. Enter the path to the profile or click Browse to locate the
profilename.cfgp profile file.
For example, select the myDevelopment1.cfgp file.
    3. Click OK.
2 Optional: If needed, edit the profile propertyvalues:

1. Click File > Edit
Profile Properties.
2. Edit the existing property values.

Tip: Click Next to view all properties.
3. Click Finish.
The
properties are saved to the configuration XML file, but the property
changes are not applied until you run the task that uses the properties.
3 Edit the property values for a specific task in the profile:

1. Right-click the task name in the profile pane and select Edit
Task.
2. Edit the existing property values.
3. Click File > Save to save your changes.
4. Apply the property changes by right-clicking the task
name in the profile pane and selecting Run Task. 
Running the configuration task can take several minutes. The
task execution status messages are displayed in the console pane below
the connection properties.

- Changing the network shared directory

You can change the location of the network shared directory on all IBM® Business Automation Workflow nodes in the cluster by using the BPMConfig command and the Case configuration tool.