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

## Interface TJSP

- All Superinterfaces:
org.eclipse.emf.ecore.EObject, org.eclipse.emf.common.notify.Notifier

public interface TJSP
extends org.eclipse.emf.ecore.EObject

 A representation of the model object 'TJSP'.
 

 
         If the attribute 'for' has the value 'fault', 
         the attribute 'faultQName' becomes mandatory.
         For all other values of the attribute 'for',
         the attribute 'faultQName' will be ignored.
Since:
6.0.1
See Also:TaskPackage.getTJSP()

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description org.eclipse.emf.common.util.EList getApplyTo () Returns the value of the 'Apply To ' containment reference list. java.lang.String getContextRoot () Returns the value of the 'Context Root ' attribute javax.xml.namespace.QName getFaultQName () Returns the value of the 'Fault QName ' attribute TJspUsagePattern getFor () Returns the value of the 'For ' attribute. org.eclipse.emf.common.util.URI getUri () Returns the value of the 'Uri ' attribute boolean isSetFor () Returns whether the value of the 'For ' attribute is set void setContextRoot (java.lang.String value) Sets the value of the 'Context Root ' attribute void setFaultQName (javax.xml.namespace.QName value) Sets the value of the 'Fault QName ' attribute void setFor (TJspUsagePattern value) Sets the value of the 'For ' attribute void setUri (org.eclipse.emf.common.util.URI value) Sets the value of the 'Uri ' attribute void unsetFor () Unsets the value of the 'For ' attribute

### Method Summary

| Modifier and Type                 | Method and Description                                                                       |
|-----------------------------------|----------------------------------------------------------------------------------------------|
| org.eclipse.emf.common.util.EList | getApplyTo() Returns the value of the 'Apply To' containment reference list.                 |
| java.lang.String                  | getContextRoot() Returns the value of the 'Context Root' attribute                           |
| javax.xml.namespace.QName         | getFaultQName() Returns the value of the 'Fault QName' attribute                             |
| TJspUsagePattern                  | getFor() Returns the value of the 'For' attribute.                                           |
| org.eclipse.emf.common.util.URI   | getUri() Returns the value of the 'Uri' attribute                                            |
| boolean                           | isSetFor() Returns whether the value of the 'For' attribute is set                           |
| void                              | setContextRoot(java.lang.String value) Sets the value of the 'Context Root' attribute        |
| void                              | setFaultQName(javax.xml.namespace.QName value) Sets the value of the 'Fault QName' attribute |
| void                              | setFor(TJspUsagePattern value) Sets the value of the 'For' attribute                         |
| void                              | setUri(org.eclipse.emf.common.util.URI value) Sets the value of the 'Uri' attribute          |
| void                              | unsetFor() Unsets the value of the 'For' attribute                                           |

- Methods inherited from interface org.eclipse.emf.ecore.EObject
eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eIsProxy, eIsSet, eResource, eSet, eUnset

- Methods inherited from interface org.eclipse.emf.common.notify.Notifier
eAdapters, eDeliver, eNotify, eSetDeliver