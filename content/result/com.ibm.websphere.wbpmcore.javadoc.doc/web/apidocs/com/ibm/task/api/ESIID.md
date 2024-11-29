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

## Interface ESIID

- All Superinterfaces:
java.lang.Comparable, OID, java.io.Serializable

public interface ESIID
extends OID
Interface for an escalation instance object identifier.
 
 An escalation instance object identifier uniquely identifies an escalation instance.
 It is created when the escalation instance is created and stays with the escalation instance
 during its lifetime.
 
 The object identifier can be retrieved using the
 getID() method of the escalation instance.
 
Since:
6.0

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