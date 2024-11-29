# Support for weak types

## Business Object Maps

| Input type            | Output type            | Supported                                   |
|-----------------------|------------------------|---------------------------------------------|
| any (simple)          | any (simple)           | Yes - assign input to output                |
|                       | anyAttribute           | Yes - custom transformation required        |
|                       | anyType (simple)       | Yes - assign input to output                |
|                       | anySimpleType          | Yes - assign input to output                |
|                       | Concrete complex type  | Yes - custom transformation required        |
|                       | Concrete simple type   | Yes - assign input to output                |
| any (complex)         | any (complex)          | Yes - assign input to output                |
|                       | anyAttribute           | Yes - custom transformation required        |
|                       | anyType (complex)      | Yes - assign input to output                |
|                       | anySimpleType          | Yes - custom transformation required        |
|                       | Concrete complex type  | Yes - assign input to output                |
|                       | Concrete simple type   | Yes - custom transformation required        |
| anyAttribute          | any                    | Yes - custom transformation required        |
|                       | anyAttribute           | Yes - custom transformation required        |
|                       | anyType                | Yes - custom transformation required        |
|                       | anySimpleType          | Yes - custom transformation required        |
|                       | Concrete complex type  | Yes - custom transformation required        |
|                       | Concrete simple type   | Yes - custom transformation required        |
| anyType (simple)      | anyType                | Yes (simple type) - assign input to output  |
|                       | any                    | Yes (simple type)                           |
|                       | anyAttribute           | Yes - custom transformation required        |
|                       | anySimpleType          | Yes - assign input to output                |
|                       | Concrete complex types | Yes - custom transformation required        |
|                       | Concrete simple types  | Yes - assign input to output                |
| anyType (complex)     | any                    | Yes (complex type) - assign input to output |
|                       | anyType                | Yes (complex type) - assign input to output |
|                       | anyAttribute           | Yes - custom transformation required        |
|                       | anySimpleType          | Yes - custom transformation required        |
|                       | Concrete complex type  | Yes - assign input to output                |
|                       | Concrete simple type   | Yes - custom transformation required        |
| AnySimpleType         | AnySimpleType          | Yes - assign input to output                |
|                       | any                    | Yes (simple type) - assign input to output  |
|                       | anyAttribute           | Yes - custom transformation required        |
|                       | anyType                | Yes (simple type) - assign input to output  |
|                       | Concrete complex type  | Yes - custom transformation required        |
|                       | Concrete simple types  | Assign input to output                      |
| Concrete simple type  | any                    | Yes (simple type) - assign input to output  |
|                       | anyAttribute           | Yes - custom transformation required        |
|                       | anyType                | Yes (simple type) - assign input to output  |
|                       | anySimpleType          | Yes - assign input to output                |
|                       | concrete simple type   | Yes - assign input to output                |
|                       | concrete complex type  | Yes - custom transformation required        |
| Concrete complex type | any                    | Yes (complex type) - assign input to output |
|                       | anyAttribute           | Yes - custom transformation required        |
|                       | anyType                | Yes (complex type) - assign input to output |
|                       | anySimpleType          | Yes - custom transformation required        |
|                       | concrete simple type   | Yes - custom transformation required        |
|                       | concrete complex type  | Yes - assign input to output                |

## BPEL processes

Business Process Execution Language (BPEL) processes support weak types in Java™ snippets and Assign
activities. For BPEL variables in Java snippets the programming model for business objects applies as BPEL
variables are represented as business objects.

Table 2 shows how business processes
support weak types for Assign activities.

| Input type            | Output type            | Supported                    |
|-----------------------|------------------------|------------------------------|
| any                   | any                    | No                           |
|                       | anyAttribute           | No                           |
|                       | anyType                | Yes - assign input to output |
|                       | anySimpleType          | Yes - assign input to output |
|                       | Concrete complex type  | Yes - assign input to output |
|                       | Concrete simple type   | Yes - assign input to output |
| anyAttribute          | any                    | No                           |
|                       | anyAttribute           | No                           |
|                       | anyType                | No                           |
|                       | anySimpleType          | No                           |
|                       | Concrete complex type  | No                           |
|                       | Concrete simple type   | No                           |
| anyType               | anyType                | Yes - assign input to output |
|                       | any                    | No                           |
|                       | anyAttribute           | No                           |
|                       | anySimpleType          | Yes - assign input to output |
|                       | Concrete complex types | Yes - assign input to output |
|                       | Concrete simple types  | Yes - assign input to output |
| AnySimpleType         | AnySimpleType          | Yes - assign input to output |
|                       | any                    | No                           |
|                       | anyAttribute           | No                           |
|                       | anyType                | Yes - assign input to output |
|                       | Concrete complex type  | No                           |
|                       | Concrete simple types  | Yes - assign input to output |
| Concrete simple type  | any                    | No                           |
|                       | anyAttribute           | No                           |
|                       | anyType                | Yes - assign input to output |
|                       | anySimpleType          | Yes - assign input to output |
| Concrete complex type | any                    | No                           |
|                       | anyAttribute           | No                           |
|                       | anyType                | Yes - assign input to output |
|                       | anySimpleType          | No                           |

## Business rules

- No local variables in a rule set can be of weak type.
- You cannot use weak types in computations or comparisons.

| Input type            | Output type           | Supported                                                                                                                             |
|-----------------------|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| any                   | any                   | Yes. All existing open elements are deleted from the source and the source open elements are added to the end of the closed elements. |
|                       | anyAttribute          | No                                                                                                                                    |
|                       | anyType               | No                                                                                                                                    |
|                       | anySimpleType         | No                                                                                                                                    |
|                       | Concrete complex type | No                                                                                                                                    |
|                       | Concrete simple type  | No                                                                                                                                    |
| anyAtrribute          | any                   | No                                                                                                                                    |
|                       | anyAttribute          | Yes. All of the attributes are removed and replaced.                                                                                  |
|                       | anyType               | No                                                                                                                                    |
|                       | anySimpleType         | No                                                                                                                                    |
|                       | Concrete complex type | No                                                                                                                                    |
|                       | Concrete simple type  | No                                                                                                                                    |
| anyType               | anyType               | Yes. Assignment allowed.                                                                                                              |
|                       | Any                   | No                                                                                                                                    |
|                       | anyAttribute          | No                                                                                                                                    |
|                       | anySimpleType         | Yes. Assignment allowed if data is a simple type, for example a string.                                                               |
|                       | Concrete complex type | Yes. Assignment allowed if data is of a compatible type.                                                                              |
|                       | Concrete simple type  | Yes. Assignment allowed if data is of a compatible type.                                                                              |
| AnySimpleType         | anySimpleType         | Yes. Assignment allowed.                                                                                                              |
|                       | any                   | No                                                                                                                                    |
|                       | anyAttribute          | No                                                                                                                                    |
|                       | anyType               | Yes. Assignment allowed.                                                                                                              |
|                       | Concrete simple type  | No                                                                                                                                    |
|                       | Concrete complex type | Yes                                                                                                                                   |
| Concrete simple type  | any                   | No                                                                                                                                    |
|                       | anyAttribute          | No                                                                                                                                    |
|                       | anyType               | Yes. Assignment allowed.                                                                                                              |
|                       | anySimpleType         | Yes. Assignment allowed.                                                                                                              |
| Concrete complex type | any                   | No                                                                                                                                    |
|                       | anyAttribute          | No                                                                                                                                    |
|                       | anyType               | Yes. Assignment allowed.                                                                                                              |
|                       | anySimpleType         | No                                                                                                                                    |

## XML mapper

Table 4 shows how XML mapper supports
weak types.

| Input type            | Output type            | Supported         |
|-----------------------|------------------------|-------------------|
| any                   | any                    | Yes - use submaps |
|                       | anyAttribute           | No                |
|                       | anyType                | Yes - use submaps |
|                       | anySimpleType          | Yes - use submaps |
|                       | Concrete complex type  | Yes - use submaps |
|                       | Concrete simple type   | Yes - use submaps |
| anyAttribute          | any                    | No                |
|                       | anyAttribute           | Yes - use submaps |
|                       | anyType                | No                |
|                       | anySimpleType          | No                |
|                       | Concrete complex type  | No                |
|                       | Concrete simple type   | No                |
| anyType               | anyType                | Yes               |
|                       | any                    | Yes               |
|                       | anyAttribute           | No                |
|                       | anySimpleType          | Yes               |
|                       | Concrete complex types | No                |
|                       | Concrete simple types  | No                |
| AnySimpleType         | AnySimpleType          | Yes               |
|                       | any                    | No                |
|                       | anyAttribute           | No                |
|                       | anyType                | Yes               |
|                       | Concrete complex type  | No                |
|                       | Concrete simple types  | No                |
| Concrete simple type  | any                    | No                |
|                       | anyAttribute           | No                |
|                       | anyType                | Yes               |
|                       | anySimpleType          | Yes               |
| Concrete complex type | any                    | Yes - use submaps |
|                       | anyAttribute           | No                |
|                       | anyType                | Yes               |
|                       | anySimpleType          | Yes               |