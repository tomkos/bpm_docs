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

## Interface TCriterion

- All Superinterfaces:
org.eclipse.emf.ecore.EObject, org.eclipse.emf.common.notify.Notifier

public interface TCriterion
extends org.eclipse.emf.ecore.EObject

 A representation of the model object 'TCriterion'.
 

Since:
7.0
See Also:TaskPackage.getTCriterion()

- ========== METHOD SUMMARY ===========
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getCondition () Returns the value of the 'Condition ' attribute java.lang.String getFor () Returns the value of the 'For ' attribute void setCondition (java.lang.String value) Sets the value of the 'Condition ' attribute void setFor (java.lang.String value) Sets the value of the 'For ' attribute

### Method Summary

| Modifier and Type   | Method and Description                                                           |
|---------------------|----------------------------------------------------------------------------------|
| java.lang.String    | getCondition() Returns the value of the 'Condition' attribute                    |
| java.lang.String    | getFor() Returns the value of the 'For' attribute                                |
| void                | setCondition(java.lang.String value) Sets the value of the 'Condition' attribute |
| void                | setFor(java.lang.String value) Sets the value of the 'For' attribute             |

- Methods inherited from interface org.eclipse.emf.ecore.EObject
eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eIsProxy, eIsSet, eResource, eSet, eUnset

- Methods inherited from interface org.eclipse.emf.common.notify.Notifier
eAdapters, eDeliver, eNotify, eSetDeliver