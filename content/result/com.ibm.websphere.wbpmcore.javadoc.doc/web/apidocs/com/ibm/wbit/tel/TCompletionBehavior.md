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

## Interface TCompletionBehavior

- All Superinterfaces:
org.eclipse.emf.ecore.EObject, org.eclipse.emf.common.notify.Notifier

public interface TCompletionBehavior
extends org.eclipse.emf.ecore.EObject

 A representation of the model object 'TCompletion Behavior'.
 

Since:
7.0
See Also:TaskPackage.getTCompletionBehavior()

- ========== METHOD SUMMARY ===========
    - Method Summary Methods Modifier and Type Method and Description org.eclipse.emf.common.util.EList getCompletion () Returns the value of the 'Completion ' containment reference list. TDefaultCompletion getDefaultCompletion () Returns the value of the 'Default Completion ' containment reference void setDefaultCompletion (TDefaultCompletion value) Sets the value of the 'Default Completion ' containment reference

### Method Summary

| Modifier and Type                 | Method and Description                                                                                          |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------|
| org.eclipse.emf.common.util.EList | getCompletion() Returns the value of the 'Completion' containment reference list.                               |
| TDefaultCompletion                | getDefaultCompletion() Returns the value of the 'Default Completion' containment reference                      |
| void                              | setDefaultCompletion(TDefaultCompletion value) Sets the value of the 'Default Completion' containment reference |

- Methods inherited from interface org.eclipse.emf.ecore.EObject
eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eIsProxy, eIsSet, eResource, eSet, eUnset

- Methods inherited from interface org.eclipse.emf.common.notify.Notifier
eAdapters, eDeliver, eNotify, eSetDeliver