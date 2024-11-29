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

## Interface QueryPropertyExtension

- All Superinterfaces:
QueryProperty, java.io.Serializable

public interface QueryPropertyExtension
extends QueryProperty
Returns the properties of a variable that can be queried and information about
 the associated process template.
 
 Query properties can be declared for process-level variables.
 The type of a query property can be a built-in XML schema simple type or a user-defined
 simple type based on a built-in XML schema type using restrictions.
Since:
6.1.2

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary Fields Modifier and Type Field and Description static java.lang.String COPYRIGHT

### Field Summary

| Modifier and Type       | Field and Description   |
|-------------------------|-------------------------|
| static java.lang.String | COPYRIGHT               |

- Fields inherited from interface com.ibm.bpe.api.QueryProperty
TYPE\_DECIMAL, TYPE\_GENERIC, TYPE\_NUMBER, TYPE\_STRING, TYPE\_TIMESTAMP

- Method Summary Methods Modifier and Type Method and Description java.lang.String getDisplayName () Returns the display name of the process template. PTID getProcessTemplateID () Returns the object ID of the process template that contains the query property. java.lang.String getProcessTemplateName () Returns the name of the process template. java.util.Calendar getValidFromTime () Returns the time the process template became or becomes valid.

### Method Summary

| Modifier and Type   | Method and Description                                                                                 |
|---------------------|--------------------------------------------------------------------------------------------------------|
| java.lang.String    | getDisplayName() Returns the display name of the process template.                                     |
| PTID                | getProcessTemplateID() Returns the object ID of the process template that contains the query property. |
| java.lang.String    | getProcessTemplateName() Returns the name of the process template.                                     |
| java.util.Calendar  | getValidFromTime() Returns the time the process template became or becomes valid.                      |

    - Methods inherited from interface com.ibm.bpe.api.QueryProperty
getMappedType, getName, getNamespace, getType, getVariableName