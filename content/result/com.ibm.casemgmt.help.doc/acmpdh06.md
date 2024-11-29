# Defining a custom role

## About this task

## Procedure

To define a custom role, queue, and inbasket:

1. In a stand-alone IBM
FileNet Process Designer, open the solution for
editing the FileNet P8 activity workflow.
2. In IBM
FileNet Process Designer go
to View > Configuration > Work Queue > New and name the new queue.
For example,
name the queue Processing.
3. Expose the system fields and properties or data fields
that you want displayed in this queue.
Only single value
properties are available for selection.
4. On the In-baskets page, create an in-basket and assign the properties that you want
displayed for this view.
Only exposed fields for the queue are available to be used as in-basket columns and
filters.
Name the in-basket, for example, My Inbox.
5. Create a role by going to View > Roles and clicking the Add icon.
For example, name the role Adjuster.
6 Associate the role with the in-basket.
    1. Select the role and click the Modify icon
on the Select In-baskets and Members page.
    2. Select the new in-basket and click OK.
7 Optional: If you want to create a swimlanefor this role in the Step Designer, add the CB\_PrimaryQueue attributeto the role:

1. Select the role, and then go to the Custom Attributes
page.
2. Enter CB\_PrimaryQueue for the
attribute name, select string as the attribute
type, and enter Processing for the value.
8. Click File > Solution > Save and Close to save and close
the solution.

## Results