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

## Interface AIID

- All Superinterfaces:
java.lang.Comparable, OID, java.io.Serializable

public interface AIID
extends OID
Interface for an activity instance object identifier.
 
 An activity instance object identifier uniquely identifies an activity instance.
 It is created when the activity instance is created and stays with the activity instance
 during its lifetime.
 
 The object identifier can be retrieved using the
 getID() method of the activity instance.
Since:
5.0

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary Fields Modifier and Type Field and Description static java.lang.String COPYRIGHT

### Field Summary

| Modifier and Type       | Field and Description   |
|-------------------------|-------------------------|
| static java.lang.String | COPYRIGHT               |

- Fields inherited from interface com.ibm.bpe.api.OID
OBJECT\_META\_TYPE\_A, OBJECT\_META\_TYPE\_B, OBJECT\_META\_TYPE\_C, OBJECT\_META\_TYPE\_D

- Method Summary

### Method Summary

    - Methods inherited from interface com.ibm.bpe.api.OID
compareTo, getObjectMetaType, isPersistent, toByteArray, toString