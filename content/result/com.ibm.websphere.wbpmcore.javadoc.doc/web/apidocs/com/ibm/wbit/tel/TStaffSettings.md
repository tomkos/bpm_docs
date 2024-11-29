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

## Interface TStaffSettings

- All Superinterfaces:
org.eclipse.emf.ecore.EObject, org.eclipse.emf.common.notify.Notifier

public interface TStaffSettings
extends org.eclipse.emf.ecore.EObject

 A representation of the model object 'TStaff Settings'.
 

 Contains the staff settings as required by the 
         individual tasks. Not all elements are applicable for all task 
         kinds. Pls. refer to the SDD to see which may be used for which 
         tasks.
Since:
6.0.1
See Also:TaskPackage.getTStaffSettings()

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description TAdministrator getAdministrator () Returns the value of the 'Administrator ' containment reference org.eclipse.emf.common.util.EList getContactQuery () Returns the value of the 'Contact Query ' containment reference list. TEditor getEditor () Returns the value of the 'Editor ' containment reference TInheritedAuthorization getInheritedAuthorization () Returns the value of the 'Inherited Authorization ' attribute. TPotentialInstanceCreator getPotentialInstanceCreator () Returns the value of the 'Potential Instance Creator ' containment reference TPotentialOwner getPotentialOwner () Returns the value of the 'Potential Owner ' containment reference TPotentialStarter getPotentialStarter () Returns the value of the 'Potential Starter ' containment reference TReader getReader () Returns the value of the 'Reader ' containment reference boolean isSetInheritedAuthorization () Returns whether the value of the 'Inherited Authorization ' attribute is set void setAdministrator (TAdministrator value) Sets the value of the 'Administrator ' containment reference void setEditor (TEditor value) Sets the value of the 'Editor ' containment reference void setInheritedAuthorization (TInheritedAuthorization value) Sets the value of the 'Inherited Authorization ' attribute void setPotentialInstanceCreator (TPotentialInstanceCreator value) Sets the value of the 'Potential Instance Creator ' containment reference void setPotentialOwner (TPotentialOwner value) Sets the value of the 'Potential Owner ' containment reference void setPotentialStarter (TPotentialStarter value) Sets the value of the 'Potential Starter ' containment reference void setReader (TReader value) Sets the value of the 'Reader ' containment reference void unsetInheritedAuthorization () Unsets the value of the 'Inherited Authorization ' attribute

### Method Summary

| Modifier and Type                 | Method and Description                                                                                                                |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| TAdministrator                    | getAdministrator() Returns the value of the 'Administrator' containment reference                                                     |
| org.eclipse.emf.common.util.EList | getContactQuery() Returns the value of the 'Contact Query' containment reference list.                                                |
| TEditor                           | getEditor() Returns the value of the 'Editor' containment reference                                                                   |
| TInheritedAuthorization           | getInheritedAuthorization() Returns the value of the 'Inherited Authorization' attribute.                                             |
| TPotentialInstanceCreator         | getPotentialInstanceCreator() Returns the value of the 'Potential Instance Creator' containment reference                             |
| TPotentialOwner                   | getPotentialOwner() Returns the value of the 'Potential Owner' containment reference                                                  |
| TPotentialStarter                 | getPotentialStarter() Returns the value of the 'Potential Starter' containment reference                                              |
| TReader                           | getReader() Returns the value of the 'Reader' containment reference                                                                   |
| boolean                           | isSetInheritedAuthorization() Returns whether the value of the 'Inherited Authorization' attribute is set                             |
| void                              | setAdministrator(TAdministrator value) Sets the value of the 'Administrator' containment reference                                    |
| void                              | setEditor(TEditor value) Sets the value of the 'Editor' containment reference                                                         |
| void                              | setInheritedAuthorization(TInheritedAuthorization value) Sets the value of the 'Inherited Authorization' attribute                    |
| void                              | setPotentialInstanceCreator(TPotentialInstanceCreator value) Sets the value of the 'Potential Instance Creator' containment reference |
| void                              | setPotentialOwner(TPotentialOwner value) Sets the value of the 'Potential Owner' containment reference                                |
| void                              | setPotentialStarter(TPotentialStarter value) Sets the value of the 'Potential Starter' containment reference                          |
| void                              | setReader(TReader value) Sets the value of the 'Reader' containment reference                                                         |
| void                              | unsetInheritedAuthorization() Unsets the value of the 'Inherited Authorization' attribute                                             |

- Methods inherited from interface org.eclipse.emf.ecore.EObject
eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eIsProxy, eIsSet, eResource, eSet, eUnset

- Methods inherited from interface org.eclipse.emf.common.notify.Notifier
eAdapters, eDeliver, eNotify, eSetDeliver