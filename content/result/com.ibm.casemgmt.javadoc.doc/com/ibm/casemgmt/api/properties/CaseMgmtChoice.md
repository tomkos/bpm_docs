- Overview
- Package
- Class
- Tree
- Deprecated
- Index
- Help

- Prev Class
- Next Class

- Frames
- No Frames

- All Classes

- Summary:
- Nested |
- Field |
- Constr |
- Method

- Detail:
- Field |
- Constr |
- Method

## Class CaseMgmtChoice

- java.lang.Object
    - com.ibm.casemgmt.api.properties.CaseMgmtChoice

- public final class CaseMgmtChoice
extends java.lang.Object
Represents a single choice item in a choice list assigned to a property,
 or represents a group node for a nested collection of choice items within
 a choice list.  A single choice item can be of two possible types: integer or string.
 An integer type choice item holds a single integer value and is assigned only to 
 an integer-valued property. A string type choice item holds a single value and can
 be assigned only to a string-valued property.
 
 A choice object that represents a group node of nested choice items contains
 choice items that are all integer or string type choice items depending on the
 data type of the overall choice list.
 
 The type of this choice object is indicated by the getChoiceType
 method and returns a Content Engine Java API ChoiceType value.
 The choice type indicates the data type of the choice object, either string
 or integer, and also whether the choice object represents a single choice item
 or a group node containing a nested collection of choice items. The choice
 type determines what method should be called to get the value of a
 choice object, one of getIntegerChoice, getStringChoice, 
 or getChoices.

ID status:
ID review by David Newhall

- ========== METHOD SUMMARY ===========
    - Method Summary All Methods Instance Methods Concrete Methods Modifier and Type Method and Description java.util.List<CaseMgmtChoice > getChoices () Returns the collection of nested choice objects if this choice object represents a group node of additional choices. com.filenet.api.constants.ChoiceType getChoiceType () Indicates the type of this choice. java.lang.String getDisplayName () Returns the display name of this choice. java.lang.Integer getIntegerChoice () Returns the single integer value if this choice object represents a single choice item for an integer type property. java.lang.String getStringChoice () Returns the single string value if this choice object represents a single choice item for a string type property.

### Method Summary

| Modifier and Type                    | Method and Description                                                                                                                   |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| java.util.List<CaseMgmtChoice>       | getChoices() Returns the collection of nested choice objects if this choice  object represents a group node of additional choices.       |
| com.filenet.api.constants.ChoiceType | getChoiceType() Indicates the type of this choice.                                                                                       |
| java.lang.String                     | getDisplayName() Returns the display name of this choice.                                                                                |
| java.lang.Integer                    | getIntegerChoice() Returns the single integer value if this choice object  represents a single choice item for an integer type property. |
| java.lang.String                     | getStringChoice() Returns the single string value if this choice object represents  a single choice item for a string type property.     |

- Methods inherited from class java.lang.Object
equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait