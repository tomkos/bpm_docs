<!-- image -->

# Editing business objects

## About this task

## Procedure

1. In the editor view, select the business object by clicking
on it once.
2. Click the  to add a field to the business object. If you want
to delete a field from a business object, select it and click  or
press the delete key.
3. Once you have added or selected an existing field, you
can edit its properties in the Properties view of the editor.
For example, if you want to specify that a field is mandatory,
click the field and then click the Description tab of the Properties view
and select the Required check box. If the business object is
used in a human task and you later generate a client user interface
for the human task, the field that you specified as required will
be marked with an asterisk in the client user interface to indicate
that it is mandatory and a value must be specified.
4. If you want to change the field type, click once on the
type in the business object and a drop-down box of choices opens.
Select the type that you want to set it to.

## What to do next

- You can also edit field and business object names on the canvas
by clicking on the name text.
- You can drag resources from the Business Integration view to the
canvas of the business object editor to work with them.
- You can reorder field in the business object by selecting the
field in the business object and then clicking on the Move
field up  button  or on the Move
field down button.
- It is important to note that a business object has its own properties
(name, parent, namespace, documentation, and so on) which can be edited
in the properties view as well. Although you can rename business objects
and fields directly in the business object editor when they are initially
created, once you have built the business objects into an application,
you should always use refactoring to ensure that you do not
break any dependencies. If you rename using refactoring, all of the
dependencies will be automatically updated to use the new name. For
more information on refactoring, see the following "Related tasks"
links.

- Editing business objects containing XSD wildcards

There are validation rules implemented in the business object editor to ensure that wildcards are used correctly.