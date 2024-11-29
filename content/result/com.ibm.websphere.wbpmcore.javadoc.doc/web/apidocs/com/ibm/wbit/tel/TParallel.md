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

## Interface TParallel

- All Superinterfaces:
org.eclipse.emf.ecore.EObject, org.eclipse.emf.common.notify.Notifier

public interface TParallel
extends org.eclipse.emf.ecore.EObject

 A representation of the model object 'TParallel'.
 

 
         Existence of this element marks this task as parallel routing task
Since:
7.0
See Also:TaskPackage.getTParallel()

- ========== METHOD SUMMARY ===========
    - Method Summary Methods Modifier and Type Method and Description TCompletionBehavior getCompletionBehavior () Returns the value of the 'Completion Behavior ' containment reference TInheritedAuthorization getInheritedAuthorization () Returns the value of the 'Inherited Authorization ' attribute. boolean isSetInheritedAuthorization () Returns whether the value of the 'Inherited Authorization ' attribute is set void setCompletionBehavior (TCompletionBehavior value) Sets the value of the 'Completion Behavior ' containment reference void setInheritedAuthorization (TInheritedAuthorization value) Sets the value of the 'Inherited Authorization ' attribute void unsetInheritedAuthorization () Unsets the value of the 'Inherited Authorization ' attribute

### Method Summary

| Modifier and Type       | Method and Description                                                                                             |
|-------------------------|--------------------------------------------------------------------------------------------------------------------|
| TCompletionBehavior     | getCompletionBehavior() Returns the value of the 'Completion Behavior' containment reference                       |
| TInheritedAuthorization | getInheritedAuthorization() Returns the value of the 'Inherited Authorization' attribute.                          |
| boolean                 | isSetInheritedAuthorization() Returns whether the value of the 'Inherited Authorization' attribute is set          |
| void                    | setCompletionBehavior(TCompletionBehavior value) Sets the value of the 'Completion Behavior' containment reference |
| void                    | setInheritedAuthorization(TInheritedAuthorization value) Sets the value of the 'Inherited Authorization' attribute |
| void                    | unsetInheritedAuthorization() Unsets the value of the 'Inherited Authorization' attribute                          |

- Methods inherited from interface org.eclipse.emf.ecore.EObject
eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eIsProxy, eIsSet, eResource, eSet, eUnset

- Methods inherited from interface org.eclipse.emf.common.notify.Notifier
eAdapters, eDeliver, eNotify, eSetDeliver