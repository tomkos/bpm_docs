<!-- image -->

# Declaring a query property for a variable

## About this task

You can define query properties on your global variables.
Query properties can be included in runtime queries using the query
API function. You can also use query tables to expose the query properties
to the business user in Business Space. The query property may be
either a built-in XML schema simple type, or a user-defined simple
type based on a built-in XML schema type using restrictions. Complex
types, list, and union types (neither built-in nor user-defined) are
not supported for query properties.

1. A local query property is created from a query and can
be used for getting and filtering data from a single process.
2 A global query property that is created from a property isused when you would like to filter data from multiple processes. Thereare two conditions that must be met in order to define a global queryproperty: Since a correlation property can be shared between multiple processes,you must define a query property from a property in the correspondinginterface typed variable for each process.
    - you must have an interface typed variable,
    - a correlation property must be defined for the underlying WSDL
message.

## Procedure

1. Select an existing variable in the tray and click the Query
Properties tab in the Properties view.
2. Click Add.
3 In the Add a Query Property definethe query property. Option Description Data type variable You can only define a local query property. Enter a name forthis query property in the Name field, and,if populated, select the data type from the hierarchical list. The Name fieldmust not contain spaces or special characters. Click OK . Interface type variable Define the query property, either: Click OK .

| Option                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Data type variable      | You can only define a local query property. Enter a name for this query property in the Name field, and, if populated, select the data type from the hierarchical list. The Name field must not contain spaces or special characters. Click OK.                                                                                                                                                                                            |
| Interface type variable | Define the query property, either:  create a global query property by selecting From property. Click Browse to select an appropriate property from the Select a Property window. Click OK. create a local query property by selecting From query. Provide a name for the query property and, if populated, select the data type that the query property will use. The Name field must not contain spaces or special characters.  Click OK. |

## Results

| Column heading   | Description                                                                                                                                                                     | Notes                                                                                                                                                                                                                           |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Query Property   | The name of the query property.                                                                                                                                                 | Taken from the correlation property for global query properties.                                                                                                                                                                |
| Type             | The data type that the query returns, must be of a simple type.                                                                                                                 | Taken from the correlation property for global query properties.                                                                                                                                                                |
| Part             | The part of the WSDL message to which the query refers.                                                                                                                         | Disabled for global query properties.  Disabled for business object data type variables. In this case the query works directly on the business object and there is no message defined. Disabled for simple type data variables. |
| Query            | The expression that defines the query, this entry can be modified by clicking  on the right side of the field, this opens an XPath editor using which you can define the query. | Disabled for global query properties. Disabled for simple type data variables.                                                                                                                                                  |

For
more information on using query tables see Query tables in Business Process Choreographer if you have IBM Workflow
Server installed.