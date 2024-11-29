<!-- image -->

# Automatic mapping

<!-- image -->

1. Compares input business object field names to output business
object field names.  Names with small string differences are recognized
as being similar.
2. Compares input business object field types to output business
object field types.  Only XSD complex types are considered and a match
is recognized between exact XSD complex types.
3. All matching input and output fields are compared and transforms
are created between most similar pairings.

<!-- image -->

<!-- image -->

You can select the Consider nested business object fields check
box from the business object map editor preference page. This performs
a more exhaustive search of pairings involving nested fields.  If
the check box is not selected, just one level of fields are considered.

You can also select only the necessary input business object fields
and output object fields before running the map similar fields action.
 This limits the inputs and outputs compared when determining which
fields to create automatic transforms between.  Otherwise, if no input
or output fields are selected, all are considered.

<!-- image -->

<!-- image -->