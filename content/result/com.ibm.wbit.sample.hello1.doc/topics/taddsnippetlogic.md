<!-- image -->

# Create the new service interface

## About this task

To create the service interface:

## Procedure

1. In the Business Integration view, within the HelloWorldLibrary,
right-click the Data category and select New
> Business Object. The New Business Object wizard opens.
2. In the Name field, enter FullName and
click Finish. The business object editor opens.
3. To create a new field, click the little F icon in
the local toolbar (or right-click the FullName box
and select Add Field), as shown in the following
figure:
4. Type over the generated field's name of field1 and
replace it with title. If the name is not selected,
then first click to select it.
5. Repeat the previous step to create two more fields; one
named firstName and the other named lastName.
The final business object should look like this:   Optional: Select
one of the string cells in the Type column.
A list of types appears. Although you only need fields of type string for
this sample, this is where you can specify other types. Press the Esc key
to close the list. Optional: Select a field and look
at the Properties view below the editor. Although
you do not need to set any of these fields for this sample, this is
where you can specify certain properties for fields, such as specifying
field repetition or maximum length.
6. Press Ctrl-S to save your work,
and then close the business object editor. Optional:  Under
the covers, you have just created a new XSD or XML schema file with
a complex type in it. If you are curious, you can see the file by
right-clicking the FullName business object and selecting Open
With > XML Schema Editor, then choosing the Source tab.
7. Back in the Business Integration view, within the HelloWorldLibrary,
right-click the Interfaces category and select New
> Interface, as shown here:  The New Interface wizard opens.
8. In the Name field, enter HelloWorld and
click Finish. The interface editor opens.
9. To add a request response operation, click the Add
Request Response Operation icon in the local toolbar,
or right-click and select Add Request Response Operation.
10. Double-click the generated operation name operation1 and
type over it with callHello as shown here:
11. Double-click the generated parameter name input1 and
type over it with fullname.
12. Click in the type string cell of
the table, in the Inputs row, to change the
type. In the pop-up list, scroll to the bottom and select FullName,
which is the business object you recently created.
13. Double-click the generated parameter name output1 and
type over it with result. The interface should
look like this:
14. Save and close the interface editor.

## Results