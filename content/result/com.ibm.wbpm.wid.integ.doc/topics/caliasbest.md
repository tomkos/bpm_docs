<!-- image -->

# Choosing alias names for promoted properties

The mediation flow editor does not enforce strict type checking for promoted
properties. This means that the editor will allow you to share the name of
an alias for properties of the same native type, such as String or float.
Sharing the name of an alias between promoted properties means that the promoted
properties will also share the value. When you assign a value to a property,
all properties that have the same alias name will be assigned that value.

For example, in a Database Lookup primitive, you could have the same name
for the alias of the Table name and Key column name properties because they
are both of type String. However, when you change the value of Table name,
the Key column name property will also change.

As often as possible, give your properties unique names for their aliases.
If you want to share the names of aliases, share only the names for the properties
that are of the same primitive property type, such as; validate input.

To understand the potential consequences of sharing the names of aliases
between promoted properties, view the promoted properties of the complete
flow by clicking in the top section of the mediation flow editor.