<!-- image -->

# Relationship editor

- Relationship section
- Roles section
- Property pages

## Relationship section

The Relationship
section has no actions defined, therefore, there is no toolbar available.

- Undo Add role - you can undo the last action
done in the editor.
- Redo - you can revoke the last action which
has been undone.
- Show in Properties - the properties view
of the relationship will be opened.
- Add Role  - the Select Data Type window
will launch and after selecting a data type a new role will be added
to the Roles section.

## Roles section

- Add role action - this action is always
enabled and launches the Select Data Type window to select a data
type for the new role which should be added.
- Delete role action - this
action is only enabled if a role is selected which can be deleted.
Deleting a role will also remove the role file from the project (a
window will open to ask for confirmation). Internal roles do not need
a confirmation as no file will be deleted because they are inlined
into the relationship file.
- Add key attribute action -
this action is only enabled if a role or role object is selected.
This launches the Select Key Attribute window. The add key attribute
action is disabled for simple XSD data types as the key attribute
always is "Data".
- Remove key attribute action -
this action is only enabled if a key attribute is selected and removes
the selected key attribute. The "Data" key attribute
of a simple XSD data type cannot be removed, therefore, the remove
key attribute action is disabled for those key attributes.

The Roles section contains roles and there are four different
appearances of the roles. There are internal roles and external roles
which can also be regular or managed. The managed role is always colored
in light blue and is the first role in the Roles section.

As
the external roles are in separate files than the relationship, they
have a location information attached to them.

The Customer information
is needed as the roles can be spread across different modules in the
non-lookup relationship. Internal roles do not need that information
because they are inlined in the relationship.

The Key attribute
ID part of the role shows the role object, which is the data type
used for the role.

The Key attributes list shows the key attribute
which is used for the role. Key attributes can be any attribute of
the data type. Normally there are attributes used which have a special
function in the data type such as the unique key. For combined key
attributes several attributes can be chosen as key attributes.

## Property pages

In the relationship editor, there are four property pages available
for the relationship. The Description page handles general detailed
information about the relationship. The Details page displays the
type of the relationship. The Properties page allows you to define
user defined properties. The Instance Data page is only available
if the static flag is activated during relationship creation.

The following information provides more details on each of the
property pages:

| Type of relationship   | A one-to-one relationship between business objects using the unique primary key   | A one-to-one, one-to-many or many-to-many relationship between business objects using any attribute   | Used to transform data attributes according to a static mapping   |
|------------------------|-----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| Identity               | X                                                                                 |                                                                                                       |                                                                   |
| Non-identity           |                                                                                   | X                                                                                                     |                                                                   |
| Identity-lookup        | X                                                                                 |                                                                                                       | X                                                                 |
| Non-identity lookup    |                                                                                   | X                                                                                                     | X                                                                 |