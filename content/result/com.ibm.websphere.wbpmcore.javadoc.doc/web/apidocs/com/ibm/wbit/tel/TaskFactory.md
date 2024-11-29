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

## Interface TaskFactory

- All Superinterfaces:
org.eclipse.emf.ecore.EFactory, org.eclipse.emf.ecore.EModelElement, org.eclipse.emf.ecore.EObject, org.eclipse.emf.common.notify.Notifier

public interface TaskFactory
extends org.eclipse.emf.ecore.EFactory

 The Factory for the model.
 It provides a create method for each non-abstract class of the model.
Since:
6.0.1
See Also:TaskPackage

- =========== PROPERTY SUMMARY =========== =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Property Summary

Properties 

Type
Property and Description

TCustomProperty
createTCustom
Returns a new object of class 'TCustom Property'
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static TaskFactory
eINSTANCE
The singleton instance of the factory
    - Method Summary Methods Modifier and Type Method and Description DocumentRoot createDocumentRoot () Returns a new object of class 'Document Root ' ParameterType createParameterType () Returns a new object of class 'Parameter Type ' TAdministrator createTAdministrator () Returns a new object of class 'TAdministrator ' TAggregate createTAggregate () Returns a new object of class 'TAggregate ' TApplyTo createTApplyTo () Returns a new object of class 'TApply To ' TCompletion createTCompletion () Returns a new object of class 'TCompletion ' TCompletionBehavior createTCompletionBehavior () Returns a new object of class 'TCompletion Behavior ' TContactQuery createTContactQuery () Returns a new object of class 'TContact Query ' TCriterion createTCriterion () Returns a new object of class 'TCriterion ' TCustomClientSettings createTCustomClientSettings () Returns a new object of class 'TCustom Client Settings ' TCustomProperty createTCustomProperty () Returns a new object of class 'TCustom Property ' TCustomSetting createTCustomSetting () Returns a new object of class 'TCustom Setting ' TDefaultCompletion createTDefaultCompletion () Returns a new object of class 'TDefault Completion ' TDescription createTDescription () Returns a new object of class 'TDescription ' TDisplayName createTDisplayName () Returns a new object of class 'TDisplay Name ' TDocumentation createTDocumentation () Returns a new object of class 'TDocumentation ' TEditor createTEditor () Returns a new object of class 'TEditor ' TEmail createTEmail () Returns a new object of class 'TEmail ' TEMailReceiver createTEMailReceiver () Returns a new object of class 'TE Mail Receiver ' TEscalation createTEscalation () Returns a new object of class 'TEscalation ' TEscalationChain createTEscalationChain () Returns a new object of class 'TEscalation Chain ' TEscalationReceiver createTEscalationReceiver () Returns a new object of class 'TEscalation Receiver ' TEscalationSettings createTEscalationSettings () Returns a new object of class 'TEscalation Settings ' TImport createTImport () Returns a new object of class 'TImport ' TInterface createTInterface () Returns a new object of class 'TInterface ' TJSP createTJSP () Returns a new object of class 'TJSP ' TLocalizedEmail createTLocalizedEmail () Returns a new object of class 'TLocalized Email ' TParallel createTParallel () Returns a new object of class 'TParallel ' TPortalClientSettings createTPortalClientSettings () Returns a new object of class 'TPortal Client Settings ' TPotentialInstanceCreator createTPotentialInstanceCreator () Returns a new object of class 'TPotential Instance Creator ' TPotentialOwner createTPotentialOwner () Returns a new object of class 'TPotential Owner ' TPotentialStarter createTPotentialStarter () Returns a new object of class 'TPotential Starter ' TReader createTReader () Returns a new object of class 'TReader ' TResult createTResult () Returns a new object of class 'TResult ' TStaffSettings createTStaffSettings () Returns a new object of class 'TStaff Settings ' TTask createTTask () Returns a new object of class 'TTask ' TUISettings createTUISettings () Returns a new object of class 'TUI Settings ' TVerb createTVerb () Returns a new object of class 'TVerb ' TWebClientSettings createTWebClientSettings () Returns a new object of class 'TWeb Client Settings ' TaskPackage getTaskPackage () Returns the package supported by this factory

### Method Summary

| Modifier and Type         | Method and Description                                                                        |
|---------------------------|-----------------------------------------------------------------------------------------------|
| DocumentRoot              | createDocumentRoot() Returns a new object of class 'Document Root'                            |
| ParameterType             | createParameterType() Returns a new object of class 'Parameter Type'                          |
| TAdministrator            | createTAdministrator() Returns a new object of class 'TAdministrator'                         |
| TAggregate                | createTAggregate() Returns a new object of class 'TAggregate'                                 |
| TApplyTo                  | createTApplyTo() Returns a new object of class 'TApply To'                                    |
| TCompletion               | createTCompletion() Returns a new object of class 'TCompletion'                               |
| TCompletionBehavior       | createTCompletionBehavior() Returns a new object of class 'TCompletion Behavior'              |
| TContactQuery             | createTContactQuery() Returns a new object of class 'TContact Query'                          |
| TCriterion                | createTCriterion() Returns a new object of class 'TCriterion'                                 |
| TCustomClientSettings     | createTCustomClientSettings() Returns a new object of class 'TCustom Client Settings'         |
| TCustomProperty           | createTCustomProperty() Returns a new object of class 'TCustom Property'                      |
| TCustomSetting            | createTCustomSetting() Returns a new object of class 'TCustom Setting'                        |
| TDefaultCompletion        | createTDefaultCompletion() Returns a new object of class 'TDefault Completion'                |
| TDescription              | createTDescription() Returns a new object of class 'TDescription'                             |
| TDisplayName              | createTDisplayName() Returns a new object of class 'TDisplay Name'                            |
| TDocumentation            | createTDocumentation() Returns a new object of class 'TDocumentation'                         |
| TEditor                   | createTEditor() Returns a new object of class 'TEditor'                                       |
| TEmail                    | createTEmail() Returns a new object of class 'TEmail'                                         |
| TEMailReceiver            | createTEMailReceiver() Returns a new object of class 'TE Mail Receiver'                       |
| TEscalation               | createTEscalation() Returns a new object of class 'TEscalation'                               |
| TEscalationChain          | createTEscalationChain() Returns a new object of class 'TEscalation Chain'                    |
| TEscalationReceiver       | createTEscalationReceiver() Returns a new object of class 'TEscalation Receiver'              |
| TEscalationSettings       | createTEscalationSettings() Returns a new object of class 'TEscalation Settings'              |
| TImport                   | createTImport() Returns a new object of class 'TImport'                                       |
| TInterface                | createTInterface() Returns a new object of class 'TInterface'                                 |
| TJSP                      | createTJSP() Returns a new object of class 'TJSP'                                             |
| TLocalizedEmail           | createTLocalizedEmail() Returns a new object of class 'TLocalized Email'                      |
| TParallel                 | createTParallel() Returns a new object of class 'TParallel'                                   |
| TPortalClientSettings     | createTPortalClientSettings() Returns a new object of class 'TPortal Client Settings'         |
| TPotentialInstanceCreator | createTPotentialInstanceCreator() Returns a new object of class 'TPotential Instance Creator' |
| TPotentialOwner           | createTPotentialOwner() Returns a new object of class 'TPotential Owner'                      |
| TPotentialStarter         | createTPotentialStarter() Returns a new object of class 'TPotential Starter'                  |
| TReader                   | createTReader() Returns a new object of class 'TReader'                                       |
| TResult                   | createTResult() Returns a new object of class 'TResult'                                       |
| TStaffSettings            | createTStaffSettings() Returns a new object of class 'TStaff Settings'                        |
| TTask                     | createTTask() Returns a new object of class 'TTask'                                           |
| TUISettings               | createTUISettings() Returns a new object of class 'TUI Settings'                              |
| TVerb                     | createTVerb() Returns a new object of class 'TVerb'                                           |
| TWebClientSettings        | createTWebClientSettings() Returns a new object of class 'TWeb Client Settings'               |
| TaskPackage               | getTaskPackage() Returns the package supported by this factory                                |

- Methods inherited from interface org.eclipse.emf.ecore.EFactory
convertToString, create, createFromString, getEPackage, setEPackage

- Methods inherited from interface org.eclipse.emf.ecore.EModelElement
getEAnnotation, getEAnnotations

- Methods inherited from interface org.eclipse.emf.ecore.EObject
eAllContents, eClass, eContainer, eContainingFeature, eContainmentFeature, eContents, eCrossReferences, eGet, eGet, eIsProxy, eIsSet, eResource, eSet, eUnset

- Methods inherited from interface org.eclipse.emf.common.notify.Notifier
eAdapters, eDeliver, eNotify, eSetDeliver