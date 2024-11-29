<!-- image -->

# Specifying operation values

## Before you begin

## About this task

## Procedure

1. Select an operation to test as described in the topic "Selecting
operations for testing."
2 If you are testing a wsdl operation, you can choose towork with the Value editor or the XML editor. Otherwise, you can specifythe values in the Value editor.
    - If you want to work with the XML editor, select the XML
Editor button. The XML editor opens and displays the values
of the parameters in XML document format.In the test client, the
value editor is the editor that is open by default. If you switch
to the XML editor, a serialization of the value structure occurs for
the purpose of populating the XML editor. When you switch to the XML
editor strictly for viewing the content and you do not perform any
editing or import any file, you can switch back to the value editor
if you so choose. However, if you perform any editing or import any
file in the XML editor, then switching back to the value editor will
invoke a message that warns you that data may be lost, such as XML
comments.
    - If you want to work with the value editor, select the Value
Editor button. The value editor opens and displays the
values of the parameters.
3. If you are working with the XML editor, you can directly
enter values in the editor, or choose to import a message from a file,
by clicking the Import Message icon:
4 If you are working with the value editor, specify valuesfor a selected operation by completing the following steps:

1. In the Value column, click the
field cell where you want to specify a new value.
2. Press the F2 key or simply begin typing some
characters. A text box automatically opens, as shown in the following
figure:
3. In the text box, type the new value that you want to
assign to the field. For date, dateTime, gMonthDay and
gYearMonth types, you can alternately select the date and time through
a user interface. gDay, gMonth and gYear types do not have this user
interface. 
The five date types - gDay, gMonth, gYear, gYearMonth
and gMonthDay - always use the Gregorian calendar as a reference even
if another calendar type is selected from the Preferences page. These
types require a precision that another calendar type like the Hijri
calendar cannot provide. 
You can press Alt+Enter at
any time to add additional input lines. (If you decide that you do
not want to retain the new value that you are specifying in the text
box, you can press the Esc key to discard the new value.)
4. Press Enter or simply click another cell to save
your new value.
5. If you want to specify values for arrays, right-click the
name of each array field in the Name column
and select Add Element to open the Add Element
window, then specify a value for the selected field in the Enter
the number of new elements to add field and click OK.
For example, in the figure, the items array
field was right-clicked and Add Element was
selected, then values were specified for the individual fields under
the items[0] element (such as the value 2 that
is specified for the quantity attribute).

## Example

## What to do next