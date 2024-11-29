<!-- image -->

# Delimited format with hierarchical business objects

## Single cardinality

This is a CSV file that
contains customer record with an address in it.

```
8A7111,John,Doe,577 Airport Blvd,Burlingame,CA,94010,80000
```

The
corresponding business object for the record is as follows. Note,
the business object property names are in order of the data in the
file. This is a requirement if the business object is not a flat business
object.

| CustomerBO                                                                   | CustomerBO                                                                   |
|------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| id firstName lastName                                                        | 8A7111 John Doe                                                              |
| address 	street 577 Airport Blvd 	city   Burlingame 	state  CA 	zip    94010 | address 	street 577 Airport Blvd 	city   Burlingame 	state  CA 	zip    94010 |
| salary                                                                       | 80000                                                                        |

## Multiple cardinality contained business object

This
scenario is supported only with the caveat that the maxOccurs property
is not unbounded and the maxOccurs number of elements are present
in the stream.

## Property value is not set

If a property
is unset, then there are two consecutive delimiters.

```
8A7111,,Doe,80000
```

## Property value contains a comma

If the property
contains a comma in it, then it is put in double quotation marks.

```
8A7111,John,Doe,"80,000"
```

## Property value contains a double quote

If
the property contains a double quote in it, then the double quote
is followed by another double quote and the entire property is put
in double quotation marks.

```
8A7111,"John-""Junior""",Doe,80000
```