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

## Class CaseMgmtProperties

- java.lang.Object
    - com.ibm.casemgmt.api.properties.CaseMgmtProperties

- public class CaseMgmtProperties
extends java.lang.Object
Represents a collection of CaseMgmtProperty objects. Each
 CaseMgmtProperty object allows a property value to be accessed
 or modified as well as provides additional attributes about a property.

ID status:
ID review by David Newhall

- ========== METHOD SUMMARY ===========
    - Method Summary All Methods Instance Methods Concrete Methods Deprecated Methods Modifier and Type Method and Description java.util.List<CaseMgmtProperty > asList () Returns a read-only list. java.util.List<CaseMgmtProperty > copyList () Deprecated. A deep copy is not generated for all types of properties. In particular properties with dependent object values are copied by reference. In almost all cases the caller just wants the list of embedded CaseMgmtProperty objects as a list and asList() can be called for that. CaseMgmtProperty find (java.lang.String propertyName) Returns a CaseMgmtProperty object if it exists in the collection. CaseMgmtProperty get (java.lang.String propertyName) Obtains a CaseMgmtProperty object contained in the collection. java.lang.Object getObjectValue (java.lang.String propertyName) Returns the value of a particular property in the collection. com.filenet.api.meta.PropertyDescription getPropertyDescription (java.lang.String propertyName) Returns the a Content Engine Java API PropertyDescription with the given symbolic name appropriate for this property collection. boolean isDirty () Indicates if this collection has been modified. boolean isPropertyPresent (java.lang.String propertyName) Indicates if a CaseMgmtProperty object with the specified symbolic name is currently present in the collection. void putObjectValue (java.lang.String propertyName, java.lang.Object value) Updates an existing CaseMgmtProperty object in the collection or adds a new object to the collection with the specified value. int size () Returns the number of CaseMgmtProperty objects in the collection. boolean supportsProperty (java.lang.String propertyName) Indicates if a property symbolic name is valid for the type of object represented by this property collection (for example a particular case type).

### Method Summary

| Modifier and Type                        | Method and Description                                                                                                                                                                                                                                                                                      |
|------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| java.util.List<CaseMgmtProperty>         | asList() Returns a read-only list.                                                                                                                                                                                                                                                                          |
| java.util.List<CaseMgmtProperty>         | copyList() Deprecated.  A deep copy is not generated for all types of properties.  In particular properties with dependent  object values are copied by reference.  In almost all cases the caller just wants the list of embedded  CaseMgmtProperty objects as a list and asList() can be called for that. |
| CaseMgmtProperty                         | find(java.lang.String propertyName) Returns a CaseMgmtProperty object if it exists in the  collection.                                                                                                                                                                                                      |
| CaseMgmtProperty                         | get(java.lang.String propertyName) Obtains a CaseMgmtProperty object contained in   the collection.                                                                                                                                                                                                         |
| java.lang.Object                         | getObjectValue(java.lang.String propertyName) Returns the value of a particular property in the collection.                                                                                                                                                                                                 |
| com.filenet.api.meta.PropertyDescription | getPropertyDescription(java.lang.String propertyName) Returns the a Content Engine Java API PropertyDescription   with the given symbolic name appropriate for this property collection.                                                                                                                    |
| boolean                                  | isDirty() Indicates if this collection has been modified.                                                                                                                                                                                                                                                   |
| boolean                                  | isPropertyPresent(java.lang.String propertyName) Indicates if a CaseMgmtProperty object with the  specified symbolic name is currently present in the collection.                                                                                                                                           |
| void                                     | putObjectValue(java.lang.String propertyName,               java.lang.Object value) Updates an existing CaseMgmtProperty object in the collection  or adds a new object to the collection with the specified value.                                                                                         |
| int                                      | size() Returns the number of CaseMgmtProperty objects in the collection.                                                                                                                                                                                                                                    |
| boolean                                  | supportsProperty(java.lang.String propertyName) Indicates if a property symbolic name is valid for the type  of object represented by this property collection  (for example a particular case type).                                                                                                       |

- Methods inherited from class java.lang.Object
equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait