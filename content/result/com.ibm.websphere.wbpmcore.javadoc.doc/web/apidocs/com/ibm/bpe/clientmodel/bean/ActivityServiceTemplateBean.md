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

## Class ActivityServiceTemplateBean

- java.lang.Object
    - com.ibm.bpe.clientmodel.bean.ActivityServiceTemplateBean

- All Implemented Interfaces:
ActivityServiceTemplateData, java.io.Serializable

public class ActivityServiceTemplateBean
extends java.lang.Object
implements ActivityServiceTemplateData
Accesses the properties of the original ActivityServiceTemplateData object
 and adds metadata for national language support and converters.
 An ActivityServiceTemplateBean object can be instantiated from an ActivityServiceTemplateData object. 

 Use the static method getLabel(String, Locale) to
 retrieve the localized label for a property.
 Use the static method getConverter(String) to
 retrieve a converter for a property. As converters
 are optional, the return value might be null.
 
See Also:ActivityServiceTemplateData, 
Serialized Form

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
ACTIVITYDESCRIPTION\_PROPERTY
Use the property name to determine labels and converters for the "activity description" property.

static java.lang.String
ACTIVITYDISPLAYNAME\_PROPERTY
Use the property name to determine labels and converters for the "activity display name" property.

static java.lang.String
ACTIVITYNAME\_PROPERTY
Use the property name to determine labels and converters for the "activity name" property.

static java.lang.String
AVAILABLEACTIONS\_PROPERTY
Use the property name to determine labels and converters for the "available actions" property.

static java.lang.String
COPYRIGHT
(C) Copyright IBM Corporation 2004, 2008.

static java.lang.String
INPUTMESSAGETYPENAME\_PROPERTY
Use the property name to determine labels and converters for the "input message type name" property.

static java.lang.String
INPUTMESSAGETYPETYPESYSTEMNAME\_PROPERTY
Deprecated.  

static java.lang.String
OPERATIONNAME\_PROPERTY
Use the property name to determine labels and converters for the "operation name" property.

static java.lang.String
PARTNERLINKNAME\_PROPERTY
Use the property name to determine labels and converters for the "partner link name" property.

static java.lang.String
PORTTYPENAME\_PROPERTY
Use the property name to determine labels and converters for the "port type" property.

static java.lang.String
PORTTYPENAMESPACE\_PROPERTY
Use the property name to determine labels and converters for the "port type namespace" property.

static java.lang.String
PROCESSTEMPLATEID\_PROPERTY
Use the property name to determine labels and converters for the "process template ID" property.

static java.lang.String
SERVICETEMPLATEID\_PROPERTY
Use the property name to determine labels and converters for the "service template ID" property.
    - Constructor Summary

Constructors 

Constructor and Description

ActivityServiceTemplateBean(ActivityServiceTemplateData activityTemplate,
                           BFMConnection bfmConnection)
Constructs a new ActivityServiceTemplateBean from an original
 ActivityServiceTemplateData object.
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getActivityDescription () Returns the activityDescription property. java.lang.String getActivityDisplayName () Returns the activityDisplayName property. java.lang.String getActivityName () Returns the activityName property. ATID getActivityTemplateID () Returns the activityTemplateID property. int[] getAvailableActions () Returns the availableActions property. static SimpleConverter getConverter (java.lang.String propertyName) Returns the default converter for a given property. OID getID () Returns the ID property. java.lang.String getInputMessageTypeName () Returns the inputMessageTypeName property. java.lang.String getInputMessageTypeTypeSystemName () Deprecated. MessageWrapper getInputMessageWrapper () Retrieves the input message. static java.lang.String getLabel (java.lang.String propertyName) Returns the resource bundle key for a property. static java.lang.String getLabel (java.lang.String propertyName, java.util.Locale locale) Returns the label of a property from the resource bundle. java.lang.String getOperationName () Returns the operationName property. java.lang.String getPartnerLinkName () Returns the partnerLinkName property. java.lang.String getPortTypeName () Returns the portTypeName property. java.lang.String getPortTypeNamespace () Returns the portTypeNamespace property. ProcessTemplateBean getProcessTemplate () Returns a ProcessTemplateBean object for the associated ProcessTemplateData object. PTID getProcessTemplateID () Returns the processTemplateID property. java.lang.String getProcessTemplateName () Returns the processTemplateName property. VTID getServiceTemplateID () Returns the serviceTemplateID property. TKTID getTaskTemplateID () Returns the taskTemplateID property. boolean isTwoWayOperation () Returns the twoWayOperation property. static boolean isValid (java.lang.String propertyName) Checks that the property is valid.

### Method Summary

| Modifier and Type       | Method and Description                                                                                                             |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| java.lang.String        | getActivityDescription() Returns the activityDescription property.                                                                 |
| java.lang.String        | getActivityDisplayName() Returns the activityDisplayName property.                                                                 |
| java.lang.String        | getActivityName() Returns the activityName property.                                                                               |
| ATID                    | getActivityTemplateID() Returns the activityTemplateID property.                                                                   |
| int[]                   | getAvailableActions() Returns the availableActions property.                                                                       |
| static SimpleConverter  | getConverter(java.lang.String propertyName) Returns the default converter for a given property.                                    |
| OID                     | getID() Returns the ID property.                                                                                                   |
| java.lang.String        | getInputMessageTypeName() Returns the inputMessageTypeName property.                                                               |
| java.lang.String        | getInputMessageTypeTypeSystemName() Deprecated.                                                                                    |
| MessageWrapper          | getInputMessageWrapper() Retrieves the input message.                                                                              |
| static java.lang.String | getLabel(java.lang.String propertyName) Returns the resource bundle key for a property.                                            |
| static java.lang.String | getLabel(java.lang.String propertyName,         java.util.Locale locale) Returns the label of a property from the resource bundle. |
| java.lang.String        | getOperationName() Returns the operationName property.                                                                             |
| java.lang.String        | getPartnerLinkName() Returns the partnerLinkName property.                                                                         |
| java.lang.String        | getPortTypeName() Returns the portTypeName property.                                                                               |
| java.lang.String        | getPortTypeNamespace() Returns the portTypeNamespace property.                                                                     |
| ProcessTemplateBean     | getProcessTemplate() Returns a ProcessTemplateBean object for the associated ProcessTemplateData object.                           |
| PTID                    | getProcessTemplateID() Returns the processTemplateID property.                                                                     |
| java.lang.String        | getProcessTemplateName() Returns the processTemplateName property.                                                                 |
| VTID                    | getServiceTemplateID() Returns the serviceTemplateID property.                                                                     |
| TKTID                   | getTaskTemplateID() Returns the taskTemplateID property.                                                                           |
| boolean                 | isTwoWayOperation() Returns the twoWayOperation property.                                                                          |
| static boolean          | isValid(java.lang.String propertyName) Checks that the property is valid.                                                          |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait