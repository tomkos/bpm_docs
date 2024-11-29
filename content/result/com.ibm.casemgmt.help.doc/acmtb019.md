# Workgroups are not marked as required fields in the Properties
widget

## Symptoms

## Resolving the problem

- Create a custom properties layout view that sets the workgroup
field to required. Use this view instead of the system-generated view
on any page that is used for the task.
- Create a JavaScript to
set the required state programmatically by using the following syntax:controller.getPropertyController("Workgroup1").set("required", true);This
method marks the workgroup as required in the system-generated view
and in any custom views.