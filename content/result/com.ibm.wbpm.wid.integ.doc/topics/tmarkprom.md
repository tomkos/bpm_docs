<!-- image -->

# Promoting a property in the mediation flow editor

## Promoted properties page

- If you click the canvas of the Operations connections section,
all the promotable properties of all the wired operations in the mediation
flow appear in the Promoted properties page.
- If you click the canvas of the request flow or response flow,
all the promotable properties of all the primitives and nodes in the
flow appear in the Promoted properties page.
- If you make a selection, such as an operation or primitive, the
Promoted properties page will display all the promotable properties
of that selection.

## Marking a property as promoted

To promote a property, and assign an alias and value to
the promoted property, work in the Promoted properties page and follow
these steps.

### Procedure

1. If you want to promote a property that is in a table, such
as the Pattern property in Message Filter, first add the property
in the details page, and save your changes. The property will now
appear in the Promoted Properties page.
2. To view the property you want to promote, click the Promoted
Properties page
3. Select the Promoted check box for
the property. A default alias is created. If the property
already has a value, that value is assigned to the alias. Otherwise,
the default value for the property is assigned to the alias.
4. To change the alias, type a name in the Alias column,
or choose a name from the list of alias names.

### Table-based properties

Some primitives have table-based properties with multiple
columns. You can promote one column in an individual row of the table
and assign an alias name to the row.

For example, the message filter primitive has a table based property
named Filter which has two columns: Pattern and Terminal name. Of
the two properties, only Pattern is promotable. The following image
shows the Promoted properties page of a Message Filter, showing that
Pattern is promoted.

A table property is displayed in the promoted properties view only
if it has a value.

<!-- image -->