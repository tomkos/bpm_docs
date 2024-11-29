<!-- image -->

# Delimited format

This format typically stores tabular data. It uses comma
to separate the fields of data. The last field ends with a new line
character. In the case where the comma is part of the field, the field
is surrounded by double quotation marks. If there are double quotation
marks or new line characters in the field, then the double quote is
followed by another double quote and the entire property value is
put in double quotation marks. This data handler follows the RFC4180
specification and Microsoft Excel
CSV format. The CSV data may contain a header line.

- The header is optional.
- The header is always on the first line and takes up only one line.
- The order of the fields in the file is the same as the order of
the properties in the business object irrespective of the header.
- The file may contain multiple records. In this case, it will be
read into a business object that contains one property which is an
array. The multiple records will be read in the array.

## CSV file with no header and one record

This
is a CSV file with one record and it does not contain a header. In
this case, the business object properties have to be in the order
of the fields in the data.

```
8A7111,John,Doe,80000
```

The
corresponding business object for the record is as follows. Note that
the business object property names are in order of the data in the
file. Note the lastName and firstName fields.

| CustomerBO                   | CustomerBO            |
|------------------------------|-----------------------|
| id firstName lastName salary | 8A7111 John Doe 80000 |

## CSV file with header and one record

This
is a CSV file with one record and a header.

```
id,firstName,lastName,salary
8A7111,John,Doe,80000
```

| CustomerBO                   | CustomerBO            |
|------------------------------|-----------------------|
| id firstName lastName salary | 8A7111 John Doe 80000 |

## CSV file with multiple records and header

This
is a CSV file with multiple records and also a header. This file will
be read into a business object that contains a single property which
is an array. This array will be populated with the records from the
incoming data.

```
id,firstName,lastName,salary
8A7111,John,Doe,80000
8A7112,Mary,Cay,100000
8A7113,Tom,Howard,600000
8A7114,Liz,Taylor,700000
```

| CustomerBO                   | CustomerBO               |
|------------------------------|--------------------------|
| customers[]                  | customers[]              |
| id firstName lastName salary | 8A7111 John Doe 80000    |
| id firstName lastName salary | 8A7112 Mary Cay 100000   |
| id firstName lastName salary | 8A7113 Tom Howard 600000 |
| id firstName lastName salary | 8A7114 Liz Taylor 700000 |

- Delimited format with hierarchical business objects

The hierarchical business objects in a delimited format are described.
- Delimited format properties

Properties of the delimited format are described.

## Related reference

- Atom feed format
- Fixed width format
- JavaScript Object Notation (JSON) format
- SOAP data handler