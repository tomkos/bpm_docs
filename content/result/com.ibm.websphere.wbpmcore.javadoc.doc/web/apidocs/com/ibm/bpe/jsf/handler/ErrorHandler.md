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

## Interface ErrorHandler

- All Superinterfaces:
ItemProvider

All Known Implementing Classes:
BPCListHandler

public interface ErrorHandler
extends ItemProvider
A container that is able to display exceptions for individual items that have also been provided.
 To use this container, you must set up a map that associates the exceptions with the IDs of the items provided.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description java.util.Map getErrors () Retrieve the errors that were reported for the items. void setErrors (java.util.Map errors) Command implementations can use this method to report errors for individual items.

### Method Summary

| Modifier and Type   | Method and Description                                                                                             |
|---------------------|--------------------------------------------------------------------------------------------------------------------|
| java.util.Map       | getErrors() Retrieve the errors that were reported for the items.                                                  |
| void                | setErrors(java.util.Map errors) Command implementations can use this method to report errors for individual items. |

- Methods inherited from interface com.ibm.bpe.jsf.handler.ItemProvider
getSelectedItems