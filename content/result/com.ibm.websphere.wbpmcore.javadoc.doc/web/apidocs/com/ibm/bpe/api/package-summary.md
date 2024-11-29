- Overview
- Package
- Class
- Tree
- Deprecated
- Index
- Help

- Prev Package
- Next Package

- Frames
- No Frames

- All Classes

# Package com.ibm.bpe.api

- Interface Summary 

Interface
Description

ActivityInstanceActionIndex

This interface defines symbolic constants to be used as a column index for the array of
 available action flags - see
 getAvailableActionFlags().

ActivityInstanceActions

This interface defines symbolic constants for all actions that can be performed on
 activity instances.

ActivityInstanceData

Accesses the properties of an activity instance.

ActivityServiceTemplateActions

This interface defines symbolic constants for all actions that can be performed on
 activity service templates.

ActivityServiceTemplateData

Accesses the properties of an activity service.

AIID

Interface for an activity instance object identifier.

ATID

Interface for an activity template object identifier.

AttributeInfo

Provides information about an attribute of a query table.

AttributeMetaData

Returns the meta data of a query table attribute.

AuthorizationInfo

Provides authorizations specifications of a query table.

AutoDeletionMode

This interface defines symbolic constants that state whether a process instance is
 automatically deleted once it reaches an end execution state or not.

BfmConfiguration

This interface returns Business Flow Manager configuration settings.

BranchTemplateData

Accesses the properties of a branch that follows a switch activity.

BusinessFlowManager

The remote interface of the BusinessFlowManager bean.

BusinessFlowManagerHome

The remote home interface of the BusinessFlowManager session bean.

BusinessFlowManagerService

BusinessFlowManagerService defines the business functions that can be called by a local or remote client.

ClientSetting

Interface that supports the definition of user specific client settings.

CompensationBehaviour

This interface defines symbolic constants that state how to deal with compensation.

CompleteAndClaimSuccessorResult

Returns the result of a completeAndClaimSuccessor() call, that is, a description of
 the claimed successor activity instance.

CorrelationPropertyInstanceData

Provides information about a property of a correlation set instance.

CorrelationSetInstanceData

Provides information about correlation set instances.

CustomClientSettings

CustomClientSettings defines the interface for all client and Web client settings
 that are associated with a process template, process instance, or activity instance.

CustomProperty

Provides a named custom property.

CustomPropertyInfo

Provides information about a custom property.

EHTID

Interface for an event handler template object identifier.

Entity

Describes an entity that is returned as the result of an entity-based query request
 against a query table.

EntityInfo

Provides information about an entity that is returned as a result of a query
 against a query table.

EntityResultSet

Provides the results of an entity-based query against a query table.

EventHandlerTemplateActions

This interface defines symbolic constants for all actions that can be performed on
 event handler templates.

EventHandlerTemplateData

Accesses the properties of an event (action) that can be triggered as part
 of an active event handler.

ExpirationBehavior
Deprecated
As of version 7.0, replaced by the more generalized TimerBehavior interface.

ICIID

Interface for an iteration counter instance object identifier.

InitiateAndClaimFirstResult

Returns the result of an initiateAndClaimFirst() call.

InlineCustomProperty

Describes an inline custom property.

JspLocation

Interface to retrieve JSP locations of a Web client setting.

KeyAttributes

Provides information about key attributes.

LinkTemplateData

Accesses the properties of a link template.

LocalBusinessFlowManager

The local interface of the BusinessFlowManager bean.

LocalBusinessFlowManagerHome

The local home interface of the BusinessFlowManager session bean.

LocalBusinessFlowManagerService

LocalBusinessFlowManagerService defines the business functions that can be called by a local client.

ObjectType

This interface defines symbolic constants for object types.

OID

Interface for an object identifier.

OperationMode

This interface defines symbolic constants that state whether the business flow manager database is used
 as an archive or for production purposes.

PageflowClientSetting

Interface for pageflow client settings.

PIID

Interface for a process instance object identifier.

PortalClientSetting

Interface for Portal client settings.

ProcessInstanceActionIndex

This interface defines symbolic constants to be used as a column index for the array of
 available action flags - see
 getAvailableActionFlags().

ProcessInstanceActions

This interface defines symbolic constants for all actions that can be performed on
 process instances.

ProcessInstanceData

Accesses the properties of a process instance.

ProcessResult

Returns the result of an API call that processes multiple process instances,
 for example, the result of a
 BusinessFlowManagerService.setInlineCustomProperty(PIID[],InlineCustomProperty) call.

ProcessTemplateActions

This interface defines symbolic constants for all actions that can be performed on
 process templates.

ProcessTemplateData

Accesses the properties of a process template.

PTID

Interface for a process template object identifier.

QueryProperty

Returns the properties of a variable that can be queried.

QueryPropertyExtension

Returns the properties of a variable that can be queried and information about
 the associated process template.

QueryResultSet

Provides the results of a query request.

QueryTableMetaData

Provides the meta data of a query table.

ReplyContext

This interface supports an asynchronous mode of operation.

RowResultSet

Provides the results of a row-based query against a query table.

StaffResultSet

Returns the persons or groups that are members of a specific role.

StateObserverEvent

This interface returns observer event specific information as there are the event number
 and the creation time.

StoredQueryData

Accesses the properties of a query stored persistently.

TimerBehavior

This interface defines symbolic constants that state how to deal with timers.

VTID

Interface for a service template object identifier.

WebClientSetting

Interface for Web client settings.

WorkItemActions
Deprecated 

WorkItemData

Accesses the properties of a work item.

WorkListActions
Deprecated 

WorkListData
Deprecated
As of version 6.0, replaced by the StoredQueryData object.
- Class Summary 

Class
Description

AdminAuthorizationOptions

Describes administrative authorizations options for a query that uses a predefined or composite query table.

AttributeType

This enumeration class defines symbolic constants for attribute types.

AuthorizationOptions

States authorizations options for a query that uses a predefined or composite query table.

AuthorizationType

This enumeration class defines symbolic constants for types of authorization.

BinaryCustomProperty

Describes a custom property that has a binary value.

ClientObjectWrapper

Wraps messages and variables passed between the caller and the process engine.

CustomPropertyFactory

Factory to create a custom property or an inline custom property object.

ErrorTypeEnum

This enumeration class defines symbolic constants for error types that are
 found during validation of objects created spontaneously (ad-hoc).

FilterOptions

Describes filtering options for a query against a query table.

JspApplicableRoleEnum

This enumeration class defines symbolic constants for JSP applicable role
 patterns.

JspUsageEnum

This enumeration class defines symbolic constants for JSP usage patterns.

MetaDataOptions

Describes filtering options for retrieving the meta data of query tables.

Parameter

Describes a parameter and its value to set the value of a parameter that is used in
 query table filters and selection criteria.

ProcessResponseWrapper

Wraps the output message returned by a microflow and its associated custom client settings.

QueryColumnInfo

Provides information on the columns of a query result set.

QueryTableKind

This enumeration class defines symbolic constants for query table kinds.

ReplyContextWrapper

Wraps the reply context passed to the process engine.

StoredQueryProperty

Describes a property of a stored query.

TimerSpecification

Describes options that can be used to set timers.
- Exception Summary 

Exception
Description

ActivityNameNotUniqueException

Exception class for error message Api.ActivityNameNotUnique.

ApplicationFaultException

An ApplicationFaultException wraps fault responses
 from invoke, throw, or script activities.

ApplicationFaultException2

An ApplicationFaultException2 extends ApplicationFaultException
 and additionally provides the namespace of the WSDL message that is
 associated with the thrown fault variable in case the
 fault variable is represented by a boxed Java simple type.

ApplicationNotStartedException

Exception class for error message Api.ApplicationNotStarted.

ApplicationVetoException

Exception class for error message Api.ApplicationVeto.

ArchiveUnsupportedOperationException

Exception class for error message Api.ArchiveUnsupportedOperation.

BpelException

Super class for all navigation related exceptions that can occur
 during the execution of BPEL processes.

CannotAccessObjectException

Exception class for error message Api.CannotAccessObject.

CannotDeleteNamespaceException

Exception class for error message Api.CannotDeleteNamespace.

CannotSendExceptionException

Exception class for error message Api.CannotSendException.

CannotSendPIIDException

Exception class for error message Api.CannotSendPIID.

CannotSendProcessResultException

Exception class for error message Api.CannotSendProcessResult.

CannotSendVoidReplyException

Exception class for error message Api.CannotSendVoidReply.

CouldNotCreateWSIFPort\_ProcessException

Exception class for error message Api.CouldNotCreateWSIFPort\_Process.

CreateFailedException

Exception class for error message Api.CreateFailed.

CreateRejectedException

Exception class for error message Api.CreateRejected.

DatabaseException

Exception class for error message Api.Database.

DataHandlingException

Exception class for error message Api.DataHandling.

EngineActivityCorrelationHandlingFailureException

Exception class for error message Engine.ActivityCorrelationHandlingFailure.

EngineActivityDoesNotExistException

Exception class for error message Engine.ActivityDoesNotExist.

EngineActivityExpiringException

Exception class for error message Engine.ActivityExpiring.

EngineActivityInputCreationFailureException

Exception class for error message Engine.ActivityInputCreationFailure.

EngineActivityMultipleJumpRequestsException

Exception class for error message Engine.ActivityMultipleJumpRequests.

EngineActivityNotAuthorizedException

Exception class for error message Engine.ActivityNotAuthorized.

EngineActivityStoppedException

Exception class for error message Engine.ActivityStopped.

EngineActivityWrongKindException

Exception class for error message Engine.ActivityWrongKind.

EngineActivityWrongKindForSignatureException

Exception class for error message Engine.ActivityWrongKindForSignature.

EngineActivityWrongStateException

Exception class for error message Engine.ActivityWrongState.

EngineActivityWrongStopReasonException

Exception class for error message Engine.ActivityWrongStopReason.

EngineAdministratorCannotBeResolvedException

Exception class for error message Engine.AdministratorCannotBeResolved.

EngineAmbiguousActivityException

Exception class for error message Engine.AmbiguousActivity.

EngineAmbiguousOnAlarmBranchException

Exception class for error message Engine.AmbiguousOnAlarmBranch.

EngineAmbiguousPropertyDefinitionException

Exception class for error message Engine.AmbiguousPropertyDefinition.

EngineAssignmentFailureExceptionException

Exception class for error message Engine.AssignmentFailureException.

EngineAuthorizationPluginException

Exception class for error message Engine.AuthorizationPlugin.

EngineBaseClassNotFoundException

Exception class for error message Engine.BaseClassNotFound.

EngineCalendarNotFoundException

Exception class for error message Engine.CalendarNotFound.

EngineCannotCreateWorkItemException

Exception class for error message Engine.CannotCreateWorkItem.

EngineCannotDeleteProcessException

Exception class for error message Engine.CannotDeleteProcess.

EngineCannotDeserializeReplyContextException

Exception class for error message Engine.CannotDeserializeReplyContext.

EngineCannotInitializePluginException

Exception class for error message Engine.CannotInitializePlugin.

EngineCannotInitializeVariableException

Exception class for error message Engine.CannotInitializeVariable.

EngineCannotInitializeWorkItemManagerException

Exception class for error message Engine.CannotInitializeWorkItemManager.

EngineCannotOpenCompensationSphereException

Exception class for error message Engine.CannotOpenCompensationSphere.

EngineCannotResolveEndpointException

Exception class for error message Engine.CannotResolveEndpoint.

EngineCannotResolveReplacementStringException

Exception class for error message Engine.CannotResolveReplacementString.

EngineCannotRunInAtomicSphereException

Exception class for error message Engine.CannotRunInAtomicSphere.

EngineCannotRunInterruptibleException

Exception class for error message Engine.CannotRunInterruptible.

EngineCannotRunSynchronousException

Exception class for error message Engine.CannotRunSynchronous.

EngineCannotUnwrapReplyContextException

Exception class for error message Engine.CannotUnwrapReplyContext.

EngineCompensateActivityFailedExceptionException

Exception class for error message Engine.CompensateActivityFailedException.

EngineCompensationNotSupportedException

Exception class for error message Engine.CompensationNotSupported.

EngineCompensationSphereNotCompletedError

Exception class for error message Engine.CompensationSphereNotCompleted.

EngineCompensationSphereRequiredException

Exception class for error message Engine.CompensationSphereRequired.

EngineCompensationSphereStateUnknownError

Exception class for error message Engine.CompensationSphereStateUnknown.

EngineConditionEvaluationException

Exception class for error message Engine.ConditionEvaluation.

EngineConditionEvaluationFailedException

Exception class for error message Engine.ConditionEvaluationFailed.

EngineConflictingProcessException

Exception class for error message Engine.ConflictingProcess.

EngineContainerAppNotReachableError

Exception class for error message Engine.ContainerAppNotReachable.

EngineCopyDataObjectError

Exception class for error message Engine.CopyDataObject.

EngineCorrelationSetAlreadyInitializedException

Exception class for error message Engine.CorrelationSetAlreadyInitialized.

EngineCorrelationSetDoesNotExistException

Exception class for error message Engine.CorrelationSetDoesNotExist.

EngineCreateDataObjectError

Exception class for error message Engine.CreateDataObject.

EngineCreateServiceReferenceException

Exception class for error message Engine.CreateServiceReference.

EngineCustomAttributeAccessViolationException

Exception class for error message Engine.CustomAttributeAccessViolation.

EngineDataAssociationFailureException

Exception class for error message Engine.DataAssociationFailure.

EngineDataCannotBeProcessedException

Exception class for error message Engine.DataCannotBeProcessed.

EngineDataMappingException

Exception class for error message Engine.DataMapping.

EngineDataPluginException

Exception class for error message Engine.DataPlugin.

EngineDuplicateAwaitedEventException

Exception class for error message Engine.DuplicateAwaitedEvent.

EngineDurationFormatException

Exception class for error message Engine.DurationFormat.

EngineEndlessLoopException

Exception class for error message Engine.EndlessLoop.

EngineEnforceRollbackError

Exception class for error message Engine.EnforceRollback.

EngineErrorInActivityCustomPropertyResolutionException

Exception class for error message Engine.ErrorInActivityCustomPropertyResolution.

EngineErrorInDescriptionResolutionException

Exception class for error message Engine.ErrorInDescriptionResolution.

EngineEventHandlerCorrelationHandlingFailureException

Exception class for error message Engine.EventHandlerCorrelationHandlingFailure.

EngineEventNotKnownException

Exception class for error message Engine.EventNotKnown.

EngineEverybodyWorkItemException

Exception class for error message Engine.EverybodyWorkItem.

EngineExitConditionEvaluationException

Exception class for error message Engine.ExitConditionEvaluation.

EngineExitConditionExpressionEvaluationFailedException

Exception class for error message Engine.ExitConditionExpressionEvaluationFailed.

EngineExitConditionFailedException

Exception class for error message Engine.ExitConditionFailed.

EngineFaultTerminalMessageIsNullException

Exception class for error message Engine.FaultTerminalMessageIsNull.

EngineFaultTerminalNotConnectedException

Exception class for error message Engine.FaultTerminalNotConnected.

EngineForEachExpressionEvaluationException

Exception class for error message Engine.ForEachExpressionEvaluation.

EngineGenericErrorException

Exception class for error message Engine.GenericError.

EngineGetTypeError

Exception class for error message Engine.GetType.

EngineImplementationDoesNotExistException

Exception class for error message Engine.ImplementationDoesNotExist.

EngineImplementationInvocationException

Exception class for error message Engine.ImplementationInvocation.

EngineImplQualTranMustBeGlobalException

Exception class for error message Engine.ImplQualTranMustBeGlobal.

EngineIncompatibleTypesException

Exception class for error message Engine.IncompatibleTypes.

EngineIncompleteUserInputException

Exception class for error message Engine.IncompleteUserInput.

EngineInitializingScopeNotReachedException

Exception class for error message Engine.InitializingScopeNotReached.

EngineInstanceLocationFailureException

Exception class for error message Engine.InstanceLocationFailure.

EngineInvalidCompensationSphereDescriptorException

Exception class for error message Engine.InvalidCompensationSphereDescriptor.

EngineInvalidDurationException

Exception class for error message Engine.InvalidDuration.

EngineInvalidDurationInEventHandlerException

Exception class for error message Engine.InvalidDurationInEventHandler.

EngineInvalidFaultTerminalException

Exception class for error message Engine.InvalidFaultTerminal.

EngineInvalidFromExpressionException

Exception class for error message Engine.InvalidFromExpression.

EngineInvalidLinkTypeException

Exception class for error message Engine.InvalidLinkType.

EngineInvalidMaxCompletedBranchesException

Exception class for error message Engine.InvalidMaxCompletedBranches.

EngineInvalidMigrationTargetException

Exception class for error message Engine.InvalidMigrationTarget.

EngineInvalidNamespaceURIException

Exception class for error message Engine.InvalidNamespaceURI.

EngineInvalidNumberOfLinksException

Exception class for error message Engine.InvalidNumberOfLinks.

EngineInvalidReplacementVariableException

Exception class for error message Engine.InvalidReplacementVariable.

EngineInvalidToExpressionException

Exception class for error message Engine.InvalidToExpression.

EngineJavaExecutionFailedException

Exception class for error message Engine.JavaExecutionFailed.

EngineJmsApiContextException

Exception class for error message Engine.JmsApiContext.

EngineJoinConditionEvaluationException

Exception class for error message Engine.JoinConditionEvaluation.

EngineJoinConditionFailedException

Exception class for error message Engine.JoinConditionFailed.

EngineLastAdminWorkItemException

Exception class for error message Engine.LastAdminWorkItem.

EngineLateBindingInfoException

Exception class for error message Engine.LateBindingInfo.

EngineLinkConditionEvaluationException

Exception class for error message Engine.LinkConditionEvaluation.

EngineLinkDoesNotExistException

Exception class for error message Engine.LinkDoesNotExist.

EngineLookupProcessBeanError

Exception class for error message Engine.LookupProcessBean.

EngineLoopConditionEvaluationException

Exception class for error message Engine.LoopConditionEvaluation.

EngineLoopDefaultMappingException

Exception class for error message Engine.LoopDefaultMapping.

EngineLoopMappingException

Exception class for error message Engine.LoopMapping.

EngineMaxNumberLoopIterationsExceededException

Exception class for error message Engine.MaxNumberLoopIterationsExceeded.

EngineMaxNumberRetryExceededException

Exception class for error message Engine.MaxNumberRetryExceeded.

EngineMessageAndCorrelationSetMismatchException

Exception class for error message Engine.MessageAndCorrelationSetMismatch.

EngineMissingReceiveException

An EngineMisssingReceiveException is thrown when a message has been received
 and stored by Process Choreographer and when that message has not been processed
 before the completion of the process instance for which it was received.

EngineMissingReplyException

An EngineMisssingReplyException is thrown when the process instance ends and when
 there is a reply missing for
 a receive or pick activity that implements a two-way operation.

EngineNoExpirationDefinedException

Exception class for error message Engine.NoExpirationDefined.

EngineNoInitialReceiveException

Exception class for error message Engine.NoInitialReceive.

EngineNoServiceRefTypeException

Exception class for error message Engine.NoServiceRefType.

EngineNotAuthorizedException

Exception class for error message Engine.NotAuthorized.

EngineNullMessageException

Exception class for error message Engine.NullMessage.

EngineParameterNullException

Exception class for error message Engine.ParameterNull.

EngineParentProcessContextException

Exception class for error message Engine.ParentProcessContext.

EngineProcessCannotBeMigratedException

Exception class for error message Engine.ProcessCannotBeMigrated.

EngineProcessDoesNotExistException

Exception class for error message Engine.ProcessDoesNotExist.

EngineProcessInstanceNameNotUniqueException

Exception class for error message Engine.ProcessInstanceNameNotUnique.

EngineProcessIsMigratedException

Exception class for error message Engine.ProcessIsMigrated.

EngineProcessModelDoesNotExistException

Exception class for error message Engine.ProcessModelDoesNotExist.

EngineProcessModelStoppedException

Exception class for error message Engine.ProcessModelStopped.

EngineProcessNotAuthorizedException

Exception class for error message Engine.ProcessNotAuthorized.

EngineProcessReaderWorkItemException

Exception class for error message Engine.ProcessReaderWorkItem.

EngineProcessStarterDeletedException

Exception class for error message Engine.ProcessStarterDeleted.

EngineProcessTemplateDoesNotExistException

Exception class for error message Engine.ProcessTemplateDoesNotExist.

EngineProcessWrongBuildVersionException

Exception class for error message Engine.ProcessWrongBuildVersion.

EngineProcessWrongKindException

Exception class for error message Engine.ProcessWrongKind.

EngineProcessWrongStateException

Exception class for error message Engine.ProcessWrongState.

EngineRefQualDeliverAsyncAtMustBeCommitException

Exception class for error message Engine.RefQualDeliverAsyncAtMustBeCommit.

EngineRepeatedCompensationExceptionException

Exception class for error message Engine.RepeatedCompensationException.

EngineRequestPendingException

Exception class for error message Engine.RequestPending.

EngineRequestRejectedException

Exception class for error message Engine.RequestRejected.

EngineRollbackOnlyError

Exception class for error message Engine.RollbackOnly.

EngineSchedulerException

Exception class for error message Engine.Scheduler.

EngineSchedulerNotFoundException

Exception class for error message Engine.SchedulerNotFound.

EngineScopeInitializationFailureException

Exception class for error message Engine.ScopeInitializationFailure.

EngineSelectionFailureExceptionException

Exception class for error message Engine.SelectionFailureException.

EngineServiceNotAuthorizedException

Exception class for error message Engine.ServiceNotAuthorized.

EngineStateObserverEventError

Exception class for error message Engine.StateObserverEvent.

EngineSubProcessHasNoMatchingEventException

Exception class for error message Engine.SubProcessHasNoMatchingEvent.

EngineTimeoutExpressionEvaluationException

Exception class for error message Engine.TimeoutExpressionEvaluation.

EngineTimeoutExpressionEvaluationFailedException

Exception class for error message Engine.TimeoutExpressionEvaluationFailed.

EngineTimeoutExpressionEvaluationInEventHandlerException

Exception class for error message Engine.TimeoutExpressionEvaluationInEventHandler.

EngineTransitionConditionEvaluationException

Exception class for error message Engine.TransitionConditionEvaluation.

EngineTransitionConditionFailedException

Exception class for error message Engine.TransitionConditionFailed.

EngineUncaughtExceptionInActivityException

Exception class for error message Engine.UncaughtExceptionInActivity.

EngineUncheckedBusinessFaultException

Exception class for error message Engine.UncheckedBusinessFault.

EngineUnknownActivityException

Exception class for error message Engine.UnknownActivity.

EngineUnknownInboundOperationException

Exception class for error message Engine.UnknownInboundOperation.

EngineUnknownNamespaceURIException

Exception class for error message Engine.UnknownNamespaceURI.

EngineUnknownOperationException

Exception class for error message Engine.UnknownOperation.

EngineUnsupportedJumpException

Exception class for error message Engine.UnsupportedJump.

EngineVariableDoesNotExistException

Exception class for error message Engine.VariableDoesNotExist.

EngineVariableNotVisibleException

Exception class for error message Engine.VariableNotVisible.

EngineWorkCompletionContractRollbackError

Exception class for error message Engine.WorkCompletionContractRollback.

EngineWrongActivityNameException

Exception class for error message Engine.WrongActivityName.

EngineWrongDataTypeException

Exception class for error message Engine.WrongDataType.

EngineWrongKindException

Exception class for error message Engine.WrongKind.

EngineWrongMessageTypeException

Exception class for error message Engine.WrongMessageType.

EngineWrongStateException

Exception class for error message Engine.WrongState.

EngineWrongTaskKindException

An EngineWrongTaskKindException encapsulates a TaskWrongKindException
 thrown by the Human Task Manager and signals such a failure to a Business Flow Manager user.

EngineWrongTaskStateException

An EngineWrongTaskStateException encapsulates a TaskWrongStateException
 thrown by the Human Task Manager and signals such a failure to a Business Flow Manager user.

EngineWrongTaskTemplateException

Exception class for error message Engine.WrongTaskTemplate.

EngineXPathCannotCreatePathException

Exception class for error message Engine.XPathCannotCreatePath.

EngineXPathCannotSetPathException

Exception class for error message Engine.XPathCannotSetPath.

EngineXPathDataTypeMismatchException

Exception class for error message Engine.XPathDataTypeMismatch.

EngineXPathExtensionFunctionFailedException

Exception class for error message Engine.XPathExtensionFunctionFailed.

ExecuteInputOnlyOperation\_NotSupportedException

Exception class for error message Api.ExecuteInputOnlyOperation\_NotSupported.

FaultReplyException

A FaultReplyException states that a modelled fault is returned.

FaultReplyException2

A FaultReplyException2 states that a modelled fault is returned.

GenericErrorException

Exception class for error message Api.GenericError.

GroupWorkItemException

Exception class for error message Api.GroupWorkItem.

HumanTaskManagerException

Exception class for error message Api.HumanTaskManager.

IdAndCorrelationSetMismatchException

Exception class for error message Api.IdAndCorrelationSetMismatch.

IdWrongFormatException

Exception class for error message Api.IdWrongFormat.

IdWrongTypeException

Exception class for error message Api.IdWrongType.

ImplementationNotFoundException

Exception class for error message Api.ImplementationNotFound.

InvalidAssignmentReasonException

Exception class for error message Api.InvalidAssignmentReason.

InvalidLengthException

Exception class for error message Api.InvalidLength.

InvalidMessagePartTypeException

Exception class for error message Api.InvalidMessagePartType.

InvalidMessageTypeException

Exception class for error message Api.InvalidMessageType.

InvalidObjectNameException

Exception class for error message Api.InvalidObjectName.

InvalidParameterException

Exception class for error message Api.InvalidParameter.

InvalidParameterValueException

Exception class for error message Api.InvalidParameterValue.

InvalidPropertyAliasTypeException

Exception class for error message Api.InvalidPropertyAliasType.

InvalidStoredQueryParametersException

Exception class for error message Api.InvalidStoredQueryParameters.

MandatoryParameterMissingException

Exception class for error message Api.MandatoryParameterMissing.

MessagePartNotFoundException

Exception class for error message Api.MessagePartNotFound.

MessagePartQueryFailedException

Exception class for error message Api.MessagePartQueryFailed.

MethodNotApplicableException

Exception class for error message Api.MethodNotApplicable.

MissingPartsException

Exception class for error message Api.MissingParts.

MultipleInstanceException

Exception class for error message Api.MultipleInstance.

NoMacroFlowException

Exception class for error message Api.NoMacroFlow.

NotSerializableException

NotSerializableException is basically a placeholder for nested exceptions
 that serialization fails.

ObjectDoesNotExistException

Exception class for error message Api.ObjectDoesNotExist.

ProcessBindingMissingFormatTypeException

Exception class for error message Api.ProcessBindingMissingFormatType.

ProcessBindingMissingTypeMappingException

Exception class for error message Api.ProcessBindingMissingTypeMapping.

ProcessError

This is the base class for all Business Flow Manager runtime exceptions.

ProcessException

This is the base class for all exceptions thrown by the Business Flow Manager EJB API.

ProcessInputTypeNameNullException

Exception class for error message Api.ProcessInputTypeNameNull.

ProcessInputTypeSystemNullException

Exception class for error message Api.ProcessInputTypeSystemNull.

ProcessInputUnknownTypeSystemException

Exception class for error message Api.ProcessInputUnknownTypeSystem.

ProcessInstanceNotUniqueException

Exception class for error message Api.ProcessInstanceNotUnique.

ProcessOperationCannotFindModelException

Exception class for error message Api.ProcessOperationCannotFindModel.

ProcessOperationCannotInvokeException

Exception class for error message Api.ProcessOperationCannotInvoke.

ProcessOperationFailedException

Exception class for error message Api.ProcessOperationFailed.

ProcessOperationFaultNameNotSetException

Exception class for error message Api.ProcessOperationFaultNameNotSet.

ProcessOperationMissingFaultMessageException

Exception class for error message Api.ProcessOperationMissingFaultMessage.

ProcessOperationNoOutputMessageException

Exception class for error message Api.ProcessOperationNoOutputMessage.

ProcessOperationNotKnownByPortException

Exception class for error message Api.ProcessOperationNotKnownByPort.

ProcessOperationUnknownFaultMessageTypeException

Exception class for error message Api.ProcessOperationUnknownFaultMessageType.

ProcessTemplateNotFoundException

Exception class for error message Api.ProcessTemplateNotFound.

QueryCannotJoinException

Exception class for error message Api.QueryCannotJoin.

QueryException

Exception class for error message Api.Query.

QueryHintException

Exception class for error message Api.QueryHint.

QueryHintInvalidException

Exception class for error message Api.QueryHintInvalid.

QueryHintScopeInvalidException

Exception class for error message Api.QueryHintScopeInvalid.

QueryHintValueInvalidException

Exception class for error message Api.QueryHintValueInvalid.

QueryInvalidOperandException

Exception class for error message Api.QueryInvalidOperand.

QueryInvalidParameterException

Exception class for error message Api.QueryInvalidParameter.

QueryInvalidTimestampException

Exception class for error message Api.QueryInvalidTimestamp.

QueryNameMissingException

Exception class for error message Api.QueryNameMissing.

QueryUndefinedParameterException

Exception class for error message Api.QueryUndefinedParameter.

QueryUnknownColumnException

Exception class for error message Api.QueryUnknownColumn.

QueryUnknownOperatorException

Exception class for error message Api.QueryUnknownOperator.

QueryUnknownTableException

Exception class for error message Api.QueryUnknownTable.

RuntimeFaultException

RuntimeFaultException wraps all runtime failures that
 can happen during the execution of BPEL processes, for example, when executing
 a script activity or when evaluating a transition condition.

SendReplyErrorException

Represents the exception that is thrown by ReplyContext methods if
 sending the reply generates an error.

ServiceNotUniqueException

Exception class for error message Api.ServiceNotUnique.

SpecificFaultReplyException
Deprecated
As of version 6.1, no replacement.

StandardFaultException

Super class for all BPEL standard faults such as bpws:forceTermination.

StoredQueryNameNotUniqueException

Exception class for error message Api.StoredQueryNameNotUnique.

SystemFaultException

Defines an exception which is thrown when during the execution of an
 activity or the invocation of a plug-in (except the observer plug-in),
 Process Choreographer itself runs into an error situation.

TaskManagerNotFoundException

Exception class for error message Api.TaskManagerNotFound.

TemplateInUseException

Exception class for error message Api.TemplateInUse.

UnexpectedFailureException

Exception class for error message Api.UnexpectedFailure.

UnhandledFaultException

Super class for all unhandled fault exceptions.

UnknownProcessAppException

Exception class for error message Api.UnknownProcessApp.

UnsupportedAcceptHeaderException

Exception class for error message Api.UnsupportedAcceptHeader.

UnsupportedParameterValueException

Exception class for error message Api.UnsupportedParameterValue.

UserDoesNotExistException

Exception class for error message Api.UserDoesNotExist.

UserRegistryException

Exception class for error message Api.UserRegistry.

WorkItemDoesNotExistException

Exception class for error message Api.WorkItemDoesNotExist.

WorkItemManagerException

A general non-recoverable exception that occured with Work Item Management functions.

XMLSchemaValidationException

Exception class for error message Api.XMLSchemaValidation.

- Overview
- Package
- Class
- Tree
- Deprecated
- Index
- Help

- Prev Package
- Next Package

- Frames
- No Frames

- All Classes