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

## Interface BOCopy

- public interface BOCopy
The BOCopy interface represents the client programming model interface
 for the BOCopy service.  The BOCopy service provides operations for
 copying Business Objects.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary

Methods 

Modifier and Type
Method and Description

commonj.sdo.DataObject
copy(commonj.sdo.DataObject sourceBusinessObject)
Creates a deep copy of the Business Object.

void
copyInto(commonj.sdo.DataObject sourceBusinessObject,
        commonj.sdo.DataObject targetBusinessObject,
        java.lang.String targetPropertyPath)
Deprecated. 
Instead call copy on the source and then set the copy into the destination.

void
copyIntoShallow(commonj.sdo.DataObject sourceBusinessObject,
               commonj.sdo.DataObject targetBusinessObject,
               java.lang.String targetPropertyPath)
Deprecated. 
Instead call copy on the source and then set the copy into the destination.

void
copyPropertyInto(commonj.sdo.DataObject sourceBusinessObject,
                java.lang.String sourcePropertyPath,
                commonj.sdo.DataObject targetBusinessObject,
                java.lang.String targetPropertyPath)
Deprecated. 
Instead get the property on the source and set on the destination.

commonj.sdo.DataObject
copyShallow(commonj.sdo.DataObject sourceBusinessObject)
Creates a shallow copy of the Business Object.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - copy
commonj.sdo.DataObject copy(commonj.sdo.DataObject sourceBusinessObject)
Creates a deep copy of the Business Object.

 BOCopy boCopy = (BOCopy) new ServiceManager().locateService("com/ibm/websphere/bo/BOCopy");

 DataObject copiedCustomer = boCopy.copy(customer);

Parameters:sourceBusinessObject - The Business Object to be copied
Returns:The deep copy of the Business Object
    - copyShallow
commonj.sdo.DataObject copyShallow(commonj.sdo.DataObject sourceBusinessObject)
Creates a shallow copy of the Business Object.

 BOCopy boCopy = (BOCopy) new ServiceManager().locateService("com/ibm/websphere/bo/BOCopy");

 DataObject copiedCustomer = boCopy.copyShallow(customer);

Parameters:sourceBusinessObject - The Business Object to be copied
Returns:The shallow copy of the Business Object
    - copyInto
void copyInto(commonj.sdo.DataObject sourceBusinessObject,
            commonj.sdo.DataObject targetBusinessObject,
            java.lang.String targetPropertyPath)
Deprecated. Instead call copy on the source and then set the copy into the destination.

 Replacement code:
        DataObject copyBO = boCopy.copy(sourceBO);
        targetBO.set(path, copyBO);
 End of replacement code.
 

 Creates a deep copy of the source Business Object into the property
 referenced by the combination of the target Business Object and the
 target property path parameters.

 If the property referenced by the target Business Object and the
 associated target property path has a cardinality of 1 and has a
 value, it will be overwritten by the copy operation.
 
 If the property referenced by the target Business Object and the
 associated target property path has a cardinality of N, the copy
 operation will result in the copied Business Object being added to
 the list.

 The source Business Object cannot be a Business Graph.

 The source Business Object's type must match the type of the property
 referenced by the target Business Object and the associated target
 property path.
 
 For example, if the source Business Object consisted of a Customer
 containing an Address, and the target Business Object consisted of
 a Company containing a Site containing an Address, the following
 represent valid ways to copy the source Business Object's address
 Business Object to the target:

 BOCopy boCopy = (BOCopy) new ServiceManager().locateService("com/ibm/websphere/bo/BOCopy");

 boCopy.copyInto(addressSource, companyTarget, "site/address");

 boCopy.copyInto(addressSource, siteTarget, "address");

Parameters:sourceBusinessObject - The source Business Object to be copiedtargetBusinessObject - The Business Object used in combination
 with the target property path to determine the property the Business
 Object is copied intotargetPropertyPath - The target property path used in combination
 with the target Business Object to determine the property the Business
 Object is copied into
    - copyIntoShallow
void copyIntoShallow(commonj.sdo.DataObject sourceBusinessObject,
                   commonj.sdo.DataObject targetBusinessObject,
                   java.lang.String targetPropertyPath)
Deprecated. Instead call copy on the source and then set the copy into the destination.

 Replacement code:
        DataObject copyBO = boCopy.copyShallow(sourceBO);
        targetBO.set(path, copyBO);
 End of replacement code.
 

 Creates a shallow copy of the source Business Object into the property
 referenced by the combination of the target Business Object and the
 target property path parameters.

 If the property referenced by the target Business Object and the
 target property path has a cardinality of 1 and has a value,
 it will be overwritten by the copy operation.
 
 If the property referenced by the target Business Object and the
 target property path has a cardinality of N, the copy operation
 will result in the copied Business Object being added to the list.

 The source Business Object cannot be a Business Graph.

 The source Business Object's type must match the type of the property
 referenced by the target Business Object and the associated property
 path.
 
 For example, if the source Business Object consisted of a Customer
 containing an Address, and the target Business Object consisted of
 a Company containing a Site containing an Address, the following
 represent valid ways to copy the source Business Object's address
 Business Object to the target:

 BOCopy boCopy = (BOCopy) new ServiceManager().locateService("com/ibm/websphere/bo/BOCopy");

 boCopy.copyIntoShallow(addressSource, companyTarget, "site/address");

 boCopy.copyIntoShallow(addressSource, siteTarget, "address");

Parameters:sourceBusinessObject - The source Business Object to be copiedtargetBusinessObject - The Business Object used in combination with
 the target property path to determine the property the Business Object is
 copied intotargetPropertyPath - The property path used in combination with the
 target Business Object to determine the property the source Business
 Object is copied into
    - copyPropertyInto
void copyPropertyInto(commonj.sdo.DataObject sourceBusinessObject,
                    java.lang.String sourcePropertyPath,
                    commonj.sdo.DataObject targetBusinessObject,
                    java.lang.String targetPropertyPath)
Deprecated. Instead get the property on the source and set on the destination.

 Replacement code:
        Object value = sourceBO.get(sourcePath);
        targetBO.set(targetPath, value); 
 End of replacement code.
 
 You may want to special case check for Date type and make a copy of the Date
 before setting into the destination. Otherwise the same Date object will be
 in both, and changing one will change the other. The same occurs if it is a List,
 and the contents of the List are Date objects.
 
 
 Creates a copy of the simple type property referenced by the source
 Business Object combined with the source property path into the
 property referenced by the target Business Object combined with the
 target property path.

 If the simple type property referenced by the target Business Object
 combined with the target property path has a cardinality of 1 and
 has a value, it will be overwritten by the copy operation.

 If the simple type property referenced by the target Business Object
 combined with the target property path has a cardinality of N, the
 copy operation will result in the copied simple type being added
 to the list.

 The property to be copied must be a simple type, and it must have the
 same type as the property it is being copied into.
 
 For example, if the source Business Object consisted of a Customer
 containing an Address that contained a street property, and the
 target Business Object consisted of a Company containing a Site
 containing an Address that contained a street, the following represent
 valid ways to copy the street property from the source to the target:

 BOCopy boCopy = (BOCopy) new ServiceManager().locateService("com/ibm/websphere/bo/BOCopy");

 boCopy.copyPropertyInto(customer, "address/street", company, "site/address/street");

 boCopy.copyPropertyInto(address, "street", site, "address/street");

 boCopy.copyPropertyInto(addressSource, "street", addressTarget, "street");

Parameters:sourceBusinessObject - The source Business Object used in
 combination with the source property path to determine the source
 property to be copiedsourcePropertyPath - The source property path when combined with
 the source Business Object determines the source property to be copiedtargetBusinessObject - The target Business Object used in
 combination with the target property path to determine the target
 property to be copied intotargetProperty - The target property path used in combination
 with the target Business Object to determine the property to be
 copied into