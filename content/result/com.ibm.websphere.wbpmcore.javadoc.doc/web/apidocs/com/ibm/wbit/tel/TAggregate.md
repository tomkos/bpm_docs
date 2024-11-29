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

## Interface TAggregate

- All Superinterfaces:
org.eclipse.emf.ecore.EObject, org.eclipse.emf.common.notify.Notifier

public interface TAggregate
extends org.eclipse.emf.ecore.EObject

 A representation of the model object 'TAggregate'.
 

Since:
7.0
See Also:TaskPackage.getTAggregate()

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getCondition () Returns the value of the 'Condition ' attribute java.lang.String getFunction () Returns the value of the 'Function ' attribute java.lang.String getLocation () Returns the value of the 'Location ' attribute java.lang.String getPart () Returns the value of the 'Part ' attribute void setCondition (java.lang.String value) Sets the value of the 'Condition ' attribute void setFunction (java.lang.String value) Sets the value of the 'Function ' attribute void setLocation (java.lang.String value) Sets the value of the 'Location ' attribute void setPart (java.lang.String value) Sets the value of the 'Part ' attribute

### Method Summary

| Modifier and Type   | Method and Description                                                           |
|---------------------|----------------------------------------------------------------------------------|
| java.lang.String    | getCondition() Returns the value of the 'Condition' attribute                    |
| java.lang.String    | getFunction() Returns the value of the 'Function' attribute                      |
| java.lang.String    | getLocation() Returns the value of the 'Location' attribute                      |
| java.lang.String    | getPart() Returns the value of the 'Part' attribute                              |
| void                | setCondition(java.lang.String value) Sets the value of the 'Condition' attribute |
| void                | setFunction(java.lang.String value) Sets the value of the 'Function' attribute   |
| void                | setLocation(java.lang.String value) Sets the value of the 'Location' attribute   |
| void                | setPart(java.lang.String value) Sets the value of the 'Part' attribute           |

- Methods inherited from interface org.eclipse.emf.ecore.EObject
eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eIsProxy, eIsSet, eResource, eSet, eUnset

- Methods inherited from interface org.eclipse.emf.common.notify.Notifier
eAdapters, eDeliver, eNotify, eSetDeliver