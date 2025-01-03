# Containers

## Layout container

This container provides a simple, rectangular container that can contain any type of property or
container. You can configure the layout container to display the contents either horizontally or
vertically. You can also configure the position of labels to display either beside or above the
property editor.

## Multiple column layout container

This container consists of a series of columns. You can click the Insert
button and Delete button to add or remove columns. Each column contains a
layout container that can contain any type of property or container and can be configured
separately.

You can drag columns to reorder them in the container. You can also drag a layout container from
elsewhere in the view or from the container palette into the multiple column layout container.
Similarly, you can drag a column from the multiple column layout container to another location in
the view.

## Titled layout container

This container consists of a layout container that has a title bar and that can contain any type
of property or container. You can configure the titled layout container so that it can be expanded
or collapsed at run time.

## Property list container

This container can contain any type of property except for a property whose type is business
object. The container displays the properties in a vertical list with the labels beside the property
editor.

## Property table container

This container consists of a table in which each column contains a multivalued property. Unlike
other containers, the property table container groups the content in addition to organizing the
layout.

- Values in a property table cannot be empty or null. Therefore, all properties in a property
table container, except for string properties, are required.
- Case workers can enter only a single value in a property table cell. They cannot enter multiple
values for a property in the same row.

You can include multivalued properties that get values from an external data service in a
property table. However, problems can occur if the values that are returned for one property depend
on the value of another property in the same property table and the external data service returns
the values as dynamic choice lists. In this situation, the choice list can contain values that do
not apply to a specific instance of the dependent property in the table.

If one of the properties in a property table container is read-only, the toolbar is not available
for the table at run time. A case worker cannot add a row, delete a row, or move a row. However, a
case worker can double-click any property in an existing row that is not set to read-only and edit
the value for that property.

- Container width and height

You configure the width and height of containers in Properties View Designer to best fit the layout of your page.