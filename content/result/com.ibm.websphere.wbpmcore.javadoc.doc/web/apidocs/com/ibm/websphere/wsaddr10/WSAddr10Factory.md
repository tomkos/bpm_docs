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

## Interface WSAddr10Factory

- All Superinterfaces:
org.eclipse.emf.ecore.EFactory, org.eclipse.emf.ecore.EModelElement, org.eclipse.emf.ecore.EObject, org.eclipse.emf.common.notify.Notifier

public interface WSAddr10Factory
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

static WSAddr10Factory
eINSTANCE 

static WSAddr10Factory
INSTANCE
The singleton instance of the factory.
    - Method Summary Methods Modifier and Type Method and Description AttributedQNameType createAttributedQNameType () Returns a new object of class 'Attributed QName Type '. AttributedUnsignedLongType createAttributedUnsignedLongType () Returns a new object of class 'Attributed Unsigned Long Type '. AttributedURIType createAttributedURIType () Returns a new object of class 'Attributed URI Type '. DocumentRoot createDocumentRoot () Returns a new object of class 'Document Root '. EndpointReferenceType createEndpointReferenceType () Returns a new object of class 'Endpoint Reference Type '. MetadataType createMetadataType () Returns a new object of class 'Metadata Type '. ProblemActionType createProblemActionType () Returns a new object of class 'Problem Action Type '. ReferenceParametersType createReferenceParametersType () Returns a new object of class 'Reference Parameters Type '. RelatesToType createRelatesToType () Returns a new object of class 'Relates To Type '. WSAddr10Package getWSAddr10Package () Returns the package supported by this factory.

### Method Summary

| Modifier and Type          | Method and Description                                                                            |
|----------------------------|---------------------------------------------------------------------------------------------------|
| AttributedQNameType        | createAttributedQNameType() Returns a new object of class 'Attributed QName Type'.                |
| AttributedUnsignedLongType | createAttributedUnsignedLongType() Returns a new object of class 'Attributed Unsigned Long Type'. |
| AttributedURIType          | createAttributedURIType() Returns a new object of class 'Attributed URI Type'.                    |
| DocumentRoot               | createDocumentRoot() Returns a new object of class 'Document Root'.                               |
| EndpointReferenceType      | createEndpointReferenceType() Returns a new object of class 'Endpoint Reference Type'.            |
| MetadataType               | createMetadataType() Returns a new object of class 'Metadata Type'.                               |
| ProblemActionType          | createProblemActionType() Returns a new object of class 'Problem Action Type'.                    |
| ReferenceParametersType    | createReferenceParametersType() Returns a new object of class 'Reference Parameters Type'.        |
| RelatesToType              | createRelatesToType() Returns a new object of class 'Relates To Type'.                            |
| WSAddr10Package            | getWSAddr10Package() Returns the package supported by this factory.                               |

- Methods inherited from interface org.eclipse.emf.ecore.EFactory
convertToString, create, createFromString, getEPackage, setEPackage

- Methods inherited from interface org.eclipse.emf.ecore.EModelElement
getEAnnotation, getEAnnotations

- Methods inherited from interface org.eclipse.emf.ecore.EObject
eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eIsProxy, eIsSet, eResource, eSet, eUnset

- Methods inherited from interface org.eclipse.emf.common.notify.Notifier
eAdapters, eDeliver, eNotify, eSetDeliver