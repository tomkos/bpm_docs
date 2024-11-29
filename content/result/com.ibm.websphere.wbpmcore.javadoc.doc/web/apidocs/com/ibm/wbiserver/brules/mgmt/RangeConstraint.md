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

## Interface RangeConstraint

- All Superinterfaces:
Constraint, java.io.Serializable

public interface RangeConstraint
extends Constraint
This interface represents a range constraint on a value.  The value must be within the specified
 range in order to be valid.

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
getLowerBound()
Get the lower bound of the range.

java.lang.String
getUpperBound()
Get the upper bound of the range.

boolean
isLowerBoundInclusive()
Determine whether or not the lower bound of this range is inclusive, i.e. whether or not the
 lower bound value is included in the range.

boolean
isUpperBoundInclusive()
Determine whether or not the upper bound of this range is inclusive, i.e. whether or not the
 upper bound value is included in the range.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getLowerBound
java.lang.String getLowerBound()
Get the lower bound of the range.  The returned string can be parsed into the numeric type
 that the associated variable is declared to be.  For example, if the associated variable is
 declared to be of type float, then the returned string can be parsed to produce a float value
 using the Float.valueOf() method.  Returns null if there is no lower bound.
Returns:The lower bound as a String.  Returns null if there is no lower bound.
    - isLowerBoundInclusive
boolean isLowerBoundInclusive()
Determine whether or not the lower bound of this range is inclusive, i.e. whether or not the
 lower bound value is included in the range.
Returns:true if the lower bound is included in the range; otherwise false.
    - getUpperBound
java.lang.String getUpperBound()
Get the upper bound of the range.  The returned string can be parsed into the numeric type
 that the associated variable is declared to be.  For example, if the associated variable is
 declared to be of type float, then the returned string can be parsed to produce a float value
 using the Float.valueOf() method.  Returns null if there is no upper bound.
Returns:The upper bound as a String.  Returns null if there is no upper bound.
    - isUpperBoundInclusive
boolean isUpperBoundInclusive()
Determine whether or not the upper bound of this range is inclusive, i.e. whether or not the
 upper bound value is included in the range.
Returns:true if the upper bound is included in the range; otherwise false.