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

# Deprecated API

## Contents

- Deprecated Interfaces
- Deprecated Classes
- Deprecated Exceptions
- Deprecated Fields
- Deprecated Methods
- Deprecated Constructors

- Deprecated Interfaces 

Interface and Description

com.ibm.bpe.api.ExpirationBehavior
As of version 7.0, replaced by the more generalized TimerBehavior interface.

com.ibm.wbiserver.manualrecovery.FailedEventWithParameters 

com.ibm.bpe.api.WorkItemActions 

com.ibm.bpe.api.WorkListActions 

com.ibm.bpe.api.WorkListData
As of version 6.0, replaced by the StoredQueryData object. The WorkList has been renamed to better
 express its meaning.

- Deprecated Classes 

Class and Description

com.ibm.websphere.cem.ECSEmitter
To emit CEI events, instead of calling the APIs of this class, please call WebSphere Application Server CEI APIs directly.

- Deprecated Exceptions 

Exceptions and Description

com.ibm.bpe.api.SpecificFaultReplyException
As of version 6.1, no replacement.

- Deprecated Fields 

Field and Description

com.ibm.bpe.api.StateObserverEvent.ACTIVITY\_RESCHEDULED
As of version 7.0, replaced by ACTIVITY\_TIMER\_RESCHEDULED.

com.ibm.task.api.TaskActions.CREATEMESSAGE
Use CREATEINPUTMESSAGE, CREATEOUTPUTMESSAGE, CREATEFAULTMESSAGE.

com.ibm.task.clientmodel.bean.WorkItemBean.CREATIONIME\_PROPERTY
use WorkItemBean.CREATIONTIME\_PROPERTY

com.ibm.bpe.api.ProcessTemplateActions.GETCUSTOMATTRIBUTE
Use GETCUSTOMPROPERTY.

com.ibm.bpe.api.ProcessInstanceActions.GETCUSTOMATTRIBUTE
Use GETCUSTOMPROPERTY.

com.ibm.bpe.api.ActivityInstanceActions.GETCUSTOMATTRIBUTE
As of version 6.0, replaced by GETCUSTOMPROPERTY.

com.ibm.task.api.TaskActions.GETTASKINSTANCE
Use GETTASK.

com.ibm.task.api.JspUsageEnum.INFO 

com.ibm.bpe.clientmodel.bean.ProcessTemplateBean.INPUTMESSAGETYPETYPESYSTEM\_PROPERTY 

com.ibm.bpe.clientmodel.bean.ProcessInstanceBean.INPUTMESSAGETYPETYPESYSTEMNAME\_PROPERTY 

com.ibm.bpe.clientmodel.bean.ActivityServiceTemplateBean.INPUTMESSAGETYPETYPESYSTEMNAME\_PROPERTY 

com.ibm.bpe.clientmodel.bean.ActivityInstanceBean.INPUTMESSAGETYPETYPESYSTEMNAME\_PROPERTY 

com.ibm.task.api.JspUsageEnum.INSTANCE 

com.ibm.bpe.clientmodel.bean.ProcessTemplateBean.OUTPUTMESSAGETYPETYPESYSTEM\_PROPERTY 

com.ibm.bpe.clientmodel.bean.ProcessInstanceBean.OUTPUTMESSAGETYPETYPESYSTEMNAME\_PROPERTY 

com.ibm.bpe.clientmodel.bean.ActivityInstanceBean.OUTPUTMESSAGETYPETYPESYSTEMNAME\_PROPERTY 

com.ibm.bpe.clientmodel.bean.ProcessTemplateBean.PROCESSADMINSTRATORS\_PROPERTY 

com.ibm.bpe.api.WorkItemData.REASON\_POTENTIAL\_SENDER
Not used.

com.ibm.task.api.WorkItem.REASON\_POTENTIAL\_SENDER
Not used.

com.ibm.bpe.api.ActivityInstanceActions.RESCHEDULE
As of version 7.0, replaced by RESCHEDULE\_TIMER.

com.ibm.bpe.api.ActivityInstanceActionIndex.RESCHEDULE
As of version 7.0, replaced by RESCHEDULE\_TIMER.

com.ibm.bpe.api.ProcessInstanceActions.SENDEVENT
As of version 7.5, no replacement.

com.ibm.bpe.api.ProcessInstanceActions.SETCUSTOMATTRIBUTE
Use SETCUSTOMPROPERTY.

com.ibm.bpe.api.ActivityInstanceActions.SETCUSTOMATTRIBUTE
As of version 6.0, replaced by SETCUSTOMPROPERTY.

com.ibm.task.api.Task.STATE\_FAILING 

com.ibm.task.api.Task.STATE\_PROCESSING\_UNDO 

com.ibm.task.api.Task.STATE\_SKIPPED 

com.ibm.task.api.Task.STATE\_STOPPED 

com.ibm.task.api.Task.STATE\_TERMINATING 

com.ibm.task.api.Task.STATE\_WAITING 

com.ibm.task.api.JspUsageEnum.TEMPLATE

- Deprecated Methods 

Method and Description

com.ibm.websphere.bo.BOCopy.copyInto(DataObject, DataObject, String)
Instead call copy on the source and then set the copy into the destination.

com.ibm.websphere.bo.BOCopy.copyIntoShallow(DataObject, DataObject, String)
Instead call copy on the source and then set the copy into the destination.

com.ibm.websphere.bo.BOCopy.copyPropertyInto(DataObject, String, DataObject, String)
Instead get the property on the source and set on the destination.

com.ibm.websphere.bo.BOFactory.createByClass(Class)
This method is going to be removed.

com.ibm.task.api.HumanTaskManagerService.createMessage(String, String)
As of version 6.0, replaced by createInputMessage,
 createOutputMessage, and
 createFaultMessage.

com.ibm.task.api.HumanTaskManagerDelegate.createMessage(String, String)
As of version 6.0, replaced by createInputMessage,
 createOutputMessage, and
 createFaultMessage.

com.ibm.task.api.HumanTaskManagerService.createMessage(TKIID, String)
As of version 6.0, replaced by createInputMessage,
 createOutputMessage, and
 createFaultMessage.

com.ibm.task.api.HumanTaskManagerDelegate.createMessage(TKIID, String)
As of version 6.0, replaced by createInputMessage,
 createOutputMessage, and
 createFaultMessage.

com.ibm.bpe.api.LocalBusinessFlowManager.deleteWorkList(String)
As of version 6.0, replaced by deleteStoredQuery.

com.ibm.bpe.api.BusinessFlowManagerService.deleteWorkList(String)
As of version 6.0, replaced by deleteStoredQuery.

com.ibm.bpe.api.BusinessFlowManager.deleteWorkList(String)
As of version 6.0, replaced by deleteStoredQuery.

com.ibm.wbiserver.manualrecovery.FailedEventManager.discardFailedEvents(String[])
since 6.2 Use discardFailedEvents(List failedEvents) instead.

com.ibm.bpe.api.LocalBusinessFlowManager.executeWorkList(String)
As of version 6.0, replaced by query.

com.ibm.bpe.api.BusinessFlowManagerService.executeWorkList(String)
As of version 6.0, replaced by query.

com.ibm.bpe.api.BusinessFlowManager.executeWorkList(String)
As of version 6.0, replaced by query.

com.ibm.task.api.HumanTaskManagerService.getAbsence()
As of version 7.0, replaced by getUserSubstitutionDetail.
 

com.ibm.task.api.HumanTaskManagerDelegate.getAbsence()
As of version 7.0, replaced by getUserSubstitutionDetail.
 

com.ibm.task.api.HumanTaskManagerService.getAbsence(String)
As of version 7.0, replaced by getUserSubstitutionDetail.

com.ibm.task.api.HumanTaskManagerDelegate.getAbsence(String)
As of version 7.0, replaced by getUserSubstitutionDetail.

com.ibm.websphere.wsaddr10.ReferenceParametersType.getAny() 

com.ibm.websphere.wsaddr10.MetadataType.getAny() 

com.ibm.websphere.wsaddr10.EndpointReferenceType.getAny() 

com.ibm.websphere.wsaddr10.RelatesToType.getAnyAttribute() 

com.ibm.websphere.wsaddr10.ReferenceParametersType.getAnyAttribute() 

com.ibm.websphere.wsaddr10.ProblemActionType.getAnyAttribute() 

com.ibm.websphere.wsaddr10.MetadataType.getAnyAttribute() 

com.ibm.websphere.wsaddr10.EndpointReferenceType.getAnyAttribute() 

com.ibm.websphere.wsaddr10.AttributedUnsignedLongType.getAnyAttribute() 

com.ibm.websphere.wsaddr10.AttributedURIType.getAnyAttribute() 

com.ibm.websphere.wsaddr10.AttributedQNameType.getAnyAttribute() 

com.ibm.bpe.api.WorkItemData.getAssociatedObjectType()
As of version 7.0,0.3, obsolete for shared work items.

com.ibm.task.api.WorkItem.getAssociatedObjectType()
As of version 7.0,0.3, obsolete for shared work items.

com.ibm.bpe.api.WorkItemData.getAssociatedOid()
As of version 7.0,0.3, obsolete for shared work items.

com.ibm.task.api.WorkItem.getAssociatedOid()
As of version 7.0,0.3, obsolete for shared work items.

com.ibm.bpe.api.ProcessTemplateData.getAutoDelete()
As of version 6.1, replaced by getAutoDeletionMode.

com.ibm.bpe.clientmodel.bean.ProcessTemplateBean.getAutoDelete() 

com.ibm.websphere.sibx.smobo.ServiceMessageObject.getBodyForSCAMessage(boolean, boolean) 

com.ibm.websphere.sibx.smobo.ServiceMessageObject.getBodyPopulated() 

com.ibm.bpe.api.WorkItemData.getCreationTime()
As of version 7.0,0.3, obsolete for shared work items.

com.ibm.task.api.WorkItem.getCreationTime()
As of version 7.0,0.3, obsolete for shared work items.

com.ibm.wbiserver.manualrecovery.FailedEventManager.getFailedEventsForDestination(String, String, String, int)
since 6.2 use FailedEventManager.queryFailedEvents(QueryFilters queryFilters, int offset, int maxRows) instead.

com.ibm.wbiserver.manualrecovery.FailedEventManager.getFailedEventsForTimePeriod(Date, Date, int)
since 6.2 use FailedEventManager.queryFailedEvents(QueryFilters queryFilters, int offset, int maxRows) instead.

com.ibm.wbiserver.manualrecovery.FailedEventManager.getFailedEventWithParameters(String)
since 6.2 use FailedEventManager.getEventDetailForSCA(FailedEvent failedEvent) instead.

com.ibm.bpe.api.WorkItemData.getID()
As of version 7.0,0.3, obsolete for shared work items.

com.ibm.task.api.WorkItem.getID()
As of version 7.0,0.3, obsolete for shared work items.

com.ibm.bpe.api.ProcessTemplateData.getInputMessageTypeTypeSystemName()
As of version 6.0, no replacement.

com.ibm.bpe.api.ProcessInstanceData.getInputMessageTypeTypeSystemName()
As of version 6.0, no replacement.

com.ibm.bpe.api.ActivityServiceTemplateData.getInputMessageTypeTypeSystemName()
As of version 6.0, no replacement.

com.ibm.bpe.api.ActivityInstanceData.getInputMessageTypeTypeSystemName()
As of version 6.0, no replacement.

com.ibm.bpe.clientmodel.bean.ProcessTemplateBean.getInputMessageTypeTypeSystemName() 

com.ibm.bpe.clientmodel.bean.ProcessInstanceBean.getInputMessageTypeTypeSystemName() 

com.ibm.bpe.clientmodel.bean.ActivityServiceTemplateBean.getInputMessageTypeTypeSystemName() 

com.ibm.bpe.clientmodel.bean.ActivityInstanceBean.getInputMessageTypeTypeSystemName() 

com.ibm.bpe.api.WorkItemData.getObjectID()
As of version 7.0,0.3, obsolete for shared work items.

com.ibm.task.api.WorkItem.getObjectID()
As of version 7.0,0.3, obsolete for shared work items.

com.ibm.bpe.api.WorkItemData.getObjectType()
As of version 7.0,0.3, obsolete for shared work items.

com.ibm.task.api.WorkItem.getObjectType()
As of version 7.0,0.3, obsolete for shared work items.

com.ibm.bpe.clientmodel.BFMConnection.getObserver()
As of version 8.0.1, the reporting feature is no longer supported. This method always returns false.

com.ibm.task.clientmodel.HTMConnection.getObserver()
As of version 8.0.1, the reporting feature is no longer supported. This method always returns false.

com.ibm.bpe.api.ProcessTemplateData.getOutputMessageTypeTypeSystemName()
As of version 6.0, no replacement.

com.ibm.bpe.api.ProcessInstanceData.getOutputMessageTypeTypeSystemName()
As of version 6.0, no replacement.

com.ibm.bpe.api.ActivityInstanceData.getOutputMessageTypeTypeSystemName()
As of version 6.0, no replacement.

com.ibm.bpe.clientmodel.bean.ProcessTemplateBean.getOutputMessageTypeTypeSystemName() 

com.ibm.bpe.clientmodel.bean.ProcessInstanceBean.getOutputMessageTypeTypeSystemName() 

com.ibm.bpe.clientmodel.bean.ActivityInstanceBean.getOutputMessageTypeTypeSystemName() 

com.ibm.bpe.api.ProcessTemplateData.getProcessAdministrators()
As of version 6.0.2, replaced by HumanTaskManager.getUsersInRole(getAdminTaskTemplateID(), WorkItem.REASON\_ADMINISTRATOR).

com.ibm.bpe.clientmodel.bean.ProcessTemplateBean.getProcessAdministrators() 

com.ibm.websphere.sca.jms.data.impl.JMSDataBindingImplJava.getSerializableObject()
JMSDataBindingImplJava.getObject() is used instead

com.ibm.websphere.sibx.smobo.ServiceMessageObject.getSoapFaultInfoPopulated() 

com.ibm.task.api.HumanTaskManagerService.getSubstitutes()
As of version 7.0, replaced by getUserSubstitutionDetail.
 

com.ibm.task.api.HumanTaskManagerDelegate.getSubstitutes()
As of version 7.0, replaced by getUserSubstitutionDetail.
 

com.ibm.task.api.HumanTaskManagerService.getSubstitutes(String)
As of version 7.0, replaced by getUserSubstitutionDetail.

com.ibm.task.api.HumanTaskManagerDelegate.getSubstitutes(String)
As of version 7.0, replaced by getUserSubstitutionDetail.

com.ibm.websphere.bo.BOType.getTypeByClass(Class)
This method is going to be removed.

com.ibm.bpe.api.JspLocation.getUriAsString()
Use method JspLocation.getUri() instead.

com.ibm.task.api.JspLocation.getUriAsString()
Use method JspLocation.getUri() instead.

com.ibm.bpe.api.ProcessTemplateData.getVersion()
As of version 7.5, no replacement.

com.ibm.bpe.api.CustomClientSettings.getWebClientSetting()
Use CustomClientSettings.getWebClientSetting(String)
            instead.

com.ibm.task.api.CustomClientSettings.getWebClientSetting()
Use CustomClientSettings.getWebClientSetting(String) instead.

com.ibm.bpe.api.LocalBusinessFlowManager.getWorkList(String)
As of version 6.0, replaced by getStoredQuery.

com.ibm.bpe.api.BusinessFlowManagerService.getWorkList(String)
As of version 6.0, replaced by getStoredQuery.

com.ibm.bpe.api.BusinessFlowManager.getWorkList(String)
As of version 6.0, replaced by getStoredQuery.

com.ibm.bpe.api.LocalBusinessFlowManager.getWorkListActions()
As of version 6.0.2, no replacement.
 

com.ibm.bpe.api.BusinessFlowManagerService.getWorkListActions()
As of version 6.0.2, no replacement.
 

com.ibm.bpe.api.BusinessFlowManager.getWorkListActions()
As of version 6.0.2, no replacement.
 

com.ibm.bpe.api.LocalBusinessFlowManager.getWorkListNames()
As of version 6.0, replaced by getStoredQueryNames.
 

com.ibm.bpe.api.BusinessFlowManagerService.getWorkListNames()
As of version 6.0, replaced by getStoredQueryNames.
 

com.ibm.bpe.api.BusinessFlowManager.getWorkListNames()
As of version 6.0, replaced by getStoredQueryNames.
 

com.ibm.bpe.api.LocalBusinessFlowManager.initiateAndClaimFirst(String, String, String, String, ClientObjectWrapper)
As of version 7.5, replaced by initiateAndClaimFirst.

com.ibm.bpe.api.BusinessFlowManagerService.initiateAndClaimFirst(String, String, String, String, ClientObjectWrapper)
As of version 7.5, replaced by initiateAndClaimFirst.

com.ibm.bpe.api.BusinessFlowManager.initiateAndClaimFirst(String, String, String, String, ClientObjectWrapper)
As of version 7.5, replaced by initiateAndClaimFirst.

com.ibm.bpe.api.LocalBusinessFlowManager.initiateAndClaimFirst(String, VTID, ATID, String, ClientObjectWrapper)
As of version 7.5, replaced by initiateAndClaimFirst.

com.ibm.bpe.api.BusinessFlowManagerService.initiateAndClaimFirst(String, VTID, ATID, String, ClientObjectWrapper)
As of version 7.5, replaced by initiateAndClaimFirst.

com.ibm.bpe.api.BusinessFlowManager.initiateAndClaimFirst(String, VTID, ATID, String, ClientObjectWrapper)
As of version 7.5, replaced by initiateAndClaimFirst.

com.ibm.websphere.sca.jms.data.impl.JMSDataBindingImplJava.isPrimitiveType()
JMSDataBindingImplJava.isObjectType() is used instead

com.ibm.wbiserver.rel.RelationshipService.maintainIdentityRelationship(String, String, DataObject, DataObject, DataObject, DataObject, String)
since WPS6.1 use correlate to maintain relationships
 and correlateToList and correlateFromList to maintain containment relatoinships

com.ibm.bpe.api.LocalBusinessFlowManager.newWorkList(String, String, String, String, Integer, TimeZone)
As of version 6.0, replaced by createStoredQuery.

com.ibm.bpe.api.BusinessFlowManagerService.newWorkList(String, String, String, String, Integer, TimeZone)
As of version 6.0, replaced by createStoredQuery.

com.ibm.bpe.api.BusinessFlowManager.newWorkList(String, String, String, String, Integer, TimeZone)
As of version 6.0, replaced by createStoredQuery.

com.ibm.task.spi.APIEventHandlerPlugin.postClaim(Task, Object, TaskException)
since v6.0.2 - use postClaim(Task, Serializable, TaskException)

com.ibm.task.spi.APIEventHandler.postClaim(Task, Object, TaskException)
since v6.0.2 - use postClaim(Task, Serializable, TaskException)

com.ibm.task.spi.APIEventHandlerPlugin.postReplaceWorkItem(Task, int, String, TaskException)
since v7.0 - this method is not used.

com.ibm.task.spi.APIEventHandlerPlugin.postSetBinaryCustomProperty(Task, String, String, Serializable, TaskException)
since v6.0.2 - use postSetBinaryCustomProperty(Task, BinaryCustomProperty)

com.ibm.task.spi.APIEventHandler.postSetBinaryCustomProperty(Task, String, String, Serializable, TaskException)
since v6.0.2 - use postSetBinaryCustomProperty(Task, BinaryCustomProperty)

com.ibm.task.spi.APIEventHandlerPlugin.preReplaceWorkItem(Task, int, String)
since v7.0 - this method is not used.

com.ibm.task.spi.APIEventHandlerPlugin.preSetBinaryCustomProperty(Task, String, String, Serializable)
since v6.0.2 - use preSetBinaryCustomProperty(Task, BinaryCustomProperty)

com.ibm.task.spi.APIEventHandler.preSetBinaryCustomProperty(Task, String, String, Serializable)
since v6.0.2 - use preSetBinaryCustomProperty(Task, BinaryCustomProperty)

com.ibm.bpe.api.LocalBusinessFlowManager.query(String, Integer)
As of version 6.0.2,  replaced by query(Sting storedQueryName, Integer skipTuples, List parameters),

com.ibm.bpe.api.BusinessFlowManagerService.query(String, Integer)
As of version 6.0.2,  replaced by query(Sting storedQueryName, Integer skipTuples, List parameters),

com.ibm.bpe.api.BusinessFlowManager.query(String, Integer)
As of version 6.0.2,  replaced by query(Sting storedQueryName, Integer skipTuples, List parameters),

com.ibm.task.api.HumanTaskManagerService.query(String, Integer)
As of version 6.0.2, replaced by query(Sting storedQueryName, Integer skipTuples, List parameters),

com.ibm.task.api.HumanTaskManagerDelegate.query(String, Integer)
As of version 6.0.2, replaced by query(Sting storedQueryName, Integer skipTuples, List parameters),

com.ibm.bpe.api.LocalBusinessFlowManager.query(String, Integer, Integer)
As of version 6.0.2, replaced by query(Sting storedQueryName, Integer skipTuples, Integer threshold, List parameters),

com.ibm.bpe.api.BusinessFlowManagerService.query(String, Integer, Integer)
As of version 6.0.2, replaced by query(Sting storedQueryName, Integer skipTuples, Integer threshold, List parameters),

com.ibm.bpe.api.BusinessFlowManager.query(String, Integer, Integer)
As of version 6.0.2, replaced by query(Sting storedQueryName, Integer skipTuples, Integer threshold, List parameters),

com.ibm.task.api.HumanTaskManagerService.query(String, Integer, Integer)
As of version 6.0.2, replaced by query(Sting storedQueryName, Integer skipTuples, Integer threshold, List parameters),

com.ibm.task.api.HumanTaskManagerDelegate.query(String, Integer, Integer)
As of version 6.0.2, replaced by query(Sting storedQueryName, Integer skipTuples, Integer threshold, List parameters),

com.ibm.wbiserver.manualrecovery.FailedEventManager.resubmitFailedEvents(String[])
since 6.2 use FailedEventManager.resubmitFailedEvents(List failedEvents) instead

com.ibm.task.clientmodel.HTMConnection.retrieve(TKIID)
use HTMConnection.retrieve(OID)

com.ibm.websphere.sibx.smobo.ServiceMessageObject.saveSCAData(Message, ServiceMessageObject) 

com.ibm.task.api.HumanTaskManagerService.setAbsence(boolean)
As of version 7.0, replaced by setUserSubstitutionDetail.

com.ibm.task.api.HumanTaskManagerDelegate.setAbsence(boolean)
As of version 7.0, replaced by setUserSubstitutionDetail.

com.ibm.task.api.HumanTaskManagerService.setAbsence(String, boolean)
As of version 7.0, replaced by setUserSubstitutionDetail.

com.ibm.task.api.HumanTaskManagerDelegate.setAbsence(String, boolean)
As of version 7.0, replaced by setUserSubstitutionDetail.

com.ibm.websphere.sibx.smobo.ServiceMessageObject.setBodyPopulated() 

com.ibm.bpe.api.FaultReplyException.setFaultMessage(Serializable) 

com.ibm.websphere.ant.tasks.ServiceDeployTask.setFileEncoding(String)
set the -Dfile.encoding jvm parameter instead

com.ibm.websphere.ant.tasks.ServiceDeployTask.setJavaDebug(String)
no longer applicable

com.ibm.websphere.ant.tasks.ServiceDeployTask.setNoJ2EEDeploy(boolean)
no longer applicable

com.ibm.websphere.ant.tasks.ServiceDeployTask.setNoJavaSource(boolean)
no longer applicable

com.ibm.bpe.clientmodel.BFMConnection.setObserver(Boolean)
As of version 8.0.1, the reporting feature is no longer supported. This value is ignored.

com.ibm.task.clientmodel.HTMConnection.setObserver(Boolean)
As of version 8.0.1, the reporting feature is no longer supported. This value is ignored.

com.ibm.websphere.sca.jms.data.impl.JMSDataBindingImplJava.setPrimitiveType(boolean)
JMSDataBindingImplJava.setObjectType(boolean) is used instead

com.ibm.websphere.ant.tasks.ServiceDeployTask.setProgressMonitor(String)
no longer applicable

com.ibm.websphere.sca.jms.data.impl.JMSDataBindingImplJava.setSerializableObject(Serializable)
JMSDataBindingImplJava.setObject(Object) is used instead

com.ibm.websphere.sibx.smobo.ServiceMessageObject.setSoapFaultInfoPopulated() 

com.ibm.task.api.HumanTaskManagerService.setSubstitutes(List)
As of version 7.0, replaced by setUserSubstitutionDetail.

com.ibm.task.api.HumanTaskManagerDelegate.setSubstitutes(List)
As of version 7.0, replaced by setUserSubstitutionDetail.

com.ibm.task.api.HumanTaskManagerService.setSubstitutes(String, List)
As of version 7.0, replaced by setUserSubstitutionDetail.

com.ibm.task.api.HumanTaskManagerDelegate.setSubstitutes(String, List)
As of version 7.0, replaced by setUserSubstitutionDetail.

- Deprecated Constructors 

Constructor and Description

com.ibm.task.api.ApplicationVetoException(Object[])
This exception does not support message variables. Use ApplicationVetoException.ApplicationVetoException()

com.ibm.task.api.ApplicationVetoException(Object[], Throwable)
This exception does not support message variables. Use ApplicationVetoException.ApplicationVetoException()

com.ibm.bpe.api.BpelException(String, Object[])
Use BpelException.BpelException(String, Object[], String) instead.

com.ibm.bpe.api.BpelException(String, Object[], Throwable)
Use BpelException.BpelException(String, Object[], String, Throwable) instead.

com.ibm.bpc.clientcore.ClientException(String, Object[], Throwable)
Use ClientException.ClientException(String, String, Object[], Throwable) instead.

com.ibm.bpe.api.EngineMissingReceiveException(String, Object[])
Use EngineMissingReceiveException.EngineMissingReceiveException(String, Object[], String) instead.

com.ibm.bpe.api.EngineMissingReceiveException(String, Object[], Throwable)
Use EngineMissingReceiveException.EngineMissingReceiveException(String, Object[], String, Throwable) instead.

com.ibm.bpe.api.EngineMissingReplyException(String, Object[])
Use EngineMissingReplyException.EngineMissingReplyException(String, Object[], String) instead.

com.ibm.bpe.api.EngineMissingReplyException(String, Object[], Throwable)
Use EngineMissingReplyException.EngineMissingReplyException(String, Object[], String, Throwable) instead.

com.ibm.bpe.api.FaultReplyException(Object[], String, Serializable) 

com.ibm.bpe.api.FaultReplyException2(Object[], String, String, String, Serializable) 

com.ibm.bpe.api.RuntimeFaultException(String, Object[])
Use RuntimeFaultException.RuntimeFaultException(String, Object[], String) instead.

com.ibm.bpe.api.RuntimeFaultException(String, Object[], Throwable)
Use RuntimeFaultException.RuntimeFaultException(String, Object[], String, Throwable) instead.

com.ibm.bpe.api.SendReplyErrorException(String, Object[])
Use SendReplyErrorException.SendReplyErrorException(String, String, Object[]) instead.

com.ibm.bpe.api.SendReplyErrorException(String, Object[], Throwable)
Use SendReplyErrorException.SendReplyErrorException(String, Object[], String, Throwable) instead.

com.ibm.bpe.api.SystemFaultException(String, Object[])
Use SystemFaultException.SystemFaultException(String, Object[], String) instead.

com.ibm.task.api.SystemFaultException(String, Object[])
Use SystemFaultException.SystemFaultException(String, Object[], String) instead.

com.ibm.bpe.api.SystemFaultException(String, Object[], Throwable)
Use SystemFaultException.SystemFaultException(String, Object[], String, Throwable) instead.

com.ibm.task.api.SystemFaultException(String, Object[], Throwable)
Use SystemFaultException.SystemFaultException(String, Object[], String, Throwable) instead.

com.ibm.task.api.TaskError(String, Object[])
Use TaskError.TaskError(String, Object[], String) instead.

com.ibm.task.api.TaskError(String, Object[], Throwable)
Use TaskError.TaskError(String, Object[], String, Throwable) instead.

com.ibm.task.api.TaskException(String, Object[])
Use TaskException.TaskException(String, Object[], String) instead.

com.ibm.task.api.TaskException(String, Object[], Throwable)
Use TaskException.TaskException(String, Object[], String, Throwable) instead.

com.ibm.bpe.api.UnhandledFaultException(String, Object[])
Use UnhandledFaultException.UnhandledFaultException(String, Object[], String) instead.

com.ibm.bpe.api.UnhandledFaultException(String, Object[], Throwable)
Use UnhandledFaultException.UnhandledFaultException(String, Object[], String, Throwable) instead.

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