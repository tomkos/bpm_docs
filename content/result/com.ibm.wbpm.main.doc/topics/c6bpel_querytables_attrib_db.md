<!-- image -->

# Database type to attribute type mapping

| Database type                                                                                                                          | Attribute type   |
|----------------------------------------------------------------------------------------------------------------------------------------|------------------|
| A binary type with 16 bytes. This is the type used for IDs such as TKIID on TASK of the Business Process Choreographer tables.         | ID               |
| A character based type. The length depends on the column in the database table that is referenced by the attribute of the query table. | STRING           |
| An integer database type, such as integer, short, or long.                                                                             | NUMBER           |
| A timestamp database type.                                                                                                             | TIMESTAMP        |
| A decimal type, such as float or double.                                                                                               | DECIMAL          |
| A type that is convertible to a Boolean value, such as a number. 1 is interpreted as true, and all other numbers as false.             | BOOLEAN          |

Supplemental query tables typically refer to existing database
tables and views, such that table or view creation is not necessary.

## Example

```
CREATE TABLE CUSTOM.ADDITIONAL\_INFO
(
  PIID       CHAR(16) FOR BIT DATA,
  INFO       VARCHAR(220),
  COUNT      INTEGER
);
```

| Database column and type   | Query table attribute and type   |
|----------------------------|----------------------------------|
| PIID CHAR(16) FOR BIT DATA | PIID (ID)                        |
| INFO VARCHAR(220)          | INFO (STRING)                    |
| COUNT INTEGER              | COUNT (NUMBER)                   |