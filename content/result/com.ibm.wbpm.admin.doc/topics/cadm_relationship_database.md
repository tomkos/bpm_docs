<!-- image -->

# Querying relationship data

## Using the relationship manager to query relationship
data

For more information
on querying relationship data with the relationship manager, see the
relationship manager online help.

## Using database views to query relationship data

- using SQL statements with a DB client (for example, with the DB2® command center)
- using JDBC to run SQL statements with a Java™ program

- relationship\_display\_name = SAMPLECUSTID
- role\_display\_name = MYCUSTOMER
- uuid = 80C (this number is generated automatically
by the server)

Each view will contain the columns (including the
associated properties of type, value, and nullable) listed in the
following table:

| Name                                                                                                | Data type                                                                       | Value                                                                                                                                                                                                                          | Nullable?   |
|-----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| INSTANCEID                                                                                          | Integer                                                                         | The ID number used to correlate instance data between different applications.                                                                                                                                                  | No          |
| ROLE\_ATTRIBUTE\_COLUMNS Dynamic relationship - defined in business object Static relationship - DATA | Dynamic relationship - defined in business object Static relationship - Varchar | The column name and type depends on the role definition. Column names are based on the key attribute names, while column types are database data types that are mapped based on key attribute type defined in role definition. | No          |
| STATUS                                                                                              | Integer                                                                         | 0-4 0 - created 1 - updated 2 - deleted  3 - activated 4 - deactivated  Note: When populating instances through views, ensure that the value for this column is 0.                                                             | Yes         |
| LOGICAL\_STATE                                                                                       | Integer                                                                         | 0 = activated 1 = deactivated  Ensure that you set the proper value when you populate the database with data.                                                                                                                  | No          |
| LOGICAL\_STATE\_TIMESTAMP                                                                             | Timestamp                                                                       | Date and time when the logical state column data was last updated.                                                                                                                                                             | Yes         |
| CREATE\_TIMESTAMP                                                                                    | Timestamp                                                                       | Date and time when the role instance was created.                                                                                                                                                                              | Yes         |
| UPDATE\_TIMESTAMP                                                                                    | Timestamp                                                                       | Date and time when the role instance was last updated.                                                                                                                                                                         | Yes         |
| ROLEID                                                                                              | Integer                                                                         | ID number used to identify a role instance                                                                                                                                                                                     | No          |

- Example: Querying relationship data using database views

This example uses SQL scripts with a DB2 Universal Database to query an identity relationship with three sets of data from three enterprise applications: Clarify, SAP, and Siebel.