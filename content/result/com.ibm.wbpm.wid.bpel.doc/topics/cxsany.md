<!-- image -->

# Assigning from and to xs:any

- an arbitrary simple type (xs:anySimpleType)
- an arbitrary complexType (xs:anyComplexType)
- an arbitrary type (simple or complex, called 'xs:anyType')
- an arbitrary element (xs:any)

Assigning from and to such wildcards has a number of specialities.
This works very well for type based wildcards (anyType, anySimpleType,
anyComplexType). For xs:any, there are a few things to consider, as
discussed in the following sections.

## Assigning from any (using the assign activity)

Once
you select an xs:any element, a window will appear that asks you for
a name. Since xs:any is a wildcard, it typically represents a concrete
element. For example, in the business object definition, an xs:any
is modeled, but at run time there is a concrete order element
at the position of the any. Therefore, in the window, insert the name
of the concrete element that will be there at run time (for example, order).

In
cases you do not know the name, you might also access the element
using the syntax *[n], where n stands for the position of the
element within the business object at run time.

## Assigning to any (using the assign activity)

You
might wonder why there is no xs:any shown in the assign on the to side.
The reason is: xs:any on the to-side of assign is currently not supported.
 As a workaround, use a Java™ Snippet
to achieve this.

| Input type            | Output type           | Supported?                   |
|-----------------------|-----------------------|------------------------------|
| any                   | any                   | No                           |
|                       | anyAttribute          | No                           |
|                       | anyType               | Yes - assign input to output |
|                       | anySimpleType         | Yes - assign input to output |
|                       | Concrete complex type | Yes - assign input to output |
|                       | Concrete simple type  | Yes - assign input to output |
| anyAttribute          | any                   | No                           |
|                       | anyAttribute          | No                           |
|                       | anyType               | No                           |
|                       | anySimpleType         | No                           |
|                       | Concrete complex type | No                           |
|                       | Concrete simple type  | No                           |
| anyType               | anyType               | Yes - assign input to output |
|                       | any                   | No                           |
|                       | anyAttribute          | No                           |
|                       | anySimpleType         | Yes - assign input to output |
|                       | Concrete complex type | Yes - assign input to output |
|                       | Concrete simple type  | Yes - assign input to output |
| AnySimpleType         | AnySimpleType         | Yes - assign input to output |
|                       | any                   | No                           |
|                       | anyAttribute          | No                           |
|                       | anyType               | Yes - assign input to output |
|                       | Concrete complex type | No                           |
|                       | Concrete simple types | Yes - assign input to output |
| Concrete simple type  | any                   | No                           |
|                       | anyAttribute          | No                           |
|                       | anyType               | Yes - assign input to output |
|                       | anySimpleType         | Yes - assign input to output |
| Concrete complex type | any                   | No                           |
|                       | anyAttribute          | No                           |
|                       | anyType               | Yes - assign input to output |
|                       | anySimpleType         | No                           |