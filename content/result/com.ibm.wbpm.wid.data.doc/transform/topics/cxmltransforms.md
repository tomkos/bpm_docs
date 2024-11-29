<!-- image -->

# IBM supplied transform types in the XML map editor

| Transform                           | Description                                                                                                                                                                                                                                                                                                                  |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| XML transform: Append               | Iterates over multiple inputs in the order specified to insert, remove and concatenate data.                                                                                                                                                                                                                                 |
| XML transform: Assign               | Sets a hard coded value in the output element. There is no input element.                                                                                                                                                                                                                                                    |
| XML transform: Custom               | Allows you to enter your own code or to call reference code to be used in the transform. You can use your own XPath expressions, XSLT functions, or Java™ code. You can extend built-in transformation functions using custom XPath expressions and XSLT templates.                                                          |
| XML transform: Concat               | Allows you to retrieve data from two or more inputs and combine the data into a single concatenated string.                                                                                                                                                                                                                  |
| XML transform: Convert              | The Convert transform performs conversions between simple data types.                                                                                                                                                                                                                                                        |
| XML transform: For each             | Iterates over a single input array element (either a simple type or a complex type). The output element must be an array of complex types. The for each transform contains a nested map where the mapping is performed when the transform executes.                                                                          |
| XML transform: Group                | Takes a single list as input and creates a number of lists.  It is used to map a "flat" repeatable structure (an array) to a nested repeatable structure  (a nested array) based on some criteria from the input structure.                                                                                                  |
| XML transform: If, Else if and Else | If, Else if, and Else operate as a group of conditional transforms that allow you to control the flow of the mapping by setting conditions. The condition is applied to the input element of the conditional transform. If the condition is satisfied, the transform that is nested within the conditional transform is run. |
| XML transform: Join                 | Join multiple input arrays into a single output based on a common value, similar to the way tables are joined in database operations. The join transform replaces the merge transform that was available in previous releases.                                                                                               |
| XML transform: Local map            | A transform with only one element as input (either a simple type or complex type) that can contain nested maps. The target can be either a single element or an array element but must be a complex type.                                                                                                                    |
| XML transform: Lookup               | Retrieve values from a file based on a key from the input element. The output element is populated with the retrieved value.   You can use several file formats to perform this type of lookup. The map editor provides lookups for some formats. You can also contribute support for your own custom file types.            |
| Merge                               | See Join.                                                                                                                                                                                                                                                                                                                    |
| XML transform: Move                 | Copies data from the input element to the output element.                                                                                                                                                                                                                                                                    |
| XML transform: Normalize            | Removes white space such as spaces, tabs, and returns from the input string and moves the resulting normalized string to the output element. For example, you can use the normalize transform to remove multiple occurrences of white space characters before doing a data comparison.                                       |
| XML transform: Submap               | Allows you to invoke another map within the current map. If you want to reuse an existing map, use the submap transform.                                                                                                                                                                                                     |
| XML transform: Substring            | Extracts information from the input string and moves the extracted string to the output element.                                                                                                                                                                                                                             |

- XML Transform: Append

Iterates over multiple inputs in the order specified to insert, remove and concatenate data.
- XML transform: Assign

Sets a hard coded value in the output element. There is no input element.
- XML transform: Concat

Allows you to retrieve data from two or more inputs and combine the data into a single concatenated string.
- XML transform: Convert

The Convert transform performs conversions between simple data types.
- XML transform: Custom

Allows you to enter your own code or to call reference code to be used in the transform. You can use your own XPath expressions, XSLT functions, or Java code. You can extend built-in transformation functions using custom XPath expressions and XSLT templates.
- XML Transform: For each

Iterates over a single input array element (either a simple type or a complex type). The output element must be an array of complex types. The for each transform contains a nested map where the mapping is performed when the transform executes.
- XML Transform: Group

Takes a single list as input and creates a number of lists.  It is used to map a "flat" repeatable structure (an array) to a nested repeatable structure  (a nested array) based on some criteria from the input structure.
- XML transform: If, Else if, and Else transforms

If, Else if, and Else operate as a group of conditional transforms that allow you to control the flow of the mapping by setting conditions. The condition is applied to the input element of the conditional transform. If the condition is satisfied, the transform that is nested within the conditional transform is run.
- XML Transform: Join

Join multiple input arrays into a single output based on a common value, similar to the way tables are joined in database operations. The join transform replaces the merge transform that was available in previous releases.
- XML transform: Local map

A transform with only one element as input (either a simple type or complex type) that can contain nested maps. The target can be either a single element or an array element but must be a complex type.
- XML transform: Lookup

Retrieve values from a file based on a key from the input element. The output element is populated with the retrieved value.   You can use several file formats to perform this type of lookup. The map editor provides lookups for some formats. You can also contribute support for your own custom file types.
- XML transform: Move

Copies data from the input element to the output element.
- XML transform: Normalize

Removes white space such as spaces, tabs, and returns from the input string and moves the resulting normalized string to the output element. For example, you can use the normalize transform to remove multiple occurrences of white space characters before doing a data comparison.
- XML transform: Submap

Allows you to invoke another map within the current map. If you want to reuse an existing map, use the submap transform.
- XML transform: Substring

Extracts information from the input string and moves the extracted string to the output element.