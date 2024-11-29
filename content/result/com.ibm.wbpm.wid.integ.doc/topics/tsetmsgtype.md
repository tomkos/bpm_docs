<!-- image -->

# Mapping weakly typed elements using the set message type mediation
primitive

## Before you begin

The
Set Message Type primitive allows you to 'overlay' message fields
in the SMO with type information that is different from the type described
in the original business object definition. This is useful when the
business object definition contains weakly-typed field definitions,
but you know that content of a particular data type will be present
in the instance message at run time.

You can manipulate strong-type
fields more easily than weak-type because their structure and type
is known. Using the Set Message Type you can cast a weakly-typed field
to a strongly typed field. Primitives that are connected to the output
terminal of Set Message Type can then access the elements to which
the any type element was cast. For example, you can use the XML map
editor or the business object map editor to view the fields with the
type that was cast instead of xsd:any, xsd:anyType, or xsd:anySimpleType.
You can then manipulate the content of these fields.

## About this task

## Procedure

1. In the mediation flow editor, under the Transformation
group, click the Set Message Type primitive and drop it onto the canvas.
2. Wire the input terminal to have access to the SMO structure.
3. Right-click the primitive and select Show in
Properties. In the Properties view, click Details.
4. In the Details tab, click Add... and
then click Edit... beside to the Weakly typed
field text box, to select the field you want to refine.
5. In the XPath Expression Builder window, navigate the SMO
structure and click the field you want to add it to the expression.
Click Finish.
6. To see a list of types, click Browse next
to the Actual field type text box. Select a type, click OK and
then click Finish.