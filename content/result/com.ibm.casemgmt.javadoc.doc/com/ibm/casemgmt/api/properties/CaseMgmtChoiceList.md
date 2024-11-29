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

## Class CaseMgmtChoiceList

- java.lang.Object
    - com.ibm.casemgmt.api.properties.CaseMgmtChoiceList

- public final class CaseMgmtChoiceList
extends java.lang.Object
Represents a list of choices that control what values can be assigned to
 a property. A choice list has a collection of CaseMgmtChoice
 objects. Each choice object has either a single value or is a group node
 containing a nested collection of choice objects.
 
 There are two types of choice lists: integer and string. All of the choice
 objects in the choice list are choices with single values of the same type, integer
 or string, or are group node collections of choices of that same type.
 
 The type of a choice list is indicated by the getDataType method
 which returns a Content Engine Java API TypeID value.  The only
 TypeID values that can be returned are the values corresponding to 
 integer (LONG) or string (STRING).

ID status:
ID review by David Newhall

- ========== METHOD SUMMARY ===========
    - Method Summary All Methods Instance Methods Concrete Methods Modifier and Type Method and Description java.util.List<CaseMgmtChoice > getChoices () Returns the choice objects contained by this choice list. com.filenet.api.constants.TypeID getDataType () Returns the data type of the choice list. java.lang.String getDisplayName () Returns the display name of the choice list. boolean hasHierarchy () Indicates if this choice list is flat, holding only single value choice items, or hierarchical, containing one or more additional levels of group nodes with nested collections of choice items.

### Method Summary

| Modifier and Type                | Method and Description                                                                                                                                                                                            |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| java.util.List<CaseMgmtChoice>   | getChoices() Returns the choice objects contained by this choice list.                                                                                                                                            |
| com.filenet.api.constants.TypeID | getDataType() Returns the data type of the choice list.                                                                                                                                                           |
| java.lang.String                 | getDisplayName() Returns the display name of the choice list.                                                                                                                                                     |
| boolean                          | hasHierarchy() Indicates if this choice list is flat, holding only single value choice  items, or hierarchical, containing one or more additional levels of group  nodes with nested collections of choice items. |

- Methods inherited from class java.lang.Object
equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait