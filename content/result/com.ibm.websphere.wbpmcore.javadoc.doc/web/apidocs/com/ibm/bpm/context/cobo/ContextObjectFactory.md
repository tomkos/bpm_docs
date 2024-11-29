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

## Interface ContextObjectFactory

- All Superinterfaces:
org.eclipse.emf.ecore.EFactory, org.eclipse.emf.ecore.EModelElement, org.eclipse.emf.ecore.EObject, org.eclipse.emf.common.notify.Notifier

public interface ContextObjectFactory
extends org.eclipse.emf.ecore.EFactory

 The Factory for the model.
 It provides a create method for each non-abstract class of the model.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
$sccsid 

static java.lang.String
COPYRIGHT 

static ContextObjectFactory
eINSTANCE 

static ContextObjectFactory
INSTANCE
The singleton instance of the factory
    - Method Summary Methods Modifier and Type Method and Description ContextObject createContextObject () Returns a new object of class 'Context Object ' DocumentRoot createDocumentRoot () Returns a new object of class 'Document Root ' HeaderInfoType createHeaderInfoType () Returns a new object of class 'Header Info Type ' SourceInfoType createSourceInfoType () Returns a new object of class 'Source Info Type ' UserDefinedContextType createUserDefinedContextType () Returns a new object of class 'User Defined Context Type ' com.ibm.bpm.context.cobo.ContextObjectPackage getContextObjectPackage ()

### Method Summary

| Modifier and Type                             | Method and Description                                                                   |
|-----------------------------------------------|------------------------------------------------------------------------------------------|
| ContextObject                                 | createContextObject() Returns a new object of class 'Context Object'                     |
| DocumentRoot                                  | createDocumentRoot() Returns a new object of class 'Document Root'                       |
| HeaderInfoType                                | createHeaderInfoType() Returns a new object of class 'Header Info Type'                  |
| SourceInfoType                                | createSourceInfoType() Returns a new object of class 'Source Info Type'                  |
| UserDefinedContextType                        | createUserDefinedContextType() Returns a new object of class 'User Defined Context Type' |
| com.ibm.bpm.context.cobo.ContextObjectPackage | getContextObjectPackage()                                                                |

- Methods inherited from interface org.eclipse.emf.ecore.EFactory
convertToString, create, createFromString, getEPackage, setEPackage

- Methods inherited from interface org.eclipse.emf.ecore.EModelElement
getEAnnotation, getEAnnotations

- Methods inherited from interface org.eclipse.emf.ecore.EObject
eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eIsProxy, eIsSet, eResource, eSet, eUnset

- Methods inherited from interface org.eclipse.emf.common.notify.Notifier
eAdapters, eDeliver, eNotify, eSetDeliver