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

# Package com.ibm.task.api

- Interface Summary 

Interface
Description

ACOID

Interface for an application component object identifier.

ApplicationComponent

Accesses the properties of an application component.

AttributeInfo

Provides information about an attribute of a query table.

AttributeMetaData

Returns the meta data of a query table attribute.

AuthorizationInfo

Provides authorizations specifications of a query table.

AutoDeletionMode

This interface defines symbolic constants that state whether a task instance is
 automatically deleted once it reaches an end execution state or not.

AvailableActionsResult

Returns the result of a request for available actions.

BCID

Interface for a business category identifier.

BusinessCategory

Accesses the properties of a business category.

BusinessCategoryActionIndex

This interface defines symbolic constants to be used as column index when accessing
 the array of available action flags - see
 getAvailableActionFlagsForBusinessCategories().

BusinessCategoryActions

This interface defines symbolic constants for all actions that can be performed on
 business categories.

BusinessCategoryDefinition

Accesses and sets the properties of a business category definition.

BusinessCategoryManagerService

BusinessCategoryManagerService defines the business category methods that can be called by a local or remote client.

BusinessCategoryResult

Returns the result of an API call that processes multiple business categories,
 for example, the result of a
 setPriorityOfBusinessCategories call.

ClaimResult

Returns the result of a special claim request.

ClientSetting

Interface that supports the definition of user specific client settings.

CustomClientSettings

Interface for all client and Web client settings.

CustomProperty

Describes a named custom property.

CustomPropertyInfo

Provides information about a custom property.

Entity

Describes an entity that is returned as the result of an entity-based query request
 against a query table.

EntityInfo

Provides information about an entity that is returned as a result of a query
 against a query table.

EntityResultSet

Provides the results of an entity-based query against a query table.

Escalation

Accesses the properties of an escalation instance.

EscalationActionIndex

This interface defines symbolic constants to be used as column index when accessing
 the array of available action flags - see
 getAvailableActionFlags().

EscalationActions

This interface defines symbolic constants for all actions that can be performed on
 escalation instances.

EscalationChain

Describes an escalation chain.

EscalationInfo

Returns information about all escalations of a task instance.

EscalationResult

Returns the result of an API call that processes multiple escalation instances,
 for example, the result of a bulkTransferWorkItem(ESIID[], ...), call.

EscalationTemplate

Accesses the properties of an escalation template.

EscalationTemplateActionIndex

This interface defines symbolic constants to be used as column index when accessing the
 array of available action flags.

EscalationTemplateActions

This interface defines symbolic constants for all actions that can be performed on
 escalation templates.

ESIID

Interface for an escalation instance object identifier.

ESTID

Interface for an escalation template object identifier.

Everybody

Describes an everybody people assignment.

ExecutableQuery

Interface for customizable queries.

GroupDetail

Interface for accessing group details.

GroupMembersAndUsers

Describes a people assignment containing groups members and individual users.

HtmConfiguration

This interface returns Human Task Manager configuration settings.

HumanTaskManager

Remote EJB interface for Enterprise Bean: HumanTaskManager

HumanTaskManagerDelegate

HumanTaskManagerDelegate wraps the functions of the Human Task Manager API
 and hides the details of setting up the communication.

HumanTaskManagerHome

The remote home interface of the HumanTaskManager session bean.

HumanTaskManagerService

HumanTaskManagerService defines the human task methods that can be called by a local or remote client.

InlineCustomProperty

Describes an inline custom property.

JspLocation

Interface to retrieve JSP locations of a Web client setting.

KeyAttributes

Provides information about key attributes.

LocalBusinessCategoryManagerService

LocalBusinessCategoryManagerService defines the business category methods that can be called
 by a local client.

LocalHumanTaskManager

Local EJB interface for Enterprise Bean: HumanTaskManager

LocalHumanTaskManagerHome

The local home interface of the HumanTaskManager session bean.

LocalHumanTaskManagerService

LocalHumanTaskManagerService defines the human task methods that can be called
 by a local client.

LocalWorkBasketManagerService

LocalWorkBasketManagerService defines the work basket methods that can be called
 by a local client.

ObjectType

This interface defines symbolic constants for object types.

OperationMode

This interface defines symbolic constants that state whether the human task manager database is used
 as an archive or for production purposes.

OrganizationalEntity

Describes an organizational entity.

PageflowClientSetting

Interface for pageflow client settings.

PeopleAssignment

Interface that supports people assignments.

PortalClientSetting

Interface for Portal client settings.

QueryColumnType

This interface defines symbolic constants for all column types of a query result set.

QueryResultSet

Provides the results of a query request.

QueryTableMetaData

Provides the meta data of a query table.

ReplyHandler

This interface supports an asynchronous mode of operation.

RowResultSet

Provides the results of a row-based query against a query table.

StaffResultSet

Returns the persons or groups that are members of a specific role.

StoredQuery

Accesses the properties of a query stored persistently.

Task

Accesses the properties of a task instance.

TaskActionIndex

This interface defines symbolic constants to be used as column index when accessing
 the array of available action flags - see
 getAvailableActionFlags().

TaskActions

This interface defines symbolic constants for all actions that can be performed on
 task instances.

TaskHistoryEvent

Accesses the properties of a task history event.

TaskModel

Wraps task instances and templates that are created spontaneously.

TaskResult

Returns the result of an API call that processes multiple task instances,
 for example, the result of a complete(TKIID[]) call.

TaskTemplate

Accesses the properties of a task template.

TaskTemplateActionIndex

This interface defines symbolic constants to be used as column index when accessing the
 array of available action flags.

TaskTemplateActions

This interface defines symbolic constants for all actions that can be performed on
 Task Templates.

TimerSpecification

This interface defines symbolic constants that state how to deal with timers.

TKIID

Interface for a task instance object identifier.

TKTID

Interface for a task template object identifier.

UserDetail

Interface for accessing user details.

ValidationProblem

Describes validation problems of task instances or templates that have been created
 spontaneously (ad hoc).

WBID

Interface for a work basket object identifier.

WebClientSetting

Interface for Web client settings.

WorkBasket

Accesses the properties of a work basket.

WorkBasketActionIndex

This interface defines symbolic constants to be used as column index when accessing
 the array of available action flags - see
 getAvailableActionFlagsForWorkBaskets().

WorkBasketActions

This interface defines symbolic constants for all actions that can be performed on
 work baskets.

WorkBasketDefinition

Accesses the properties of a work basket and allows for setting values.

WorkBasketManagerService

WorkBasketManagerService defines the work basket methods that can be called by a local or remote client.

WorkBasketResult

Returns the result of an API call that processes multiple work baskets,
 for example, the result of a
 removeAsDistributionTarget call.

WorkItem

Accesses the properties of a work item.
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

BusinessCategoryDefinitionFactory

Factory to create a business category definition object.

ClientObjectWrapper

Wraps messages passed between the caller and the Human Task Manager.

ClientTaskFactory

Factory to create a ClientTaskFactory object.

CustomPropertyFactory

Factory to create a custom property or an inline custom property object.

ErrorTypeEnum

This enumeration class defines symbolic constants for error types that are
 found during validation of objects created spontaneously (ad-hoc).

FilterOptions

Describes filtering options for a query against a query table.

HumanTaskManagerDelegateFactory

Factory to create a HumanTaskManagerDelegate object.

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

PeopleAssignmentFactory

Factory to create people assignments, for example, an organizational entity.

QueryHelper

Helper class to support native SQL requests against the ProcessChoreographer database.

QueryTableKind

This enumeration class defines symbolic constants for query table kinds.

ReplyHandlerWrapper

Wraps the reply handler passed to the Human Task Manager.

StoredQueryProperty

Describes a property of a stored query.

UserSubstitutionDetail

Handles the absence and substitution details of a user.

WorkBasketDefinitionFactory

Factory to create a work basket definition object.
- Exception Summary 

Exception
Description

AdminActionException

Exception class for error message Api.AdminAction.

AdministeredObjectDoesNotExistException

Exception class for error message Api.AdministeredObjectDoesNotExist.

AdministratorCannotBeResolvedException

Exception class for error message Api.AdministratorCannotBeResolved.

ApplicationComponentDoesNotExistException

Exception class for error message Api.ApplicationComponentDoesNotExist.

ApplicationVetoException

Exception class for error message Api.ApplicationVeto.

ArchiveUnsupportedOperationException

Exception class for error message Api.ArchiveUnsupportedOperation.

BusinessCategoryAlreadyExistsException

Exception class for error message Api.BusinessCategoryAlreadyExists.

BusinessCategoryDoesNotExistException

Exception class for error message Api.BusinessCategoryDoesNotExist.

BusinessCategoryHasChildrenException

Exception class for error message Api.BusinessCategoryHasChildren.

BusinessCategoryInUseException

Exception class for error message Api.BusinessCategoryInUse.

BusinessCategoryNotAuthorizedException

Exception class for error message Api.BusinessCategoryNotAuthorized.

BusinessCategoryNotEnabledException

Exception class for error message Api.BusinessCategoryNotEnabled.

BusinessCategoryParentCircularException

Exception class for error message Api.BusinessCategoryParentCircular.

CannotAccessVMMServiceException

Exception class for error message Api.CannotAccessVMMService.

CannotCreateWorkItemException

Exception class for error message Api.CannotCreateWorkItem.

ChainIsCompletedException

Exception class for error message Api.ChainIsCompleted.

ChainIsNotCompletedException

Exception class for error message Api.ChainIsNotCompleted.

ChildTaskInstanceActiveException

Exception class for error message Api.ChildTaskInstanceActive.

CommunicationException

Exception class for error message Api.Communication.

ConflictingTypesException

Exception class for error message Api.ConflictingTypes.

ConflictingUpdateException

Exception class for error message Api.ConflictingUpdate.

CoreOTaskServiceInvalidResultException

Exception class for error message Core.OTaskServiceInvalidResult.

CoreOTaskServiceResultHasInvalidFaultMessageQNameException

Exception class for error message Core.OTaskServiceResultHasInvalidFaultMessageQName.

CoreOTaskServiceResultHasInvalidFaultMessageTypeException

Exception class for error message Core.OTaskServiceResultHasInvalidFaultMessageType.

CoreOTaskServiceResultHasInvalidOutputMessageTypeException

Exception class for error message Core.OTaskServiceResultHasInvalidOutputMessageType.

CoreOTaskServiceRuntimeExceptionReceivedException

Exception class for error message Core.OTaskServiceRuntimeExceptionReceived.

CreateBusinessCategoryNotAuthorizedException

Exception class for error message Api.CreateBusinessCategoryNotAuthorized.

CreateWorkBasketNotAuthorizedException

Exception class for error message Api.CreateWorkBasketNotAuthorized.

DataHandlingException

Exception class for error message Api.DataHandling.

EscalationDoesNotExistException

Exception class for error message Api.EscalationDoesNotExist.

EscalationIsFinishedException

Exception class for error message Api.EscalationIsFinished.

EscalationNotAuthorizedException

Exception class for error message Api.EscalationNotAuthorized.

EscalationNotificationException

Exception class for error message Api.EscalationNotification.

EscalationTemplateDoesNotExistException

Exception class for error message Api.EscalationTemplateDoesNotExist.

EscalationTemplateNotAuthorizedException

Exception class for error message Api.EscalationTemplateNotAuthorized.

EverybodyWorkItemException

Exception class for error message Api.EverybodyWorkItem.

ExpirationNotSupportedException

Exception class for error message Api.ExpirationNotSupported.

FaultMessageDefinitionDoesNotMatchException

Exception class for error message Api.FaultMessageDefinitionDoesNotMatch.

FaultReplyException

A FaultReplyException states that a modelled fault is returned.

FollowOnTasksNotSupportedException

Exception class for error message Api.FollowOnTasksNotSupported.

GenericTaskException

Exception class for error message Api.GenericTask.

GroupWorkItemException

Exception class for error message Api.GroupWorkItem.

HeadTaskIsInlineException

Exception class for error message Api.HeadTaskIsInline.

IdWrongFormatException

Exception class for error message Api.IdWrongFormat.

IdWrongTypeException

Exception class for error message Api.IdWrongType.

InheritedAccessRightException

Exception class for error message Api.InheritedAccessRight.

InvalidApplicationStateException

Exception class for error message Api.InvalidApplicationState.

InvalidAssignmentReasonException

Exception class for error message Api.InvalidAssignmentReason.

InvalidBusinessCategoryAssignmentReasonException

Exception class for error message Api.InvalidBusinessCategoryAssignmentReason.

InvalidDurationException

Exception class for error message Api.InvalidDuration.

InvalidLengthException

Exception class for error message Api.InvalidLength.

InvalidNCNamePropertyValueException

Exception class for error message Api.InvalidNCNamePropertyValue.

InvalidParameterException

Exception class for error message Api.InvalidParameter.

InvalidPriorityValueException

Exception class for error message Api.InvalidPriorityValue.

InvalidPropertyValueException

Exception class for error message Api.InvalidPropertyValue.

InvalidProtocolException

Exception class for error message Api.InvalidProtocol.

InvalidQNameException

Exception class for error message Api.InvalidQName.

InvalidStoredQueryParametersException

Exception class for error message Api.InvalidStoredQueryParameters.

InvalidWorkBasketAssignmentReasonException

Exception class for error message Api.InvalidWorkBasketAssignmentReason.

IsAdHocException

Exception class for error message Api.IsAdHoc.

IsAdministrativeTaskException

Exception class for error message Api.IsAdministrativeTask.

IsChildException

Exception class for error message Api.IsChild.

IsDistributionTargetException

Exception class for error message Api.IsDistributionTarget.

IsInlineException

Exception class for error message Api.IsInline.

IsNotAdHocException

Exception class for error message Api.IsNotAdHoc.

IsNotDistributionTargetException

Exception class for error message Api.IsNotDistributionTarget.

IsNotInlineException

Exception class for error message Api.IsNotInline.

IsNotTopLevelTaskException

Exception class for error message Api.IsNotTopLevelTask.

IsRoutingTaskException

Exception class for error message Api.IsRoutingTask.

KeepOutputForCancelClaimNotSupportedException

Exception class for error message Api.KeepOutputForCancelClaimNotSupported.

LastAdminWorkItemException

Exception class for error message Api.LastAdminWorkItem.

MandatoryParameterMissingException

Exception class for error message Api.MandatoryParameterMissing.

MandatoryPropertyMissingException

Exception class for error message Api.MandatoryPropertyMissing.

MessageDefinitionDoesNotMatchException

Exception class for error message Api.MessageDefinitionDoesNotMatch.

MethodNotApplicableException

Exception class for error message Api.MethodNotApplicable.

NotAuthorizedException

Exception class for error message Api.NotAuthorized.

ObjectDoesNotExistException

Exception class for error message Api.ObjectDoesNotExist.

OutputMessageDefinitionDoesNotMatchException

Exception class for error message Api.OutputMessageDefinitionDoesNotMatch.

ParallelRoutingTaskCompletionFailedException

Exception class for error message Api.ParallelRoutingTaskCompletionFailed.

ParallelRoutingTaskException

Exception class for error message Api.ParallelRoutingTask.

ParallelRoutingTaskStartFailedException

Exception class for error message Api.ParallelRoutingTaskStartFailed.

ParameterNullException

Exception class for error message Api.ParameterNull.

ParentTaskIsSuspendedException

Exception class for error message Api.ParentTaskIsSuspended.

PropertyControlledByHeadTaskException

Exception class for error message Api.PropertyControlledByHeadTask.

PropertyVetoException

Exception class for error message Api.PropertyVeto.

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

QueryInteractionFilterWithMissingSourceAttributeException

Exception class for error message Api.QueryInteractionFilterWithMissingSourceAttribute.

QueryInvalidOperandException

Exception class for error message Api.QueryInvalidOperand.

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

RefreshTimeoutInvalidException

Exception class for error message Api.RefreshTimeoutInvalid.

RunningInstancesException

Exception class for error message Api.RunningInstances.

SCAServiceAccessFailureException

Exception class for error message Api.SCAServiceAccessFailure.

SCAServiceResultErrorException

Exception class for error message Api.SCAServiceResultError.

SchedulingEscalationFailedException

Exception class for error message Api.SchedulingEscalationFailed.

SchedulingFailedException

Exception class for error message Api.SchedulingFailed.

SenderAddressInvalidException

Exception class for error message Api.SenderAddressInvalid.

ServiceNotUniqueException

Exception class for error message Api.ServiceNotUnique.

SourceAttributeMissingException

Exception class for error message Api.SourceAttributeMissing.

StaffServiceCannotAccessVMMException

Exception class for error message Api.StaffServiceCannotAccessVMM.

StaffServiceNestedGroupResolutionIsNotSupportedException

Exception class for error message Api.StaffServiceNestedGroupResolutionIsNotSupported.

StaffServiceRuntimeException

Exception class for error message Api.StaffServiceRuntime.

StaffServiceSubstitutionNotEnabledException

Exception class for error message Api.StaffServiceSubstitutionNotEnabled.

StaffServiceVMMEntityAttributeNotAvailableException

Exception class for error message Api.StaffServiceVMMEntityAttributeNotAvailable.

StaffServiceVMMEntityNameIsInvalidException

Exception class for error message Api.StaffServiceVMMEntityNameIsInvalid.

StaffServiceVMMEntityPropertyIsNotInSchemaException

Exception class for error message Api.StaffServiceVMMEntityPropertyIsNotInSchema.

StateObserverError

Exception class for error message Api.StateObserver.

StoredQueryNameNotUniqueException

Exception class for error message Api.StoredQueryNameNotUnique.

SubstituteDoesNotExistException

Exception class for error message Api.SubstituteDoesNotExist.

SubstitutionEndDateConflictException

Exception class for error message Api.SubstitutionEndDateConflict.

SubstitutionEndDateIsInThePastException

Exception class for error message Api.SubstitutionEndDateIsInThePast.

SubstitutionEndDateIsNotAfterStartDateException

Exception class for error message Api.SubstitutionEndDateIsNotAfterStartDate.

SubstitutionInvalidParametersException

Exception class for error message Api.SubstitutionInvalidParameters.

SubstitutionNotAuthorizedException

Exception class for error message Api.SubstitutionNotAuthorized.

SubstitutionStartDateConflictException

Exception class for error message Api.SubstitutionStartDateConflict.

SubstitutionStartDateIsInThePastException

Exception class for error message Api.SubstitutionStartDateIsInThePast.

SubTasksNotSupportedException

Exception class for error message Api.SubTasksNotSupported.

SystemFaultException

Defines an exception which is thrown when during the execution of a task
 the Human Task Manager itself runs into an error situation.

TaskBusinessException

A TaskBusinessException wraps fault responses from tasks.

TaskDelegationNotSupportedException

Exception class for error message Api.TaskDelegationNotSupported.

TaskDeploymentException

Base class for all exceptions thrown during task deployment.

TaskDoesNotExistException

Exception class for error message Api.TaskDoesNotExist.

TaskError

This class is the base class for all Human Task Manager runtime exceptions.

TaskException

This is the base class for all exceptions thrown by the Human Task Manager.

TaskExpiredException

Exception class for error message Api.TaskExpired.

TaskHistoryNotEnabledException

Exception class for error message Api.TaskHistoryNotEnabled.

TaskInstanceActiveException

Exception class for error message Api.TaskInstanceActive.

TaskIsEscalatedException

Exception class for error message Api.TaskIsEscalated.

TaskIsSuspendedException

Exception class for error message Api.TaskIsSuspended.

TaskIsWaitingForSubTaskException

Exception class for error message Api.TaskIsWaitingForSubTask.

TaskMigrationAdhocNotSupportedException

Exception class for error message Api.TaskMigrationAdhocNotSupported.

TaskMigrationCriticalChangeNotSupportedException

Exception class for error message Api.TaskMigrationCriticalChangeNotSupported.

TaskMigrationNotSupportedException

Exception class for error message Api.TaskMigrationNotSupported.

TaskMigrationNotSupportedForStandaloneException

Exception class for error message Api.TaskMigrationNotSupportedForStandalone.

TaskMigrationNotSupportedIfEndedException

Exception class for error message Api.TaskMigrationNotSupportedIfEnded.

TaskMigrationToAdhocNotSupportedException

Exception class for error message Api.TaskMigrationToAdhocNotSupported.

TaskMigrationWithCriticalEscalationChangeNotSupportedException

Exception class for error message Api.TaskMigrationWithCriticalEscalationChangeNotSupported.

TaskMigrationWithNewEscalationNameNotSupportedException

Exception class for error message Api.TaskMigrationWithNewEscalationNameNotSupported.

TaskModelNotAuthorizedException

Exception class for error message Api.TaskModelNotAuthorized.

TaskNotAuthorizedException

Exception class for error message Api.TaskNotAuthorized.

TaskNotInWorkBasketException

Exception class for error message Api.TaskNotInWorkBasket.

TaskNotSuspendedException

Exception class for error message Api.TaskNotSuspended.

TaskTemplateDoesNotExistException

Exception class for error message Api.TaskTemplateDoesNotExist.

TaskTemplateNotAuthorizedException

Exception class for error message Api.TaskTemplateNotAuthorized.

TaskTemplateNotStoppedException

Exception class for error message Api.TaskTemplateNotStopped.

TaskTerminatedException

Exception class for error message Api.TaskTerminated.

TaskTransferTargetNotAuthorizedException

Exception class for error message Api.TaskTransferTargetNotAuthorized.

TimeIntervalInvalidException

Exception class for error message Api.TimeIntervalInvalid.

UnexpectedFailureException

Exception class for error message Api.UnexpectedFailure.

UnknownAdminOperationException

Exception class for error message Api.UnknownAdminOperation.

UnknownProcessAppException

Exception class for error message Api.UnknownProcessApp.

UnsupportedAcceptHeaderException

Exception class for error message Api.UnsupportedAcceptHeader.

UnsupportedParameterValueException

Exception class for error message Api.UnsupportedParameterValue.

URLInvalidException

Exception class for error message Api.URLInvalid.

UserDoesNotExistException

Exception class for error message Api.UserDoesNotExist.

UserRegistryException

Exception class for error message Api.UserRegistry.

VMMEntityAttributeNotAvailableException

Exception class for error message Api.VMMEntityAttributeNotAvailable.

WorkBasketAlreadyExistsException

Exception class for error message Api.WorkBasketAlreadyExists.

WorkBasketDoesNotExistException

Exception class for error message Api.WorkBasketDoesNotExist.

WorkBasketNotAuthorizedException

Exception class for error message Api.WorkBasketNotAuthorized.

WorkBasketNotEmptyException

Exception class for error message Api.WorkBasketNotEmpty.

WorkBasketNotEnabledException

Exception class for error message Api.WorkBasketNotEnabled.

WorkItemDoesNotExistException

Exception class for error message Api.WorkItemDoesNotExist.

WorkItemManagerException

A general non-recoverable exception that occurred with Work Item Management functions.

WorkItemNotFoundException

Exception class for error message Api.WorkItemNotFound.

WrongEscalationStateException

Exception class for error message Api.WrongEscalationState.

WrongFaultMessageTypeException

Exception class for error message Api.WrongFaultMessageType.

WrongInputMessageTypeException

Exception class for error message Api.WrongInputMessageType.

WrongKindException

Exception class for error message Api.WrongKind.

WrongMessageTypeException

Exception class for error message Api.WrongMessageType.

WrongOutputMessageTypeException

Exception class for error message Api.WrongOutputMessageType.

WrongStateException

Exception class for error message Api.WrongState.

WrongTaskKindException

Exception class for error message Api.WrongTaskKind.

WrongTaskStateException

Exception class for error message Api.WrongTaskState.

WrongTaskTemplateKindException

Exception class for error message Api.WrongTaskTemplateKind.

WrongTaskTemplateStateException

Exception class for error message Api.WrongTaskTemplateState.

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