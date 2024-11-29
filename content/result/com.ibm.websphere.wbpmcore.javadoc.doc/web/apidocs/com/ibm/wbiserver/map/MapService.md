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

## Interface MapService

- public interface MapService
The MapService interface represents the client programming model for
 the Map Service.  The MapService provides operations for transforming
 incoming BusinessGraphs/DataObjects to outgoing BusinessGraphs/
 DataObjects.

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

void
simpleTransform(java.lang.String mapTNS,
               java.lang.String mapName,
               commonj.sdo.DataObject inputObject,
               commonj.sdo.DataObject outputObject)
Transforms an input BusinessGraph/DataObject to an output BusinessGraph/DataObject
 using a given map.

void
transform(java.lang.String mapTNS,
         java.lang.String mapName,
         java.util.HashMap inputObjects,
         java.util.HashMap outputObjects,
         com.ibm.wbiserver.relationshipservice.common.ExecutionContext callingContext)
Transforms the input objects to the output objects using the given map.

void
transformSMO(java.lang.String mapTNS,
            java.lang.String mapName,
            java.util.HashMap inputObjects,
            java.util.HashMap outputObjects,
            java.util.HashMap assertedTypes,
            com.ibm.wbiserver.relationshipservice.common.ExecutionContext context)

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - transform
void transform(java.lang.String mapTNS,
             java.lang.String mapName,
             java.util.HashMap inputObjects,
             java.util.HashMap outputObjects,
             com.ibm.wbiserver.relationshipservice.common.ExecutionContext callingContext)
               throws com.ibm.wbiserver.map.exceptions.WBIMapServiceException,
                      com.ibm.wbiserver.map.exceptions.WBIMapNotFoundException,
                      com.ibm.wbiserver.map.exceptions.WBIMapFailureException
Transforms the input objects to the output objects using the given map.
 The inputObjects and outputObjects is a HashMap of BusinessGraph/DataObject
 keyed on a variable name. This variable name is provided by the
 user when creating the map definition 
 example 

 &ltmap:inputBusinessObjectVariable name="source\_SAPCustomerBG" .../>

 &ltmap:outputBusinessObjectVariable name="target\_CustomerBG" .../>

 variable name for the input SAPCustomerBG is source\_SAPCustomer 

 variable name for the output CustomerBG is target\_CustomerBG
 
 For a reverse map, the same variable names should be used for the
 BusinessGraph/DataObject as that for the forward map.
 
 The ExecutionContext is needed only if the map has relationship calls. It
 contains the following

 Context string indicating whether this is a request, response, delivery or failure.
    This context is used for relationship calls.
  HashMap of original input BusinessGraph/DataObject. This original input object
    is used by relationships called from an ASBO to GBO reverse map for Create.
  HashMap of original output BusinessGraph/DataObject. This original output object
    is used by relationships called from an ASBO to GBO reverse map for Delete.
 

Parameters:mapTNS - Targetnamespace of the map, available in the map definition.mapName - Name of the mapinputObjects - HashMap of input objects to be transformed. HashMap contains
 variable name and BusinessGraph/DataObject pairs, keyed on variable name.outputObjects - HashMap of output objects that will be generated. HashMap
 contains variable name and BusinessObject/DataObject pairs, keyed on variable name.
 An empty HashMap can be passed in as a parameter and will be populated with the output
 objects as a result of the method call.callingContext - contains the context string and the original input and output
 BusinessGraph/DataObject.
Throws:
com.ibm.wbiserver.map.exceptions.WBIMapServiceException
com.ibm.wbiserver.map.exceptions.WBIMapNotFoundException
com.ibm.wbiserver.map.exceptions.WBIMapFailureException
    - simpleTransform
void simpleTransform(java.lang.String mapTNS,
                   java.lang.String mapName,
                   commonj.sdo.DataObject inputObject,
                   commonj.sdo.DataObject outputObject)
                     throws com.ibm.wbiserver.map.exceptions.WBIMapServiceException,
                            com.ibm.wbiserver.map.exceptions.WBIMapNotFoundException,
                            com.ibm.wbiserver.map.exceptions.WBIMapFailureException
Transforms an input BusinessGraph/DataObject to an output BusinessGraph/DataObject
 using a given map.
 This method should be used only if the map does not contain any relationship calls.
Parameters:mapTNS - Targetnamespace of the mapmapName - Name of the mapinputObject - The input object to be transformed by the mapoutputObject - The output object that will be created as a
 result of the transformation. The output object has to be created and
 passed into the method and cannot be null.
Throws:
com.ibm.wbiserver.map.exceptions.WBIMapServiceException
com.ibm.wbiserver.map.exceptions.WBIMapNotFoundException
com.ibm.wbiserver.map.exceptions.WBIMapFailureException
    - transformSMO
void transformSMO(java.lang.String mapTNS,
                java.lang.String mapName,
                java.util.HashMap inputObjects,
                java.util.HashMap outputObjects,
                java.util.HashMap assertedTypes,
                com.ibm.wbiserver.relationshipservice.common.ExecutionContext context)
                  throws com.ibm.wbiserver.map.exceptions.WBIMapServiceException,
                         com.ibm.wbiserver.map.exceptions.WBIMapFailureException,
                         com.ibm.wbiserver.map.exceptions.WBIMapNotFoundException
Parameters:mapTNS - mapName - inputObjects - outputObjects - assertedTypes - context - 
Throws:
com.ibm.wbiserver.map.exceptions.WBIMapServiceException
com.ibm.wbiserver.map.exceptions.WBIMapFailureException
com.ibm.wbiserver.map.exceptions.WBIMapNotFoundException