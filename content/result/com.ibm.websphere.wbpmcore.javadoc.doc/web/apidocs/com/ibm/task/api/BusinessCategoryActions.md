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

## Interface BusinessCategoryActions

- public interface BusinessCategoryActions
This interface defines symbolic constants for all actions that can be performed on
 business categories. These constants are to be used when determining the actions
 allowed by the currently logged-on user.
 Currently allowed actions are returned when calling the
 getAvailableActionsForBusinessCategory()
 or getAvailableActionFlagsForBusinessCategories()
 methods for a business category.
Since:
6.2.0.3

- =========== FIELD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static int
CREATEBUSINESSCATEGORY
Symbolic constant for business category action create.

static int
DELETEBUSINESSCATEGORY
Symbolic constant for business category action delete.

static int
GETBUSINESSCATEGORY
Symbolic constant for business category action get.

static int
GETBUSINESSCATEGORYDEFINITION
Symbolic constant for business category action get business category definition.

static int
GETROLEINFO
Symbolic constant for business category action get (all) work items.

static int
UPDATE
Symbolic constant for business category action update.

- ============ FIELD DETAIL ===========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- GETBUSINESSCATEGORY
static final int GETBUSINESSCATEGORY
Symbolic constant for business category action get.
See Also:Constant Field Values

- GETROLEINFO
static final int GETROLEINFO
Symbolic constant for business category action get (all) work items.
See Also:Constant Field Values

- GETBUSINESSCATEGORYDEFINITION
static final int GETBUSINESSCATEGORYDEFINITION
Symbolic constant for business category action get business category definition.
See Also:Constant Field Values

- CREATEBUSINESSCATEGORY
static final int CREATEBUSINESSCATEGORY
Symbolic constant for business category action create.
See Also:Constant Field Values

- UPDATE
static final int UPDATE
Symbolic constant for business category action update.
See Also:Constant Field Values

- DELETEBUSINESSCATEGORY
static final int DELETEBUSINESSCATEGORY
Symbolic constant for business category action delete.
See Also:Constant Field Values