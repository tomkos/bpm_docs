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

## Interface EHTID

- All Superinterfaces:
java.lang.Comparable, OID, java.io.Serializable

public interface EHTID
extends OID
Interface for an event handler template object identifier.
 
 An event handler template object identifier uniquely identifies an event handler template.
 It is created when the event handler template is created and stays with the event handler
 template during its lifetime.
 
 The object identifier can be retrieved using the
 getID() method of the event handler template.
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