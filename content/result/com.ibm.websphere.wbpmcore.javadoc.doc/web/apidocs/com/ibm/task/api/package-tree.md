- Overview
- Package
- Class
- Tree
- Deprecated
- Index
- Help

- Prev
- Next

- Frames
- No Frames

- All Classes

# Hierarchy For Package com.ibm.task.api

- All Packages

## Class Hierarchy

- java.lang.Object
    - com.ibm.task.api.AttributeType (implements java.io.Serializable)
    - com.ibm.task.api.AuthorizationOptions (implements java.io.Serializable)
        - com.ibm.task.api.AdminAuthorizationOptions (implements java.io.Serializable)
- com.ibm.task.api.AuthorizationType (implements java.io.Serializable)
- com.ibm.task.api.BinaryCustomProperty (implements java.io.Serializable)
- com.ibm.task.api.BusinessCategoryDefinitionFactory
- com.ibm.task.api.ClientObjectWrapper (implements java.lang.Cloneable, java.io.Serializable)
- com.ibm.task.api.ClientTaskFactory
- com.ibm.task.api.CustomPropertyFactory
- com.ibm.task.api.ErrorTypeEnum (implements java.io.Serializable)
- com.ibm.task.api.FilterOptions (implements java.io.Serializable)
- com.ibm.task.api.HumanTaskManagerDelegateFactory
- com.ibm.task.api.JspApplicableRoleEnum (implements java.io.Serializable)
- com.ibm.task.api.JspUsageEnum (implements java.io.Serializable)
- com.ibm.task.api.MetaDataOptions (implements java.io.Serializable)
- com.ibm.task.api.Parameter (implements java.io.Serializable)
- com.ibm.task.api.PeopleAssignmentFactory
- com.ibm.task.api.QueryHelper
- com.ibm.task.api.QueryTableKind (implements java.io.Serializable)
- com.ibm.task.api.ReplyHandlerWrapper (implements java.lang.Cloneable, java.io.Serializable)
- com.ibm.task.api.StoredQueryProperty (implements java.io.Serializable)
- java.lang.Throwable (implements java.io.Serializable)
    - java.lang.Exception
        - java.lang.RuntimeException
            - com.ibm.task.api.TaskError
                - com.ibm.task.api.StateObserverError
- com.ibm.task.api.TaskException
    - com.ibm.task.api.AdminActionException
    - com.ibm.task.api.AdministratorCannotBeResolvedException
    - com.ibm.task.api.ApplicationVetoException
    - com.ibm.task.api.ArchiveUnsupportedOperationException
    - com.ibm.task.api.BusinessCategoryAlreadyExistsException
    - com.ibm.task.api.BusinessCategoryHasChildrenException
    - com.ibm.task.api.BusinessCategoryInUseException
    - com.ibm.task.api.BusinessCategoryNotEnabledException
    - com.ibm.task.api.BusinessCategoryParentCircularException
    - com.ibm.task.api.CannotAccessVMMServiceException
    - com.ibm.task.api.ChildTaskInstanceActiveException
    - com.ibm.task.api.CommunicationException
    - com.ibm.task.api.ConflictingTypesException
    - com.ibm.task.api.DataHandlingException
    - com.ibm.task.api.EscalationNotificationException
    - com.ibm.task.api.EverybodyWorkItemException
    - com.ibm.task.api.ExpirationNotSupportedException
    - com.ibm.task.api.FaultReplyException
    - com.ibm.task.api.FollowOnTasksNotSupportedException
    - com.ibm.task.api.GenericTaskException
    - com.ibm.task.api.GroupWorkItemException
    - com.ibm.task.api.IdWrongFormatException
    - com.ibm.task.api.IdWrongTypeException
    - com.ibm.task.api.InvalidApplicationStateException
    - com.ibm.task.api.InvalidAssignmentReasonException
        - com.ibm.task.api.InvalidBusinessCategoryAssignmentReasonException
        - com.ibm.task.api.InvalidWorkBasketAssignmentReasonException
- com.ibm.task.api.InvalidDurationException
- com.ibm.task.api.InvalidLengthException
- com.ibm.task.api.InvalidParameterException
- com.ibm.task.api.InvalidPriorityValueException
- com.ibm.task.api.InvalidPropertyValueException
    - com.ibm.task.api.InvalidNCNamePropertyValueException
- com.ibm.task.api.InvalidProtocolException
- com.ibm.task.api.InvalidQNameException
- com.ibm.task.api.InvalidStoredQueryParametersException
- com.ibm.task.api.IsDistributionTargetException
- com.ibm.task.api.IsNotDistributionTargetException
- com.ibm.task.api.IsNotTopLevelTaskException
- com.ibm.task.api.LastAdminWorkItemException
- com.ibm.task.api.MandatoryParameterMissingException
- com.ibm.task.api.MandatoryPropertyMissingException
- com.ibm.task.api.MessageDefinitionDoesNotMatchException

- com.ibm.task.api.FaultMessageDefinitionDoesNotMatchException
- com.ibm.task.api.OutputMessageDefinitionDoesNotMatchException
- com.ibm.task.api.MethodNotApplicableException
- com.ibm.task.api.NotAuthorizedException

- com.ibm.task.api.BusinessCategoryNotAuthorizedException
    - com.ibm.task.api.CreateBusinessCategoryNotAuthorizedException
- com.ibm.task.api.EscalationNotAuthorizedException
- com.ibm.task.api.EscalationTemplateNotAuthorizedException
- com.ibm.task.api.InheritedAccessRightException
- com.ibm.task.api.SubstitutionNotAuthorizedException
- com.ibm.task.api.TaskModelNotAuthorizedException
- com.ibm.task.api.TaskNotAuthorizedException

- com.ibm.task.api.TaskTransferTargetNotAuthorizedException
- com.ibm.task.api.TaskTemplateNotAuthorizedException
- com.ibm.task.api.WorkBasketNotAuthorizedException

- com.ibm.task.api.CreateWorkBasketNotAuthorizedException
- com.ibm.task.api.ObjectDoesNotExistException

- com.ibm.task.api.AdministeredObjectDoesNotExistException
- com.ibm.task.api.ApplicationComponentDoesNotExistException
- com.ibm.task.api.BusinessCategoryDoesNotExistException
- com.ibm.task.api.EscalationDoesNotExistException
- com.ibm.task.api.EscalationTemplateDoesNotExistException
- com.ibm.task.api.TaskDoesNotExistException
- com.ibm.task.api.TaskTemplateDoesNotExistException
- com.ibm.task.api.UserDoesNotExistException
    - com.ibm.task.api.SubstituteDoesNotExistException
- com.ibm.task.api.WorkBasketDoesNotExistException
- com.ibm.task.api.WorkItemDoesNotExistException
- com.ibm.task.api.WorkItemNotFoundException
- com.ibm.task.api.ParallelRoutingTaskException

- com.ibm.task.api.ParallelRoutingTaskCompletionFailedException
- com.ibm.task.api.ParallelRoutingTaskStartFailedException
- com.ibm.task.api.ParameterNullException
- com.ibm.task.api.PropertyVetoException

- com.ibm.task.api.ConflictingUpdateException
- com.ibm.task.api.QueryCannotJoinException
- com.ibm.task.api.QueryException

- com.ibm.task.api.QueryHintException
    - com.ibm.task.api.QueryHintInvalidException
    - com.ibm.task.api.QueryHintScopeInvalidException
    - com.ibm.task.api.QueryHintValueInvalidException
- com.ibm.task.api.QueryInteractionFilterWithMissingSourceAttributeException
- com.ibm.task.api.QueryInvalidOperandException
- com.ibm.task.api.QueryInvalidTimestampException
- com.ibm.task.api.QueryNameMissingException
- com.ibm.task.api.QueryUndefinedParameterException
- com.ibm.task.api.QueryUnknownColumnException
- com.ibm.task.api.QueryUnknownOperatorException
- com.ibm.task.api.QueryUnknownTableException
- com.ibm.task.api.RefreshTimeoutInvalidException
- com.ibm.task.api.RunningInstancesException
- com.ibm.task.api.SCAServiceAccessFailureException
- com.ibm.task.api.SCAServiceResultErrorException

- com.ibm.task.api.CoreOTaskServiceInvalidResultException
- com.ibm.task.api.CoreOTaskServiceResultHasInvalidFaultMessageQNameException
- com.ibm.task.api.CoreOTaskServiceRuntimeExceptionReceivedException
- com.ibm.task.api.SchedulingFailedException

- com.ibm.task.api.SchedulingEscalationFailedException
- com.ibm.task.api.SenderAddressInvalidException
- com.ibm.task.api.ServiceNotUniqueException
- com.ibm.task.api.SourceAttributeMissingException
- com.ibm.task.api.StaffServiceNestedGroupResolutionIsNotSupportedException
- com.ibm.task.api.StaffServiceRuntimeException

- com.ibm.task.api.StaffServiceCannotAccessVMMException
- com.ibm.task.api.StaffServiceSubstitutionNotEnabledException
- com.ibm.task.api.StaffServiceVMMEntityAttributeNotAvailableException
- com.ibm.task.api.StaffServiceVMMEntityNameIsInvalidException
- com.ibm.task.api.StaffServiceVMMEntityPropertyIsNotInSchemaException
- com.ibm.task.api.StoredQueryNameNotUniqueException
- com.ibm.task.api.SubstitutionInvalidParametersException

- com.ibm.task.api.SubstitutionEndDateConflictException
- com.ibm.task.api.SubstitutionEndDateIsInThePastException
- com.ibm.task.api.SubstitutionEndDateIsNotAfterStartDateException
- com.ibm.task.api.SubstitutionStartDateConflictException
- com.ibm.task.api.SubstitutionStartDateIsInThePastException
- com.ibm.task.api.SubTasksNotSupportedException
- com.ibm.task.api.SystemFaultException

- com.ibm.task.api.CannotCreateWorkItemException
- com.ibm.task.api.TaskBusinessException
- com.ibm.task.api.TaskDelegationNotSupportedException
- com.ibm.task.api.TaskDeploymentException
- com.ibm.task.api.TaskExpiredException
- com.ibm.task.api.TaskHistoryNotEnabledException
- com.ibm.task.api.TaskInstanceActiveException
- com.ibm.task.api.TaskMigrationNotSupportedException

- com.ibm.task.api.TaskMigrationAdhocNotSupportedException
- com.ibm.task.api.TaskMigrationCriticalChangeNotSupportedException
- com.ibm.task.api.TaskMigrationNotSupportedForStandaloneException
- com.ibm.task.api.TaskMigrationNotSupportedIfEndedException
- com.ibm.task.api.TaskMigrationToAdhocNotSupportedException
- com.ibm.task.api.TaskMigrationWithCriticalEscalationChangeNotSupportedException
- com.ibm.task.api.TaskMigrationWithNewEscalationNameNotSupportedException
- com.ibm.task.api.TaskNotInWorkBasketException
- com.ibm.task.api.TaskTemplateNotStoppedException
- com.ibm.task.api.TaskTerminatedException
- com.ibm.task.api.TimeIntervalInvalidException
- com.ibm.task.api.UnexpectedFailureException
- com.ibm.task.api.UnknownAdminOperationException
- com.ibm.task.api.UnknownProcessAppException
- com.ibm.task.api.UnsupportedAcceptHeaderException
- com.ibm.task.api.UnsupportedParameterValueException
- com.ibm.task.api.URLInvalidException
- com.ibm.task.api.UserRegistryException
- com.ibm.task.api.VMMEntityAttributeNotAvailableException
- com.ibm.task.api.WorkBasketAlreadyExistsException
- com.ibm.task.api.WorkBasketNotEmptyException
- com.ibm.task.api.WorkBasketNotEnabledException
- com.ibm.task.api.WorkItemManagerException
- com.ibm.task.api.WrongKindException

- com.ibm.task.api.IsAdHocException
- com.ibm.task.api.IsInlineException
- com.ibm.task.api.IsNotAdHocException
- com.ibm.task.api.IsNotInlineException
- com.ibm.task.api.WrongTaskKindException
    - com.ibm.task.api.HeadTaskIsInlineException
    - com.ibm.task.api.IsAdministrativeTaskException
    - com.ibm.task.api.IsChildException
    - com.ibm.task.api.IsRoutingTaskException
    - com.ibm.task.api.KeepOutputForCancelClaimNotSupportedException
    - com.ibm.task.api.PropertyControlledByHeadTaskException
- com.ibm.task.api.WrongTaskTemplateKindException
- com.ibm.task.api.WrongMessageTypeException

- com.ibm.task.api.CoreOTaskServiceResultHasInvalidFaultMessageTypeException
- com.ibm.task.api.CoreOTaskServiceResultHasInvalidOutputMessageTypeException
- com.ibm.task.api.WrongFaultMessageTypeException
- com.ibm.task.api.WrongInputMessageTypeException
- com.ibm.task.api.WrongOutputMessageTypeException
- com.ibm.task.api.WrongStateException

- com.ibm.task.api.WrongEscalationStateException
    - com.ibm.task.api.EscalationIsFinishedException
- com.ibm.task.api.WrongTaskStateException

- com.ibm.task.api.ChainIsCompletedException
- com.ibm.task.api.ChainIsNotCompletedException
- com.ibm.task.api.ParentTaskIsSuspendedException
- com.ibm.task.api.TaskIsEscalatedException
- com.ibm.task.api.TaskIsSuspendedException
- com.ibm.task.api.TaskIsWaitingForSubTaskException
- com.ibm.task.api.TaskNotSuspendedException
- com.ibm.task.api.WrongTaskTemplateStateException
- com.ibm.task.api.XMLSchemaValidationException
- com.ibm.task.api.UserSubstitutionDetail (implements java.io.Serializable)
- com.ibm.task.api.WorkBasketDefinitionFactory

## Interface Hierarchy

- com.ibm.task.api.AutoDeletionMode
- com.ibm.task.api.BusinessCategoryActionIndex
- com.ibm.task.api.BusinessCategoryActions
- com.ibm.task.api.BusinessCategoryManagerService
    - com.ibm.task.api.HumanTaskManager (also extends javax.ejb.EJBObject, com.ibm.task.api.HumanTaskManagerService, com.ibm.task.api.WorkBasketManagerService)
    - com.ibm.task.api.LocalBusinessCategoryManagerService
        - com.ibm.task.api.LocalHumanTaskManager (also extends javax.ejb.EJBLocalObject, com.ibm.task.api.LocalHumanTaskManagerService, com.ibm.task.api.LocalWorkBasketManagerService)
- java.lang.Cloneable

- com.ibm.task.api.ClientSetting (also extends java.io.Serializable)
    - com.ibm.task.api.PageflowClientSetting
    - com.ibm.task.api.PortalClientSetting
    - com.ibm.task.api.WebClientSetting
- com.ibm.task.api.CustomClientSettings (also extends java.io.Serializable)
- com.ibm.task.api.JspLocation (also extends java.io.Serializable)
- java.lang.Comparable<T>

- com.ibm.bpe.api.OID (also extends java.io.Serializable)
    - com.ibm.task.api.ACOID
    - com.ibm.task.api.BCID
    - com.ibm.task.api.ESIID
    - com.ibm.task.api.ESTID
    - com.ibm.task.api.TKIID
    - com.ibm.task.api.TKTID
    - com.ibm.task.api.WBID
- javax.ejb.EJBLocalHome

- com.ibm.task.api.LocalHumanTaskManagerHome
- javax.ejb.EJBLocalObject

- com.ibm.task.api.LocalHumanTaskManager (also extends com.ibm.task.api.LocalBusinessCategoryManagerService, com.ibm.task.api.LocalHumanTaskManagerService, com.ibm.task.api.LocalWorkBasketManagerService)
- com.ibm.task.api.EscalationActionIndex
- com.ibm.task.api.EscalationActions
- com.ibm.task.api.EscalationTemplateActionIndex
- com.ibm.task.api.EscalationTemplateActions
- com.ibm.task.api.ExecutableQuery
- com.ibm.task.api.HumanTaskManagerDelegate
- com.ibm.task.api.HumanTaskManagerService

- com.ibm.task.api.HumanTaskManager (also extends com.ibm.task.api.BusinessCategoryManagerService, javax.ejb.EJBObject, com.ibm.task.api.WorkBasketManagerService)
- com.ibm.task.api.LocalHumanTaskManagerService
    - com.ibm.task.api.LocalHumanTaskManager (also extends javax.ejb.EJBLocalObject, com.ibm.task.api.LocalBusinessCategoryManagerService, com.ibm.task.api.LocalWorkBasketManagerService)
- com.ibm.task.api.ObjectType
- com.ibm.task.api.OperationMode
- com.ibm.task.api.QueryColumnType
- java.rmi.Remote

- javax.ejb.EJBHome
    - com.ibm.task.api.HumanTaskManagerHome
- javax.ejb.EJBObject

- com.ibm.task.api.HumanTaskManager (also extends com.ibm.task.api.BusinessCategoryManagerService, com.ibm.task.api.HumanTaskManagerService, com.ibm.task.api.WorkBasketManagerService)
- java.io.Serializable

- com.ibm.task.api.ApplicationComponent
- com.ibm.task.api.AttributeInfo
    - com.ibm.task.api.AttributeMetaData
- com.ibm.task.api.AuthorizationInfo
- com.ibm.task.api.AvailableActionsResult
- com.ibm.task.api.BusinessCategory
- com.ibm.task.api.BusinessCategoryDefinition
- com.ibm.task.api.BusinessCategoryResult
- com.ibm.task.api.ClaimResult
- com.ibm.task.api.ClientSetting (also extends java.lang.Cloneable)

- com.ibm.task.api.PageflowClientSetting
- com.ibm.task.api.PortalClientSetting
- com.ibm.task.api.WebClientSetting
- com.ibm.task.api.CustomClientSettings (also extends java.lang.Cloneable)
- com.ibm.task.api.CustomProperty

- com.ibm.task.api.InlineCustomProperty
- com.ibm.task.api.CustomPropertyInfo
- com.ibm.task.api.Entity
- com.ibm.task.api.EntityInfo
- com.ibm.task.api.EntityResultSet
- com.ibm.task.api.Escalation
- com.ibm.task.api.EscalationChain
- com.ibm.task.api.EscalationInfo
- com.ibm.task.api.EscalationResult
- com.ibm.task.api.EscalationTemplate
- com.ibm.task.api.GroupDetail
- com.ibm.task.api.HtmConfiguration
- com.ibm.task.api.JspLocation (also extends java.lang.Cloneable)
- com.ibm.task.api.KeyAttributes
- com.ibm.bpe.api.OID (also extends java.lang.Comparable<T>)

- com.ibm.task.api.ACOID
- com.ibm.task.api.BCID
- com.ibm.task.api.ESIID
- com.ibm.task.api.ESTID
- com.ibm.task.api.TKIID
- com.ibm.task.api.TKTID
- com.ibm.task.api.WBID
- com.ibm.task.api.PeopleAssignment

- com.ibm.task.api.Everybody
- com.ibm.task.api.GroupMembersAndUsers
- com.ibm.task.api.OrganizationalEntity
- com.ibm.task.api.QueryResultSet
- com.ibm.task.api.QueryTableMetaData
- com.ibm.task.api.ReplyHandler
- com.ibm.task.api.RowResultSet
- com.ibm.task.api.StaffResultSet
- com.ibm.task.api.StoredQuery
- com.ibm.task.api.Task
- com.ibm.task.api.TaskHistoryEvent
- com.ibm.task.api.TaskModel
- com.ibm.task.api.TaskResult
- com.ibm.task.api.TaskTemplate
- com.ibm.task.api.UserDetail
- com.ibm.task.api.WorkBasket
- com.ibm.task.api.WorkBasketDefinition
- com.ibm.task.api.WorkBasketResult
- com.ibm.task.api.WorkItem
- com.ibm.task.api.TaskActionIndex
- com.ibm.task.api.TaskActions
- com.ibm.task.api.TaskTemplateActionIndex
- com.ibm.task.api.TaskTemplateActions
- com.ibm.task.api.TimerSpecification
- com.ibm.task.api.ValidationProblem
- com.ibm.task.api.WorkBasketActionIndex
- com.ibm.task.api.WorkBasketActions
- com.ibm.task.api.WorkBasketManagerService

- com.ibm.task.api.HumanTaskManager (also extends com.ibm.task.api.BusinessCategoryManagerService, javax.ejb.EJBObject, com.ibm.task.api.HumanTaskManagerService)
- com.ibm.task.api.LocalWorkBasketManagerService
    - com.ibm.task.api.LocalHumanTaskManager (also extends javax.ejb.EJBLocalObject, com.ibm.task.api.LocalBusinessCategoryManagerService, com.ibm.task.api.LocalHumanTaskManagerService)

- Overview
- Package
- Class
- Tree
- Deprecated
- Index
- Help

- Prev
- Next

- Frames
- No Frames

- All Classes