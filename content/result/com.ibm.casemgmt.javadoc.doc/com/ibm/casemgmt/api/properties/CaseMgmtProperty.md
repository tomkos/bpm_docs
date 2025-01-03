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

## Class CaseMgmtProperty

- java.lang.Object
    - com.ibm.casemgmt.api.properties.CaseMgmtProperty

- public final class CaseMgmtProperty extends java.lang.Object Represents a property belonging to an object in the case management system such as a Case object. Property objects allow you to access and modify the values of properties. Property objects also provide additional attributes about properties such as minimum and maximum values and choice lists. These attributes are typically associated with property descriptions in a Content Engine repository, representing the metadata of properties, and are associated with classes of objects rather than object instances. In a case management system, these attributes can potentially be determined dynamically based on the working values of the properties in a collection. This dynamic behavior can be configured by integrating with an external data service. The data type of a property is indicated by the getPropertyType method and returns a Content Engine Java API TypeID value. The following data types are supported for single-value type properties. Multivalue property values are represented by a java.util.List object for the simple types -- BOOLEAN , LONG , STRING , DOUBLE , DATE or GUID . The List object contains a list of objects of the types described above. When setting these multivalue property values, lists of other object types are accepted if they can be converted to the appropriate type of object as described above. Multivalue properties of type OBJECT are supported for properties that hold custom dependent objects. These types of OBJECT properties have a cardinality of LIST . Dependent objects are Content Engine objects that exist only in the context of a parent object, such as a Case object. Custom dependent objects are instances of CmAbstractDependent classes that are defined by a custom application, such as part of a solution in IBM Case Manager. Business objects that are defined in a Case Manager solution are created as dependent object classes and properties when deployed. The Content Engine includes other system-defined properties with system-defined dependent objects. These are not exposed through this API. Multivalue properties that hold custom dependent objects are represented by a Content Engine Java API DependentObjectList object. When properties are retrieved, this type of object is returned as the value of dependent object properties. When modifying this type of property, construct a DependentObjectList object and set as the property value. You can also modify the existing DependentObjectList object in the property value and the changes are saved when saving the parent object.

```
public final class CaseMgmtProperty
extends java.lang.Object
```

Property objects also provide additional attributes about properties such
 as minimum and maximum values and choice lists. These attributes are typically
 associated with property descriptions in a Content Engine repository, representing
 the metadata of properties, and are associated with classes of objects rather than
 object instances.  In a case management system, these attributes can potentially 
 be determined dynamically based on the working values of the properties in a collection.  This dynamic
 behavior can be configured by integrating with an external data service.
 
 The data type of a property is indicated by the getPropertyType
 method and returns a Content Engine Java API TypeID value. The following data types
 are supported for single-value type properties.  
 
BOOLEAN: Represented by a Java Boolean object or null
         if the property is not set. When setting the property value, a String
         object is also accepted if it represents the string representation of a boolean.
LONG: Represented by a Java Integer object or null
         if the property is not set. When setting the property value, any Number
         object is accepted if it can be converted to an integer. Also a String object 
         is accepted if it represents the string representation of an integer.
STRING: Represented by a Java String object or null
         if the property is not set.
DOUBLE: Represented by a Java Double object or null
         if the property is not set. When setting the property value, any Number
         object is accepted if it can be converted to a Double. A String
         object is accepted if it represents the string representation of a double value.
DATE: Represented by a Java Date object or null
         if the property is not set. When setting the property value, a String
         object is also accepted with a date in W3C format using the UTC time zone.  
         Such a format corresponds to the following pattern that can be applied to a 
         Java SimpleDateFormat object: "yyyy-MM-dd'T'HH:mm:ss'Z'".
         The time zone is "UTC".
GUID: Represented by a Content Engine Java API Id object or 
         null if the property is not set. When setting the property value, 
         a Java String object is also accepted if it is a string value of a 
         GUID with or without the curly braces.
OBJECT: Represented by a Content Engine Java API ObjectReference
         object or null if the property is not set. Currently only object references 
         are supported through the Case Manager Java API for properties. The API does not 
         currently support dereferencing object-valued properties to retrieve the actual 
         objects referenced. Also, the API currently only supports retrieving these single-value object 
         property values but not persisting changes to them

 Multivalue property values are represented by a java.util.List object for the simple
 types -- BOOLEAN, LONG, STRING, DOUBLE, DATE or GUID.
 The List object contains a list of objects of the types described above. When setting these multivalue
 property values, lists of other object types are accepted if they can be converted
 to the appropriate type of object as described above.
 
 Multivalue properties of type OBJECT are supported for properties that hold custom dependent objects.
 These types of OBJECT properties have a cardinality of LIST. 
 Dependent objects are Content Engine objects that exist only in the context of a parent object,
 such as a Case object.
   
 Custom dependent objects are instances of CmAbstractDependent classes that are defined by a custom application,
 such as part of a solution in IBM Case Manager.  Business objects that are defined in a Case Manager solution are created
 as dependent object classes and properties when deployed.  The Content Engine includes other system-defined properties with 
 system-defined dependent objects.  These are not exposed through this API.
 
 Multivalue properties that hold custom dependent objects are represented by a Content Engine Java API 
 DependentObjectList object.  When properties are retrieved, this type of object is returned
 as the value of dependent object properties.  When modifying this type of property, construct a DependentObjectList object 
 and set as the property value.  You can also modify the existing DependentObjectList object in the
 property value and the changes are saved when saving the parent object.

- ========== METHOD SUMMARY ===========
    - Method Summary All Methods Static Methods Instance Methods Concrete Methods Deprecated Methods Modifier and Type Method and Description CaseMgmtProperty copy () Deprecated. A deep copy is not generated for all types of properties. In particular properties with dependent object values are copied by reference. In almost all cases the caller just wants the list of embedded CaseMgmtProperty objects as a list and asList() on the collection can be called for that. static java.util.List<CaseMgmtProperty > copyList (java.util.List<CaseMgmtProperty > propsList) Deprecated. A deep copy is not generated for all types of properties. In particular properties with dependent object values are copied by reference. In almost all cases the caller just wants the list of embedded CaseMgmtProperty objects as a list and asList() on the collection can be called for that. com.filenet.api.constants.Cardinality getCardinality () Returns the cardinality of the property. CaseMgmtChoiceList getChoiceList () Returns the choice list if the property has a choice list. java.util.List<java.lang.Integer> getCustomInvalidItems () If an external data service performs custom validation of a property value and the property is a multivalue property, it can also indicate the individual items of the multivalue list that are invalid. java.lang.String getCustomValidationError () An external data service can perform any validation of its choosing on the current property values. java.lang.Object getDefaultValue () Returns the default value of this property. java.lang.String getDescription () Returns a textual description of the property. DisplayMode getDisplayMode () An external data service can determine what the value for a property must be. java.lang.String getDisplayName () Returns the name of the property that should be displayed to users. ExternalDataModifications getExternalDataModifications () Returns an object that indicates what attributes of this property object have been modified by an external data service, if any. static java.util.Map<java.lang.String,CaseMgmtProperty > getMap (java.util.List<CaseMgmtProperty > props) Returns a map to an existing list of CaseMgmtProperty objects keyed by symbolic name. java.lang.Integer getMaximumLength () Returns the maximum length of this property if any. java.lang.Object getMaximumValue () Returns the maximum value of this property if any. java.lang.Object getMinimumValue () Returns the minimum value of this property if any. java.lang.Object getOriginalValue () Indicates the original persisted value even if the current or working value has been modified. CaseMgmtPropertyState getOriginalValueState () Returns the state of the original value of this property object. com.filenet.api.constants.TypeID getPropertyType () Returns the data type of the property. java.lang.String getRequiredClassName () boolean getRequiresUniqueElements () For a multivalue property, indicates if the multivalue list requires unique elements. com.filenet.api.constants.PropertySettability getSettability () Returns the settability restrictions of the property. java.lang.String getSymbolicName () Returns the symbolic name of the property. java.lang.Object getValue () Returns the current value held by this property object. CaseMgmtPropertyState getValueState () Returns the state of the value of this property object. boolean hasDependentProperties () Indicates that one or more other properties depend on the value of this property. boolean isDirty () Indicates if this property has been modified by calling setObjectValue . boolean isHidden () Indicates if the property should be hidden in a user interface. boolean isInherited () Indicates if the property exists on the superclass of the class of object this property object is associated with. boolean isOrderable () Indicates if the property can be used in an Order By clause of a query. boolean isQueryable () Indicates if the property can be used in a query condition. boolean isRequired () Indicates if the property requires a value. boolean isSelectable () Indicates if the property can be selected in a query. boolean isSystemOwned () Indicates if this property is managed by the system. void setObjectOriginalValue (java.lang.Object value) Modifies the original value of the property. void setObjectValue (java.lang.Object value) Modifies the current value of the property. void unspecifyOriginalValue () Unspecifies the original value if an original value is currently specified.

### Method Summary

| Modifier and Type                                       | Method and Description                                                                                                                                                                                                                                                                                                                                                  |
|---------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CaseMgmtProperty                                        | copy() Deprecated.  A deep copy is not generated for all types of properties.  In particular properties with dependent  object values are copied by reference.  In almost all cases the caller just wants the list of embedded  CaseMgmtProperty objects as a list and asList() on the collection can be called for that.                                               |
| static java.util.List<CaseMgmtProperty>                 | copyList(java.util.List<CaseMgmtProperty> propsList) Deprecated.  A deep copy is not generated for all types of properties.  In particular properties with dependent  object values are copied by reference.  In almost all cases the caller just wants the list of embedded  CaseMgmtProperty objects as a list and asList() on the collection can be called for that. |
| com.filenet.api.constants.Cardinality                   | getCardinality() Returns the cardinality of the property.                                                                                                                                                                                                                                                                                                               |
| CaseMgmtChoiceList                                      | getChoiceList() Returns the choice list if the property has a choice list.                                                                                                                                                                                                                                                                                              |
| java.util.List<java.lang.Integer>                       | getCustomInvalidItems() If an external data service performs custom validation of a property value   and the property is a multivalue property, it can also indicate the   individual items of the multivalue list that are invalid.                                                                                                                                    |
| java.lang.String                                        | getCustomValidationError() An external data service can perform any validation of its choosing on the current   property values.                                                                                                                                                                                                                                        |
| java.lang.Object                                        | getDefaultValue() Returns the default value of this property.                                                                                                                                                                                                                                                                                                           |
| java.lang.String                                        | getDescription() Returns a textual description of the property.                                                                                                                                                                                                                                                                                                         |
| DisplayMode                                             | getDisplayMode() An external data service can determine what the value for a property must be.                                                                                                                                                                                                                                                                          |
| java.lang.String                                        | getDisplayName() Returns the name of the property that should be displayed to users.                                                                                                                                                                                                                                                                                    |
| ExternalDataModifications                               | getExternalDataModifications() Returns an object that indicates what attributes of this property object have been  modified by an external data service, if any.                                                                                                                                                                                                        |
| static java.util.Map<java.lang.String,CaseMgmtProperty> | getMap(java.util.List<CaseMgmtProperty> props) Returns a map to an existing list of CaseMgmtProperty objects keyed by symbolic name.                                                                                                                                                                                                                                    |
| java.lang.Integer                                       | getMaximumLength() Returns the maximum length of this property if any.                                                                                                                                                                                                                                                                                                  |
| java.lang.Object                                        | getMaximumValue() Returns the maximum value of this property if any.                                                                                                                                                                                                                                                                                                    |
| java.lang.Object                                        | getMinimumValue() Returns the minimum value of this property if any.                                                                                                                                                                                                                                                                                                    |
| java.lang.Object                                        | getOriginalValue() Indicates the original persisted value even if the current or working value  has been modified.                                                                                                                                                                                                                                                      |
| CaseMgmtPropertyState                                   | getOriginalValueState() Returns the state of the original value of this property object.                                                                                                                                                                                                                                                                                |
| com.filenet.api.constants.TypeID                        | getPropertyType() Returns the data type of the property.                                                                                                                                                                                                                                                                                                                |
| java.lang.String                                        | getRequiredClassName()                                                                                                                                                                                                                                                                                                                                                  |
| boolean                                                 | getRequiresUniqueElements() For a multivalue property, indicates if the multivalue list requires  unique elements.                                                                                                                                                                                                                                                      |
| com.filenet.api.constants.PropertySettability           | getSettability() Returns the settability restrictions of the property.                                                                                                                                                                                                                                                                                                  |
| java.lang.String                                        | getSymbolicName() Returns the symbolic name of the property.                                                                                                                                                                                                                                                                                                            |
| java.lang.Object                                        | getValue() Returns the current value held by this property object.                                                                                                                                                                                                                                                                                                      |
| CaseMgmtPropertyState                                   | getValueState() Returns the state of the value of this property object.                                                                                                                                                                                                                                                                                                 |
| boolean                                                 | hasDependentProperties() Indicates that one or more other properties depend on the value of this property.                                                                                                                                                                                                                                                              |
| boolean                                                 | isDirty() Indicates if this property has been modified by calling   setObjectValue.                                                                                                                                                                                                                                                                                     |
| boolean                                                 | isHidden() Indicates if the property should be hidden in a user interface.                                                                                                                                                                                                                                                                                              |
| boolean                                                 | isInherited() Indicates if the property exists on the superclass of the class of  object this property object is associated with.                                                                                                                                                                                                                                       |
| boolean                                                 | isOrderable() Indicates if the property can be used in an Order By clause of a query.                                                                                                                                                                                                                                                                                   |
| boolean                                                 | isQueryable() Indicates if the property can be used in a query condition.                                                                                                                                                                                                                                                                                               |
| boolean                                                 | isRequired() Indicates if the property requires a value.                                                                                                                                                                                                                                                                                                                |
| boolean                                                 | isSelectable() Indicates if the property can be selected in a query.                                                                                                                                                                                                                                                                                                    |
| boolean                                                 | isSystemOwned() Indicates if this property is managed by the system.                                                                                                                                                                                                                                                                                                    |
| void                                                    | setObjectOriginalValue(java.lang.Object value) Modifies the original value of the property.                                                                                                                                                                                                                                                                             |
| void                                                    | setObjectValue(java.lang.Object value) Modifies the current value of the property.                                                                                                                                                                                                                                                                                      |
| void                                                    | unspecifyOriginalValue() Unspecifies the original value if an original value is currently specified.                                                                                                                                                                                                                                                                    |

- Methods inherited from class java.lang.Object
equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait