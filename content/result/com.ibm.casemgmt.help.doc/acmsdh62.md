# Adding workflow data fields and workgroups to the properties
view

## About this task

You can add data fields and workgroups to a view one at
a time. By using this method, you can define settings such as labels
and user interface controls for these fields.

You can also use
the Automatically include setting to add to
a container         all the data fields or workgroups that are exposed
in a step. By using this method, you can         ensure that all data
fields or all workgroups for the step are included in the view.  
      However, you cannot define settings for specific fields. Instead,
the default settings are         used for each field.

To have
a data field or workgroup displayed in the Properties widget at run
time, you must         associate that data field or workgroup with
the task and step that a user is performing. If         these conditions
are not met, the field is not displayed in the view.

## Procedure

To add a single data field or workgroup to a container
in Properties View Designer:

1. In the Properties palette,
select Run time             only from the drop-down
list.. Then, drag Workflow             Field into
the container.
2 Select the workflow field and edit the settings:
    1. Enter the name of the data field or workgroup exactly
as it is defined in the workflow.
    2. Select the data type of the field.
For a
workgroup, select Workgroup. 
You can leave
the data type as Unspecified. In this situation, Case Client determines the data type
at run time and uses the appropriate default control for editing the
field.
    3. If the data field or workgroup can have multiple values,
select the Multiple values check box.
    4. Specify the property settings for the workflow field.
The property settings depend on the data type of the field.
Tip: At runtime, the workflow system assigns values to all of
the workflow data fields. Use Process Designer if you want to specify
a default value for workflow fields.