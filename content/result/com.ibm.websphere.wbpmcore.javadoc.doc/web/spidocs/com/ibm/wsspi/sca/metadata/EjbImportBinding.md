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

## Interface EjbImportBinding

- All Superinterfaces:
ImportBinding

public interface EjbImportBinding
extends ImportBinding
Interface that represent the EJB binding information on a SCA import.
Since:
7.5.1.0

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getJndiName () Method returns the JNDI name of the EJB import binding.

### Method Summary

| Modifier and Type   | Method and Description                                                |
|---------------------|-----------------------------------------------------------------------|
| java.lang.String    | getJndiName() Method returns the JNDI name of the EJB import binding. |

- Methods inherited from interface com.ibm.wsspi.sca.metadata.ImportBinding
getBindingType