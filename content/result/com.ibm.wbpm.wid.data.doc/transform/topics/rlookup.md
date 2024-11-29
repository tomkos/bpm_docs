<!-- image -->

# XML transform: Lookup

The files that are used for looking up values must already
exist in the workspace within the current  module or in a library.
 The map editor provides the following types of lookups:

If you want to use a comma in
one of the token strings, precede the comma with the escape character
forward slash /.

Because a lookup takes a source
as input and produces a value for the target, you can control the
index in the CSV file that is used to match the key and the index
from which the value is returned. To specify the index, use the Column
index setting. The first index is zero. You can also use
a heading name and the index of the given header name will be used
as the index. If a heading name is used, it is assumed that the first
line of the csv file has the headings for the subsequent rows.

```
ID, City, Country
A001, Vienna, Austria
B020, Dhaka, Bangladesh
C005, Beijing, China
```