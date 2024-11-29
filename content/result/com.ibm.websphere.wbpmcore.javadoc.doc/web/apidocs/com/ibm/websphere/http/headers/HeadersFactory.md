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

## Interface HeadersFactory

- All Superinterfaces:
org.eclipse.emf.ecore.EFactory, org.eclipse.emf.ecore.EModelElement, org.eclipse.emf.ecore.EObject, org.eclipse.emf.common.notify.Notifier

public interface HeadersFactory
extends org.eclipse.emf.ecore.EFactory

 The Factory for the model.
 It provides a create method for each non-abstract class of the model.
 
See Also:HeadersPackage

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static HeadersFactory
eINSTANCE 

static HeadersFactory
INSTANCE
The singleton instance of the factory
    - Method Summary Methods Modifier and Type Method and Description com.ibm.websphere.http.headers.DocumentRoot createDocumentRoot () Returns a new object of class 'Document Root ' HTTPAuthentication createHTTPAuthentication () Returns a new object of class 'HTTP Authentication ' HTTPControl createHTTPControl () Returns a new object of class 'HTTP Control ' HTTPCredentials createHTTPCredentials () Returns a new object of class 'HTTP Credentials ' HTTPHeader createHTTPHeader () Returns a new object of class 'HTTP Header ' HTTPHeaders createHTTPHeaders () Returns a new object of class 'HTTP Headers ' com.ibm.websphere.http.headers.HTTPMessageParameters createHTTPMessageParameters () Returns a new object of class 'HTTP Message Parameters ' HTTPProxySettings createHTTPProxySettings () Returns a new object of class 'HTTP Proxy Settings ' HTTPSSLSettings createHTTPSSLSettings () Returns a new object of class 'HTTPSSL Settings ' com.ibm.websphere.http.headers.HeadersPackage getHeadersPackage () Returns the package supported by this factory

### Method Summary

| Modifier and Type                                    | Method and Description                                                                |
|------------------------------------------------------|---------------------------------------------------------------------------------------|
| com.ibm.websphere.http.headers.DocumentRoot          | createDocumentRoot() Returns a new object of class 'Document Root'                    |
| HTTPAuthentication                                   | createHTTPAuthentication() Returns a new object of class 'HTTP Authentication'        |
| HTTPControl                                          | createHTTPControl() Returns a new object of class 'HTTP Control'                      |
| HTTPCredentials                                      | createHTTPCredentials() Returns a new object of class 'HTTP Credentials'              |
| HTTPHeader                                           | createHTTPHeader() Returns a new object of class 'HTTP Header'                        |
| HTTPHeaders                                          | createHTTPHeaders() Returns a new object of class 'HTTP Headers'                      |
| com.ibm.websphere.http.headers.HTTPMessageParameters | createHTTPMessageParameters() Returns a new object of class 'HTTP Message Parameters' |
| HTTPProxySettings                                    | createHTTPProxySettings() Returns a new object of class 'HTTP Proxy Settings'         |
| HTTPSSLSettings                                      | createHTTPSSLSettings() Returns a new object of class 'HTTPSSL Settings'              |
| com.ibm.websphere.http.headers.HeadersPackage        | getHeadersPackage() Returns the package supported by this factory                     |

- Methods inherited from interface org.eclipse.emf.ecore.EFactory
convertToString, create, createFromString, getEPackage, setEPackage

- Methods inherited from interface org.eclipse.emf.ecore.EModelElement
getEAnnotation, getEAnnotations

- Methods inherited from interface org.eclipse.emf.ecore.EObject
eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eIsProxy, eIsSet, eResource, eSet, eUnset

- Methods inherited from interface org.eclipse.emf.common.notify.Notifier
eAdapters, eDeliver, eNotify, eSetDeliver