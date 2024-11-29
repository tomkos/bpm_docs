<!-- image -->

# Attribute type to parameter mapping

The following table describes the attribute types and their mapping
to parameter values that can be used in expressions to define filter
and selection criteria, such as in filters of composite query tables,
and in filters passed to the query table API.

| Attribute type   | Usage as parameter value in expressions                                                                                                                                                                                                                          |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ID               | PARAM(name)When developing client applications, IDs are represented either as a string or as an instance of the com.ibm.bpe.api.OID interface. As a parameter, both representations are valid. An array of bytes reflecting a valid OID can also be used (byte). |
| STRING           | PARAM(name)The string representation of the object that is passed to the query table API at run time by the toString method.                                                                                                                                     |
| NUMBER           | PARAM(name)A java.lang.Long, java.lang.Integer, java.lang.Short, or a java.lang.String representation of the number is passed to the query table API. Names of constants, as defined on some attributes of predefined query tables, can be also passed.          |
| TIMESTAMP        | PARAM(name)The following representations are valid:  A java.lang.String representation of the timestamp Instances of com.ibm.bpe.api.UTCDate  Instances of java.util.Calendar                                                                                    |
| DECIMAL          | PARAM(name)A java.lang.Long, java.lang.Integer, java.lang.Short, java.lang.Double, java.lang.Float, or a java.lang.String representation of the decimal is passed to the query table API.                                                                        |
| BOOLEAN          | PARAM(name)Valid values are:  A java.lang.String representation of the boolean  A java.lang.Short, java.lang.Integer, java.lang.Long with appropriate values; 0 (for false), or 1 (for true) A java.lang.Boolean object                                          |

## Example

```
…
// this example shows a query against a composite query table
// COMP.TASKS with a parameter "customer"
java.util.List params = new java.util.ArrayList();

list.add(new com.ibm.bpe.api.Parameter("customer", "IBM");
// the business flow manager Enterprise JavaBeans or the
// human task manager Enterprise JavaBeans can be used to access query tables
service.bfm.queryEntities("COMP.TASKS", null, null, params);
…
```