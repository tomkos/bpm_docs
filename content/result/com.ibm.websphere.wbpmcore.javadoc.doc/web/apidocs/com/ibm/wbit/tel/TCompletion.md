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

## Interface TCompletion

- All Superinterfaces:
org.eclipse.emf.ecore.EObject, org.eclipse.emf.common.notify.Notifier

public interface TCompletion
extends org.eclipse.emf.ecore.EObject

 A representation of the model object 'TCompletion'.
 

Since:
7.0
See Also:TaskPackage.getTCompletion()

- ========== METHOD SUMMARY ===========
    - Method Summary Methods Modifier and Type Method and Description TCriterion getCriterion () Returns the value of the 'Criterion ' containment reference java.lang.String getName () Returns the value of the 'Name ' attribute TResult getResult () Returns the value of the 'Result ' containment reference TBoolean getUseDefaultResultConstruction () Returns the value of the 'Use Default Result Construction ' attribute. boolean isSetUseDefaultResultConstruction () Returns whether the value of the 'Use Default Result Construction ' attribute is set void setCriterion (TCriterion value) Sets the value of the 'Criterion ' containment reference void setName (java.lang.String value) Sets the value of the 'Name ' attribute void setResult (TResult value) Sets the value of the 'Result ' containment reference void setUseDefaultResultConstruction (TBoolean value) Sets the value of the 'Use Default Result Construction ' attribute void unsetUseDefaultResultConstruction () Unsets the value of the 'Use Default Result Construction ' attribute

### Method Summary

| Modifier and Type   | Method and Description                                                                                                  |
|---------------------|-------------------------------------------------------------------------------------------------------------------------|
| TCriterion          | getCriterion() Returns the value of the 'Criterion' containment reference                                               |
| java.lang.String    | getName() Returns the value of the 'Name' attribute                                                                     |
| TResult             | getResult() Returns the value of the 'Result' containment reference                                                     |
| TBoolean            | getUseDefaultResultConstruction() Returns the value of the 'Use Default Result Construction' attribute.                 |
| boolean             | isSetUseDefaultResultConstruction() Returns whether the value of the 'Use Default Result Construction' attribute is set |
| void                | setCriterion(TCriterion value) Sets the value of the 'Criterion' containment reference                                  |
| void                | setName(java.lang.String value) Sets the value of the 'Name' attribute                                                  |
| void                | setResult(TResult value) Sets the value of the 'Result' containment reference                                           |
| void                | setUseDefaultResultConstruction(TBoolean value) Sets the value of the 'Use Default Result Construction' attribute       |
| void                | unsetUseDefaultResultConstruction() Unsets the value of the 'Use Default Result Construction' attribute                 |

- Methods inherited from interface org.eclipse.emf.ecore.EObject
eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eIsProxy, eIsSet, eResource, eSet, eUnset

- Methods inherited from interface org.eclipse.emf.common.notify.Notifier
eAdapters, eDeliver, eNotify, eSetDeliver