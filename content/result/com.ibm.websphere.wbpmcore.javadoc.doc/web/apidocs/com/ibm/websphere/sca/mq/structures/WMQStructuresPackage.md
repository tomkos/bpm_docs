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

## Interface WMQStructuresPackage

- All Superinterfaces: org.eclipse.emf.ecore.EModelElement, org.eclipse.emf.ecore.ENamedElement, org.eclipse.emf.ecore.EObject, org.eclipse.emf.ecore.EPackage, org.eclipse.emf.common.notify.Notifier public interface WMQStructuresPackage extends org.eclipse.emf.ecore.EPackage begin-user-doc The Package for the model. It contains accessors for the meta objects to represent end-user-doc See Also: WMQStructuresFactory

```
public interface WMQStructuresPackage
extends org.eclipse.emf.ecore.EPackage
```

    - each class,
    - each feature of each class,
    - each enum,
    - and each data type

- ======== NESTED CLASS SUMMARY ======== =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Nested Class Summary Nested Classes Modifier and Type Interface and Description static interface WMQStructuresPackage.Literals Defines literals for the meta objects that represent each class, each feature of each class, each enum, and each data type </div

### Nested Class Summary

| Modifier and Type   | Interface and Description                                                                                                                                              |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static interface    | WMQStructuresPackage.Literals Defines literals for the meta objects that represent      each class,    each feature of each class,    each enum,    and each data type |

- Nested classes/interfaces inherited from interface org.eclipse.emf.ecore.EPackage
org.eclipse.emf.ecore.EPackage.Descriptor, org.eclipse.emf.ecore.EPackage.Registry

- Field Summary

Fields 

Modifier and Type
Field and Description

static int
DOCUMENT\_ROOT
The meta object id for the 'Document Root' class

static int
DOCUMENT\_ROOT\_\_MIXED
The feature id for the 'Mixed' attribute list

static int
DOCUMENT\_ROOT\_\_MQ\_CONTROL
The feature id for the 'Mq Control' containment reference

static int
DOCUMENT\_ROOT\_\_MQ\_HEADERS
The feature id for the 'Mq Headers' containment reference

static int
DOCUMENT\_ROOT\_\_MQMD
The feature id for the 'Mqmd' containment reference

static int
DOCUMENT\_ROOT\_\_XMLNS\_PREFIX\_MAP
The feature id for the 'XMLNS Prefix Map' map

static int
DOCUMENT\_ROOT\_\_XSI\_SCHEMA\_LOCATION
The feature id for the 'XSI Schema Location' map

static int
DOCUMENT\_ROOT\_FEATURE\_COUNT
The number of structural features of the 'Document Root' class

static WMQStructuresPackage
eINSTANCE 

static java.lang.String
eNAME
The package name

static java.lang.String
eNS\_PREFIX
The package namespace name

static java.lang.String
eNS\_URI
The package namespace URI

static WMQStructuresPackage
INSTANCE
The singleton instance of the package

static int
MQ\_CONTROL
The meta object id for the 'MQ Control' class

static int
MQ\_CONTROL\_\_CODED\_CHAR\_SET\_ID
The feature id for the 'Coded Char Set Id' attribute

static int
MQ\_CONTROL\_\_ENCODING
The feature id for the 'Encoding' attribute

static int
MQ\_CONTROL\_\_FORMAT
The feature id for the 'Format' attribute

static int
MQ\_CONTROL\_FEATURE\_COUNT
The number of structural features of the 'MQ Control' class

static int
MQ\_HEADER
The meta object id for the 'MQ Header' class

static int
MQ\_HEADER\_\_CODED\_CHAR\_SET\_ID
The feature id for the 'Coded Char Set Id' attribute

static int
MQ\_HEADER\_\_ENCODING
The feature id for the 'Encoding' attribute

static int
MQ\_HEADER\_\_FORMAT
The feature id for the 'Format' attribute

static int
MQ\_HEADER\_\_VALUE
The feature id for the 'Value' containment reference

static int
MQ\_HEADER\_FEATURE\_COUNT
The number of structural features of the 'MQ Header' class

static int
MQ\_HEADERS
The meta object id for the 'MQ Headers' class

static int
MQ\_HEADERS\_\_HEADER
The feature id for the 'Header' containment reference list

static int
MQ\_HEADERS\_FEATURE\_COUNT
The number of structural features of the 'MQ Headers' class

static int
MQ\_OPAQUE\_HEADER
The meta object id for the 'MQ Opaque Header' class

static int
MQ\_OPAQUE\_HEADER\_\_DATA
The feature id for the 'Data' attribute

static int
MQ\_OPAQUE\_HEADER\_\_FLAGS
The feature id for the 'Flags' attribute

static int
MQ\_OPAQUE\_HEADER\_\_STRUC\_ID
The feature id for the 'Struc Id' attribute

static int
MQ\_OPAQUE\_HEADER\_\_VERSION
The feature id for the 'Version' attribute

static int
MQ\_OPAQUE\_HEADER\_FEATURE\_COUNT
The number of structural features of the 'MQ Opaque Header' class

static int
MQBYTE
The meta object id for the 'MQBYTE' data type

static int
MQBYTE16
The meta object id for the 'MQBYTE16' data type

static int
MQBYTE24
The meta object id for the 'MQBYTE24' data type

static int
MQBYTE32
The meta object id for the 'MQBYTE32' data type

static int
MQBYTE8
The meta object id for the 'MQBYTE8' data type

static int
MQCHAR
The meta object id for the 'MQCHAR' data type

static int
MQCHAR12
The meta object id for the 'MQCHAR12' data type

static int
MQCHAR128
The meta object id for the 'MQCHAR128' data type

static int
MQCHAR16
The meta object id for the 'MQCHAR16' data type

static int
MQCHAR20
The meta object id for the 'MQCHAR20' data type

static int
MQCHAR24
The meta object id for the 'MQCHAR24' data type

static int
MQCHAR256
The meta object id for the 'MQCHAR256' data type

static int
MQCHAR28
The meta object id for the 'MQCHAR28' data type

static int
MQCHAR32
The meta object id for the 'MQCHAR32' data type

static int
MQCHAR4
The meta object id for the 'MQCHAR4' data type

static int
MQCHAR48
The meta object id for the 'MQCHAR48' data type

static int
MQCHAR64
The meta object id for the 'MQCHAR64' data type

static int
MQCHAR8
The meta object id for the 'MQCHAR8' data type

static int
MQCIH
The meta object id for the 'MQCIH' class

static int
MQCIH\_\_ABEND\_CODE
The feature id for the 'Abend Code' attribute

static int
MQCIH\_\_ADS\_DESCRIPTOR
The feature id for the 'ADS Descriptor' attribute

static int
MQCIH\_\_ATTENTION\_ID
The feature id for the 'Attention Id' attribute

static int
MQCIH\_\_AUTHENTICATOR
The feature id for the 'Authenticator' attribute

static int
MQCIH\_\_CANCEL\_CODE
The feature id for the 'Cancel Code' attribute

static int
MQCIH\_\_COMP\_CODE
The feature id for the 'Comp Code' attribute

static int
MQCIH\_\_CONVERSATIONAL\_TASK
The feature id for the 'Conversational Task' attribute

static int
MQCIH\_\_CURSOR\_POSITION
The feature id for the 'Cursor Position' attribute

static int
MQCIH\_\_ERROR\_OFFSET
The feature id for the 'Error Offset' attribute

static int
MQCIH\_\_FACILITY
The feature id for the 'Facility' attribute

static int
MQCIH\_\_FACILITY\_KEEP\_TIME
The feature id for the 'Facility Keep Time' attribute

static int
MQCIH\_\_FACILITY\_LIKE
The feature id for the 'Facility Like' attribute

static int
MQCIH\_\_FLAGS
The feature id for the 'Flags' attribute

static int
MQCIH\_\_FUNCTION
The feature id for the 'Function' attribute

static int
MQCIH\_\_GET\_WAIT\_INTERVAL
The feature id for the 'Get Wait Interval' attribute

static int
MQCIH\_\_INPUT\_ITEM
The feature id for the 'Input Item' attribute

static int
MQCIH\_\_LINK\_TYPE
The feature id for the 'Link Type' attribute

static int
MQCIH\_\_NEXT\_TRANSACTION\_ID
The feature id for the 'Next Transaction Id' attribute

static int
MQCIH\_\_OUTPUT\_DATA\_LENGTH
The feature id for the 'Output Data Length' attribute

static int
MQCIH\_\_PROGRAM\_NAME
The feature id for the 'Program Name' attribute

static int
MQCIH\_\_REASON
The feature id for the 'Reason' attribute

static int
MQCIH\_\_REMOTE\_SYS\_ID
The feature id for the 'Remote Sys Id' attribute

static int
MQCIH\_\_REMOTE\_TRANS\_ID
The feature id for the 'Remote Trans Id' attribute

static int
MQCIH\_\_REPLY\_TO\_FORMAT
The feature id for the 'Reply To Format' attribute

static int
MQCIH\_\_RESERVED1
The feature id for the 'Reserved1' attribute

static int
MQCIH\_\_RESERVED2
The feature id for the 'Reserved2' attribute

static int
MQCIH\_\_RESERVED3
The feature id for the 'Reserved3' attribute

static int
MQCIH\_\_RESERVED4
The feature id for the 'Reserved4' attribute

static int
MQCIH\_\_RETURN\_CODE
The feature id for the 'Return Code' attribute

static int
MQCIH\_\_START\_CODE
The feature id for the 'Start Code' attribute

static int
MQCIH\_\_TASK\_END\_STATUS
The feature id for the 'Task End Status' attribute

static int
MQCIH\_\_TRANSACTION\_ID
The feature id for the 'Transaction Id' attribute

static int
MQCIH\_\_UOW\_CONTROL
The feature id for the 'UOW Control' attribute

static int
MQCIH\_\_VERSION
The feature id for the 'Version' attribute

static int
MQCIH\_FEATURE\_COUNT
The number of structural features of the 'MQCIH' class

static int
MQIIH
The meta object id for the 'MQIIH' class

static int
MQIIH\_\_AUTHENTICATOR
The feature id for the 'Authenticator' attribute

static int
MQIIH\_\_COMMIT\_MODE
The feature id for the 'Commit Mode' attribute

static int
MQIIH\_\_FLAGS
The feature id for the 'Flags' attribute

static int
MQIIH\_\_LTERM\_OVERRIDE
The feature id for the 'LTerm Override' attribute

static int
MQIIH\_\_MFS\_MAP\_NAME
The feature id for the 'MFS Map Name' attribute

static int
MQIIH\_\_REPLY\_TO\_FORMAT
The feature id for the 'Reply To Format' attribute

static int
MQIIH\_\_RESERVED
The feature id for the 'Reserved' attribute

static int
MQIIH\_\_SECURITY\_SCOPE
The feature id for the 'Security Scope' attribute

static int
MQIIH\_\_TRAN\_INSTANCE\_ID
The feature id for the 'Tran Instance Id' attribute

static int
MQIIH\_\_TRAN\_STATE
The feature id for the 'Tran State' attribute

static int
MQIIH\_\_VERSION
The feature id for the 'Version' attribute

static int
MQIIH\_FEATURE\_COUNT
The number of structural features of the 'MQIIH' class

static int
MQINT32
The meta object id for the 'MQINT32' data type

static int
MQINT32\_OBJECT
The meta object id for the 'MQINT32 Object' data type

static int
MQINT64
The meta object id for the 'MQINT64' data type

static int
MQINT64\_OBJECT
The meta object id for the 'MQINT64 Object' data type

static int
MQLONG
The meta object id for the 'MQLONG' data type

static int
MQLONG\_OBJECT
The meta object id for the 'MQLONG Object' data type

static int
MQMD
The meta object id for the 'MQMD' class

static int
MQMD\_\_ACCOUNTING\_TOKEN
The feature id for the 'Accounting Token' attribute

static int
MQMD\_\_APPL\_IDENTITY\_DATA
The feature id for the 'Appl Identity Data' attribute

static int
MQMD\_\_APPL\_ORIGIN\_DATA
The feature id for the 'Appl Origin Data' attribute

static int
MQMD\_\_BACKOUT\_COUNT
The feature id for the 'Backout Count' attribute

static int
MQMD\_\_CORREL\_ID
The feature id for the 'Correl Id' attribute

static int
MQMD\_\_EXPIRY
The feature id for the 'Expiry' attribute

static int
MQMD\_\_FEEDBACK
The feature id for the 'Feedback' attribute

static int
MQMD\_\_GROUP\_ID
The feature id for the 'Group Id' attribute

static int
MQMD\_\_MSG\_FLAGS
The feature id for the 'Msg Flags' attribute

static int
MQMD\_\_MSG\_ID
The feature id for the 'Msg Id' attribute

static int
MQMD\_\_MSG\_SEQ\_NUMBER
The feature id for the 'Msg Seq Number' attribute

static int
MQMD\_\_MSG\_TYPE
The feature id for the 'Msg Type' attribute

static int
MQMD\_\_OFFSET
The feature id for the 'Offset' attribute

static int
MQMD\_\_ORIGINAL\_LENGTH
The feature id for the 'Original Length' attribute

static int
MQMD\_\_PERSISTENCE
The feature id for the 'Persistence' attribute

static int
MQMD\_\_PRIORITY
The feature id for the 'Priority' attribute

static int
MQMD\_\_PUT\_APPL\_NAME
The feature id for the 'Put Appl Name' attribute

static int
MQMD\_\_PUT\_APPL\_TYPE
The feature id for the 'Put Appl Type' attribute

static int
MQMD\_\_PUT\_DATE
The feature id for the 'Put Date' attribute

static int
MQMD\_\_PUT\_TIME
The feature id for the 'Put Time' attribute

static int
MQMD\_\_REPLY\_TO\_Q
The feature id for the 'Reply To Q' attribute

static int
MQMD\_\_REPLY\_TO\_QMGR
The feature id for the 'Reply To QMgr' attribute

static int
MQMD\_\_REPORT
The feature id for the 'Report' attribute

static int
MQMD\_\_USER\_IDENTIFIER
The feature id for the 'User Identifier' attribute

static int
MQMD\_FEATURE\_COUNT
The number of structural features of the 'MQMD' class

static int
MQRFH
The meta object id for the 'MQRFH' class

static int
MQRFH\_\_FLAGS
The feature id for the 'Flags' attribute

static int
MQRFH\_\_PROPERTY
The feature id for the 'Property' containment reference list

static int
MQRFH\_FEATURE\_COUNT
The number of structural features of the 'MQRFH' class

static int
MQRFH\_PROPERTY
The meta object id for the 'MQRFH Property' class

static int
MQRFH\_PROPERTY\_\_NAME
The feature id for the 'Name' attribute

static int
MQRFH\_PROPERTY\_\_VALUE
The feature id for the 'Value' attribute

static int
MQRFH\_PROPERTY\_FEATURE\_COUNT
The number of structural features of the 'MQRFH Property' class

static int
MQRFH2
The meta object id for the 'MQRFH2' class

static int
MQRFH2\_\_FLAGS
The feature id for the 'Flags' attribute

static int
MQRFH2\_\_FOLDER
The feature id for the 'Folder' containment reference list

static int
MQRFH2\_\_NAME\_VALUE\_CCSID
The feature id for the 'Name Value CCSID' attribute

static int
MQRFH2\_FEATURE\_COUNT
The number of structural features of the 'MQRFH2' class

static int
MQRFH2\_GROUP
The meta object id for the 'MQRFH2 Group' class

static int
MQRFH2\_GROUP\_\_GROUP
The feature id for the 'Group' containment reference list

static int
MQRFH2\_GROUP\_\_NAME
The feature id for the 'Name' attribute

static int
MQRFH2\_GROUP\_\_PROPERTY
The feature id for the 'Property' containment reference list

static int
MQRFH2\_GROUP\_\_RFH2\_CONTENTS
The feature id for the 'Rfh2 Contents' attribute list

static int
MQRFH2\_GROUP\_FEATURE\_COUNT
The number of structural features of the 'MQRFH2 Group' class

static int
MQRFH2\_PROPERTY
The meta object id for the 'MQRFH2 Property' class

static int
MQRFH2\_PROPERTY\_\_NAME
The feature id for the 'Name' attribute

static int
MQRFH2\_PROPERTY\_\_TYPE
The feature id for the 'Type' attribute

static int
MQRFH2\_PROPERTY\_\_VALUE
The feature id for the 'Value' attribute

static int
MQRFH2\_PROPERTY\_FEATURE\_COUNT
The number of structural features of the 'MQRFH2 Property' class

static int
MQRFH2\_PROPERTY\_TYPE
The meta object id for the 'MQRFH2 Property Type' data type

static int
MQSHORT
The meta object id for the 'MQSHORT' data type

static int
MQSHORT\_OBJECT
The meta object id for the 'MQSHORT Object' data type

static int
MQUINT32
The meta object id for the 'MQUINT32' data type

static int
MQUINT32\_OBJECT
The meta object id for the 'MQUINT32 Object' data type

static int
MQUINT64
The meta object id for the 'MQUINT64' data type

static int
MQULONG
The meta object id for the 'MQULONG' data type

static int
MQULONG\_OBJECT
The meta object id for the 'MQULONG Object' data type

static int
MQUSHORT
The meta object id for the 'MQUSHORT' data type

static int
MQUSHORT\_OBJECT
The meta object id for the 'MQUSHORT Object' data type

static int
NINE\_DIGITS
The meta object id for the 'Nine Digits' data type

static int
NINE\_DIGITS\_OBJECT
The meta object id for the 'Nine Digits Object' data type

- Method Summary Methods Modifier and Type Method and Description org.eclipse.emf.ecore.EAttribute getDocumentRoot\_Mixed () Returns the meta object for the attribute list 'Mixed ' org.eclipse.emf.ecore.EReference getDocumentRoot\_MqControl () Returns the meta object for the containment reference 'Mq Control ' org.eclipse.emf.ecore.EReference getDocumentRoot\_MqHeaders () Returns the meta object for the containment reference 'Mq Headers ' org.eclipse.emf.ecore.EReference getDocumentRoot\_Mqmd () Returns the meta object for the containment reference 'Mqmd ' org.eclipse.emf.ecore.EReference getDocumentRoot\_XMLNSPrefixMap () Returns the meta object for the map 'XMLNS Prefix Map ' org.eclipse.emf.ecore.EReference getDocumentRoot\_XSISchemaLocation () Returns the meta object for the map 'XSI Schema Location ' org.eclipse.emf.ecore.EClass getDocumentRoot () Returns the meta object for class 'Document Root ' org.eclipse.emf.ecore.EDataType getMQBYTE () Returns the meta object for data type 'MQBYTE ' org.eclipse.emf.ecore.EDataType getMQBYTE16 () Returns the meta object for data type 'MQBYTE16 ' org.eclipse.emf.ecore.EDataType getMQBYTE24 () Returns the meta object for data type 'MQBYTE24 ' org.eclipse.emf.ecore.EDataType getMQBYTE32 () Returns the meta object for data type 'MQBYTE32 ' org.eclipse.emf.ecore.EDataType getMQBYTE8 () Returns the meta object for data type 'MQBYTE8 ' org.eclipse.emf.ecore.EDataType getMQCHAR () Returns the meta object for data type 'MQCHAR ' org.eclipse.emf.ecore.EDataType getMQCHAR12 () Returns the meta object for data type 'MQCHAR12 ' org.eclipse.emf.ecore.EDataType getMQCHAR128 () Returns the meta object for data type 'MQCHAR128 ' org.eclipse.emf.ecore.EDataType getMQCHAR16 () Returns the meta object for data type 'MQCHAR16 ' org.eclipse.emf.ecore.EDataType getMQCHAR20 () Returns the meta object for data type 'MQCHAR20 ' org.eclipse.emf.ecore.EDataType getMQCHAR24 () Returns the meta object for data type 'MQCHAR24 ' org.eclipse.emf.ecore.EDataType getMQCHAR256 () Returns the meta object for data type 'MQCHAR256 ' org.eclipse.emf.ecore.EDataType getMQCHAR28 () Returns the meta object for data type 'MQCHAR28 ' org.eclipse.emf.ecore.EDataType getMQCHAR32 () Returns the meta object for data type 'MQCHAR32 ' org.eclipse.emf.ecore.EDataType getMQCHAR4 () Returns the meta object for data type 'MQCHAR4 ' org.eclipse.emf.ecore.EDataType getMQCHAR48 () Returns the meta object for data type 'MQCHAR48 ' org.eclipse.emf.ecore.EDataType getMQCHAR64 () Returns the meta object for data type 'MQCHAR64 ' org.eclipse.emf.ecore.EDataType getMQCHAR8 () Returns the meta object for data type 'MQCHAR8 ' org.eclipse.emf.ecore.EAttribute getMQCIH\_AbendCode () Returns the meta object for the attribute 'Abend Code ' org.eclipse.emf.ecore.EAttribute getMQCIH\_ADSDescriptor () Returns the meta object for the attribute 'ADS Descriptor ' org.eclipse.emf.ecore.EAttribute getMQCIH\_AttentionId () Returns the meta object for the attribute 'Attention Id ' org.eclipse.emf.ecore.EAttribute getMQCIH\_Authenticator () Returns the meta object for the attribute 'Authenticator ' org.eclipse.emf.ecore.EAttribute getMQCIH\_CancelCode () Returns the meta object for the attribute 'Cancel Code ' org.eclipse.emf.ecore.EAttribute getMQCIH\_CompCode () Returns the meta object for the attribute 'Comp Code ' org.eclipse.emf.ecore.EAttribute getMQCIH\_ConversationalTask () Returns the meta object for the attribute 'Conversational Task ' org.eclipse.emf.ecore.EAttribute getMQCIH\_CursorPosition () Returns the meta object for the attribute 'Cursor Position ' org.eclipse.emf.ecore.EAttribute getMQCIH\_ErrorOffset () Returns the meta object for the attribute 'Error Offset ' org.eclipse.emf.ecore.EAttribute getMQCIH\_Facility () Returns the meta object for the attribute 'Facility ' org.eclipse.emf.ecore.EAttribute getMQCIH\_FacilityKeepTime () Returns the meta object for the attribute 'Facility Keep Time ' org.eclipse.emf.ecore.EAttribute getMQCIH\_FacilityLike () Returns the meta object for the attribute 'Facility Like ' org.eclipse.emf.ecore.EAttribute getMQCIH\_Flags () Returns the meta object for the attribute 'Flags ' org.eclipse.emf.ecore.EAttribute getMQCIH\_Function () Returns the meta object for the attribute 'Function ' org.eclipse.emf.ecore.EAttribute getMQCIH\_GetWaitInterval () Returns the meta object for the attribute 'Get Wait Interval ' org.eclipse.emf.ecore.EAttribute getMQCIH\_InputItem () Returns the meta object for the attribute 'Input Item ' org.eclipse.emf.ecore.EAttribute getMQCIH\_LinkType () Returns the meta object for the attribute 'Link Type ' org.eclipse.emf.ecore.EAttribute getMQCIH\_NextTransactionId () Returns the meta object for the attribute 'Next Transaction Id ' org.eclipse.emf.ecore.EAttribute getMQCIH\_OutputDataLength () Returns the meta object for the attribute 'Output Data Length ' org.eclipse.emf.ecore.EAttribute getMQCIH\_ProgramName () Returns the meta object for the attribute 'Program Name ' org.eclipse.emf.ecore.EAttribute getMQCIH\_Reason () Returns the meta object for the attribute 'Reason ' org.eclipse.emf.ecore.EAttribute getMQCIH\_RemoteSysId () Returns the meta object for the attribute 'Remote Sys Id ' org.eclipse.emf.ecore.EAttribute getMQCIH\_RemoteTransId () Returns the meta object for the attribute 'Remote Trans Id ' org.eclipse.emf.ecore.EAttribute getMQCIH\_ReplyToFormat () Returns the meta object for the attribute 'Reply To Format ' org.eclipse.emf.ecore.EAttribute getMQCIH\_Reserved1 () Returns the meta object for the attribute 'Reserved1 ' org.eclipse.emf.ecore.EAttribute getMQCIH\_Reserved2 () Returns the meta object for the attribute 'Reserved2 ' org.eclipse.emf.ecore.EAttribute getMQCIH\_Reserved3 () Returns the meta object for the attribute 'Reserved3 ' org.eclipse.emf.ecore.EAttribute getMQCIH\_Reserved4 () Returns the meta object for the attribute 'Reserved4 ' org.eclipse.emf.ecore.EAttribute getMQCIH\_ReturnCode () Returns the meta object for the attribute 'Return Code ' org.eclipse.emf.ecore.EAttribute getMQCIH\_StartCode () Returns the meta object for the attribute 'Start Code ' org.eclipse.emf.ecore.EAttribute getMQCIH\_TaskEndStatus () Returns the meta object for the attribute 'Task End Status ' org.eclipse.emf.ecore.EAttribute getMQCIH\_TransactionId () Returns the meta object for the attribute 'Transaction Id ' org.eclipse.emf.ecore.EAttribute getMQCIH\_UOWControl () Returns the meta object for the attribute 'UOW Control ' org.eclipse.emf.ecore.EAttribute getMQCIH\_Version () Returns the meta object for the attribute 'Version ' org.eclipse.emf.ecore.EClass getMQCIH () Returns the meta object for class 'MQCIH ' org.eclipse.emf.ecore.EAttribute getMQControl\_CodedCharSetId () Returns the meta object for the attribute 'Coded Char Set Id ' org.eclipse.emf.ecore.EAttribute getMQControl\_Encoding () Returns the meta object for the attribute 'Encoding ' org.eclipse.emf.ecore.EAttribute getMQControl\_Format () Returns the meta object for the attribute 'Format ' org.eclipse.emf.ecore.EClass getMQControl () Returns the meta object for class 'MQ Control ' org.eclipse.emf.ecore.EReference getMQHeader\_Value () Returns the meta object for the containment reference 'Value ' org.eclipse.emf.ecore.EClass getMQHeader () Returns the meta object for class 'MQ Header ' org.eclipse.emf.ecore.EReference getMQHeaders\_Header () Returns the meta object for the containment reference list 'Header ' org.eclipse.emf.ecore.EClass getMQHeaders () Returns the meta object for class 'MQ Headers ' org.eclipse.emf.ecore.EAttribute getMQIIH\_Authenticator () Returns the meta object for the attribute 'Authenticator ' org.eclipse.emf.ecore.EAttribute getMQIIH\_CommitMode () Returns the meta object for the attribute 'Commit Mode ' org.eclipse.emf.ecore.EAttribute getMQIIH\_Flags () Returns the meta object for the attribute 'Flags ' org.eclipse.emf.ecore.EAttribute getMQIIH\_LTermOverride () Returns the meta object for the attribute 'LTerm Override ' org.eclipse.emf.ecore.EAttribute getMQIIH\_MFSMapName () Returns the meta object for the attribute 'MFS Map Name ' org.eclipse.emf.ecore.EAttribute getMQIIH\_ReplyToFormat () Returns the meta object for the attribute 'Reply To Format ' org.eclipse.emf.ecore.EAttribute getMQIIH\_Reserved () Returns the meta object for the attribute 'Reserved ' org.eclipse.emf.ecore.EAttribute getMQIIH\_SecurityScope () Returns the meta object for the attribute 'Security Scope ' org.eclipse.emf.ecore.EAttribute getMQIIH\_TranInstanceId () Returns the meta object for the attribute 'Tran Instance Id ' org.eclipse.emf.ecore.EAttribute getMQIIH\_TranState () Returns the meta object for the attribute 'Tran State ' org.eclipse.emf.ecore.EAttribute getMQIIH\_Version () Returns the meta object for the attribute 'Version ' org.eclipse.emf.ecore.EClass getMQIIH () Returns the meta object for class 'MQIIH ' org.eclipse.emf.ecore.EDataType getMQINT32 () Returns the meta object for data type 'MQINT32 ' org.eclipse.emf.ecore.EDataType getMQINT32Object () Returns the meta object for data type 'MQINT32 Object ' org.eclipse.emf.ecore.EDataType getMQINT64 () Returns the meta object for data type 'MQINT64 ' org.eclipse.emf.ecore.EDataType getMQINT64Object () Returns the meta object for data type 'MQINT64 Object ' org.eclipse.emf.ecore.EDataType getMQLONG () Returns the meta object for data type 'MQLONG ' org.eclipse.emf.ecore.EDataType getMQLONGObject () Returns the meta object for data type 'MQLONG Object ' org.eclipse.emf.ecore.EAttribute getMQMD\_AccountingToken () Returns the meta object for the attribute 'Accounting Token ' org.eclipse.emf.ecore.EAttribute getMQMD\_ApplIdentityData () Returns the meta object for the attribute 'Appl Identity Data ' org.eclipse.emf.ecore.EAttribute getMQMD\_ApplOriginData () Returns the meta object for the attribute 'Appl Origin Data ' org.eclipse.emf.ecore.EAttribute getMQMD\_BackoutCount () Returns the meta object for the attribute 'Backout Count ' org.eclipse.emf.ecore.EAttribute getMQMD\_CorrelId () Returns the meta object for the attribute 'Correl Id ' org.eclipse.emf.ecore.EAttribute getMQMD\_Expiry () Returns the meta object for the attribute 'Expiry ' org.eclipse.emf.ecore.EAttribute getMQMD\_Feedback () Returns the meta object for the attribute 'Feedback ' org.eclipse.emf.ecore.EAttribute getMQMD\_GroupId () Returns the meta object for the attribute 'Group Id ' org.eclipse.emf.ecore.EAttribute getMQMD\_MsgFlags () Returns the meta object for the attribute 'Msg Flags ' org.eclipse.emf.ecore.EAttribute getMQMD\_MsgId () Returns the meta object for the attribute 'Msg Id ' org.eclipse.emf.ecore.EAttribute getMQMD\_MsgSeqNumber () Returns the meta object for the attribute 'Msg Seq Number ' org.eclipse.emf.ecore.EAttribute getMQMD\_MsgType () Returns the meta object for the attribute 'Msg Type ' org.eclipse.emf.ecore.EAttribute getMQMD\_Offset () Returns the meta object for the attribute 'Offset ' org.eclipse.emf.ecore.EAttribute getMQMD\_OriginalLength () Returns the meta object for the attribute 'Original Length ' org.eclipse.emf.ecore.EAttribute getMQMD\_Persistence () Returns the meta object for the attribute 'Persistence ' org.eclipse.emf.ecore.EAttribute getMQMD\_Priority () Returns the meta object for the attribute 'Priority ' org.eclipse.emf.ecore.EAttribute getMQMD\_PutApplName () Returns the meta object for the attribute 'Put Appl Name ' org.eclipse.emf.ecore.EAttribute getMQMD\_PutApplType () Returns the meta object for the attribute 'Put Appl Type ' org.eclipse.emf.ecore.EAttribute getMQMD\_PutDate () Returns the meta object for the attribute 'Put Date ' org.eclipse.emf.ecore.EAttribute getMQMD\_PutTime () Returns the meta object for the attribute 'Put Time ' org.eclipse.emf.ecore.EAttribute getMQMD\_ReplyToQ () Returns the meta object for the attribute 'Reply To Q ' org.eclipse.emf.ecore.EAttribute getMQMD\_ReplyToQMgr () Returns the meta object for the attribute 'Reply To QMgr ' org.eclipse.emf.ecore.EAttribute getMQMD\_Report () Returns the meta object for the attribute 'Report ' org.eclipse.emf.ecore.EAttribute getMQMD\_UserIdentifier () Returns the meta object for the attribute 'User Identifier ' org.eclipse.emf.ecore.EClass getMQMD () Returns the meta object for class 'MQMD ' org.eclipse.emf.ecore.EAttribute getMQOpaqueHeader\_Data () Returns the meta object for the attribute 'Data ' org.eclipse.emf.ecore.EAttribute getMQOpaqueHeader\_Flags () Returns the meta object for the attribute 'Flags ' org.eclipse.emf.ecore.EAttribute getMQOpaqueHeader\_StrucId () Returns the meta object for the attribute 'Struc Id ' org.eclipse.emf.ecore.EAttribute getMQOpaqueHeader\_Version () Returns the meta object for the attribute 'Version ' org.eclipse.emf.ecore.EClass getMQOpaqueHeader () Returns the meta object for class 'MQ Opaque Header ' org.eclipse.emf.ecore.EAttribute getMQRFH\_Flags () Returns the meta object for the attribute 'Flags ' org.eclipse.emf.ecore.EReference getMQRFH\_Property () Returns the meta object for the containment reference list 'Property ' org.eclipse.emf.ecore.EClass getMQRFH () Returns the meta object for class 'MQRFH ' org.eclipse.emf.ecore.EAttribute getMQRFH2\_Flags () Returns the meta object for the attribute 'Flags ' org.eclipse.emf.ecore.EReference getMQRFH2\_Folder () Returns the meta object for the containment reference list 'Folder ' org.eclipse.emf.ecore.EAttribute getMQRFH2\_NameValueCCSID () Returns the meta object for the attribute 'Name Value CCSID ' org.eclipse.emf.ecore.EClass getMQRFH2 () Returns the meta object for class 'MQRFH2 ' org.eclipse.emf.ecore.EReference getMQRFH2Group\_Group () Returns the meta object for the containment reference list 'Group ' org.eclipse.emf.ecore.EAttribute getMQRFH2Group\_Name () Returns the meta object for the attribute 'Name ' org.eclipse.emf.ecore.EReference getMQRFH2Group\_Property () Returns the meta object for the containment reference list 'Property ' org.eclipse.emf.ecore.EAttribute getMQRFH2Group\_Rfh2Contents () Returns the meta object for the attribute list 'Rfh2 Contents ' org.eclipse.emf.ecore.EClass getMQRFH2Group () Returns the meta object for class 'MQRFH2 Group ' org.eclipse.emf.ecore.EAttribute getMQRFH2Property\_Name () Returns the meta object for the attribute 'Name ' org.eclipse.emf.ecore.EAttribute getMQRFH2Property\_Type () Returns the meta object for the attribute 'Type ' org.eclipse.emf.ecore.EAttribute getMQRFH2Property\_Value () Returns the meta object for the attribute 'Value ' org.eclipse.emf.ecore.EClass getMQRFH2Property () Returns the meta object for class 'MQRFH2 Property ' org.eclipse.emf.ecore.EDataType getMQRFH2PropertyType () Returns the meta object for data type 'MQRFH2 Property Type ' org.eclipse.emf.ecore.EAttribute getMQRFHProperty\_Name () Returns the meta object for the attribute 'Name ' org.eclipse.emf.ecore.EAttribute getMQRFHProperty\_Value () Returns the meta object for the attribute 'Value ' org.eclipse.emf.ecore.EClass getMQRFHProperty () Returns the meta object for class 'MQRFH Property ' org.eclipse.emf.ecore.EDataType getMQSHORT () Returns the meta object for data type 'MQSHORT ' org.eclipse.emf.ecore.EDataType getMQSHORTObject () Returns the meta object for data type 'MQSHORT Object ' org.eclipse.emf.ecore.EDataType getMQUINT32 () Returns the meta object for data type 'MQUINT32 ' org.eclipse.emf.ecore.EDataType getMQUINT32Object () Returns the meta object for data type 'MQUINT32 Object ' org.eclipse.emf.ecore.EDataType getMQUINT64 () Returns the meta object for data type 'MQUINT64 ' org.eclipse.emf.ecore.EDataType getMQULONG () Returns the meta object for data type 'MQULONG ' org.eclipse.emf.ecore.EDataType getMQULONGObject () Returns the meta object for data type 'MQULONG Object ' org.eclipse.emf.ecore.EDataType getMQUSHORT () Returns the meta object for data type 'MQUSHORT ' org.eclipse.emf.ecore.EDataType getMQUSHORTObject () Returns the meta object for data type 'MQUSHORT Object ' org.eclipse.emf.ecore.EDataType getNineDigits () Returns the meta object for data type 'Nine Digits ' org.eclipse.emf.ecore.EDataType getNineDigitsObject () Returns the meta object for data type 'Nine Digits Object ' WMQStructuresFactory getWMQStructuresFactory () Returns the factory that creates the instances of the model

### Method Summary

| Modifier and Type                | Method and Description                                                                          |
|----------------------------------|-------------------------------------------------------------------------------------------------|
| org.eclipse.emf.ecore.EAttribute | getDocumentRoot\_Mixed() Returns the meta object for the attribute list 'Mixed'                  |
| org.eclipse.emf.ecore.EReference | getDocumentRoot\_MqControl() Returns the meta object for the containment reference 'Mq Control'  |
| org.eclipse.emf.ecore.EReference | getDocumentRoot\_MqHeaders() Returns the meta object for the containment reference 'Mq Headers'  |
| org.eclipse.emf.ecore.EReference | getDocumentRoot\_Mqmd() Returns the meta object for the containment reference 'Mqmd'             |
| org.eclipse.emf.ecore.EReference | getDocumentRoot\_XMLNSPrefixMap() Returns the meta object for the map 'XMLNS Prefix Map'         |
| org.eclipse.emf.ecore.EReference | getDocumentRoot\_XSISchemaLocation() Returns the meta object for the map 'XSI Schema Location'   |
| org.eclipse.emf.ecore.EClass     | getDocumentRoot() Returns the meta object for class 'Document Root'                             |
| org.eclipse.emf.ecore.EDataType  | getMQBYTE() Returns the meta object for data type 'MQBYTE'                                      |
| org.eclipse.emf.ecore.EDataType  | getMQBYTE16() Returns the meta object for data type 'MQBYTE16'                                  |
| org.eclipse.emf.ecore.EDataType  | getMQBYTE24() Returns the meta object for data type 'MQBYTE24'                                  |
| org.eclipse.emf.ecore.EDataType  | getMQBYTE32() Returns the meta object for data type 'MQBYTE32'                                  |
| org.eclipse.emf.ecore.EDataType  | getMQBYTE8() Returns the meta object for data type 'MQBYTE8'                                    |
| org.eclipse.emf.ecore.EDataType  | getMQCHAR() Returns the meta object for data type 'MQCHAR'                                      |
| org.eclipse.emf.ecore.EDataType  | getMQCHAR12() Returns the meta object for data type 'MQCHAR12'                                  |
| org.eclipse.emf.ecore.EDataType  | getMQCHAR128() Returns the meta object for data type 'MQCHAR128'                                |
| org.eclipse.emf.ecore.EDataType  | getMQCHAR16() Returns the meta object for data type 'MQCHAR16'                                  |
| org.eclipse.emf.ecore.EDataType  | getMQCHAR20() Returns the meta object for data type 'MQCHAR20'                                  |
| org.eclipse.emf.ecore.EDataType  | getMQCHAR24() Returns the meta object for data type 'MQCHAR24'                                  |
| org.eclipse.emf.ecore.EDataType  | getMQCHAR256() Returns the meta object for data type 'MQCHAR256'                                |
| org.eclipse.emf.ecore.EDataType  | getMQCHAR28() Returns the meta object for data type 'MQCHAR28'                                  |
| org.eclipse.emf.ecore.EDataType  | getMQCHAR32() Returns the meta object for data type 'MQCHAR32'                                  |
| org.eclipse.emf.ecore.EDataType  | getMQCHAR4() Returns the meta object for data type 'MQCHAR4'                                    |
| org.eclipse.emf.ecore.EDataType  | getMQCHAR48() Returns the meta object for data type 'MQCHAR48'                                  |
| org.eclipse.emf.ecore.EDataType  | getMQCHAR64() Returns the meta object for data type 'MQCHAR64'                                  |
| org.eclipse.emf.ecore.EDataType  | getMQCHAR8() Returns the meta object for data type 'MQCHAR8'                                    |
| org.eclipse.emf.ecore.EAttribute | getMQCIH\_AbendCode() Returns the meta object for the attribute 'Abend Code'                     |
| org.eclipse.emf.ecore.EAttribute | getMQCIH\_ADSDescriptor() Returns the meta object for the attribute 'ADS Descriptor'             |
| org.eclipse.emf.ecore.EAttribute | getMQCIH\_AttentionId() Returns the meta object for the attribute 'Attention Id'                 |
| org.eclipse.emf.ecore.EAttribute | getMQCIH\_Authenticator() Returns the meta object for the attribute 'Authenticator'              |
| org.eclipse.emf.ecore.EAttribute | getMQCIH\_CancelCode() Returns the meta object for the attribute 'Cancel Code'                   |
| org.eclipse.emf.ecore.EAttribute | getMQCIH\_CompCode() Returns the meta object for the attribute 'Comp Code'                       |
| org.eclipse.emf.ecore.EAttribute | getMQCIH\_ConversationalTask() Returns the meta object for the attribute 'Conversational Task'   |
| org.eclipse.emf.ecore.EAttribute | getMQCIH\_CursorPosition() Returns the meta object for the attribute 'Cursor Position'           |
| org.eclipse.emf.ecore.EAttribute | getMQCIH\_ErrorOffset() Returns the meta object for the attribute 'Error Offset'                 |
| org.eclipse.emf.ecore.EAttribute | getMQCIH\_Facility() Returns the meta object for the attribute 'Facility'                        |
| org.eclipse.emf.ecore.EAttribute | getMQCIH\_FacilityKeepTime() Returns the meta object for the attribute 'Facility Keep Time'      |
| org.eclipse.emf.ecore.EAttribute | getMQCIH\_FacilityLike() Returns the meta object for the attribute 'Facility Like'               |
| org.eclipse.emf.ecore.EAttribute | getMQCIH\_Flags() Returns the meta object for the attribute 'Flags'                              |
| org.eclipse.emf.ecore.EAttribute | getMQCIH\_Function() Returns the meta object for the attribute 'Function'                        |
| org.eclipse.emf.ecore.EAttribute | getMQCIH\_GetWaitInterval() Returns the meta object for the attribute 'Get Wait Interval'        |
| org.eclipse.emf.ecore.EAttribute | getMQCIH\_InputItem() Returns the meta object for the attribute 'Input Item'                     |
| org.eclipse.emf.ecore.EAttribute | getMQCIH\_LinkType() Returns the meta object for the attribute 'Link Type'                       |
| org.eclipse.emf.ecore.EAttribute | getMQCIH\_NextTransactionId() Returns the meta object for the attribute 'Next Transaction Id'    |
| org.eclipse.emf.ecore.EAttribute | getMQCIH\_OutputDataLength() Returns the meta object for the attribute 'Output Data Length'      |
| org.eclipse.emf.ecore.EAttribute | getMQCIH\_ProgramName() Returns the meta object for the attribute 'Program Name'                 |
| org.eclipse.emf.ecore.EAttribute | getMQCIH\_Reason() Returns the meta object for the attribute 'Reason'                            |
| org.eclipse.emf.ecore.EAttribute | getMQCIH\_RemoteSysId() Returns the meta object for the attribute 'Remote Sys Id'                |
| org.eclipse.emf.ecore.EAttribute | getMQCIH\_RemoteTransId() Returns the meta object for the attribute 'Remote Trans Id'            |
| org.eclipse.emf.ecore.EAttribute | getMQCIH\_ReplyToFormat() Returns the meta object for the attribute 'Reply To Format'            |
| org.eclipse.emf.ecore.EAttribute | getMQCIH\_Reserved1() Returns the meta object for the attribute 'Reserved1'                      |
| org.eclipse.emf.ecore.EAttribute | getMQCIH\_Reserved2() Returns the meta object for the attribute 'Reserved2'                      |
| org.eclipse.emf.ecore.EAttribute | getMQCIH\_Reserved3() Returns the meta object for the attribute 'Reserved3'                      |
| org.eclipse.emf.ecore.EAttribute | getMQCIH\_Reserved4() Returns the meta object for the attribute 'Reserved4'                      |
| org.eclipse.emf.ecore.EAttribute | getMQCIH\_ReturnCode() Returns the meta object for the attribute 'Return Code'                   |
| org.eclipse.emf.ecore.EAttribute | getMQCIH\_StartCode() Returns the meta object for the attribute 'Start Code'                     |
| org.eclipse.emf.ecore.EAttribute | getMQCIH\_TaskEndStatus() Returns the meta object for the attribute 'Task End Status'            |
| org.eclipse.emf.ecore.EAttribute | getMQCIH\_TransactionId() Returns the meta object for the attribute 'Transaction Id'             |
| org.eclipse.emf.ecore.EAttribute | getMQCIH\_UOWControl() Returns the meta object for the attribute 'UOW Control'                   |
| org.eclipse.emf.ecore.EAttribute | getMQCIH\_Version() Returns the meta object for the attribute 'Version'                          |
| org.eclipse.emf.ecore.EClass     | getMQCIH() Returns the meta object for class 'MQCIH'                                            |
| org.eclipse.emf.ecore.EAttribute | getMQControl\_CodedCharSetId() Returns the meta object for the attribute 'Coded Char Set Id'     |
| org.eclipse.emf.ecore.EAttribute | getMQControl\_Encoding() Returns the meta object for the attribute 'Encoding'                    |
| org.eclipse.emf.ecore.EAttribute | getMQControl\_Format() Returns the meta object for the attribute 'Format'                        |
| org.eclipse.emf.ecore.EClass     | getMQControl() Returns the meta object for class 'MQ Control'                                   |
| org.eclipse.emf.ecore.EReference | getMQHeader\_Value() Returns the meta object for the containment reference 'Value'               |
| org.eclipse.emf.ecore.EClass     | getMQHeader() Returns the meta object for class 'MQ Header'                                     |
| org.eclipse.emf.ecore.EReference | getMQHeaders\_Header() Returns the meta object for the containment reference list 'Header'       |
| org.eclipse.emf.ecore.EClass     | getMQHeaders() Returns the meta object for class 'MQ Headers'                                   |
| org.eclipse.emf.ecore.EAttribute | getMQIIH\_Authenticator() Returns the meta object for the attribute 'Authenticator'              |
| org.eclipse.emf.ecore.EAttribute | getMQIIH\_CommitMode() Returns the meta object for the attribute 'Commit Mode'                   |
| org.eclipse.emf.ecore.EAttribute | getMQIIH\_Flags() Returns the meta object for the attribute 'Flags'                              |
| org.eclipse.emf.ecore.EAttribute | getMQIIH\_LTermOverride() Returns the meta object for the attribute 'LTerm Override'             |
| org.eclipse.emf.ecore.EAttribute | getMQIIH\_MFSMapName() Returns the meta object for the attribute 'MFS Map Name'                  |
| org.eclipse.emf.ecore.EAttribute | getMQIIH\_ReplyToFormat() Returns the meta object for the attribute 'Reply To Format'            |
| org.eclipse.emf.ecore.EAttribute | getMQIIH\_Reserved() Returns the meta object for the attribute 'Reserved'                        |
| org.eclipse.emf.ecore.EAttribute | getMQIIH\_SecurityScope() Returns the meta object for the attribute 'Security Scope'             |
| org.eclipse.emf.ecore.EAttribute | getMQIIH\_TranInstanceId() Returns the meta object for the attribute 'Tran Instance Id'          |
| org.eclipse.emf.ecore.EAttribute | getMQIIH\_TranState() Returns the meta object for the attribute 'Tran State'                     |
| org.eclipse.emf.ecore.EAttribute | getMQIIH\_Version() Returns the meta object for the attribute 'Version'                          |
| org.eclipse.emf.ecore.EClass     | getMQIIH() Returns the meta object for class 'MQIIH'                                            |
| org.eclipse.emf.ecore.EDataType  | getMQINT32() Returns the meta object for data type 'MQINT32'                                    |
| org.eclipse.emf.ecore.EDataType  | getMQINT32Object() Returns the meta object for data type 'MQINT32 Object'                       |
| org.eclipse.emf.ecore.EDataType  | getMQINT64() Returns the meta object for data type 'MQINT64'                                    |
| org.eclipse.emf.ecore.EDataType  | getMQINT64Object() Returns the meta object for data type 'MQINT64 Object'                       |
| org.eclipse.emf.ecore.EDataType  | getMQLONG() Returns the meta object for data type 'MQLONG'                                      |
| org.eclipse.emf.ecore.EDataType  | getMQLONGObject() Returns the meta object for data type 'MQLONG Object'                         |
| org.eclipse.emf.ecore.EAttribute | getMQMD\_AccountingToken() Returns the meta object for the attribute 'Accounting Token'          |
| org.eclipse.emf.ecore.EAttribute | getMQMD\_ApplIdentityData() Returns the meta object for the attribute 'Appl Identity Data'       |
| org.eclipse.emf.ecore.EAttribute | getMQMD\_ApplOriginData() Returns the meta object for the attribute 'Appl Origin Data'           |
| org.eclipse.emf.ecore.EAttribute | getMQMD\_BackoutCount() Returns the meta object for the attribute 'Backout Count'                |
| org.eclipse.emf.ecore.EAttribute | getMQMD\_CorrelId() Returns the meta object for the attribute 'Correl Id'                        |
| org.eclipse.emf.ecore.EAttribute | getMQMD\_Expiry() Returns the meta object for the attribute 'Expiry'                             |
| org.eclipse.emf.ecore.EAttribute | getMQMD\_Feedback() Returns the meta object for the attribute 'Feedback'                         |
| org.eclipse.emf.ecore.EAttribute | getMQMD\_GroupId() Returns the meta object for the attribute 'Group Id'                          |
| org.eclipse.emf.ecore.EAttribute | getMQMD\_MsgFlags() Returns the meta object for the attribute 'Msg Flags'                        |
| org.eclipse.emf.ecore.EAttribute | getMQMD\_MsgId() Returns the meta object for the attribute 'Msg Id'                              |
| org.eclipse.emf.ecore.EAttribute | getMQMD\_MsgSeqNumber() Returns the meta object for the attribute 'Msg Seq Number'               |
| org.eclipse.emf.ecore.EAttribute | getMQMD\_MsgType() Returns the meta object for the attribute 'Msg Type'                          |
| org.eclipse.emf.ecore.EAttribute | getMQMD\_Offset() Returns the meta object for the attribute 'Offset'                             |
| org.eclipse.emf.ecore.EAttribute | getMQMD\_OriginalLength() Returns the meta object for the attribute 'Original Length'            |
| org.eclipse.emf.ecore.EAttribute | getMQMD\_Persistence() Returns the meta object for the attribute 'Persistence'                   |
| org.eclipse.emf.ecore.EAttribute | getMQMD\_Priority() Returns the meta object for the attribute 'Priority'                         |
| org.eclipse.emf.ecore.EAttribute | getMQMD\_PutApplName() Returns the meta object for the attribute 'Put Appl Name'                 |
| org.eclipse.emf.ecore.EAttribute | getMQMD\_PutApplType() Returns the meta object for the attribute 'Put Appl Type'                 |
| org.eclipse.emf.ecore.EAttribute | getMQMD\_PutDate() Returns the meta object for the attribute 'Put Date'                          |
| org.eclipse.emf.ecore.EAttribute | getMQMD\_PutTime() Returns the meta object for the attribute 'Put Time'                          |
| org.eclipse.emf.ecore.EAttribute | getMQMD\_ReplyToQ() Returns the meta object for the attribute 'Reply To Q'                       |
| org.eclipse.emf.ecore.EAttribute | getMQMD\_ReplyToQMgr() Returns the meta object for the attribute 'Reply To QMgr'                 |
| org.eclipse.emf.ecore.EAttribute | getMQMD\_Report() Returns the meta object for the attribute 'Report'                             |
| org.eclipse.emf.ecore.EAttribute | getMQMD\_UserIdentifier() Returns the meta object for the attribute 'User Identifier'            |
| org.eclipse.emf.ecore.EClass     | getMQMD() Returns the meta object for class 'MQMD'                                              |
| org.eclipse.emf.ecore.EAttribute | getMQOpaqueHeader\_Data() Returns the meta object for the attribute 'Data'                       |
| org.eclipse.emf.ecore.EAttribute | getMQOpaqueHeader\_Flags() Returns the meta object for the attribute 'Flags'                     |
| org.eclipse.emf.ecore.EAttribute | getMQOpaqueHeader\_StrucId() Returns the meta object for the attribute 'Struc Id'                |
| org.eclipse.emf.ecore.EAttribute | getMQOpaqueHeader\_Version() Returns the meta object for the attribute 'Version'                 |
| org.eclipse.emf.ecore.EClass     | getMQOpaqueHeader() Returns the meta object for class 'MQ Opaque Header'                        |
| org.eclipse.emf.ecore.EAttribute | getMQRFH\_Flags() Returns the meta object for the attribute 'Flags'                              |
| org.eclipse.emf.ecore.EReference | getMQRFH\_Property() Returns the meta object for the containment reference list 'Property'       |
| org.eclipse.emf.ecore.EClass     | getMQRFH() Returns the meta object for class 'MQRFH'                                            |
| org.eclipse.emf.ecore.EAttribute | getMQRFH2\_Flags() Returns the meta object for the attribute 'Flags'                             |
| org.eclipse.emf.ecore.EReference | getMQRFH2\_Folder() Returns the meta object for the containment reference list 'Folder'          |
| org.eclipse.emf.ecore.EAttribute | getMQRFH2\_NameValueCCSID() Returns the meta object for the attribute 'Name Value CCSID'         |
| org.eclipse.emf.ecore.EClass     | getMQRFH2() Returns the meta object for class 'MQRFH2'                                          |
| org.eclipse.emf.ecore.EReference | getMQRFH2Group\_Group() Returns the meta object for the containment reference list 'Group'       |
| org.eclipse.emf.ecore.EAttribute | getMQRFH2Group\_Name() Returns the meta object for the attribute 'Name'                          |
| org.eclipse.emf.ecore.EReference | getMQRFH2Group\_Property() Returns the meta object for the containment reference list 'Property' |
| org.eclipse.emf.ecore.EAttribute | getMQRFH2Group\_Rfh2Contents() Returns the meta object for the attribute list 'Rfh2 Contents'    |
| org.eclipse.emf.ecore.EClass     | getMQRFH2Group() Returns the meta object for class 'MQRFH2 Group'                               |
| org.eclipse.emf.ecore.EAttribute | getMQRFH2Property\_Name() Returns the meta object for the attribute 'Name'                       |
| org.eclipse.emf.ecore.EAttribute | getMQRFH2Property\_Type() Returns the meta object for the attribute 'Type'                       |
| org.eclipse.emf.ecore.EAttribute | getMQRFH2Property\_Value() Returns the meta object for the attribute 'Value'                     |
| org.eclipse.emf.ecore.EClass     | getMQRFH2Property() Returns the meta object for class 'MQRFH2 Property'                         |
| org.eclipse.emf.ecore.EDataType  | getMQRFH2PropertyType() Returns the meta object for data type 'MQRFH2 Property Type'            |
| org.eclipse.emf.ecore.EAttribute | getMQRFHProperty\_Name() Returns the meta object for the attribute 'Name'                        |
| org.eclipse.emf.ecore.EAttribute | getMQRFHProperty\_Value() Returns the meta object for the attribute 'Value'                      |
| org.eclipse.emf.ecore.EClass     | getMQRFHProperty() Returns the meta object for class 'MQRFH Property'                           |
| org.eclipse.emf.ecore.EDataType  | getMQSHORT() Returns the meta object for data type 'MQSHORT'                                    |
| org.eclipse.emf.ecore.EDataType  | getMQSHORTObject() Returns the meta object for data type 'MQSHORT Object'                       |
| org.eclipse.emf.ecore.EDataType  | getMQUINT32() Returns the meta object for data type 'MQUINT32'                                  |
| org.eclipse.emf.ecore.EDataType  | getMQUINT32Object() Returns the meta object for data type 'MQUINT32 Object'                     |
| org.eclipse.emf.ecore.EDataType  | getMQUINT64() Returns the meta object for data type 'MQUINT64'                                  |
| org.eclipse.emf.ecore.EDataType  | getMQULONG() Returns the meta object for data type 'MQULONG'                                    |
| org.eclipse.emf.ecore.EDataType  | getMQULONGObject() Returns the meta object for data type 'MQULONG Object'                       |
| org.eclipse.emf.ecore.EDataType  | getMQUSHORT() Returns the meta object for data type 'MQUSHORT'                                  |
| org.eclipse.emf.ecore.EDataType  | getMQUSHORTObject() Returns the meta object for data type 'MQUSHORT Object'                     |
| org.eclipse.emf.ecore.EDataType  | getNineDigits() Returns the meta object for data type 'Nine Digits'                             |
| org.eclipse.emf.ecore.EDataType  | getNineDigitsObject() Returns the meta object for data type 'Nine Digits Object'                |
| WMQStructuresFactory             | getWMQStructuresFactory() Returns the factory that creates the instances of the model           |

    - Methods inherited from interface org.eclipse.emf.ecore.EPackage
getEClassifier, getEClassifiers, getEFactoryInstance, getESubpackages, getESuperPackage, getNsPrefix, getNsURI, setEFactoryInstance, setNsPrefix, setNsURI
    - Methods inherited from interface org.eclipse.emf.ecore.ENamedElement
getName, setName
    - Methods inherited from interface org.eclipse.emf.ecore.EModelElement
getEAnnotation, getEAnnotations
    - Methods inherited from interface org.eclipse.emf.ecore.EObject
eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eIsProxy, eIsSet, eResource, eSet, eUnset
    - Methods inherited from interface org.eclipse.emf.common.notify.Notifier
eAdapters, eDeliver, eNotify, eSetDeliver