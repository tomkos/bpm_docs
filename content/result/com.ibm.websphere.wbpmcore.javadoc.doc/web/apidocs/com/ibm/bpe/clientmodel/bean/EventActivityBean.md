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

## Class EventActivityBean

- java.lang.Object
    - com.ibm.bpe.clientmodel.bean.EventActivityBean

- public class EventActivityBean extends java.lang.Object Accesses the properties of a BPEL event and adds metadata for national language support and converters. A BPEL event handler is a special activity that can receive events (with a message). An EventActivityBean object can be instantiated from an ActivityServiceTemplateData object, an EventHandlerTemplateData object, or a QueryResultSet object. If the bean was instantiated from an original object returned by the Business Process Choreographer API, all properties are loaded. If, however, the bean is instantiated from a query, only the following properties are loaded from the query result set: If the property was not found in the query result set, the property will remain empty. Accessing an empty property requires the bean to load the missing information from the server. Use the static method ActivityInstanceBean.getLabel(String, Locale) to retrieve the localized label for a property. Use the static method ActivityInstanceBean.getConverter(String) to retrieve a converter for a property. The return value may be null because converters are optional. See Also: EventHandlerTemplateData , ActivityServiceTemplateData , QueryResultSet

```
public class EventActivityBean
extends java.lang.Object
```

Accesses the properties of a BPEL event and adds metadata for national
 language support and converters. A BPEL event handler is a special activity
 that can receive events (with a message).

An EventActivityBean object can be instantiated from an
 ActivityServiceTemplateData object, an
 EventHandlerTemplateData object, or a QueryResultSet object.
 
 If the bean was instantiated from an original object returned by the Business
 Process Choreographer API, all properties are loaded. If, however, the bean
 is instantiated from a query, only the following properties are loaded from
 the query result set:
 
 
ATID
description
VTID
portTypeName
operation

 If the property was not found in the query result set, the property will
 remain empty. Accessing an empty property requires the bean to load the
 missing information from the server.

Use the static method ActivityInstanceBean.getLabel(String, Locale)
 to retrieve the localized label for a property. Use the static method
 ActivityInstanceBean.getConverter(String) to retrieve a converter for
 a property. The return value may be null because converters are optional.

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
ACTIVITY\_DESCRIPTION\_PROPERTY
Use the property name to determine labels and converters for the
 description property.

static java.lang.String
ACTIVITY\_EVENTHANDLER\_PROPERTY
Use the property name to determine labels and converters for the
 eventHandler property.

static java.lang.String
ACTIVITY\_OPERATIONNAME\_PROPERTY
Use the property name to determine labels and converters for the
 operation property.

static java.lang.String
ACTIVITY\_PORTTYPENAME\_PROPERTY
Use the property name to determine labels and converters for the
 portTypeName property.

static java.lang.String
ACTIVITY\_PORTTYPENAMESPACE\_PROPERTY
Use the property name to determine labels and converters for the
 portTypeNameSpace property.

static java.lang.String
COPYRIGHT 

static java.lang.String
PROCESSINSTANCE\_ID\_PROPERTY
Use the property name to determine labels and converters for the
 PIID property.

static java.lang.String
PROCESSINSTANCE\_INPUTMESSAGE\_PROPERTY
Use the property name to determine labels and converters for the
 inputMessageTypeName property.

static java.lang.String
PROCESSTEMPLATE\_ID\_PROPERTY
Use the property name to determine labels and converters for the
 processTemplateId property.

static java.lang.String
PROCESSTEMPLATE\_NAME\_PROPERTY
Use the property name to determine labels and converters for the
 processTemplateName property.
    - Constructor Summary

Constructors 

Constructor and Description

EventActivityBean(ActivityServiceTemplateData ast,
                 BFMConnection bfmConnection,
                 PIID piid)
Constructs a new EventyActivityBean from an original
 ActivityServiceTemplateData object.

EventActivityBean(EventHandlerTemplateData origin,
                 BFMConnection bfmConnection)
Constructs a new EventyActivityBean from an
 EventHandlerTemplateData object.

EventActivityBean(EventHandlerTemplateData origin,
                 BFMConnection bfmConnection,
                 PIID piid)
Constructs a new EventyActivityBean from an
 EventHandlerTemplateData object.

EventActivityBean(QueryResultSet resultSet)
Constructs a new EventActivityBean from a
 QueryResultSet.
    - Method Summary Methods Modifier and Type Method and Description ATID getATID () Returns the ATID . static SimpleConverter getConverter (java.lang.String propertyName) Returns the default converter for a given property. java.lang.String getDescription () Returns the description . EHTID getEHTID () Returns the EHTID . java.lang.String getID () Returns the ID . java.lang.String getInputMessageTypeName () Returns the inputMessageTypeName property. MessageWrapper getInputMessageWrapper () Retrieves the input message. static java.lang.String getLabel (java.lang.String propertyName) Returns the resource bundle key for a property. static java.lang.String getLabel (java.lang.String propertyName, java.util.Locale locale) Returns the label for a property from the resource bundle. java.lang.String getOperation () Returns the operation property. PIID getPIID () Returns the PIID property. java.lang.String getPortTypeName () Returns the portTypeName property. java.lang.String getPortTypeNameSpace () Returns the portTypeNameSpace property. PTID getProcessTemplateId () Returns the processTemplateId property. java.lang.String getProcessTemplateName () Returns the processTemplateName property. VTID getVTID () Returns the VTID property. boolean isEventHandler () Returns the eventHandler property. static boolean isValid (java.lang.String propertyName) Checks whether the property is valid.

### Method Summary

| Modifier and Type       | Method and Description                                                                                                              |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| ATID                    | getATID() Returns the ATID.                                                                                                         |
| static SimpleConverter  | getConverter(java.lang.String propertyName) Returns the default converter for a given property.                                     |
| java.lang.String        | getDescription() Returns the description.                                                                                           |
| EHTID                   | getEHTID() Returns the EHTID.                                                                                                       |
| java.lang.String        | getID() Returns the ID.                                                                                                             |
| java.lang.String        | getInputMessageTypeName() Returns the inputMessageTypeName property.                                                                |
| MessageWrapper          | getInputMessageWrapper() Retrieves the input message.                                                                               |
| static java.lang.String | getLabel(java.lang.String propertyName) Returns the resource bundle key for a property.                                             |
| static java.lang.String | getLabel(java.lang.String propertyName,         java.util.Locale locale) Returns the label for a property from the resource bundle. |
| java.lang.String        | getOperation() Returns the operation property.                                                                                      |
| PIID                    | getPIID() Returns the PIID property.                                                                                                |
| java.lang.String        | getPortTypeName() Returns the portTypeName property.                                                                                |
| java.lang.String        | getPortTypeNameSpace() Returns the portTypeNameSpace property.                                                                      |
| PTID                    | getProcessTemplateId() Returns the processTemplateId property.                                                                      |
| java.lang.String        | getProcessTemplateName() Returns the processTemplateName property.                                                                  |
| VTID                    | getVTID() Returns the VTID property.                                                                                                |
| boolean                 | isEventHandler() Returns the eventHandler property.                                                                                 |
| static boolean          | isValid(java.lang.String propertyName) Checks whether the property is valid.                                                        |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait