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

## Interface TaskPackage

- All Superinterfaces: org.eclipse.emf.ecore.EModelElement, org.eclipse.emf.ecore.ENamedElement, org.eclipse.emf.ecore.EObject, org.eclipse.emf.ecore.EPackage, org.eclipse.emf.common.notify.Notifier public interface TaskPackage extends org.eclipse.emf.ecore.EPackage begin-user-doc The Package for the model. It contains accessors for the meta objects to represent Since: 6.0.1 See Also: TaskFactory

```
public interface TaskPackage
extends org.eclipse.emf.ecore.EPackage
```

    - each class,
    - each feature of each class,
    - each enum,
    - and each data type

- ======== NESTED CLASS SUMMARY ======== =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Nested Class Summary Nested Classes Modifier and Type Interface and Description static interface TaskPackage.Literals Defines literals for the meta objects that represent each class, each feature of each class, each enum, and each data type </div

### Nested Class Summary

| Modifier and Type   | Interface and Description                                                                                                                                     |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static interface    | TaskPackage.Literals Defines literals for the meta objects that represent      each class,    each feature of each class,    each enum,    and each data type |

- Nested classes/interfaces inherited from interface org.eclipse.emf.ecore.EPackage
org.eclipse.emf.ecore.EPackage.Descriptor, org.eclipse.emf.ecore.EPackage.Registry

- Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static int
DOCUMENT\_ROOT
The meta object id for the 'Document Root' class

static int
DOCUMENT\_ROOT\_\_MIXED
The feature id for the 'Mixed' attribute list

static int
DOCUMENT\_ROOT\_\_TASK
The feature id for the 'Task' containment reference

static int
DOCUMENT\_ROOT\_\_XMLNS\_PREFIX\_MAP
The feature id for the 'XMLNS Prefix Map' map

static int
DOCUMENT\_ROOT\_\_XSI\_SCHEMA\_LOCATION
The feature id for the 'XSI Schema Location' map

static int
DOCUMENT\_ROOT\_FEATURE\_COUNT
The number of structural features of the 'Document Root' class

static TaskPackage
eINSTANCE
The singleton instance of the package

static java.lang.String
eNAME
The package name

static java.lang.String
eNS\_PREFIX
The package namespace name

static java.lang.String
eNS\_URI
The package namespace URI

static int
EQ\_NAME
The meta object id for the 'eQ Name' data type

static int
EURI
The meta object id for the 'eURI' data type

static int
PARAMETER\_TYPE
The meta object id for the 'Parameter Type' class

static int
PARAMETER\_TYPE\_\_ID
The feature id for the 'Id' attribute

static int
PARAMETER\_TYPE\_\_VALUE
The feature id for the 'Value' attribute

static int
PARAMETER\_TYPE\_FEATURE\_COUNT
The number of structural features of the 'Parameter Type' class

static int
TACTIVATION\_STATES
The meta object id for the 'TActivation States' enum

static int
TACTIVATION\_STATES\_OBJECT
The meta object id for the 'TActivation States Object' data type

static int
TADMINISTRATOR
The meta object id for the 'TAdministrator' class

static int
TADMINISTRATOR\_\_VERB
The feature id for the 'Verb' containment reference

static int
TADMINISTRATOR\_FEATURE\_COUNT
The number of structural features of the 'TAdministrator' class

static int
TAGGREGATE
The meta object id for the 'TAggregate' class

static int
TAGGREGATE\_\_CONDITION
The feature id for the 'Condition' attribute

static int
TAGGREGATE\_\_FUNCTION
The feature id for the 'Function' attribute

static int
TAGGREGATE\_\_LOCATION
The feature id for the 'Location' attribute

static int
TAGGREGATE\_\_PART
The feature id for the 'Part' attribute

static int
TAGGREGATE\_FEATURE\_COUNT
The number of structural features of the 'TAggregate' class

static int
TAPPLY\_TO
The meta object id for the 'TApply To' class

static int
TAPPLY\_TO\_\_ROLE
The feature id for the 'Role' attribute

static int
TAPPLY\_TO\_FEATURE\_COUNT
The number of structural features of the 'TApply To' class

static int
TAT\_LEAST\_EXPECTED\_STATES
The meta object id for the 'TAt Least Expected States' enum

static int
TAT\_LEAST\_EXPECTED\_STATES\_OBJECT
The meta object id for the 'TAt Least Expected States Object' data type

static int
TAUTO\_DELETION\_MODE
The meta object id for the 'TAuto Deletion Mode' enum

static int
TAUTO\_DELETION\_MODE\_OBJECT
The meta object id for the 'TAuto Deletion Mode Object' data type

static int
TAUTONOMY
The meta object id for the 'TAutonomy' enum

static int
TAUTONOMY\_OBJECT
The meta object id for the 'TAutonomy Object' data type

static int
TBOOLEAN
The meta object id for the 'TBoolean' enum

static int
TBOOLEAN\_OBJECT
The meta object id for the 'TBoolean Object' data type

static int
TCOMPLETION
The meta object id for the 'TCompletion' class

static int
TCOMPLETION\_\_CRITERION
The feature id for the 'Criterion' containment reference

static int
TCOMPLETION\_\_NAME
The feature id for the 'Name' attribute

static int
TCOMPLETION\_\_RESULT
The feature id for the 'Result' containment reference

static int
TCOMPLETION\_\_USE\_DEFAULT\_RESULT\_CONSTRUCTION
The feature id for the 'Use Default Result Construction' attribute

static int
TCOMPLETION\_BEHAVIOR
The meta object id for the 'TCompletion Behavior' class

static int
TCOMPLETION\_BEHAVIOR\_\_COMPLETION
The feature id for the 'Completion' containment reference list

static int
TCOMPLETION\_BEHAVIOR\_\_DEFAULT\_COMPLETION
The feature id for the 'Default Completion' containment reference

static int
TCOMPLETION\_BEHAVIOR\_FEATURE\_COUNT
The number of structural features of the 'TCompletion Behavior' class

static int
TCOMPLETION\_FEATURE\_COUNT
The number of structural features of the 'TCompletion' class

static int
TCONTACT\_QUERY
The meta object id for the 'TContact Query' class

static int
TCONTACT\_QUERY\_\_CATEGORY
The feature id for the 'Category' attribute

static int
TCONTACT\_QUERY\_\_VERB
The feature id for the 'Verb' containment reference

static int
TCONTACT\_QUERY\_FEATURE\_COUNT
The number of structural features of the 'TContact Query' class

static int
TCONTEXT\_AUTHORIZATION\_FOR\_OWNER
The meta object id for the 'TContext Authorization For Owner' enum

static int
TCONTEXT\_AUTHORIZATION\_FOR\_OWNER\_OBJECT
The meta object id for the 'TContext Authorization For Owner Object' data type

static int
TCRITERION
The meta object id for the 'TCriterion' class

static int
TCRITERION\_\_CONDITION
The feature id for the 'Condition' attribute

static int
TCRITERION\_\_FOR
The feature id for the 'For' attribute

static int
TCRITERION\_FEATURE\_COUNT
The number of structural features of the 'TCriterion' class

static int
TCUSTOM\_CLIENT\_SETTINGS
The meta object id for the 'TCustom Client Settings' class

static int
TCUSTOM\_CLIENT\_SETTINGS\_\_CLIENT\_TYPE
The feature id for the 'Client Type' attribute

static int
TCUSTOM\_CLIENT\_SETTINGS\_\_CUSTOM\_SETTING
The feature id for the 'Custom Setting' containment reference list

static int
TCUSTOM\_CLIENT\_SETTINGS\_FEATURE\_COUNT
The number of structural features of the 'TCustom Client Settings' class

static int
TCUSTOM\_PROPERTY
The meta object id for the 'TCustom Property' class

static int
TCUSTOM\_PROPERTY\_\_INLINE
The feature id for the 'Inline' attribute

static int
TCUSTOM\_PROPERTY\_\_NAME
The feature id for the 'Name' attribute

static int
TCUSTOM\_PROPERTY\_\_VALUE
The feature id for the 'Value' attribute

static int
TCUSTOM\_PROPERTY\_FEATURE\_COUNT
The number of structural features of the 'TCustom Property' class

static int
TCUSTOM\_SETTING
The meta object id for the 'TCustom Setting' class

static int
TCUSTOM\_SETTING\_\_NAME
The feature id for the 'Name' attribute

static int
TCUSTOM\_SETTING\_\_VALUE
The feature id for the 'Value' attribute

static int
TCUSTOM\_SETTING\_FEATURE\_COUNT
The number of structural features of the 'TCustom Setting' class

static int
TDEFAULT\_COMPLETION
The meta object id for the 'TDefault Completion' class

static int
TDEFAULT\_COMPLETION\_\_RESULT
The feature id for the 'Result' containment reference

static int
TDEFAULT\_COMPLETION\_FEATURE\_COUNT
The number of structural features of the 'TDefault Completion' class

static int
TDESCRIPTION
The meta object id for the 'TDescription' class

static int
TDESCRIPTION\_\_LOCALE
The feature id for the 'Locale' attribute

static int
TDESCRIPTION\_\_VALUE
The feature id for the 'Value' attribute

static int
TDESCRIPTION\_FEATURE\_COUNT
The number of structural features of the 'TDescription' class

static int
TDISPLAY\_NAME
The meta object id for the 'TDisplay Name' class

static int
TDISPLAY\_NAME\_\_LOCALE
The feature id for the 'Locale' attribute

static int
TDISPLAY\_NAME\_\_VALUE
The feature id for the 'Value' attribute

static int
TDISPLAY\_NAME\_FEATURE\_COUNT
The number of structural features of the 'TDisplay Name' class

static int
TDOCUMENTATION
The meta object id for the 'TDocumentation' class

static int
TDOCUMENTATION\_\_LOCALE
The feature id for the 'Locale' attribute

static int
TDOCUMENTATION\_\_VALUE
The feature id for the 'Value' attribute

static int
TDOCUMENTATION\_FEATURE\_COUNT
The number of structural features of the 'TDocumentation' class

static int
TDURATION\_CONSTANTS
The meta object id for the 'TDuration Constants' enum

static int
TDURATION\_CONSTANTS\_OBJECT
The meta object id for the 'TDuration Constants Object' data type

static int
TE\_MAIL\_RECEIVER
The meta object id for the 'TE Mail Receiver' class

static int
TE\_MAIL\_RECEIVER\_\_VERB
The feature id for the 'Verb' containment reference

static int
TE\_MAIL\_RECEIVER\_FEATURE\_COUNT
The number of structural features of the 'TE Mail Receiver' class

static int
TEDITOR
The meta object id for the 'TEditor' class

static int
TEDITOR\_\_VERB
The feature id for the 'Verb' containment reference

static int
TEDITOR\_FEATURE\_COUNT
The number of structural features of the 'TEditor' class

static int
TEMAIL
The meta object id for the 'TEmail' class

static int
TEMAIL\_\_LOCALIZED\_EMAIL
The feature id for the 'Localized Email' containment reference list

static int
TEMAIL\_\_NAME
The feature id for the 'Name' attribute

static int
TEMAIL\_FEATURE\_COUNT
The number of structural features of the 'TEmail' class

static int
TESCALATION
The meta object id for the 'TEscalation' class

static int
TESCALATION\_\_AT\_LEAST\_EXPECTED\_STATE
The feature id for the 'At Least Expected State' attribute

static int
TESCALATION\_\_AUTO\_REPEAT\_DURATION
The feature id for the 'Auto Repeat Duration' attribute

static int
TESCALATION\_\_CUSTOM\_PROPERTY
The feature id for the 'Custom Property' containment reference list

static int
TESCALATION\_\_DESCRIPTION
The feature id for the 'Description' containment reference list

static int
TESCALATION\_\_DISPLAY\_NAME
The feature id for the 'Display Name' containment reference list

static int
TESCALATION\_\_DOCUMENTATION
The feature id for the 'Documentation' containment reference list

static int
TESCALATION\_\_DURATION\_UNTIL\_ESCALATION
The feature id for the 'Duration Until Escalation' attribute

static int
TESCALATION\_\_EMAIL
The feature id for the 'Email' attribute

static int
TESCALATION\_\_EMAIL\_RECEIVER
The feature id for the 'EMail Receiver' containment reference

static int
TESCALATION\_\_ESCALATION\_ACTION
The feature id for the 'Escalation Action' attribute

static int
TESCALATION\_\_ESCALATION\_RECEIVER
The feature id for the 'Escalation Receiver' containment reference

static int
TESCALATION\_\_INCREASE\_PRIORITY
The feature id for the 'Increase Priority' attribute

static int
TESCALATION\_\_NAME
The feature id for the 'Name' attribute

static int
TESCALATION\_ACTIONS
The meta object id for the 'TEscalation Actions' enum

static int
TESCALATION\_ACTIONS\_OBJECT
The meta object id for the 'TEscalation Actions Object' data type

static int
TESCALATION\_CHAIN
The meta object id for the 'TEscalation Chain' class

static int
TESCALATION\_CHAIN\_\_ACTIVATION\_STATE
The feature id for the 'Activation State' attribute

static int
TESCALATION\_CHAIN\_\_ESCALATION
The feature id for the 'Escalation' containment reference list

static int
TESCALATION\_CHAIN\_FEATURE\_COUNT
The number of structural features of the 'TEscalation Chain' class

static int
TESCALATION\_FEATURE\_COUNT
The number of structural features of the 'TEscalation' class

static int
TESCALATION\_RECEIVER
The meta object id for the 'TEscalation Receiver' class

static int
TESCALATION\_RECEIVER\_\_VERB
The feature id for the 'Verb' containment reference

static int
TESCALATION\_RECEIVER\_FEATURE\_COUNT
The number of structural features of the 'TEscalation Receiver' class

static int
TESCALATION\_SETTINGS
The meta object id for the 'TEscalation Settings' class

static int
TESCALATION\_SETTINGS\_\_ESCALATION\_CHAIN
The feature id for the 'Escalation Chain' containment reference list

static int
TESCALATION\_SETTINGS\_FEATURE\_COUNT
The number of structural features of the 'TEscalation Settings' class

static int
TIMPORT
The meta object id for the 'TImport' class

static int
TIMPORT\_\_IMPORT\_TYPE
The feature id for the 'Import Type' attribute

static int
TIMPORT\_\_LOCATION
The feature id for the 'Location' attribute

static int
TIMPORT\_\_NAMESPACE
The feature id for the 'Namespace' attribute

static int
TIMPORT\_FEATURE\_COUNT
The number of structural features of the 'TImport' class

static int
TINCREASE\_PRIORITY
The meta object id for the 'TIncrease Priority' enum

static int
TINCREASE\_PRIORITY\_OBJECT
The meta object id for the 'TIncrease Priority Object' data type

static int
TINHERITED\_AUTHORIZATION
The meta object id for the 'TInherited Authorization' enum

static int
TINHERITED\_AUTHORIZATION\_OBJECT
The meta object id for the 'TInherited Authorization Object' data type

static int
TINLINE\_CUSTOM\_PROPERTY\_ENUM
The meta object id for the 'TInline Custom Property Enum' enum

static int
TINLINE\_CUSTOM\_PROPERTY\_ENUM\_OBJECT
The meta object id for the 'TInline Custom Property Enum Object' data type

static int
TINTERFACE
The meta object id for the 'TInterface' class

static int
TINTERFACE\_\_KIND
The feature id for the 'Kind' attribute

static int
TINTERFACE\_\_OPERATION
The feature id for the 'Operation' attribute

static int
TINTERFACE\_\_PORT\_TYPE
The feature id for the 'Port Type' attribute

static int
TINTERFACE\_FEATURE\_COUNT
The number of structural features of the 'TInterface' class

static int
TINTERFACE\_KINDS
The meta object id for the 'TInterface Kinds' enum

static int
TINTERFACE\_KINDS\_OBJECT
The meta object id for the 'TInterface Kinds Object' data type

static int
TJSP
The meta object id for the 'TJSP' class

static int
TJSP\_\_APPLY\_TO
The feature id for the 'Apply To' containment reference list

static int
TJSP\_\_CONTEXT\_ROOT
The feature id for the 'Context Root' attribute

static int
TJSP\_\_FAULT\_QNAME
The feature id for the 'Fault QName' attribute

static int
TJSP\_\_FOR
The feature id for the 'For' attribute

static int
TJSP\_\_URI
The feature id for the 'Uri' attribute

static int
TJSP\_APPLICABLE\_ROLE
The meta object id for the 'TJsp Applicable Role' enum

static int
TJSP\_APPLICABLE\_ROLE\_OBJECT
The meta object id for the 'TJsp Applicable Role Object' data type

static int
TJSP\_FEATURE\_COUNT
The number of structural features of the 'TJSP' class

static int
TJSP\_USAGE\_PATTERN
The meta object id for the 'TJsp Usage Pattern' enum

static int
TJSP\_USAGE\_PATTERN\_OBJECT
The meta object id for the 'TJsp Usage Pattern Object' data type

static int
TLANGUAGE
The meta object id for the 'TLanguage' data type

static int
TLOCALIZED\_EMAIL
The meta object id for the 'TLocalized Email' class

static int
TLOCALIZED\_EMAIL\_\_BODY
The feature id for the 'Body' attribute

static int
TLOCALIZED\_EMAIL\_\_LOCALE
The feature id for the 'Locale' attribute

static int
TLOCALIZED\_EMAIL\_\_SUBJECT
The feature id for the 'Subject' attribute

static int
TLOCALIZED\_EMAIL\_FEATURE\_COUNT
The number of structural features of the 'TLocalized Email' class

static int
TNON\_NEGATIVE\_INT
The meta object id for the 'TNon Negative Int' data type

static int
TNON\_NEGATIVE\_INT\_OBJECT
The meta object id for the 'TNon Negative Int Object' data type

static int
TPARALLEL
The meta object id for the 'TParallel' class

static int
TPARALLEL\_\_COMPLETION\_BEHAVIOR
The feature id for the 'Completion Behavior' containment reference

static int
TPARALLEL\_\_INHERITED\_AUTHORIZATION
The feature id for the 'Inherited Authorization' attribute

static int
TPARALLEL\_FEATURE\_COUNT
The number of structural features of the 'TParallel' class

static int
TPORTAL\_CLIENT\_SETTINGS
The meta object id for the 'TPortal Client Settings' class

static int
TPORTAL\_CLIENT\_SETTINGS\_\_CLIENT\_TYPE
The feature id for the 'Client Type' attribute

static int
TPORTAL\_CLIENT\_SETTINGS\_\_CUSTOM\_SETTING
The feature id for the 'Custom Setting' containment reference list

static int
TPORTAL\_CLIENT\_SETTINGS\_FEATURE\_COUNT
The number of structural features of the 'TPortal Client Settings' class

static int
TPOTENTIAL\_INSTANCE\_CREATOR
The meta object id for the 'TPotential Instance Creator' class

static int
TPOTENTIAL\_INSTANCE\_CREATOR\_\_VERB
The feature id for the 'Verb' containment reference

static int
TPOTENTIAL\_INSTANCE\_CREATOR\_FEATURE\_COUNT
The number of structural features of the 'TPotential Instance Creator' class

static int
TPOTENTIAL\_OWNER
The meta object id for the 'TPotential Owner' class

static int
TPOTENTIAL\_OWNER\_\_PARALLEL
The feature id for the 'Parallel' containment reference

static int
TPOTENTIAL\_OWNER\_\_VERB
The feature id for the 'Verb' containment reference

static int
TPOTENTIAL\_OWNER\_FEATURE\_COUNT
The number of structural features of the 'TPotential Owner' class

static int
TPOTENTIAL\_STARTER
The meta object id for the 'TPotential Starter' class

static int
TPOTENTIAL\_STARTER\_\_VERB
The feature id for the 'Verb' containment reference

static int
TPOTENTIAL\_STARTER\_FEATURE\_COUNT
The number of structural features of the 'TPotential Starter' class

static int
TREADER
The meta object id for the 'TReader' class

static int
TREADER\_\_VERB
The feature id for the 'Verb' containment reference

static int
TREADER\_FEATURE\_COUNT
The number of structural features of the 'TReader' class

static int
TRESULT
The meta object id for the 'TResult' class

static int
TRESULT\_\_AGGREGATE
The feature id for the 'Aggregate' containment reference list

static int
TRESULT\_FEATURE\_COUNT
The number of structural features of the 'TResult' class

static int
TSTAFF\_ROLE
The meta object id for the 'TStaff Role' class

static int
TSTAFF\_ROLE\_\_VERB
The feature id for the 'Verb' containment reference

static int
TSTAFF\_ROLE\_FEATURE\_COUNT
The number of structural features of the 'TStaff Role' class

static int
TSTAFF\_SETTINGS
The meta object id for the 'TStaff Settings' class

static int
TSTAFF\_SETTINGS\_\_ADMINISTRATOR
The feature id for the 'Administrator' containment reference

static int
TSTAFF\_SETTINGS\_\_CONTACT\_QUERY
The feature id for the 'Contact Query' containment reference list

static int
TSTAFF\_SETTINGS\_\_EDITOR
The feature id for the 'Editor' containment reference

static int
TSTAFF\_SETTINGS\_\_INHERITED\_AUTHORIZATION
The feature id for the 'Inherited Authorization' attribute

static int
TSTAFF\_SETTINGS\_\_POTENTIAL\_INSTANCE\_CREATOR
The feature id for the 'Potential Instance Creator' containment reference

static int
TSTAFF\_SETTINGS\_\_POTENTIAL\_OWNER
The feature id for the 'Potential Owner' containment reference

static int
TSTAFF\_SETTINGS\_\_POTENTIAL\_STARTER
The feature id for the 'Potential Starter' containment reference

static int
TSTAFF\_SETTINGS\_\_READER
The feature id for the 'Reader' containment reference

static int
TSTAFF\_SETTINGS\_FEATURE\_COUNT
The number of structural features of the 'TStaff Settings' class

static int
TSUBSTITUTION\_KINDS
The meta object id for the 'TSubstitution Kinds' enum

static int
TSUBSTITUTION\_KINDS\_OBJECT
The meta object id for the 'TSubstitution Kinds Object' data type

static int
TTASK
The meta object id for the 'TTask' class

static int
TTASK\_\_ALLOW\_CLAIM\_WHEN\_SUSPENDED
The feature id for the 'Allow Claim When Suspended' attribute

static int
TTASK\_\_APPLICATION\_DEFAULTS\_COMPONENT\_NAME
The feature id for the 'Application Defaults Component Name' attribute

static int
TTASK\_\_AUTO\_CLAIM
The feature id for the 'Auto Claim' attribute

static int
TTASK\_\_AUTO\_DELETION\_MODE
The feature id for the 'Auto Deletion Mode' attribute

static int
TTASK\_\_AUTONOMY
The feature id for the 'Autonomy' attribute

static int
TTASK\_\_BUSINESS\_RELEVANCE
The feature id for the 'Business Relevance' attribute

static int
TTASK\_\_CALENDAR\_JNDI\_NAME
The feature id for the 'Calendar JNDI Name' attribute

static int
TTASK\_\_CALENDAR\_NAME
The feature id for the 'Calendar Name' attribute

static int
TTASK\_\_CONTAINMENT\_CONTEXT\_COMPONENT\_NAME
The feature id for the 'Containment Context Component Name' attribute

static int
TTASK\_\_CONTEXT\_AUTHORIZATION\_FOR\_OWNER
The feature id for the 'Context Authorization For Owner' attribute

static int
TTASK\_\_CUSTOM\_PROPERTY
The feature id for the 'Custom Property' containment reference list

static int
TTASK\_\_DEFAULT\_LOCALE
The feature id for the 'Default Locale' attribute

static int
TTASK\_\_DESCRIPTION
The feature id for the 'Description' containment reference list

static int
TTASK\_\_DISPLAY\_NAME
The feature id for the 'Display Name' containment reference list

static int
TTASK\_\_DOCUMENTATION
The feature id for the 'Documentation' containment reference list

static int
TTASK\_\_DURATION\_UNTIL\_DELETED
The feature id for the 'Duration Until Deleted' attribute

static int
TTASK\_\_DURATION\_UNTIL\_DUE
The feature id for the 'Duration Until Due' attribute

static int
TTASK\_\_DURATION\_UNTIL\_EXPIRES
The feature id for the 'Duration Until Expires' attribute

static int
TTASK\_\_EMAIL
The feature id for the 'Email' containment reference list

static int
TTASK\_\_ESCALATION\_SETTINGS
The feature id for the 'Escalation Settings' containment reference

static int
TTASK\_\_EVENT\_HANDLER\_NAME
The feature id for the 'Event Handler Name' attribute

static int
TTASK\_\_IMPORT
The feature id for the 'Import' containment reference

static int
TTASK\_\_INTERFACE
The feature id for the 'Interface' containment reference

static int
TTASK\_\_JNDI\_NAME\_STAFF\_PLUGIN\_PROVIDER
The feature id for the 'Jndi Name Staff Plugin Provider' attribute

static int
TTASK\_\_KIND
The feature id for the 'Kind' attribute

static int
TTASK\_\_NAME
The feature id for the 'Name' attribute

static int
TTASK\_\_PRIORITY
The feature id for the 'Priority' attribute

static int
TTASK\_\_PRIORITY\_DEFINITION
The feature id for the 'Priority Definition' attribute

static int
TTASK\_\_STAFF\_SETTINGS
The feature id for the 'Staff Settings' containment reference

static int
TTASK\_\_SUBSTITUTION\_POLICY
The feature id for the 'Substitution Policy' attribute

static int
TTASK\_\_SUPPORTS\_DELEGATION
The feature id for the 'Supports Delegation' attribute

static int
TTASK\_\_SUPPORTS\_FOLLOW\_ON\_TASK
The feature id for the 'Supports Follow On Task' attribute

static int
TTASK\_\_SUPPORTS\_SUB\_TASK
The feature id for the 'Supports Sub Task' attribute

static int
TTASK\_\_TARGET\_NAMESPACE
The feature id for the 'Target Namespace' attribute

static int
TTASK\_\_TYPE
The feature id for the 'Type' attribute

static int
TTASK\_\_UI\_SETTINGS
The feature id for the 'Ui Settings' containment reference

static int
TTASK\_\_VALID\_FROM
The feature id for the 'Valid From' attribute

static int
TTASK\_\_WORK\_BASKET
The feature id for the 'Work Basket' attribute

static int
TTASK\_FEATURE\_COUNT
The number of structural features of the 'TTask' class

static int
TTASK\_KINDS
The meta object id for the 'TTask Kinds' enum

static int
TTASK\_KINDS\_OBJECT
The meta object id for the 'TTask Kinds Object' data type

static int
TTEXT1024
The meta object id for the 'TText1024' data type

static int
TTEXT254
The meta object id for the 'TText254' data type

static int
TTEXT4096
The meta object id for the 'TText4096' data type

static int
TTEXT64
The meta object id for the 'TText64' data type

static int
TUI\_SETTINGS
The meta object id for the 'TUI Settings' class

static int
TUI\_SETTINGS\_\_CUSTOM\_CLIENT\_SETTINGS
The feature id for the 'Custom Client Settings' containment reference list

static int
TUI\_SETTINGS\_\_PORTAL\_CLIENT\_SETTINGS
The feature id for the 'Portal Client Settings' containment reference list

static int
TUI\_SETTINGS\_\_WEB\_CLIENT\_SETTINGS
The feature id for the 'Web Client Settings' containment reference list

static int
TUI\_SETTINGS\_FEATURE\_COUNT
The number of structural features of the 'TUI Settings' class

static int
TVERB
The meta object id for the 'TVerb' class

static int
TVERB\_\_NAME
The feature id for the 'Name' attribute

static int
TVERB\_\_PARAMETER
The feature id for the 'Parameter' containment reference list

static int
TVERB\_FEATURE\_COUNT
The number of structural features of the 'TVerb' class

static int
TWEB\_CLIENT\_SETTINGS
The meta object id for the 'TWeb Client Settings' class

static int
TWEB\_CLIENT\_SETTINGS\_\_CLIENT\_TYPE
The feature id for the 'Client Type' attribute

static int
TWEB\_CLIENT\_SETTINGS\_\_CUSTOM\_SETTING
The feature id for the 'Custom Setting' containment reference list

static int
TWEB\_CLIENT\_SETTINGS\_\_JSP
The feature id for the 'Jsp' containment reference list

static int
TWEB\_CLIENT\_SETTINGS\_FEATURE\_COUNT
The number of structural features of the 'TWeb Client Settings' class

static int
TYPE\_UNION
The meta object id for the 'Type Union' data type

- Method Summary Methods Modifier and Type Method and Description org.eclipse.emf.ecore.EAttribute getDocumentRoot\_Mixed () Returns the meta object for the attribute list 'Mixed ' org.eclipse.emf.ecore.EReference getDocumentRoot\_Task () Returns the meta object for the containment reference 'Task ' org.eclipse.emf.ecore.EReference getDocumentRoot\_XMLNSPrefixMap () Returns the meta object for the map 'XMLNS Prefix Map ' org.eclipse.emf.ecore.EReference getDocumentRoot\_XSISchemaLocation () Returns the meta object for the map 'XSI Schema Location ' org.eclipse.emf.ecore.EClass getDocumentRoot () Returns the meta object for class 'Document Root ' org.eclipse.emf.ecore.EDataType geteQName () Returns the meta object for data type 'eQ Name ' org.eclipse.emf.ecore.EDataType geteURI () Returns the meta object for data type 'eURI ' org.eclipse.emf.ecore.EAttribute getParameterType\_Id () Returns the meta object for the attribute 'Id ' org.eclipse.emf.ecore.EAttribute getParameterType\_Value () Returns the meta object for the attribute 'Value ' org.eclipse.emf.ecore.EClass getParameterType () Returns the meta object for class 'Parameter Type ' org.eclipse.emf.ecore.EEnum getTActivationStates () Returns the meta object for enum 'TActivation States ' org.eclipse.emf.ecore.EDataType getTActivationStatesObject () Returns the meta object for data type 'TActivation States Object ' org.eclipse.emf.ecore.EClass getTAdministrator () Returns the meta object for class 'TAdministrator ' org.eclipse.emf.ecore.EAttribute getTAggregate\_Condition () Returns the meta object for the attribute 'Condition ' org.eclipse.emf.ecore.EAttribute getTAggregate\_Function () Returns the meta object for the attribute 'Function ' org.eclipse.emf.ecore.EAttribute getTAggregate\_Location () Returns the meta object for the attribute 'Location ' org.eclipse.emf.ecore.EAttribute getTAggregate\_Part () Returns the meta object for the attribute 'Part ' org.eclipse.emf.ecore.EClass getTAggregate () Returns the meta object for class 'TAggregate ' org.eclipse.emf.ecore.EAttribute getTApplyTo\_Role () Returns the meta object for the attribute 'Role ' org.eclipse.emf.ecore.EClass getTApplyTo () Returns the meta object for class 'TApply To ' TaskFactory getTaskFactory () Returns the factory that creates the instances of the model org.eclipse.emf.ecore.EEnum getTAtLeastExpectedStates () Returns the meta object for enum 'TAt Least Expected States ' org.eclipse.emf.ecore.EDataType getTAtLeastExpectedStatesObject () Returns the meta object for data type 'TAt Least Expected States Object ' org.eclipse.emf.ecore.EEnum getTAutoDeletionMode () Returns the meta object for enum 'TAuto Deletion Mode ' org.eclipse.emf.ecore.EDataType getTAutoDeletionModeObject () Returns the meta object for data type 'TAuto Deletion Mode Object ' org.eclipse.emf.ecore.EEnum getTAutonomy () Returns the meta object for enum 'TAutonomy ' org.eclipse.emf.ecore.EDataType getTAutonomyObject () Returns the meta object for data type 'TAutonomy Object ' org.eclipse.emf.ecore.EEnum getTBoolean () Returns the meta object for enum 'TBoolean ' org.eclipse.emf.ecore.EDataType getTBooleanObject () Returns the meta object for data type 'TBoolean Object ' org.eclipse.emf.ecore.EReference getTCompletion\_Criterion () Returns the meta object for the containment reference 'Criterion ' org.eclipse.emf.ecore.EAttribute getTCompletion\_Name () Returns the meta object for the attribute 'Name ' org.eclipse.emf.ecore.EReference getTCompletion\_Result () Returns the meta object for the containment reference 'Result ' org.eclipse.emf.ecore.EAttribute getTCompletion\_UseDefaultResultConstruction () Returns the meta object for the attribute 'Use Default Result Construction ' org.eclipse.emf.ecore.EClass getTCompletion () Returns the meta object for class 'TCompletion ' org.eclipse.emf.ecore.EReference getTCompletionBehavior\_Completion () Returns the meta object for the containment reference list 'Completion ' org.eclipse.emf.ecore.EReference getTCompletionBehavior\_DefaultCompletion () Returns the meta object for the containment reference 'Default Completion ' org.eclipse.emf.ecore.EClass getTCompletionBehavior () Returns the meta object for class 'TCompletion Behavior ' org.eclipse.emf.ecore.EAttribute getTContactQuery\_Category () Returns the meta object for the attribute 'Category ' org.eclipse.emf.ecore.EClass getTContactQuery () Returns the meta object for class 'TContact Query ' org.eclipse.emf.ecore.EEnum getTContextAuthorizationForOwner () Returns the meta object for enum 'TContext Authorization For Owner ' org.eclipse.emf.ecore.EDataType getTContextAuthorizationForOwnerObject () Returns the meta object for data type 'TContext Authorization For Owner Object ' org.eclipse.emf.ecore.EAttribute getTCriterion\_Condition () Returns the meta object for the attribute 'Condition ' org.eclipse.emf.ecore.EAttribute getTCriterion\_For () Returns the meta object for the attribute 'For ' org.eclipse.emf.ecore.EClass getTCriterion () Returns the meta object for class 'TCriterion ' org.eclipse.emf.ecore.EAttribute getTCustomClientSettings\_ClientType () Returns the meta object for the attribute 'Client Type ' org.eclipse.emf.ecore.EReference getTCustomClientSettings\_CustomSetting () Returns the meta object for the containment reference list 'Custom Setting ' org.eclipse.emf.ecore.EClass getTCustomClientSettings () Returns the meta object for class 'TCustom Client Settings ' org.eclipse.emf.ecore.EAttribute getTCustomProperty\_Inline () Returns the meta object for the attribute 'Inline ' org.eclipse.emf.ecore.EAttribute getTCustomProperty\_Name () Returns the meta object for the attribute 'Name ' org.eclipse.emf.ecore.EAttribute getTCustomProperty\_Value () Returns the meta object for the attribute 'Value ' org.eclipse.emf.ecore.EClass getTCustomProperty () Returns the meta object for class 'TCustom Property ' org.eclipse.emf.ecore.EAttribute getTCustomSetting\_Name () Returns the meta object for the attribute 'Name ' org.eclipse.emf.ecore.EAttribute getTCustomSetting\_Value () Returns the meta object for the attribute 'Value ' org.eclipse.emf.ecore.EClass getTCustomSetting () Returns the meta object for class 'TCustom Setting ' org.eclipse.emf.ecore.EReference getTDefaultCompletion\_Result () Returns the meta object for the containment reference 'Result ' org.eclipse.emf.ecore.EClass getTDefaultCompletion () Returns the meta object for class 'TDefault Completion ' org.eclipse.emf.ecore.EAttribute getTDescription\_Locale () Returns the meta object for the attribute 'Locale ' org.eclipse.emf.ecore.EAttribute getTDescription\_Value () Returns the meta object for the attribute 'Value ' org.eclipse.emf.ecore.EClass getTDescription () Returns the meta object for class 'TDescription ' org.eclipse.emf.ecore.EAttribute getTDisplayName\_Locale () Returns the meta object for the attribute 'Locale ' org.eclipse.emf.ecore.EAttribute getTDisplayName\_Value () Returns the meta object for the attribute 'Value ' org.eclipse.emf.ecore.EClass getTDisplayName () Returns the meta object for class 'TDisplay Name ' org.eclipse.emf.ecore.EAttribute getTDocumentation\_Locale () Returns the meta object for the attribute 'Locale ' org.eclipse.emf.ecore.EAttribute getTDocumentation\_Value () Returns the meta object for the attribute 'Value ' org.eclipse.emf.ecore.EClass getTDocumentation () Returns the meta object for class 'TDocumentation ' org.eclipse.emf.ecore.EEnum getTDurationConstants () Returns the meta object for enum 'TDuration Constants ' org.eclipse.emf.ecore.EDataType getTDurationConstantsObject () Returns the meta object for data type 'TDuration Constants Object ' org.eclipse.emf.ecore.EClass getTEditor () Returns the meta object for class 'TEditor ' org.eclipse.emf.ecore.EReference getTEmail\_LocalizedEmail () Returns the meta object for the containment reference list 'Localized Email ' org.eclipse.emf.ecore.EAttribute getTEmail\_Name () Returns the meta object for the attribute 'Name ' org.eclipse.emf.ecore.EClass getTEmail () Returns the meta object for class 'TEmail ' org.eclipse.emf.ecore.EClass getTEMailReceiver () Returns the meta object for class 'TE Mail Receiver ' org.eclipse.emf.ecore.EAttribute getTEscalation\_AtLeastExpectedState () Returns the meta object for the attribute 'At Least Expected State ' org.eclipse.emf.ecore.EAttribute getTEscalation\_AutoRepeatDuration () Returns the meta object for the attribute 'Auto Repeat Duration ' org.eclipse.emf.ecore.EReference getTEscalation\_CustomProperty () Returns the meta object for the containment reference list 'Custom Property ' org.eclipse.emf.ecore.EReference getTEscalation\_Description () Returns the meta object for the containment reference list 'Description ' org.eclipse.emf.ecore.EReference getTEscalation\_DisplayName () Returns the meta object for the containment reference list 'Display Name ' org.eclipse.emf.ecore.EReference getTEscalation\_Documentation () Returns the meta object for the containment reference list 'Documentation ' org.eclipse.emf.ecore.EAttribute getTEscalation\_DurationUntilEscalation () Returns the meta object for the attribute 'Duration Until Escalation ' org.eclipse.emf.ecore.EAttribute getTEscalation\_Email () Returns the meta object for the attribute 'Email ' org.eclipse.emf.ecore.EReference getTEscalation\_EMailReceiver () Returns the meta object for the containment reference 'EMail Receiver ' org.eclipse.emf.ecore.EAttribute getTEscalation\_EscalationAction () Returns the meta object for the attribute 'Escalation Action ' org.eclipse.emf.ecore.EReference getTEscalation\_EscalationReceiver () Returns the meta object for the containment reference 'Escalation Receiver ' org.eclipse.emf.ecore.EAttribute getTEscalation\_IncreasePriority () Returns the meta object for the attribute 'Increase Priority ' org.eclipse.emf.ecore.EAttribute getTEscalation\_Name () Returns the meta object for the attribute 'Name ' org.eclipse.emf.ecore.EClass getTEscalation () Returns the meta object for class 'TEscalation ' org.eclipse.emf.ecore.EEnum getTEscalationActions () Returns the meta object for enum 'TEscalation Actions ' org.eclipse.emf.ecore.EDataType getTEscalationActionsObject () Returns the meta object for data type 'TEscalation Actions Object ' org.eclipse.emf.ecore.EAttribute getTEscalationChain\_ActivationState () Returns the meta object for the attribute 'Activation State ' org.eclipse.emf.ecore.EReference getTEscalationChain\_Escalation () Returns the meta object for the containment reference list 'Escalation ' org.eclipse.emf.ecore.EClass getTEscalationChain () Returns the meta object for class 'TEscalation Chain ' org.eclipse.emf.ecore.EClass getTEscalationReceiver () Returns the meta object for class 'TEscalation Receiver ' org.eclipse.emf.ecore.EReference getTEscalationSettings\_EscalationChain () Returns the meta object for the containment reference list 'Escalation Chain ' org.eclipse.emf.ecore.EClass getTEscalationSettings () Returns the meta object for class 'TEscalation Settings ' org.eclipse.emf.ecore.EAttribute getTImport\_ImportType () Returns the meta object for the attribute 'Import Type ' org.eclipse.emf.ecore.EAttribute getTImport\_Location () Returns the meta object for the attribute 'Location ' org.eclipse.emf.ecore.EAttribute getTImport\_Namespace () Returns the meta object for the attribute 'Namespace ' org.eclipse.emf.ecore.EClass getTImport () Returns the meta object for class 'TImport ' org.eclipse.emf.ecore.EEnum getTIncreasePriority () Returns the meta object for enum 'TIncrease Priority ' org.eclipse.emf.ecore.EDataType getTIncreasePriorityObject () Returns the meta object for data type 'TIncrease Priority Object ' org.eclipse.emf.ecore.EEnum getTInheritedAuthorization () Returns the meta object for enum 'TInherited Authorization ' org.eclipse.emf.ecore.EDataType getTInheritedAuthorizationObject () Returns the meta object for data type 'TInherited Authorization Object ' org.eclipse.emf.ecore.EEnum getTInlineCustomPropertyEnum () Returns the meta object for enum 'TInline Custom Property Enum ' org.eclipse.emf.ecore.EDataType getTInlineCustomPropertyEnumObject () Returns the meta object for data type 'TInline Custom Property Enum Object ' org.eclipse.emf.ecore.EAttribute getTInterface\_Kind () Returns the meta object for the attribute 'Kind ' org.eclipse.emf.ecore.EAttribute getTInterface\_Operation () Returns the meta object for the attribute 'Operation ' org.eclipse.emf.ecore.EAttribute getTInterface\_PortType () Returns the meta object for the attribute 'Port Type ' org.eclipse.emf.ecore.EClass getTInterface () Returns the meta object for class 'TInterface ' org.eclipse.emf.ecore.EEnum getTInterfaceKinds () Returns the meta object for enum 'TInterface Kinds ' org.eclipse.emf.ecore.EDataType getTInterfaceKindsObject () Returns the meta object for data type 'TInterface Kinds Object ' org.eclipse.emf.ecore.EReference getTJSP\_ApplyTo () Returns the meta object for the containment reference list 'Apply To ' org.eclipse.emf.ecore.EAttribute getTJSP\_ContextRoot () Returns the meta object for the attribute 'Context Root ' org.eclipse.emf.ecore.EAttribute getTJSP\_FaultQName () Returns the meta object for the attribute 'Fault QName ' org.eclipse.emf.ecore.EAttribute getTJSP\_For () Returns the meta object for the attribute 'For ' org.eclipse.emf.ecore.EAttribute getTJSP\_Uri () Returns the meta object for the attribute 'Uri ' org.eclipse.emf.ecore.EClass getTJSP () Returns the meta object for class 'TJSP ' org.eclipse.emf.ecore.EEnum getTJspApplicableRole () Returns the meta object for enum 'TJsp Applicable Role ' org.eclipse.emf.ecore.EDataType getTJspApplicableRoleObject () Returns the meta object for data type 'TJsp Applicable Role Object ' org.eclipse.emf.ecore.EEnum getTJspUsagePattern () Returns the meta object for enum 'TJsp Usage Pattern ' org.eclipse.emf.ecore.EDataType getTJspUsagePatternObject () Returns the meta object for data type 'TJsp Usage Pattern Object ' org.eclipse.emf.ecore.EDataType getTLanguage () Returns the meta object for data type 'TLanguage ' org.eclipse.emf.ecore.EAttribute getTLocalizedEmail\_Body () Returns the meta object for the attribute 'Body ' org.eclipse.emf.ecore.EAttribute getTLocalizedEmail\_Locale () Returns the meta object for the attribute 'Locale ' org.eclipse.emf.ecore.EAttribute getTLocalizedEmail\_Subject () Returns the meta object for the attribute 'Subject ' org.eclipse.emf.ecore.EClass getTLocalizedEmail () Returns the meta object for class 'TLocalized Email ' org.eclipse.emf.ecore.EDataType getTNonNegativeInt () Returns the meta object for data type 'TNon Negative Int ' org.eclipse.emf.ecore.EDataType getTNonNegativeIntObject () Returns the meta object for data type 'TNon Negative Int Object ' org.eclipse.emf.ecore.EReference getTParallel\_CompletionBehavior () Returns the meta object for the containment reference 'Completion Behavior ' org.eclipse.emf.ecore.EAttribute getTParallel\_InheritedAuthorization () Returns the meta object for the attribute 'Inherited Authorization ' org.eclipse.emf.ecore.EClass getTParallel () Returns the meta object for class 'TParallel ' org.eclipse.emf.ecore.EClass getTPortalClientSettings () Returns the meta object for class 'TPortal Client Settings ' org.eclipse.emf.ecore.EClass getTPotentialInstanceCreator () Returns the meta object for class 'TPotential Instance Creator ' org.eclipse.emf.ecore.EReference getTPotentialOwner\_Parallel () Returns the meta object for the containment reference 'Parallel ' org.eclipse.emf.ecore.EClass getTPotentialOwner () Returns the meta object for class 'TPotential Owner ' org.eclipse.emf.ecore.EClass getTPotentialStarter () Returns the meta object for class 'TPotential Starter ' org.eclipse.emf.ecore.EClass getTReader () Returns the meta object for class 'TReader ' org.eclipse.emf.ecore.EReference getTResult\_Aggregate () Returns the meta object for the containment reference list 'Aggregate ' org.eclipse.emf.ecore.EClass getTResult () Returns the meta object for class 'TResult ' org.eclipse.emf.ecore.EReference getTStaffRole\_Verb () Returns the meta object for the containment reference 'Verb ' org.eclipse.emf.ecore.EClass getTStaffRole () Returns the meta object for class 'TStaff Role ' org.eclipse.emf.ecore.EReference getTStaffSettings\_Administrator () Returns the meta object for the containment reference 'Administrator ' org.eclipse.emf.ecore.EReference getTStaffSettings\_ContactQuery () Returns the meta object for the containment reference list 'Contact Query ' org.eclipse.emf.ecore.EReference getTStaffSettings\_Editor () Returns the meta object for the containment reference 'Editor ' org.eclipse.emf.ecore.EAttribute getTStaffSettings\_InheritedAuthorization () Returns the meta object for the attribute 'Inherited Authorization ' org.eclipse.emf.ecore.EReference getTStaffSettings\_PotentialInstanceCreator () Returns the meta object for the containment reference 'Potential Instance Creator ' org.eclipse.emf.ecore.EReference getTStaffSettings\_PotentialOwner () Returns the meta object for the containment reference 'Potential Owner ' org.eclipse.emf.ecore.EReference getTStaffSettings\_PotentialStarter () Returns the meta object for the containment reference 'Potential Starter ' org.eclipse.emf.ecore.EReference getTStaffSettings\_Reader () Returns the meta object for the containment reference 'Reader ' org.eclipse.emf.ecore.EClass getTStaffSettings () Returns the meta object for class 'TStaff Settings ' org.eclipse.emf.ecore.EEnum getTSubstitutionKinds () Returns the meta object for enum 'TSubstitution Kinds ' org.eclipse.emf.ecore.EDataType getTSubstitutionKindsObject () Returns the meta object for data type 'TSubstitution Kinds Object ' org.eclipse.emf.ecore.EAttribute getTTask\_AllowClaimWhenSuspended () Returns the meta object for the attribute 'Allow Claim When Suspended ' org.eclipse.emf.ecore.EAttribute getTTask\_ApplicationDefaultsComponentName () Returns the meta object for the attribute 'Application Defaults Component Name ' org.eclipse.emf.ecore.EAttribute getTTask\_AutoClaim () Returns the meta object for the attribute 'Auto Claim ' org.eclipse.emf.ecore.EAttribute getTTask\_AutoDeletionMode () Returns the meta object for the attribute 'Auto Deletion Mode ' org.eclipse.emf.ecore.EAttribute getTTask\_Autonomy () Returns the meta object for the attribute 'Autonomy ' org.eclipse.emf.ecore.EAttribute getTTask\_BusinessRelevance () Returns the meta object for the attribute 'Business Relevance ' org.eclipse.emf.ecore.EAttribute getTTask\_CalendarJNDIName () Returns the meta object for the attribute 'Calendar JNDI Name ' org.eclipse.emf.ecore.EAttribute getTTask\_CalendarName () Returns the meta object for the attribute 'Calendar Name ' org.eclipse.emf.ecore.EAttribute getTTask\_ContainmentContextComponentName () Returns the meta object for the attribute 'Containment Context Component Name ' org.eclipse.emf.ecore.EAttribute getTTask\_ContextAuthorizationForOwner () Returns the meta object for the attribute 'Context Authorization For Owner ' org.eclipse.emf.ecore.EReference getTTask\_CustomProperty () Returns the meta object for the containment reference list 'Custom Property ' org.eclipse.emf.ecore.EAttribute getTTask\_DefaultLocale () Returns the meta object for the attribute 'Default Locale ' org.eclipse.emf.ecore.EReference getTTask\_Description () Returns the meta object for the containment reference list 'Description ' org.eclipse.emf.ecore.EReference getTTask\_DisplayName () Returns the meta object for the containment reference list 'Display Name ' org.eclipse.emf.ecore.EReference getTTask\_Documentation () Returns the meta object for the containment reference list 'Documentation ' org.eclipse.emf.ecore.EAttribute getTTask\_DurationUntilDeleted () Returns the meta object for the attribute 'Duration Until Deleted ' org.eclipse.emf.ecore.EAttribute getTTask\_DurationUntilDue () Returns the meta object for the attribute 'Duration Until Due ' org.eclipse.emf.ecore.EAttribute getTTask\_DurationUntilExpires () Returns the meta object for the attribute 'Duration Until Expires ' org.eclipse.emf.ecore.EReference getTTask\_Email () Returns the meta object for the containment reference list 'Email ' org.eclipse.emf.ecore.EReference getTTask\_EscalationSettings () Returns the meta object for the containment reference 'Escalation Settings ' org.eclipse.emf.ecore.EAttribute getTTask\_EventHandlerName () Returns the meta object for the attribute 'Event Handler Name ' org.eclipse.emf.ecore.EReference getTTask\_Import () Returns the meta object for the containment reference 'Import ' org.eclipse.emf.ecore.EReference getTTask\_Interface () Returns the meta object for the containment reference 'Interface ' org.eclipse.emf.ecore.EAttribute getTTask\_JndiNameStaffPluginProvider () Returns the meta object for the attribute 'Jndi Name Staff Plugin Provider ' org.eclipse.emf.ecore.EAttribute getTTask\_Kind () Returns the meta object for the attribute 'Kind ' org.eclipse.emf.ecore.EAttribute getTTask\_Name () Returns the meta object for the attribute 'Name ' org.eclipse.emf.ecore.EAttribute getTTask\_Priority () Returns the meta object for the attribute 'Priority ' org.eclipse.emf.ecore.EAttribute getTTask\_PriorityDefinition () Returns the meta object for the attribute 'Priority Definition ' org.eclipse.emf.ecore.EReference getTTask\_StaffSettings () Returns the meta object for the containment reference 'Staff Settings ' org.eclipse.emf.ecore.EAttribute getTTask\_SubstitutionPolicy () Returns the meta object for the attribute 'Substitution Policy ' org.eclipse.emf.ecore.EAttribute getTTask\_SupportsDelegation () Returns the meta object for the attribute 'Supports Delegation ' org.eclipse.emf.ecore.EAttribute getTTask\_SupportsFollowOnTask () Returns the meta object for the attribute 'Supports Follow On Task ' org.eclipse.emf.ecore.EAttribute getTTask\_SupportsSubTask () Returns the meta object for the attribute 'Supports Sub Task ' org.eclipse.emf.ecore.EAttribute getTTask\_TargetNamespace () Returns the meta object for the attribute 'Target Namespace ' org.eclipse.emf.ecore.EAttribute getTTask\_Type () Returns the meta object for the attribute 'Type ' org.eclipse.emf.ecore.EReference getTTask\_UiSettings () Returns the meta object for the containment reference 'Ui Settings ' org.eclipse.emf.ecore.EAttribute getTTask\_ValidFrom () Returns the meta object for the attribute 'Valid From ' org.eclipse.emf.ecore.EAttribute getTTask\_WorkBasket () Returns the meta object for the attribute 'Work Basket ' org.eclipse.emf.ecore.EClass getTTask () Returns the meta object for class 'TTask ' org.eclipse.emf.ecore.EEnum getTTaskKinds () Returns the meta object for enum 'TTask Kinds ' org.eclipse.emf.ecore.EDataType getTTaskKindsObject () Returns the meta object for data type 'TTask Kinds Object ' org.eclipse.emf.ecore.EDataType getTText1024 () Returns the meta object for data type 'TText1024 ' org.eclipse.emf.ecore.EDataType getTText254 () Returns the meta object for data type 'TText254 ' org.eclipse.emf.ecore.EDataType getTText4096 () Returns the meta object for data type 'TText4096 ' org.eclipse.emf.ecore.EDataType getTText64 () Returns the meta object for data type 'TText64 ' org.eclipse.emf.ecore.EReference getTUISettings\_CustomClientSettings () Returns the meta object for the containment reference list 'Custom Client Settings ' org.eclipse.emf.ecore.EReference getTUISettings\_PortalClientSettings () Returns the meta object for the containment reference list 'Portal Client Settings ' org.eclipse.emf.ecore.EReference getTUISettings\_WebClientSettings () Returns the meta object for the containment reference list 'Web Client Settings ' org.eclipse.emf.ecore.EClass getTUISettings () Returns the meta object for class 'TUI Settings ' org.eclipse.emf.ecore.EAttribute getTVerb\_Name () Returns the meta object for the attribute 'Name ' org.eclipse.emf.ecore.EReference getTVerb\_Parameter () Returns the meta object for the containment reference list 'Parameter ' org.eclipse.emf.ecore.EClass getTVerb () Returns the meta object for class 'TVerb ' org.eclipse.emf.ecore.EReference getTWebClientSettings\_Jsp () Returns the meta object for the containment reference list 'Jsp ' org.eclipse.emf.ecore.EClass getTWebClientSettings () Returns the meta object for class 'TWeb Client Settings ' org.eclipse.emf.ecore.EDataType getTypeUnion () Returns the meta object for data type 'Type Union '

### Method Summary

| Modifier and Type                | Method and Description                                                                                                          |
|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| org.eclipse.emf.ecore.EAttribute | getDocumentRoot\_Mixed() Returns the meta object for the attribute list 'Mixed'                                                  |
| org.eclipse.emf.ecore.EReference | getDocumentRoot\_Task() Returns the meta object for the containment reference 'Task'                                             |
| org.eclipse.emf.ecore.EReference | getDocumentRoot\_XMLNSPrefixMap() Returns the meta object for the map 'XMLNS Prefix Map'                                         |
| org.eclipse.emf.ecore.EReference | getDocumentRoot\_XSISchemaLocation() Returns the meta object for the map 'XSI Schema Location'                                   |
| org.eclipse.emf.ecore.EClass     | getDocumentRoot() Returns the meta object for class 'Document Root'                                                             |
| org.eclipse.emf.ecore.EDataType  | geteQName() Returns the meta object for data type 'eQ Name'                                                                     |
| org.eclipse.emf.ecore.EDataType  | geteURI() Returns the meta object for data type 'eURI'                                                                          |
| org.eclipse.emf.ecore.EAttribute | getParameterType\_Id() Returns the meta object for the attribute 'Id'                                                            |
| org.eclipse.emf.ecore.EAttribute | getParameterType\_Value() Returns the meta object for the attribute 'Value'                                                      |
| org.eclipse.emf.ecore.EClass     | getParameterType() Returns the meta object for class 'Parameter Type'                                                           |
| org.eclipse.emf.ecore.EEnum      | getTActivationStates() Returns the meta object for enum 'TActivation States'                                                    |
| org.eclipse.emf.ecore.EDataType  | getTActivationStatesObject() Returns the meta object for data type 'TActivation States Object'                                  |
| org.eclipse.emf.ecore.EClass     | getTAdministrator() Returns the meta object for class 'TAdministrator'                                                          |
| org.eclipse.emf.ecore.EAttribute | getTAggregate\_Condition() Returns the meta object for the attribute 'Condition'                                                 |
| org.eclipse.emf.ecore.EAttribute | getTAggregate\_Function() Returns the meta object for the attribute 'Function'                                                   |
| org.eclipse.emf.ecore.EAttribute | getTAggregate\_Location() Returns the meta object for the attribute 'Location'                                                   |
| org.eclipse.emf.ecore.EAttribute | getTAggregate\_Part() Returns the meta object for the attribute 'Part'                                                           |
| org.eclipse.emf.ecore.EClass     | getTAggregate() Returns the meta object for class 'TAggregate'                                                                  |
| org.eclipse.emf.ecore.EAttribute | getTApplyTo\_Role() Returns the meta object for the attribute 'Role'                                                             |
| org.eclipse.emf.ecore.EClass     | getTApplyTo() Returns the meta object for class 'TApply To'                                                                     |
| TaskFactory                      | getTaskFactory() Returns the factory that creates the instances of the model                                                    |
| org.eclipse.emf.ecore.EEnum      | getTAtLeastExpectedStates() Returns the meta object for enum 'TAt Least Expected States'                                        |
| org.eclipse.emf.ecore.EDataType  | getTAtLeastExpectedStatesObject() Returns the meta object for data type 'TAt Least Expected States Object'                      |
| org.eclipse.emf.ecore.EEnum      | getTAutoDeletionMode() Returns the meta object for enum 'TAuto Deletion Mode'                                                   |
| org.eclipse.emf.ecore.EDataType  | getTAutoDeletionModeObject() Returns the meta object for data type 'TAuto Deletion Mode Object'                                 |
| org.eclipse.emf.ecore.EEnum      | getTAutonomy() Returns the meta object for enum 'TAutonomy'                                                                     |
| org.eclipse.emf.ecore.EDataType  | getTAutonomyObject() Returns the meta object for data type 'TAutonomy Object'                                                   |
| org.eclipse.emf.ecore.EEnum      | getTBoolean() Returns the meta object for enum 'TBoolean'                                                                       |
| org.eclipse.emf.ecore.EDataType  | getTBooleanObject() Returns the meta object for data type 'TBoolean Object'                                                     |
| org.eclipse.emf.ecore.EReference | getTCompletion\_Criterion() Returns the meta object for the containment reference 'Criterion'                                    |
| org.eclipse.emf.ecore.EAttribute | getTCompletion\_Name() Returns the meta object for the attribute 'Name'                                                          |
| org.eclipse.emf.ecore.EReference | getTCompletion\_Result() Returns the meta object for the containment reference 'Result'                                          |
| org.eclipse.emf.ecore.EAttribute | getTCompletion\_UseDefaultResultConstruction() Returns the meta object for the attribute 'Use Default Result Construction'       |
| org.eclipse.emf.ecore.EClass     | getTCompletion() Returns the meta object for class 'TCompletion'                                                                |
| org.eclipse.emf.ecore.EReference | getTCompletionBehavior\_Completion() Returns the meta object for the containment reference list 'Completion'                     |
| org.eclipse.emf.ecore.EReference | getTCompletionBehavior\_DefaultCompletion() Returns the meta object for the containment reference 'Default Completion'           |
| org.eclipse.emf.ecore.EClass     | getTCompletionBehavior() Returns the meta object for class 'TCompletion Behavior'                                               |
| org.eclipse.emf.ecore.EAttribute | getTContactQuery\_Category() Returns the meta object for the attribute 'Category'                                                |
| org.eclipse.emf.ecore.EClass     | getTContactQuery() Returns the meta object for class 'TContact Query'                                                           |
| org.eclipse.emf.ecore.EEnum      | getTContextAuthorizationForOwner() Returns the meta object for enum 'TContext Authorization For Owner'                          |
| org.eclipse.emf.ecore.EDataType  | getTContextAuthorizationForOwnerObject() Returns the meta object for data type 'TContext Authorization For Owner Object'        |
| org.eclipse.emf.ecore.EAttribute | getTCriterion\_Condition() Returns the meta object for the attribute 'Condition'                                                 |
| org.eclipse.emf.ecore.EAttribute | getTCriterion\_For() Returns the meta object for the attribute 'For'                                                             |
| org.eclipse.emf.ecore.EClass     | getTCriterion() Returns the meta object for class 'TCriterion'                                                                  |
| org.eclipse.emf.ecore.EAttribute | getTCustomClientSettings\_ClientType() Returns the meta object for the attribute 'Client Type'                                   |
| org.eclipse.emf.ecore.EReference | getTCustomClientSettings\_CustomSetting() Returns the meta object for the containment reference list 'Custom Setting'            |
| org.eclipse.emf.ecore.EClass     | getTCustomClientSettings() Returns the meta object for class 'TCustom Client Settings'                                          |
| org.eclipse.emf.ecore.EAttribute | getTCustomProperty\_Inline() Returns the meta object for the attribute 'Inline'                                                  |
| org.eclipse.emf.ecore.EAttribute | getTCustomProperty\_Name() Returns the meta object for the attribute 'Name'                                                      |
| org.eclipse.emf.ecore.EAttribute | getTCustomProperty\_Value() Returns the meta object for the attribute 'Value'                                                    |
| org.eclipse.emf.ecore.EClass     | getTCustomProperty() Returns the meta object for class 'TCustom Property'                                                       |
| org.eclipse.emf.ecore.EAttribute | getTCustomSetting\_Name() Returns the meta object for the attribute 'Name'                                                       |
| org.eclipse.emf.ecore.EAttribute | getTCustomSetting\_Value() Returns the meta object for the attribute 'Value'                                                     |
| org.eclipse.emf.ecore.EClass     | getTCustomSetting() Returns the meta object for class 'TCustom Setting'                                                         |
| org.eclipse.emf.ecore.EReference | getTDefaultCompletion\_Result() Returns the meta object for the containment reference 'Result'                                   |
| org.eclipse.emf.ecore.EClass     | getTDefaultCompletion() Returns the meta object for class 'TDefault Completion'                                                 |
| org.eclipse.emf.ecore.EAttribute | getTDescription\_Locale() Returns the meta object for the attribute 'Locale'                                                     |
| org.eclipse.emf.ecore.EAttribute | getTDescription\_Value() Returns the meta object for the attribute 'Value'                                                       |
| org.eclipse.emf.ecore.EClass     | getTDescription() Returns the meta object for class 'TDescription'                                                              |
| org.eclipse.emf.ecore.EAttribute | getTDisplayName\_Locale() Returns the meta object for the attribute 'Locale'                                                     |
| org.eclipse.emf.ecore.EAttribute | getTDisplayName\_Value() Returns the meta object for the attribute 'Value'                                                       |
| org.eclipse.emf.ecore.EClass     | getTDisplayName() Returns the meta object for class 'TDisplay Name'                                                             |
| org.eclipse.emf.ecore.EAttribute | getTDocumentation\_Locale() Returns the meta object for the attribute 'Locale'                                                   |
| org.eclipse.emf.ecore.EAttribute | getTDocumentation\_Value() Returns the meta object for the attribute 'Value'                                                     |
| org.eclipse.emf.ecore.EClass     | getTDocumentation() Returns the meta object for class 'TDocumentation'                                                          |
| org.eclipse.emf.ecore.EEnum      | getTDurationConstants() Returns the meta object for enum 'TDuration Constants'                                                  |
| org.eclipse.emf.ecore.EDataType  | getTDurationConstantsObject() Returns the meta object for data type 'TDuration Constants Object'                                |
| org.eclipse.emf.ecore.EClass     | getTEditor() Returns the meta object for class 'TEditor'                                                                        |
| org.eclipse.emf.ecore.EReference | getTEmail\_LocalizedEmail() Returns the meta object for the containment reference list 'Localized Email'                         |
| org.eclipse.emf.ecore.EAttribute | getTEmail\_Name() Returns the meta object for the attribute 'Name'                                                               |
| org.eclipse.emf.ecore.EClass     | getTEmail() Returns the meta object for class 'TEmail'                                                                          |
| org.eclipse.emf.ecore.EClass     | getTEMailReceiver() Returns the meta object for class 'TE Mail Receiver'                                                        |
| org.eclipse.emf.ecore.EAttribute | getTEscalation\_AtLeastExpectedState() Returns the meta object for the attribute 'At Least Expected State'                       |
| org.eclipse.emf.ecore.EAttribute | getTEscalation\_AutoRepeatDuration() Returns the meta object for the attribute 'Auto Repeat Duration'                            |
| org.eclipse.emf.ecore.EReference | getTEscalation\_CustomProperty() Returns the meta object for the containment reference list 'Custom Property'                    |
| org.eclipse.emf.ecore.EReference | getTEscalation\_Description() Returns the meta object for the containment reference list 'Description'                           |
| org.eclipse.emf.ecore.EReference | getTEscalation\_DisplayName() Returns the meta object for the containment reference list 'Display Name'                          |
| org.eclipse.emf.ecore.EReference | getTEscalation\_Documentation() Returns the meta object for the containment reference list 'Documentation'                       |
| org.eclipse.emf.ecore.EAttribute | getTEscalation\_DurationUntilEscalation() Returns the meta object for the attribute 'Duration Until Escalation'                  |
| org.eclipse.emf.ecore.EAttribute | getTEscalation\_Email() Returns the meta object for the attribute 'Email'                                                        |
| org.eclipse.emf.ecore.EReference | getTEscalation\_EMailReceiver() Returns the meta object for the containment reference 'EMail Receiver'                           |
| org.eclipse.emf.ecore.EAttribute | getTEscalation\_EscalationAction() Returns the meta object for the attribute 'Escalation Action'                                 |
| org.eclipse.emf.ecore.EReference | getTEscalation\_EscalationReceiver() Returns the meta object for the containment reference 'Escalation Receiver'                 |
| org.eclipse.emf.ecore.EAttribute | getTEscalation\_IncreasePriority() Returns the meta object for the attribute 'Increase Priority'                                 |
| org.eclipse.emf.ecore.EAttribute | getTEscalation\_Name() Returns the meta object for the attribute 'Name'                                                          |
| org.eclipse.emf.ecore.EClass     | getTEscalation() Returns the meta object for class 'TEscalation'                                                                |
| org.eclipse.emf.ecore.EEnum      | getTEscalationActions() Returns the meta object for enum 'TEscalation Actions'                                                  |
| org.eclipse.emf.ecore.EDataType  | getTEscalationActionsObject() Returns the meta object for data type 'TEscalation Actions Object'                                |
| org.eclipse.emf.ecore.EAttribute | getTEscalationChain\_ActivationState() Returns the meta object for the attribute 'Activation State'                              |
| org.eclipse.emf.ecore.EReference | getTEscalationChain\_Escalation() Returns the meta object for the containment reference list 'Escalation'                        |
| org.eclipse.emf.ecore.EClass     | getTEscalationChain() Returns the meta object for class 'TEscalation Chain'                                                     |
| org.eclipse.emf.ecore.EClass     | getTEscalationReceiver() Returns the meta object for class 'TEscalation Receiver'                                               |
| org.eclipse.emf.ecore.EReference | getTEscalationSettings\_EscalationChain() Returns the meta object for the containment reference list 'Escalation Chain'          |
| org.eclipse.emf.ecore.EClass     | getTEscalationSettings() Returns the meta object for class 'TEscalation Settings'                                               |
| org.eclipse.emf.ecore.EAttribute | getTImport\_ImportType() Returns the meta object for the attribute 'Import Type'                                                 |
| org.eclipse.emf.ecore.EAttribute | getTImport\_Location() Returns the meta object for the attribute 'Location'                                                      |
| org.eclipse.emf.ecore.EAttribute | getTImport\_Namespace() Returns the meta object for the attribute 'Namespace'                                                    |
| org.eclipse.emf.ecore.EClass     | getTImport() Returns the meta object for class 'TImport'                                                                        |
| org.eclipse.emf.ecore.EEnum      | getTIncreasePriority() Returns the meta object for enum 'TIncrease Priority'                                                    |
| org.eclipse.emf.ecore.EDataType  | getTIncreasePriorityObject() Returns the meta object for data type 'TIncrease Priority Object'                                  |
| org.eclipse.emf.ecore.EEnum      | getTInheritedAuthorization() Returns the meta object for enum 'TInherited Authorization'                                        |
| org.eclipse.emf.ecore.EDataType  | getTInheritedAuthorizationObject() Returns the meta object for data type 'TInherited Authorization Object'                      |
| org.eclipse.emf.ecore.EEnum      | getTInlineCustomPropertyEnum() Returns the meta object for enum 'TInline Custom Property Enum'                                  |
| org.eclipse.emf.ecore.EDataType  | getTInlineCustomPropertyEnumObject() Returns the meta object for data type 'TInline Custom Property Enum Object'                |
| org.eclipse.emf.ecore.EAttribute | getTInterface\_Kind() Returns the meta object for the attribute 'Kind'                                                           |
| org.eclipse.emf.ecore.EAttribute | getTInterface\_Operation() Returns the meta object for the attribute 'Operation'                                                 |
| org.eclipse.emf.ecore.EAttribute | getTInterface\_PortType() Returns the meta object for the attribute 'Port Type'                                                  |
| org.eclipse.emf.ecore.EClass     | getTInterface() Returns the meta object for class 'TInterface'                                                                  |
| org.eclipse.emf.ecore.EEnum      | getTInterfaceKinds() Returns the meta object for enum 'TInterface Kinds'                                                        |
| org.eclipse.emf.ecore.EDataType  | getTInterfaceKindsObject() Returns the meta object for data type 'TInterface Kinds Object'                                      |
| org.eclipse.emf.ecore.EReference | getTJSP\_ApplyTo() Returns the meta object for the containment reference list 'Apply To'                                         |
| org.eclipse.emf.ecore.EAttribute | getTJSP\_ContextRoot() Returns the meta object for the attribute 'Context Root'                                                  |
| org.eclipse.emf.ecore.EAttribute | getTJSP\_FaultQName() Returns the meta object for the attribute 'Fault QName'                                                    |
| org.eclipse.emf.ecore.EAttribute | getTJSP\_For() Returns the meta object for the attribute 'For'                                                                   |
| org.eclipse.emf.ecore.EAttribute | getTJSP\_Uri() Returns the meta object for the attribute 'Uri'                                                                   |
| org.eclipse.emf.ecore.EClass     | getTJSP() Returns the meta object for class 'TJSP'                                                                              |
| org.eclipse.emf.ecore.EEnum      | getTJspApplicableRole() Returns the meta object for enum 'TJsp Applicable Role'                                                 |
| org.eclipse.emf.ecore.EDataType  | getTJspApplicableRoleObject() Returns the meta object for data type 'TJsp Applicable Role Object'                               |
| org.eclipse.emf.ecore.EEnum      | getTJspUsagePattern() Returns the meta object for enum 'TJsp Usage Pattern'                                                     |
| org.eclipse.emf.ecore.EDataType  | getTJspUsagePatternObject() Returns the meta object for data type 'TJsp Usage Pattern Object'                                   |
| org.eclipse.emf.ecore.EDataType  | getTLanguage() Returns the meta object for data type 'TLanguage'                                                                |
| org.eclipse.emf.ecore.EAttribute | getTLocalizedEmail\_Body() Returns the meta object for the attribute 'Body'                                                      |
| org.eclipse.emf.ecore.EAttribute | getTLocalizedEmail\_Locale() Returns the meta object for the attribute 'Locale'                                                  |
| org.eclipse.emf.ecore.EAttribute | getTLocalizedEmail\_Subject() Returns the meta object for the attribute 'Subject'                                                |
| org.eclipse.emf.ecore.EClass     | getTLocalizedEmail() Returns the meta object for class 'TLocalized Email'                                                       |
| org.eclipse.emf.ecore.EDataType  | getTNonNegativeInt() Returns the meta object for data type 'TNon Negative Int'                                                  |
| org.eclipse.emf.ecore.EDataType  | getTNonNegativeIntObject() Returns the meta object for data type 'TNon Negative Int Object'                                     |
| org.eclipse.emf.ecore.EReference | getTParallel\_CompletionBehavior() Returns the meta object for the containment reference 'Completion Behavior'                   |
| org.eclipse.emf.ecore.EAttribute | getTParallel\_InheritedAuthorization() Returns the meta object for the attribute 'Inherited Authorization'                       |
| org.eclipse.emf.ecore.EClass     | getTParallel() Returns the meta object for class 'TParallel'                                                                    |
| org.eclipse.emf.ecore.EClass     | getTPortalClientSettings() Returns the meta object for class 'TPortal Client Settings'                                          |
| org.eclipse.emf.ecore.EClass     | getTPotentialInstanceCreator() Returns the meta object for class 'TPotential Instance Creator'                                  |
| org.eclipse.emf.ecore.EReference | getTPotentialOwner\_Parallel() Returns the meta object for the containment reference 'Parallel'                                  |
| org.eclipse.emf.ecore.EClass     | getTPotentialOwner() Returns the meta object for class 'TPotential Owner'                                                       |
| org.eclipse.emf.ecore.EClass     | getTPotentialStarter() Returns the meta object for class 'TPotential Starter'                                                   |
| org.eclipse.emf.ecore.EClass     | getTReader() Returns the meta object for class 'TReader'                                                                        |
| org.eclipse.emf.ecore.EReference | getTResult\_Aggregate() Returns the meta object for the containment reference list 'Aggregate'                                   |
| org.eclipse.emf.ecore.EClass     | getTResult() Returns the meta object for class 'TResult'                                                                        |
| org.eclipse.emf.ecore.EReference | getTStaffRole\_Verb() Returns the meta object for the containment reference 'Verb'                                               |
| org.eclipse.emf.ecore.EClass     | getTStaffRole() Returns the meta object for class 'TStaff Role'                                                                 |
| org.eclipse.emf.ecore.EReference | getTStaffSettings\_Administrator() Returns the meta object for the containment reference 'Administrator'                         |
| org.eclipse.emf.ecore.EReference | getTStaffSettings\_ContactQuery() Returns the meta object for the containment reference list 'Contact Query'                     |
| org.eclipse.emf.ecore.EReference | getTStaffSettings\_Editor() Returns the meta object for the containment reference 'Editor'                                       |
| org.eclipse.emf.ecore.EAttribute | getTStaffSettings\_InheritedAuthorization() Returns the meta object for the attribute 'Inherited Authorization'                  |
| org.eclipse.emf.ecore.EReference | getTStaffSettings\_PotentialInstanceCreator() Returns the meta object for the containment reference 'Potential Instance Creator' |
| org.eclipse.emf.ecore.EReference | getTStaffSettings\_PotentialOwner() Returns the meta object for the containment reference 'Potential Owner'                      |
| org.eclipse.emf.ecore.EReference | getTStaffSettings\_PotentialStarter() Returns the meta object for the containment reference 'Potential Starter'                  |
| org.eclipse.emf.ecore.EReference | getTStaffSettings\_Reader() Returns the meta object for the containment reference 'Reader'                                       |
| org.eclipse.emf.ecore.EClass     | getTStaffSettings() Returns the meta object for class 'TStaff Settings'                                                         |
| org.eclipse.emf.ecore.EEnum      | getTSubstitutionKinds() Returns the meta object for enum 'TSubstitution Kinds'                                                  |
| org.eclipse.emf.ecore.EDataType  | getTSubstitutionKindsObject() Returns the meta object for data type 'TSubstitution Kinds Object'                                |
| org.eclipse.emf.ecore.EAttribute | getTTask\_AllowClaimWhenSuspended() Returns the meta object for the attribute 'Allow Claim When Suspended'                       |
| org.eclipse.emf.ecore.EAttribute | getTTask\_ApplicationDefaultsComponentName() Returns the meta object for the attribute 'Application Defaults Component Name'     |
| org.eclipse.emf.ecore.EAttribute | getTTask\_AutoClaim() Returns the meta object for the attribute 'Auto Claim'                                                     |
| org.eclipse.emf.ecore.EAttribute | getTTask\_AutoDeletionMode() Returns the meta object for the attribute 'Auto Deletion Mode'                                      |
| org.eclipse.emf.ecore.EAttribute | getTTask\_Autonomy() Returns the meta object for the attribute 'Autonomy'                                                        |
| org.eclipse.emf.ecore.EAttribute | getTTask\_BusinessRelevance() Returns the meta object for the attribute 'Business Relevance'                                     |
| org.eclipse.emf.ecore.EAttribute | getTTask\_CalendarJNDIName() Returns the meta object for the attribute 'Calendar JNDI Name'                                      |
| org.eclipse.emf.ecore.EAttribute | getTTask\_CalendarName() Returns the meta object for the attribute 'Calendar Name'                                               |
| org.eclipse.emf.ecore.EAttribute | getTTask\_ContainmentContextComponentName() Returns the meta object for the attribute 'Containment Context Component Name'       |
| org.eclipse.emf.ecore.EAttribute | getTTask\_ContextAuthorizationForOwner() Returns the meta object for the attribute 'Context Authorization For Owner'             |
| org.eclipse.emf.ecore.EReference | getTTask\_CustomProperty() Returns the meta object for the containment reference list 'Custom Property'                          |
| org.eclipse.emf.ecore.EAttribute | getTTask\_DefaultLocale() Returns the meta object for the attribute 'Default Locale'                                             |
| org.eclipse.emf.ecore.EReference | getTTask\_Description() Returns the meta object for the containment reference list 'Description'                                 |
| org.eclipse.emf.ecore.EReference | getTTask\_DisplayName() Returns the meta object for the containment reference list 'Display Name'                                |
| org.eclipse.emf.ecore.EReference | getTTask\_Documentation() Returns the meta object for the containment reference list 'Documentation'                             |
| org.eclipse.emf.ecore.EAttribute | getTTask\_DurationUntilDeleted() Returns the meta object for the attribute 'Duration Until Deleted'                              |
| org.eclipse.emf.ecore.EAttribute | getTTask\_DurationUntilDue() Returns the meta object for the attribute 'Duration Until Due'                                      |
| org.eclipse.emf.ecore.EAttribute | getTTask\_DurationUntilExpires() Returns the meta object for the attribute 'Duration Until Expires'                              |
| org.eclipse.emf.ecore.EReference | getTTask\_Email() Returns the meta object for the containment reference list 'Email'                                             |
| org.eclipse.emf.ecore.EReference | getTTask\_EscalationSettings() Returns the meta object for the containment reference 'Escalation Settings'                       |
| org.eclipse.emf.ecore.EAttribute | getTTask\_EventHandlerName() Returns the meta object for the attribute 'Event Handler Name'                                      |
| org.eclipse.emf.ecore.EReference | getTTask\_Import() Returns the meta object for the containment reference 'Import'                                                |
| org.eclipse.emf.ecore.EReference | getTTask\_Interface() Returns the meta object for the containment reference 'Interface'                                          |
| org.eclipse.emf.ecore.EAttribute | getTTask\_JndiNameStaffPluginProvider() Returns the meta object for the attribute 'Jndi Name Staff Plugin Provider'              |
| org.eclipse.emf.ecore.EAttribute | getTTask\_Kind() Returns the meta object for the attribute 'Kind'                                                                |
| org.eclipse.emf.ecore.EAttribute | getTTask\_Name() Returns the meta object for the attribute 'Name'                                                                |
| org.eclipse.emf.ecore.EAttribute | getTTask\_Priority() Returns the meta object for the attribute 'Priority'                                                        |
| org.eclipse.emf.ecore.EAttribute | getTTask\_PriorityDefinition() Returns the meta object for the attribute 'Priority Definition'                                   |
| org.eclipse.emf.ecore.EReference | getTTask\_StaffSettings() Returns the meta object for the containment reference 'Staff Settings'                                 |
| org.eclipse.emf.ecore.EAttribute | getTTask\_SubstitutionPolicy() Returns the meta object for the attribute 'Substitution Policy'                                   |
| org.eclipse.emf.ecore.EAttribute | getTTask\_SupportsDelegation() Returns the meta object for the attribute 'Supports Delegation'                                   |
| org.eclipse.emf.ecore.EAttribute | getTTask\_SupportsFollowOnTask() Returns the meta object for the attribute 'Supports Follow On Task'                             |
| org.eclipse.emf.ecore.EAttribute | getTTask\_SupportsSubTask() Returns the meta object for the attribute 'Supports Sub Task'                                        |
| org.eclipse.emf.ecore.EAttribute | getTTask\_TargetNamespace() Returns the meta object for the attribute 'Target Namespace'                                         |
| org.eclipse.emf.ecore.EAttribute | getTTask\_Type() Returns the meta object for the attribute 'Type'                                                                |
| org.eclipse.emf.ecore.EReference | getTTask\_UiSettings() Returns the meta object for the containment reference 'Ui Settings'                                       |
| org.eclipse.emf.ecore.EAttribute | getTTask\_ValidFrom() Returns the meta object for the attribute 'Valid From'                                                     |
| org.eclipse.emf.ecore.EAttribute | getTTask\_WorkBasket() Returns the meta object for the attribute 'Work Basket'                                                   |
| org.eclipse.emf.ecore.EClass     | getTTask() Returns the meta object for class 'TTask'                                                                            |
| org.eclipse.emf.ecore.EEnum      | getTTaskKinds() Returns the meta object for enum 'TTask Kinds'                                                                  |
| org.eclipse.emf.ecore.EDataType  | getTTaskKindsObject() Returns the meta object for data type 'TTask Kinds Object'                                                |
| org.eclipse.emf.ecore.EDataType  | getTText1024() Returns the meta object for data type 'TText1024'                                                                |
| org.eclipse.emf.ecore.EDataType  | getTText254() Returns the meta object for data type 'TText254'                                                                  |
| org.eclipse.emf.ecore.EDataType  | getTText4096() Returns the meta object for data type 'TText4096'                                                                |
| org.eclipse.emf.ecore.EDataType  | getTText64() Returns the meta object for data type 'TText64'                                                                    |
| org.eclipse.emf.ecore.EReference | getTUISettings\_CustomClientSettings() Returns the meta object for the containment reference list 'Custom Client Settings'       |
| org.eclipse.emf.ecore.EReference | getTUISettings\_PortalClientSettings() Returns the meta object for the containment reference list 'Portal Client Settings'       |
| org.eclipse.emf.ecore.EReference | getTUISettings\_WebClientSettings() Returns the meta object for the containment reference list 'Web Client Settings'             |
| org.eclipse.emf.ecore.EClass     | getTUISettings() Returns the meta object for class 'TUI Settings'                                                               |
| org.eclipse.emf.ecore.EAttribute | getTVerb\_Name() Returns the meta object for the attribute 'Name'                                                                |
| org.eclipse.emf.ecore.EReference | getTVerb\_Parameter() Returns the meta object for the containment reference list 'Parameter'                                     |
| org.eclipse.emf.ecore.EClass     | getTVerb() Returns the meta object for class 'TVerb'                                                                            |
| org.eclipse.emf.ecore.EReference | getTWebClientSettings\_Jsp() Returns the meta object for the containment reference list 'Jsp'                                    |
| org.eclipse.emf.ecore.EClass     | getTWebClientSettings() Returns the meta object for class 'TWeb Client Settings'                                                |
| org.eclipse.emf.ecore.EDataType  | getTypeUnion() Returns the meta object for data type 'Type Union'                                                               |

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