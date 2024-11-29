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

## Interface BOEquality

- public interface BOEquality
The BOEquality interface represents the client programming model interface
 for the BOEquality service.  The BOEquality service can be used to determine
 if two Business Objects contain equivalent contents.

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

boolean
isEqual(commonj.sdo.DataObject businessObject1,
       commonj.sdo.DataObject businessObject2)
Performs a deep comparison of the contents of the two Business
 Objects.

boolean
isEqualShallow(commonj.sdo.DataObject businessObject1,
              commonj.sdo.DataObject businessObject2)
Performs a shallow comparison of the contents of the two Business
 Objects.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - isEqual
boolean isEqual(commonj.sdo.DataObject businessObject1,
              commonj.sdo.DataObject businessObject2)
Performs a deep comparison of the contents of the two Business
 Objects.

 BOEquality boEquality = (BOEquality) new ServiceManager().locateService("com/ibm/websphere/bo/BOEquality");

 boolean isEqual = boEquality.isEqual(customer1, customer2);

Parameters:businessObject1 - First Business Object to compare for equalitybusinessObject2 - Second Business Object to compare for equality
Returns:true if the two Business Object are equivalent
 and false if they are not
    - isEqualShallow
boolean isEqualShallow(commonj.sdo.DataObject businessObject1,
                     commonj.sdo.DataObject businessObject2)
Performs a shallow comparison of the contents of the two Business
 Objects.

 BOEquality boEquality = (BOEquality) new ServiceManager().locateService("com/ibm/websphere/bo/BOEquality");

 boolean isEqualShallow = boEquality.isEqualShallow(customer1, customer2);

Parameters:businessObject1 - First Business Object to compare for equalitybusinessObject2 - Second Business Object to compare for equality
Returns:true if the two Business Object are equivalent
 and false if they are not