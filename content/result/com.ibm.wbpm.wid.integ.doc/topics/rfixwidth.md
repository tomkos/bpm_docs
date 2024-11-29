<!-- image -->

# Fixed width format

This format has data where every field has a fixed width
and for those fields where their width is less than the value, it
is padded with pad characters. Every record ends with a new line character.
The field width and pad character are both user configurable. This
format may optionally contain a header at the top which corresponds
to the properties of the business object. If the header is absent,
then the order of the fields in the input data is the same as the
order of properties in the business object. Typically, fixed width
format contains data where every field has a different width. To enable
this, the field width will be represented as a list property.

Fixed
width format may be transmitted in several forms. Fixed width format
may come in a stream through data bindings such as HTTP, JMS and MQ
as well as files.

## Fixed width format with no header and one record

This
is a fixed width format with one record and does not contain a header.
In this case, the business object properties have to be in the order
of the fields in the data.

```
8A7111John~~~~~~Doe~~~~~~~80000~
```

The
corresponding business object for the record is as follows. Note the
business object property names are in order of the data in the fixed
width format. Note the lastName and firstName fields.

| CustomerBO                   | CustomerBO            |
|------------------------------|-----------------------|
| id firstName lastName salary | 8A7111 John Doe 80000 |

## Fixed width format with header and one record

This
is a fixed width format with one record and a header. The field width
format id is 6, firstName and lastName are 10 and salary is 6 as well.

```
id~~~~firstName~lastName~~salary
8A7111John~~~~~~Doe~~~~~~~80000~
```

| CustomerBO                   | CustomerBO            |
|------------------------------|-----------------------|
| id firstName lastName salary | 8A7111 John Doe 80000 |

## Fixed width format with multiple records and header

This
is a fixed width format with multiple records and also a header.

```
id~~~~firstName~lastName~~salary
8A7111John~~~~~~Doe~~~~~~~80000~
8A7112Mary~~~~~~Cay~~~~~~~100000
8A7113Tom~~~~~~~Howard~~~~600000
8A7114Liz~~~~~~~Taylor~~~~700000
```

| CustomerWrapperBO            | CustomerWrapperBO        |
|------------------------------|--------------------------|
| customers[]                  | customers[]              |
| id firstName lastName salary | 8A7111 John Doe 80000    |
| id firstName lastName salary | 8A7112 Mary Cay 100000   |
| id firstName lastName salary | 8A7113 Tom Howard 600000 |
| id firstName lastName salary | 8A7114 Liz Taylor 700000 |

- Fixed width format cardinality and properties

Cardinality and properties of the fixed width format are described.

## Related reference

- Atom feed format
- Delimited format
- JavaScript Object Notation (JSON) format
- SOAP data handler