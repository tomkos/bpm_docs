- Overview
- Package
- Class
- Tree
- Deprecated
- Index
- Help

- Prev Class
- Next Class

- Frames
- No Frames

- All Classes

- Summary:
- Nested |
- Field |
- Constr |
- Method

- Detail:
- Field |
- Constr |
- Method

## Interface ValidationProblem

- public interface ValidationProblem
Describes validation problems of task instances or templates that have been created
 spontaneously (ad hoc).
Since:
6.0.1
See Also:ErrorTypeEnum

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary

Methods 

Modifier and Type
Method and Description

java.lang.String
getMessage()
Returns the message text of the validation problem.

java.lang.Object[]
getMessageAttributes()
Returns the values of attributes that were used to make up the complete message text.

ErrorTypeEnum
getType()
Returns the type, that is, the severity of the validation problem.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getType ErrorTypeEnum getType() Returns the type, that is, the severity of the validation problem. Possible values are: Returns: ErrorTypeEnum - The type of the error.

#### getType

```
ErrorTypeEnum getType()
```

    - ErrorTypeEnum.INFO
    - ErrorTypeEnum.WARNING
    - ErrorTypeEnum.ERROR

- getMessage
java.lang.String getMessage()
Returns the message text of the validation problem.
Returns:String -
    Localized message text of the validation problem.

- getMessageAttributes
java.lang.Object[] getMessageAttributes()
Returns the values of attributes that were used to make up the complete message text.
Returns:Object[]
    The array of attribute values. An empty array is returned if there are no
    attribute values.