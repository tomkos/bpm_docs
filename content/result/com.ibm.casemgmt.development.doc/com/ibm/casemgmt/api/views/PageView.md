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

## Class PageView

- java.lang.Object
    - com.ibm.casemgmt.api.views.PageView

- public final class PageView
extends java.lang.Object
Represents a page view for a case type. Page views are defined by the solution to control how the case properties
 are displayed in different types of views, such as summary views or case data views. 
 
 The getType method indicates the type of the view.  The getProperties method returns the list of 
 symbolic names of the properties in this view. If the view is a case data view, the getGroups method
 optionally returns a list of sub-groups of properties to show in their own groups.

ID status:
ID review by David Newhall, 5/16/2012.

- ========== METHOD SUMMARY ===========
    - Method Summary All Methods Instance Methods Concrete Methods Modifier and Type Method and Description java.util.List<PageViewGroup > getGroups () Returns a list of PageViewGroup objects that represent the groups of this view. java.util.List<java.lang.String> getProperties () Returns a list of the symbolic names for the properties in this view. CaseViewType getType () Returns the type of the view, that is, whether the view is a case summary view, case data view, etc.

### Method Summary

| Modifier and Type                | Method and Description                                                                                         |
|----------------------------------|----------------------------------------------------------------------------------------------------------------|
| java.util.List<PageViewGroup>    | getGroups() Returns a list of PageViewGroup objects that represent the groups of this view.                    |
| java.util.List<java.lang.String> | getProperties() Returns a list of the symbolic names for the properties in this view.                          |
| CaseViewType                     | getType() Returns the type of the view, that is, whether the view is a case summary view, case data view, etc. |

- Methods inherited from class java.lang.Object
equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait