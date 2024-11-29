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
- No Frames

- All Classes

# Hierarchy For All Packages

- com.ibm.casemgmt.api,
- com.ibm.casemgmt.api.constants,
- com.ibm.casemgmt.api.context,
- com.ibm.casemgmt.api.deletecase,
- com.ibm.casemgmt.api.deletedeployedsolutionfolder,
- com.ibm.casemgmt.api.deletesolution,
- com.ibm.casemgmt.api.exception,
- com.ibm.casemgmt.api.icnrest,
- com.ibm.casemgmt.api.objectref,
- com.ibm.casemgmt.api.properties,
- com.ibm.casemgmt.api.tasks,
- com.ibm.casemgmt.api.upgrade,
- com.ibm.casemgmt.api.views

## Class Hierarchy

- java.lang.Object
    - com.ibm.casemgmt.api.context.BaseP8ConnectionCache (implements com.ibm.casemgmt.api.context.P8ConnectionCache )
        - com.ibm.casemgmt.api.context.SimpleP8ConnectionCache
- com.ibm.casemgmt.api.context.BaseVWSessionCache (implements com.ibm.casemgmt.api.context.VWSessionCache )
    - com.ibm.casemgmt.api.context.SimpleVWSessionCache
- com.ibm.casemgmt.api.upgrade.BPMActivityForUpgrade
- com.ibm.casemgmt.api.Case
- com.ibm.casemgmt.api.Case.FetchHistoryResult
- com.ibm.casemgmt.api.Case.RelationshipResult
- com.ibm.casemgmt.api.deletecase.CaseInstancesDeleterFromES
- com.ibm.casemgmt.api.properties.CaseMgmtChoice
- com.ibm.casemgmt.api.properties.CaseMgmtChoiceList
- com.ibm.casemgmt.api.context.CaseMgmtContext
- com.ibm.casemgmt.api.CaseMgmtObjectStore
- com.ibm.casemgmt.api.CaseMgmtObjectStore.CM8HostConfiguration
- com.ibm.casemgmt.api.properties.CaseMgmtProperties
- com.ibm.casemgmt.api.properties.CaseMgmtProperty
- com.ibm.casemgmt.api.CaseMgmtUpdatingBatch
- com.ibm.casemgmt.api.CaseRelationship
- com.ibm.casemgmt.api.CaseType
- com.ibm.casemgmt.api.CaseType.FetchDynamicTasksResult
- com.ibm.casemgmt.api.objectref.CEObjectReference <T,P>

- com.ibm.casemgmt.api.objectref.DomainReference
- com.ibm.casemgmt.api.objectref.FolderReference
- com.ibm.casemgmt.api.objectref.ObjectStoreReference
- com.ibm.casemgmt.api.objectref.TaskReference
- com.ibm.casemgmt.api.deletecase.CloseCase
- com.ibm.casemgmt.api.Comment
- com.ibm.casemgmt.api.upgrade.ContentObjectCreator
- com.ibm.casemgmt.api.icnrest.DebugMessages
- com.ibm.casemgmt.api.deletecase.DeleteCaseDocumentsFromES
- com.ibm.casemgmt.api.DeployedSolution
- com.ibm.casemgmt.api.deletedeployedsolutionfolder.DeployedSolutionDeleter
- com.ibm.casemgmt.api.DocumentType
- com.ibm.casemgmt.api.context.DynamicClientContextProvider
- com.ibm.casemgmt.api.properties.ExternalDataModifications
- com.ibm.casemgmt.api.ExternalDocumentReference
- com.ibm.casemgmt.api.HealthAlert
- com.ibm.casemgmt.api.HealthCondition
- com.ibm.casemgmt.api.upgrade.InbasketSynchronizer
- com.ibm.casemgmt.api.tasks.LaunchStep
- com.ibm.casemgmt.api.views.PageView
- com.ibm.casemgmt.api.views.PageViewGroup
- com.ibm.casemgmt.api.deletecase.ProcessInstancesDeleter
- com.ibm.casemgmt.api.icnrest.RESTURLConnection

- com.ibm.casemgmt.api.icnrest.RESTHttpsURLConnection
- com.ibm.casemgmt.api.icnrest.RESTHttpURLConnection
- com.ibm.casemgmt.api.upgrade.SearchableCasePropertyImplForUpgrade (implements com.ibm.bpm.caseapi.searchablecaseproperties.SearchableCasePropertiesAPI.SearchableCaseProperty)
- com.ibm.casemgmt.api.deletesolution.SolutionDeleter
- com.ibm.casemgmt.api.upgrade.SolutionUpgrader
- com.ibm.casemgmt.api.Stage
- com.ibm.casemgmt.api.tasks.StepParameter
- com.ibm.casemgmt.api.tasks.Task

- com.ibm.casemgmt.api.tasks.DynamicTask
- com.ibm.casemgmt.api.tasks.TaskType
- com.ibm.casemgmt.api.upgrade.TeamsCreator
- java.lang.Throwable (implements java.io.Serializable)

- java.lang.Exception
    - java.lang.RuntimeException
        - com.ibm.casemgmt.api.exception.CaseMgmtException
- com.ibm.casemgmt.api.upgrade.ToolkitDependencyInstaller
- com.ibm.casemgmt.api.upgrade.UpgradeConstants
- com.ibm.casemgmt.api.tasks.WorkItem

## Interface Hierarchy

- com.ibm.casemgmt.api.context.P8ConnectionCache
- com.ibm.casemgmt.api.properties.UnmodifiableProperties
- com.ibm.casemgmt.api.properties.UnmodifiableProperty
- com.ibm.casemgmt.api.context.VWSessionCache

## Enum Hierarchy

- java.lang.Object
    - java.lang.Enum<E> (implements java.lang.Comparable<T>, java.io.Serializable)
        - com.ibm.casemgmt.api.constants.VCSStatus
        - com.ibm.casemgmt.api.constants.TaskRequiredState
        - com.ibm.casemgmt.api.constants.TaskLaunchMode
        - com.ibm.casemgmt.api.constants.TaskDisabledState
        - com.ibm.casemgmt.api.constants.TargetEnvironmentType
        - com.ibm.casemgmt.api.constants.StageStatus
        - com.ibm.casemgmt.api.constants.StageDurationType
        - com.ibm.casemgmt.api.constants.SolutionDeploymentStatus
        - com.ibm.casemgmt.api.constants.RelationshipType
        - com.ibm.casemgmt.api.constants.ModificationIntent
        - com.ibm.casemgmt.api.constants.IntegrationType
        - com.ibm.casemgmt.api.constants.HistoryObjectType
        - com.ibm.casemgmt.api.constants.HistoryEventType
        - com.ibm.casemgmt.api.constants.ErrorCategory
        - com.ibm.casemgmt.api.constants.DisplayMode
        - com.ibm.casemgmt.api.constants.CommentType
        - com.ibm.casemgmt.api.constants.CommentContext
        - com.ibm.casemgmt.api.constants.CaseViewType
        - com.ibm.casemgmt.api.constants.CaseState
        - com.ibm.casemgmt.api.constants.CasePageType
        - com.ibm.casemgmt.api.constants.CaseMgmtPropertyState

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
- No Frames

- All Classes