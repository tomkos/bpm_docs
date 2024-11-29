<!-- image -->

# Using assign

## About this task

## Procedure

1. From the palette, drop an assign activity onto the canvas.
2. Click the Details tab in the properties
area. You will now see a table that has one column labelled Assign From, and another labelled Assign To. Quite simply the value in the left column is assigned into the
location specified in the column on the right.
3 Click Add to create a new row, or Remove to delete an existing one. You can change theorder of the rows with the Up and Down buttons. Note:
    - The order shown here represents the sequence in which the copies
will be executed in the runtime environment, so variables must be
initialized accordingly. For example, the second copy cannot use a
variable that is initialized by third copy.
    - When an existing assignment can be modified, the Edit
Query icon () will appear
in the cell. Click this icon to make the necessary changes.
4. In the Assign From column, click Select From. A content assist dialogue will
appear with the following options:

Option
Description

Input
Choose this to select a variable.

Date
Use the interactive calender display to choose a date.

String
Enter an appropriate textual value.

Number
Enter an appropriate numeric value.

Boolean
Choose either True or False from the dialogue.

XPath Expression
This choice will launch the XPath Expression Builder that
you can use to visually compose an appropriate XPath expression.

XML Literal
Enter the appropriate well-formed XML code. Note: An XM Literal
builder is provided to allow you to easily generate XML code using
a simple interface. Also note that you must set the Assign
To value before defining the Assign From as an XML Literal.

Property of a variable
Choose this to select an appropriate property from an existing
variable.

Partner reference
Choose this to select a partner.

Endpoint Reference
This choice will launch the Select Endpoint Reference window. Use it to specify an existing interface with an endpoint,
or specify the URI explicitly.
5. In the Assign To column, click Select To. A content assist dialogue will
appear with options that are appropriate to the to the choice made
in the Assign From column. Choose something appropriate.

## Example: using arrays in assign and forEach activities

This example will demonstrate how you can use an assign activity
to iterate an array within a forEach activity.

1. Create a business object called MyBO with an
element called array of type string, and with the property of array.
2. Create a new BPEL process, and have the interface generated automatically.
3. Create a new variable called VarArray in your
BPEL process that calls MyBO.
4 Drop an assign activity between the existing Receive and Replyactivities, and create three values as follows:
    1. In the Assign from field, open the code
assist, select String (enter a value), and
type test 01.
    2. In the corresponding Assign To field, select VarArray : MyBO > array : Array of
string. The value VarArray array[1] appears in the field.
    3. Click Add to create a new field in the assign activity.
    4. Repeat these steps twice more, increasing the numeric value each
time so that it matches the following screen capture:Note: You will not
be able to edit the Assign To value directly.
To make changes to array [1], click the Edit Query icon (, and make
changes to the field in the XPath Expression Builder window.
5 Drop a forEach activity below the assign activity, and configureit as follows:

1. In the Details tab, under the Iteration heading, click none in
the Type field, and select Array (dynamic bounds) > varArray :
MyBO > array : Array of string.
2. Drop an assign activity into the forEach activity.
3. In the Assign from field, select varArray : MyBO > array : Array of
string.
4. Modify the automatically generated VarArray array[1] to be VarArray array[bpws:getVariableData('Index')].
5. In the corresponding Assign To field, select Input 1: string.
6. Drop a snippet activity below the assign activity, and add the
following code to it: System.out.println( "In ForEach: " +
Input1 );.

<!-- image -->

- Troubleshooting errors related to assign activities

Occasionally, data manipulated in a BPEL process with the use of an assign activity can result in errors when that process is deployed to a runtime environment. Here are some of the most common problems as well as solutions.
- Assigning from and to xs:any

Business object definitions can have XSD wildcards that can be mapped using the assign activity.

## Related concepts

- Working with XPath in the BPEL process editor