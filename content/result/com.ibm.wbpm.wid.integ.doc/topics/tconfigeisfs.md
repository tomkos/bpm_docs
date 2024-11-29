<!-- image -->

# Creating a function selector resource configuration

## Before you begin

## About this task

## Procedure

1. Right-click the module and from the menu select New
> Binding Resource Configuration. The Binding
Resource Configuration window opens. Select Function
Selector and click Next.
2. Select either an existing function selector or create your
own custom function selector that is available in your workspace on
the class path.  In the second case, the Function
selector class name field lets you select a class from
an existing collection of custom function selectors you have created
previously. Note that only classes on the class path with a name following
this pattern <class name>Properties are selectable. 
Click Next.
3. Once you have selected your function selector, the wizard
allows you to proceed to the Function Selector Properties page,
where you can add properties such as, in this case, the incoming text
file with the customer data. The properties you are
configuring are rules on how to map from the name of a file to an
object name. The rule is a regular expression for a file name. In
the following example, if a file named Customer.txt is placed in the
event directory, which is used by the WebSphere Adapter
for Flat Files as the point where files are read, the function selector
will map the file to an operation named emit<object name>, so emitCustomer.
For the object name, you would specify the name of your input type.
When you construct your input operation, you would select the input
type.  Click Next.
4. In the final page you specify the name of your function
selector and click Finish to generate it. The
function selector resource configuration is completed and shown in
the editor. The function selector is listed in the navigation under Binding
Resources. In the editor, you can choose to expose this
function selector resource configuration to other bindings beside
a binding chosen by the wizard by selecting the binding in the Select
bindings table.