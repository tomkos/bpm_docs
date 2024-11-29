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

## Interface UserDefinedProperty

- All Superinterfaces:
BusinessRuleChangeDetector, Property, java.io.Serializable

public interface UserDefinedProperty
extends Property
This interface represents a user-defined property.  The value of a user-defined property
 can be changed.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary Fields Modifier and Type Field and Description static java.lang.String COPYRIGHT

### Field Summary

| Modifier and Type       | Field and Description   |
|-------------------------|-------------------------|
| static java.lang.String | COPYRIGHT               |

- Fields inherited from interface com.ibm.wbiserver.brules.mgmt.Property
PROPERTY\_NAME\_\_DISPLAY\_NAME, PROPERTY\_NAME\_\_NAME, PROPERTY\_NAME\_\_SHELL, PROPERTY\_NAME\_\_TARGET\_NAME\_SPACE, PROPERTY\_NAME\_\_UUID, PROPERTY\_NAME\_\_VERSION

- Method Summary Methods Modifier and Type Method and Description void setValue (java.lang.String newValue) Set the value of this property to the new value.

### Method Summary

| Modifier and Type   | Method and Description                                                               |
|---------------------|--------------------------------------------------------------------------------------|
| void                | setValue(java.lang.String newValue) Set the value of this property to the new value. |

    - Methods inherited from interface com.ibm.wbiserver.brules.mgmt.Property
getName, getValue
    - Methods inherited from interface com.ibm.wbiserver.brules.mgmt.BusinessRuleChangeDetector
hasChanges