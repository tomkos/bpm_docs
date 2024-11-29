<!-- image -->

# Example: Database Lookup mediation primitive

- The client application passes in the employee's serial number
(049728) into serialNumber field of the message body.
- There is an employee record in the EmployeeDatabase with serialNumber
= '049728' and salary = '$50,000'.
- We want to retrieve the employee's salary from the database, using
the serialNumber field of the message to locate the record in the
database.
- We then want to retrieve the value of the SALARY column for the
employee's record from the database and put it in the message body.

```
select SALARY from EMPLOYEE\_TABLE where SERIAL\_NUMBER = '049728'
```

The
result, '50000' of type long will be stored in the salary field in
the message body.

<!-- image -->

Specify these properties for the primitive
in the Details page of the Properties view.

In the Data source field,
enter the JNDI name of the data source. In the example, jdbc/sample/EmployeeDatabase

In
the Table field, enter the name of the database table, including
the schema name. In the example, myschema.EMPLOYEE\_TABLE

In
the Search column  field, enter the name of the database column
against which the search string is matched. In the example, this column
is SERIAL\_NUMBER

In the Search location field, enter
the XPath location of a field in the message body. The value of this
field is the search string. Click Edit to launch the XPath
Expression Builder  to build the required XPath expression. In
this case that is the value of the serialNumber (049728) from the
message body.

- Column specifies the name of the database column from which
to obtain the element value. In the example, this is SALARY.
- Type specifies the type of the element value. In the example,
the type is int.
- Target location specifies an XPath 1.0 expression describing
the path location of the message element where the database value
is stored. The XPath expression must evaluate to a single element
in the message. In the example, the salary value retrieved will be
stored in the message body, in the salary field.

For more information, see Database Lookup mediation primitive.