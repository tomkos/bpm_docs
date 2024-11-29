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

## Interface PropertyList

- All Superinterfaces:
BusinessRuleChangeDetector, java.lang.Iterable<Property>, java.io.Serializable

public interface PropertyList
extends BusinessRuleChangeDetector, java.io.Serializable, java.lang.Iterable<Property>
This interface represents a list of properties.  Specific methods are provided for
 getting an iterator over the list, to get the element at a specified index, and to add 
 and remove elements from the list.  In order to change an existing Property 
 in the list, obtain the Property that you want to change using either an
 iterator or the get method and then simply use set methods to change the 
 object.  Note that only UserDefinedProperty objects are changeable so you 
 must check the subclass of the Property object before you can change it.
 
 This class also has methods to create a new UserDefinedProperty object.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description void addProperty (UserDefinedProperty newProperty) Add the specified property to the list. Property get (int index) Get the property at the specified index in the list. Property getByName (java.lang.String propertyName) Get the property with the specified name from the list. boolean isEmpty () Determine whether or not this list is empty. java.util.Iterator<Property > iterator () Get an iterator over this list. UserDefinedProperty newUserDefinedProperty (java.lang.String name, java.lang.String value) Create a new UserDefinedProperty object with the specified name and value. boolean removeProperty (UserDefinedProperty property) Remove the specified user-defined property from the list. UserDefinedProperty removePropertyByName (java.lang.String propertyName) Remove the user-defined property with the specified name from the list. void setPropertyValue (java.lang.String name, java.lang.String value) Set the value of the property with the specified name to the specified value. int size () Get the number of properties in this list.

### Method Summary

| Modifier and Type            | Method and Description                                                                                                                                                  |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| void                         | addProperty(UserDefinedProperty newProperty) Add the specified property to the list.                                                                                    |
| Property                     | get(int index) Get the property at the specified index in the list.                                                                                                     |
| Property                     | getByName(java.lang.String propertyName) Get the property with the specified name from the list.                                                                        |
| boolean                      | isEmpty() Determine whether or not this list is empty.                                                                                                                  |
| java.util.Iterator<Property> | iterator() Get an iterator over this list.                                                                                                                              |
| UserDefinedProperty          | newUserDefinedProperty(java.lang.String name,                       java.lang.String value) Create a new UserDefinedProperty object with the specified name and  value. |
| boolean                      | removeProperty(UserDefinedProperty property) Remove the specified user-defined property from the list.                                                                  |
| UserDefinedProperty          | removePropertyByName(java.lang.String propertyName) Remove the user-defined property with the specified name from the list.                                             |
| void                         | setPropertyValue(java.lang.String name,                 java.lang.String value) Set the value of the property with the specified name to the specified value.           |
| int                          | size() Get the number of properties in this list.                                                                                                                       |

- Methods inherited from interface com.ibm.wbiserver.brules.mgmt.BusinessRuleChangeDetector
hasChanges