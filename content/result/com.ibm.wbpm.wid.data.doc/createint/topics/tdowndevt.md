<!-- image -->

# Developing interfaces: top-down

## Before you begin

## About this task

## Procedure

1. Right-click your module and from the pop-up menu select New
> Interface. The New Interface Wizard opens. Add a name
to the name field, in our case, CreditReport, and
click Finish. The empty interface opens in the interface editor.
2. Add an operation. Click the Add Request Response Operation icon.
A request-response operation with an input and an output is created.
Rename operation1 to getBalance.
3. By default the binding style selected for your operation
will be document/literal wrapped with is sufficient for most cases.
However, if you will be passing an attachment in your interface, change
the binding style to document/literal non-wrapped, which is selectable
at the top of the editor. See Binding style for information on
the different types of binding styles.
4. Change input1 to balance.
In the Type field, select the default, string.
From the context menu, select double. The type is changed.
5. Change output1 to approval and
the leave the type as string. Add two faults
using the Add Fault icon, a timeout fault
with a string type and systemFailure,
also with a string type. Should you make an
error, use the delete function, available as an icon or from the context
menu if you right-click the item you want deleted. Save your interface.
From the menu bar, select File > Save. These
faults will appear in the properties of bindings which use your interface.
At that time, you can implement the faults with fault selectors.
6. Similarly, add another request-response operation called getHistory with
an input of customerName with a string type
and an output of customerHistory with a string type.
Select the string type of customerHistory and
in the properties view change the Name field to customerPastHistory.
Save your interface. Note that the name is also changed in the table.
You could also click Browse to change the data
type in the Type field.
7. Add the same faults in this operation as the previous one.
These faults would return error messages for time out conditions or
a system failure. Add a one-way operation called updateCreditRating,
either from the icons by selecting Add One Way Operation or
right-clicking the canvas area in the interface editor and selecting
from the context menu. Rename the input currentRating with
a string type. One way operations only send
an input as there is no response required. Save your interface.
8. Note that operation types can be changed; that is a Request
Response operation can be changed to a One Way operation or a One
Way operation can be changed to a Request Response operation. Right-click
the operation you want to change and from the context menu select Operation
Type. Choose the type of operation you would prefer.
9. To see the properties of the interface, click anywhere
outside the table. The properties of the interface open in the properties
view. The PortType name, namespace, folder, and documentation fields
are shown, and can be modified.
10. To see the binding style, select the an operation. In the
properties view, select the Details tab. The operation type
and binding style are shown. In this case, it is a one-way operation
with a Document Literal Wrapped binding style, the default.

## What to do next