<!-- image -->

# Transform types in the business object map editor

- Move - This type of transform assigns the
value in the source to the target.
- Extract - In this type of transform, the
source value must be a string. This extracts
a portion of the string and assigns it to the target. This is similar
to the String.substring() method in Java™.
- Join - This type of transform combines
the values of two or more sources into one, and assigns it to the
target. The target of a Join transform must be a string.
- Submap - In this type of transform, the
source and target must be business objects (that is, they must be
complex types). The input and output of the specified business object
map must be of the same type as the sources and targets of the transform.
- Custom - This type of transform specifies
custom logic for mapping the input(s) and output(s) by using Java code.
- Assign - This type of transform sets the
constant value to the output.
- Relationship - This type of transform performs
relationship management. The source and target of a Relationship transform
must also be complex types.
- Relationship Lookup - This type of transform
performs relationship management between static cross-referencing
data. The source and target of a Relationship Lookup transform must
be simple types.
- Custom Assign - This type of transform
is similar to Custom, except that it does not take any input. It is
also similar to Assign, except that you can use more logic in assigning
the values using Java (using
the text or visual editors).
- Custom Callout - This type of transform
is similar to Custom, except that it does not take any output. It
may be useful for initialization before executing any transforms.

You can also use Move and Assign on
business graphs (for Change Summary, Event Summary and Verb). Although
the transform types are the same as the "regular" transform types,
they are slightly different. For Event Summary Move, you can choose
to move the event, or the event id, or both.

- Creating transforms

Transforms establish a connection between a source and target in a business object map. They can be created using either the graph view, table view, or properties view in the business object map editor.
- Editing transforms

Transforms can be edited using the business object map editor.
- Deleting transforms

Transforms can be deleted using the business object map editor.