<!-- image -->

# Fixed width format cardinality and properties

## Single cardinality

This is a fixed width
format that contains a customer record with an address in it.

```
8A7111John~~~~~~Doe~~~~~~~577 Airport Blvd~~~~BurlingameCA~~~94010180000~
```

The
corresponding business object for the record is as follows. Note the
business object property names are in order of the data in the fixed
width format. This is a requirement if the business object is not
a flat business object.

| CustomerBO                                                                   | CustomerBO                                                                   |
|------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| id firstName lastName                                                        | 8A7111 John Doe                                                              |
| address 	street 577 Airport Blvd 	city   Burlingame 	state  CA 	zip    94010 | address 	street 577 Airport Blvd 	city   Burlingame 	state  CA 	zip    94010 |
| salary                                                                       | 80000                                                                        |

## Multiple cardinality contained business object

This
scenario is supported only with the caveat that the maxOccurs property
is not unbounded and the maxOccurs property's number of elements are
present in the stream.

## Property value is not set

If a property
is unset, pad characters equal to the field width are added.

```
8A7111~~~~~~~~~~Cay~~~~~~~100000
```

## Property value is empty

This occurs in the
case of writing out fixed width data. If a property is empty (),
pad characters equal to the field width are added.

```
8A7111~~~~~~~~~~Cay~~~~~~~100000
```

## Configurable properties

The following properties
can be configured on the Fixed Width data binding or fixed width data
handler.

| Property name                       | Explanation                                                                                                                                                                                                                                                                                       | Type      | Possible values                                 | Default value                         |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-------------------------------------------------|---------------------------------------|
| Header line                         | This indicates if there is a header in the incoming data or if a header has to be created in the outgoing data.                                                                                                                                                                                   | Enum      | True or false                                   | False                                 |
| Fixed width                         | This is a list which contains the width of every property value in the stream in the order that it appears in the stream.                                                                                                                                                                         | List      |                                                 | None                                  |
| Pad character for non-numeric types | If the property value size is less than the field width then the pad characters are added to it so that the size is equal to the field width. \u is the pad character for Unicode characters. This property is applicable for non-numeric types in the data like string, boolean, date and so on. | Character | An empty character such as " " or type your own | An empty character such as " "        |
| Pad character for numeric types     | If the property value size is less than the field width then the pad characters are added to it so that the size is equals to the field width. \u is the pad character for Unicode characters. This property is applicable for numeric types like int, float, double, long and so on.             | Character | An empty character such as " " or type your own | An empty character such as " "        |
| Alignment for non-numeric types     | This indicates whether the padding is left, right or both left and right. This alignment is for non-numeric types                                                                                                                                                                                 | Enum      | LEFT\_ALIGNMENT, RIGHT\_ALIGNMENT, BOTH\_ALIGNMENT | RIGHT\_ALIGNMENT                       |
| Alignment for numeric types         | This indicates whether the padding is left, right or both left and right. This alignment is applicable for numeric types                                                                                                                                                                          | Enum      | LEFT\_ALIGNMENT, RIGHT\_ALIGNMENT, BOTH\_ALIGNMENT | RIGHT\_ALIGNMENT                       |
| Truncation                          | When writing the values out, if the field width is less than the property value, then a true value indicates that the value should be truncated and a false value indicates that an exception should be thrown.                                                                                   | boolean   | True or False                                   | True                                  |
| Encoding                            | This is the encoding that will be used in converting bytes to string and string to bytes wherever applicable.                                                                                                                                                                                     | Enum      | All encodings                                   | UTF-8                                 |
| Record delimiter type               | This can be based either on a delimiter or size of record.                                                                                                                                                                                                                                        | Enum      | By delimiter or by size                         | By delimiter                          |
| End of line delimiter               | This indicates what the separator is between the records.                                                                                                                                                                                                                                         | String    | EOL or type your own                            | End of line (either /n or /r/n or /r) |
| Value of null                       | This property indicates what value should be written out for null and what value should be treated as null when reading data in.                                                                                                                                                                  | String    | NULL or type your own                           | NULL                                  |