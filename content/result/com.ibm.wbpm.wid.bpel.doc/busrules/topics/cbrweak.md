<!-- image -->

# Weak type support with business rules

- an arbitrary simple type (xs:anySimpleType)
- an arbitrary complexType (xs:anyComplexType)
- an arbitrary type (simple or complex, called 'xs:anyType')
- an arbitrary element (xs:any)

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
| anyAttribute          | any                   | No                                                                                                                                    |
|                       | anyAttribute          | Yes. All of the attributes are removed and replaced.                                                                                  |
|                       | anyType               | No                                                                                                                                    |
|                       | anySimpleType         | No                                                                                                                                    |
|                       | Concrete complex type | No                                                                                                                                    |
|                       | Concrete simple type  | No                                                                                                                                    |
| anyType               | anyType               | Yes. Assignment allowed.                                                                                                              |
|                       | any                   | No                                                                                                                                    |
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