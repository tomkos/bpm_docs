<!-- image -->

# Parameters

The system parameters, $USER and $LOCALE,
are replaced at run time in filters and selection criteria, and are
not required to be passed into the query table API. The input value
for the calculation of the $LOCALE system parameter
is provided by setting the locale in the filter options.

User parameters must be passed into the query table API when the
query is run. This is accomplished by passing a list of instances
of the com.ibm.bpe.api.Parameter class if the Business
Flow Manager EJB is used, or an instance of the com.ibm.task.api.Parameter
class if the Human Task Manager EJB is used.

| Property   | Description                                                                                                                                                                                                                                                                                            |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name       | The name of the parameter as used in the query table definition. The name is case sensitive.                                                                                                                                                                                                           |
| Value      | The value of the parameter. The type of the parameter must be compatible with the type of the operand of all filters and selection criteria where this parameter is used. Constants that are defined on some attributes of predefined query tables can be passed as a string, for example STATE\_READY. |

## Example

```
// run a query against a composite query
// table CUST.CPM with the primary query table filter
// set to 'STATE=PARAM(theState)'
EntityResultSet ers = null;
List parameterList = new ArrayList();
parameterList.add(new Parameter
("theState", new Integer(2)));

// run the query;
// the business flow manager EJB or the
// human task manager EJB can be used to access query tables
ers = bfm.queryEntities
("CUST.CPM", null, null, parameterList);

// work on the result set
// ...
```