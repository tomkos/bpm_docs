<!-- image -->

# Testing business graphs

## Before you begin

## About this task

To test a business graph:

## Procedure

1. Open the test client as described in Opening the integration test client.
2. In the Configuration field, ensure that the correct test configuration
is selected. 

A default test configuration is automatically created whenever you open the integration test
client. If you did not open the integration test client by loading a test configuration that you
saved earlier, the default test configuration is already selected in the
Configuration field.
3. In the Module field, ensure that the correct module is selected. 

If you opened the integration test client by selecting a module, this module is already selected
in the Module field.
4. In the Component field, ensure that
the component is selected that contains your interface operation.
5. In the Interface field, ensure that
the interface is selected that contains your operation.
6. In the Operation field, select the
operation that has a business graph as its parameter.
7 If you want to specify a value for a verb business graph property,complete the following steps in the value editor:
    1. In the Name column, locate the verb
property.
    2. In the Value column, click the cell that appears in the same row as the
verb property. 
A list is displayed.
    3. Select a value from the list.
 You can choose an enumeration that is defined in the underlying XSD file of the business
graph, such as Create, Retrieve,
Update, Delete, or
UpdateWithDelete.
In the following figure, the Update enumeration is selected.
8 If you want to specify values for the changeSummary business graphproperty, complete the following steps:

1. In the Name column, right-click any of the cells and select
Show Change Summary.

The Change Summary column accepts values that represent the original state
of the business objects in the business graph. The Value column, by
comparison, accepts values that represent the current state of the business objects in the business
graph.

A Change Summary column is appended to the value editor and the
data pool editor, as shown in the following figure:
2. If you want to log all changes that occur to the business objects after the operation is
invoked, right-click any of the cells in the Name column and select
Enable Logging. 
The changes are recorded in the target adapter or component.
3. In the Value column, specify values for the business graph, verb,
business objects, or attributes as needed. 
Information about the specific values that you can specify in the Value
column is found in Value and data pool editors.
4. In the Change Summary column, specify values for the business objects or
attributes as needed. 

If you are specifying a value for a business object, you can select the
<create>, <update>, or
<delete> predefined value. If you are specifying a value for an attribute,
you can simply type a value. Information about the specific values that you can specify in the
Change Summary column is found in Value and data pool editors.
9. Click the Continue icon .
10. If the Deployment Location wizard opens, select the server where you want to deploy your
selected module, as described in Deploying modules from the integration test client.

From this point on, testing an operation that has a business graph as its parameter is similar to
testing an operation that has a business object or primitive type as its parameter.

## Example