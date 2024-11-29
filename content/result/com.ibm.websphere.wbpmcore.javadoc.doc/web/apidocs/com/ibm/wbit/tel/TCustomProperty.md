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

## Interface TCustomProperty

- All Superinterfaces:
org.eclipse.emf.ecore.EObject, org.eclipse.emf.common.notify.Notifier

public interface TCustomProperty
extends org.eclipse.emf.ecore.EObject

 A representation of the model object 'TCustom Property'.
 

 
         User-definable property, name/value pair.
Since:
6.0.1
See Also:TaskPackage.getTCustomProperty()

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description com.ibm.wbit.tel.TInlineCustomPropertyEnum getInline () Returns the value of the 'Inline ' attribute. java.lang.String getName () Returns the value of the 'Name ' attribute java.lang.String getValue () Returns the value of the 'Value ' attribute boolean isSetInline () Returns whether the value of the 'Inline ' attribute is set void setInline (com.ibm.wbit.tel.TInlineCustomPropertyEnum value) Sets the value of the 'Inline ' attribute void setName (java.lang.String value) Sets the value of the 'Name ' attribute void setValue (java.lang.String value) Sets the value of the 'Value ' attribute void unsetInline () Unsets the value of the 'Inline ' attribute

### Method Summary

| Modifier and Type                          | Method and Description                                                                               |
|--------------------------------------------|------------------------------------------------------------------------------------------------------|
| com.ibm.wbit.tel.TInlineCustomPropertyEnum | getInline() Returns the value of the 'Inline' attribute.                                             |
| java.lang.String                           | getName() Returns the value of the 'Name' attribute                                                  |
| java.lang.String                           | getValue() Returns the value of the 'Value' attribute                                                |
| boolean                                    | isSetInline() Returns whether the value of the 'Inline' attribute is set                             |
| void                                       | setInline(com.ibm.wbit.tel.TInlineCustomPropertyEnum value) Sets the value of the 'Inline' attribute |
| void                                       | setName(java.lang.String value) Sets the value of the 'Name' attribute                               |
| void                                       | setValue(java.lang.String value) Sets the value of the 'Value' attribute                             |
| void                                       | unsetInline() Unsets the value of the 'Inline' attribute                                             |

- Methods inherited from interface org.eclipse.emf.ecore.EObject
eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eIsProxy, eIsSet, eResource, eSet, eUnset

- Methods inherited from interface org.eclipse.emf.common.notify.Notifier
eAdapters, eDeliver, eNotify, eSetDeliver