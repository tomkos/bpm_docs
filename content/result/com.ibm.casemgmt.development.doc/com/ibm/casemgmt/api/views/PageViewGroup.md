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

## Class PageViewGroup

- java.lang.Object
    - com.ibm.casemgmt.api.views.PageViewGroup

- public final class PageViewGroup
extends java.lang.Object
Represents a page view group for a case type. Page views are defined by the solution to control how the case 
 properties are displayed in different types of views. If the view has subgroups of properties, the information about
 those groups is returned as instances of this class.

ID status:
ID review by David Newhall, 5/16/2012.

- ========== METHOD SUMMARY ===========
    - Method Summary All Methods Instance Methods Concrete Methods Modifier and Type Method and Description boolean getInitialOpenState () Indicates whether the group should be shown initially open. java.lang.String getLocalizedName (java.util.Locale locale) Returns a locale-sensitive name of the group. java.lang.String getName () Returns the name of the group. java.util.List<java.lang.String> getProperties () Returns a list of the symbolic names for the properties in this group. CaseViewType getType () Returns the type of the view.

### Method Summary

| Modifier and Type                | Method and Description                                                                  |
|----------------------------------|-----------------------------------------------------------------------------------------|
| boolean                          | getInitialOpenState() Indicates whether the group should be shown initially open.       |
| java.lang.String                 | getLocalizedName(java.util.Locale locale) Returns a locale-sensitive name of the group. |
| java.lang.String                 | getName() Returns the name of the group.                                                |
| java.util.List<java.lang.String> | getProperties() Returns a list of the symbolic names for the properties in this group.  |
| CaseViewType                     | getType() Returns the type of the view.                                                 |

- Methods inherited from class java.lang.Object
equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait