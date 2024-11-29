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

## Interface WorkBasketManagerService

- All Known Subinterfaces:
HumanTaskManager, LocalHumanTaskManager, LocalWorkBasketManagerService

public interface WorkBasketManagerService
WorkBasketManagerService defines the work basket methods that can be called by a local or remote client.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary

Methods 

Modifier and Type
Method and Description

WBID
createWorkBasket(WorkBasketDefinition workBasketDefinition)
Creates a work basket from the specified work basket definition.

void
deleteWorkBasket(java.lang.String identifier)
Deletes the specified work basket
  using a string representation of the work basket ID or the work basket name.

void
deleteWorkBasket(WBID wbid)
Deletes the specified work basket using the work basket ID.

java.util.List
distributeTasksToWorkBasket(java.lang.String[] tkiids,
                           java.lang.String identifier)
Distributes the specified task instances to the specified work basket
 using string representations of the task instance and work basket IDs.

java.util.List
distributeTasksToWorkBasket(TKIID[] tkiids,
                           WBID wbid)
Distributes the specified task instances to the specified work basket
 using task instance and work basket IDs.

WorkItem[]
getAllWorkItemsForWorkBasket(java.lang.String identifier)
Returns all work item assignments associated to the specified work basket
  using a string representation of the work basket ID or the work basket name.

WorkItem[]
getAllWorkItemsForWorkBasket(WBID wbid)
Returns all work item assignments associated to the specified work basket
  using the work basket ID.

boolean[][]
getAvailableActionFlagsForWorkBaskets(java.lang.String[] identifiers)
Returns the actions that can be called for the specified work baskets
 by the logged-on user
 using string representations of the work basket IDs or the work basket names.

boolean[][]
getAvailableActionFlagsForWorkBaskets(WBID[] wbids)
Returns the actions that can be called for the specified work baskets
 by the logged-on user using work basket IDs.

int[]
getAvailableActionsForWorkBasket(java.lang.String identifier)
Returns the actions that can be called by the logged-on user
 for the specified work basket
 using a string representation of the work basket ID or the work basket name.

int[]
getAvailableActionsForWorkBasket(WBID wbid)
Returns the actions that can be called by the logged-on user
 for the specified work basket
 using the work basket ID.

java.util.List
getDistributionTargets(java.lang.String identifier)
Retrieves the distribution targets of the specified work basket
 using a string representation of the work basket ID or the work basket name.

java.util.List
getDistributionTargets(WBID wbid)
Retrieves the distribution targets of the specified work basket
 using the work basket ID.

WorkBasket
getWorkBasket(java.lang.String identifier)
Retrieves the specified work basket using a string
 representation of the work basket ID or the work basket name.

WorkBasket
getWorkBasket(WBID wbid)
Retrieves the specified work basket using the work basket ID.

WorkBasketDefinition
getWorkBasketDefinition(java.lang.String identifier)
Retrieves the definition of the specified work basket using a string
 representation of the work basket ID or the work basket name.

WorkBasketDefinition
getWorkBasketDefinition(WBID wbid)
Retrieves the definition of the specified work basket using the work basket ID.

WorkItem[]
getWorkItemsForWorkBasket(java.lang.String identifier)
Returns the work item assignments for the logged-on user and the
  specified work basket using a string representation of the work basket ID or the work basket name.

WorkItem[]
getWorkItemsForWorkBasket(WBID wbid)
Returns the work item assignments for the logged-on user and the
  specified work basket using the work basket ID.

boolean
isWorkBasketSystemAdministrator()
States whether the logged-on user is a system administrator for work baskets.

java.util.List
removeAsDistributionTarget(java.lang.String identifier)
Removes the specified work basket as a distribution target from all referencing work baskets
  using a string representation of the work basket ID or the work basket name.

java.util.List
removeAsDistributionTarget(WBID wbid)
Removes the specified work basket as a distribution target from all referencing work baskets
  
  The caller must be the work basket system administrator.

java.util.List
transferTasksToWorkBasket(java.lang.String[] tkiids,
                         java.lang.String identifier,
                         boolean cancelClaimIfNeeded)
Transfers the specified task instances to the specified work basket
 using string representations of the task instance and work basket IDs or the work basket name.

java.util.List
transferTasksToWorkBasket(TKIID[] tkiids,
                         WBID wbid,
                         boolean cancelClaimIfNeeded)
Transfers the specified task instances to the specified work basket
 using task instance and work basket IDs.

void
updateWorkBasket(WorkBasketDefinition workBasketDefinition)
Updates a work basket with values from the specified work basket definition.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - createWorkBasket
WBID createWorkBasket(WorkBasketDefinition workBasketDefinition)
                      throws ArchiveUnsupportedOperationException,
                             CannotCreateWorkItemException,
                             InvalidAssignmentReasonException,
                             InvalidLengthException,
                             InvalidPropertyValueException,
                             NotAuthorizedException,
                             ParameterNullException,
                             WorkBasketAlreadyExistsException,
                             WorkBasketNotEnabledException,
                             UnexpectedFailureException,
                             java.rmi.RemoteException,
                             javax.ejb.EJBException
Creates a work basket from the specified work basket definition.
 
 The caller must be a work basket system administrator.
 
 The action associated to this method is WorkBasketActions.CREATEWORKBASKET.
 
 This method is not supported in archive mode.
Parameters:workBasketDefinition - The WorkBasketDefinition
  from which a work basket is to be created.
 
Returns:WBID -
    The object ID of the work basket created.
 
Throws:
ArchiveUnsupportedOperationException
CannotCreateWorkItemException
InvalidAssignmentReasonException
InvalidLengthException
InvalidPropertyValueException
NotAuthorizedException
ParameterNullException
WorkBasketAlreadyExistsException
WorkBasketNotEnabledException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0 Feature Pack
 
Change History

Release
 Modification
 
7.0.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
    - deleteWorkBasket
void deleteWorkBasket(java.lang.String identifier)
                      throws IdWrongFormatException,
                             IdWrongTypeException,
                             IsDistributionTargetException,
                             NotAuthorizedException,
                             ObjectDoesNotExistException,
                             WorkBasketNotEmptyException,
                             WorkBasketNotEnabledException,
                             UnexpectedFailureException,
                             java.rmi.RemoteException,
                             javax.ejb.EJBException
Deletes the specified work basket
  using a string representation of the work basket ID or the work basket name.
  
  The work basket must not contain any task instances and must not be used as
  distribution target by other work baskets.
  
  The caller must be the work basket system administrator.
 
 The action associated to this method is WorkBasketActions.DELETEWORKBASKET.
Parameters:identifier - A string representation of the work basket ID or the work basket name
    that is used to identify the work basket.
 
Throws:
IdWrongFormatException
IdWrongTypeException
IsDistributionTargetException
NotAuthorizedException
ObjectDoesNotExistException
WorkBasketNotEmptyException
WorkBasketNotEnabledException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0 Feature Pack
    - deleteWorkBasket
void deleteWorkBasket(WBID wbid)
                      throws IdWrongFormatException,
                             IsDistributionTargetException,
                             NotAuthorizedException,
                             ObjectDoesNotExistException,
                             WorkBasketNotEmptyException,
                             WorkBasketNotEnabledException,
                             UnexpectedFailureException,
                             java.rmi.RemoteException,
                             javax.ejb.EJBException
Deletes the specified work basket using the work basket ID.
  
  The work basket must not contain any task instances and must not be used as
  distribution target by other work baskets.
  
  The caller must be the work basket system administrator.
 
 The action associated to this method is WorkBasketActions.DELETEWORKBASKET.
Parameters:wbid - The work basket ID that is used to identify the work basket.
 
Throws:
IdWrongFormatException
IsDistributionTargetException
NotAuthorizedException
ObjectDoesNotExistException
WorkBasketNotEmptyException
WorkBasketNotEnabledException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0 Feature Pack
    - distributeTasksToWorkBasket java.util.List distributeTasksToWorkBasket(java.lang.String[] tkiids, java.lang.String identifier) throws ArchiveUnsupportedOperationException , IdWrongFormatException , IdWrongTypeException , WorkBasketDoesNotExistException , WorkBasketNotEnabledException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Distributes the specified task instances to the specified work basket using string representations of the task instance and work basket IDs. The task instances must be in the ready state, or for invocation tasks, in the running state. Note that invocation task instances are also known as originating task instances. The task instances' read flags are set to false. The transferredToWorkBasket flags remain unchanged. The caller must be authorized to perform action DISTRIBUTE for each work basket that contains one of the specified task instances, that is, have distributor or transfer initiator rights on the work baskets. The specified target work basket must be in the list of distribution targets for each work basket that contains one of the specified task instances. The action associated to this method is WorkBasketActions.DISTRIBUTE . This method is not supported in archive mode. Parameters: tkiids - An array of string representations of task instance IDs that are used to identify the task instances. identifier - A string representation of the work basket ID or the work basket name. This is used to identify the work basket. Returns: List - A list of TaskResult objects, one for every task instance specified. Refer to TaskResult . If a single transfer operation fails because any of the following exceptions has been thrown, then the result object contains the respective exception. Otherwise, the TaskException property is null. If any of these exceptions is thrown, processing continues. If another exception is thrown, a rollback of the global transaction is enforced, and all transfers are undone. Throws: ArchiveUnsupportedOperationException IdWrongFormatException IdWrongTypeException WorkBasketDoesNotExistException WorkBasketNotEnabledException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 7.0 Feature Pack Change History Release Modification 7.0.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode.

#### distributeTasksToWorkBasket

```
java.util.List distributeTasksToWorkBasket(java.lang.String[] tkiids,
                                         java.lang.String identifier)
                                           throws ArchiveUnsupportedOperationException,
                                                  IdWrongFormatException,
                                                  IdWrongTypeException,
                                                  WorkBasketDoesNotExistException,
                                                  WorkBasketNotEnabledException,
                                                  UnexpectedFailureException,
                                                  java.rmi.RemoteException,
                                                  javax.ejb.EJBException
```

The task instances must be in the ready state, or for invocation tasks, in the running state.
 Note that invocation task instances are also known as originating task instances.
 
 The task instances' read flags are set to false. The transferredToWorkBasket flags remain unchanged.
 
 The caller must be authorized to perform action
 DISTRIBUTE for each work basket
 that contains one of the specified task instances, that is,
 have distributor or transfer initiator rights on the work baskets.
 The specified target work basket must be in the list of distribution targets for each work basket
 that contains one of the specified task instances.
 
 The action associated to this method is WorkBasketActions.DISTRIBUTE.
 
 This method is not supported in archive mode.

If a single transfer operation fails because any of the following exceptions has been thrown,
 then the result object contains the respective exception.
 Otherwise, the TaskException property is null.
 
com.ibm.task.api.IsNotDistributionTargetException
 com.ibm.task.api.TaskDoesNotExistException
 com.ibm.task.api.TaskNotInWorkBasketException
 com.ibm.task.api.WorkBasketNotAuthorizedException
 com.ibm.task.api.WrongTaskStateException
 
 If any of these exceptions is thrown, processing continues.
 If another exception is thrown, a rollback of the global transaction is enforced,
 and all transfers are undone.

Change History

Release
 Modification
 
7.0.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- distributeTasksToWorkBasket java.util.List distributeTasksToWorkBasket(TKIID [] tkiids, WBID wbid) throws ArchiveUnsupportedOperationException , IdWrongFormatException , WorkBasketDoesNotExistException , WorkBasketNotEnabledException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Distributes the specified task instances to the specified work basket using task instance and work basket IDs. The task instances must be in the ready state, or for invocation tasks, in the running state. Note that invocation task instances are also known as originating task instances. The task instances' read flags are set to false. The transferredToWorkBasket flags remain unchanged. The caller must be authorized to perform action DISTRIBUTE for each work basket that contains one of the specified task instances, that is, have distributor or transfer initiator rights on the work baskets. The specified target work basket must be in the list of distribution targets for each work basket that contains one of the specified task instances. The action associated to this method is WorkBasketActions.DISTRIBUTE . This method is not supported in archive mode. Parameters: tkiids - An array of task instance IDs. wbid - The work basket ID. Returns: List - A list of TaskResult objects, one for every task instance specified. Refer to TaskResult . If a single transfer operation fails because any of the following exceptions has been thrown, then the result object contains the respective exception. Otherwise, the TaskException property is null. If any of these exceptions is thrown, processing continues. If another exception is thrown, a rollback of the global transaction is enforced, and all transfers are undone. Throws: ArchiveUnsupportedOperationException IdWrongFormatException WorkBasketDoesNotExistException WorkBasketNotEnabledException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 7.0 Feature Pack Change History Release Modification 7.0.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode.

#### distributeTasksToWorkBasket

```
java.util.List distributeTasksToWorkBasket(TKIID[] tkiids,
                                         WBID wbid)
                                           throws ArchiveUnsupportedOperationException,
                                                  IdWrongFormatException,
                                                  WorkBasketDoesNotExistException,
                                                  WorkBasketNotEnabledException,
                                                  UnexpectedFailureException,
                                                  java.rmi.RemoteException,
                                                  javax.ejb.EJBException
```

The task instances must be in the ready state, or for invocation tasks, in the running state.
 Note that invocation task instances are also known as originating task instances.
 
 The task instances' read flags are set to false. The transferredToWorkBasket flags remain unchanged.
 
 The caller must be authorized to perform action
 DISTRIBUTE for each work basket
 that contains one of the specified task instances, that is,
 have distributor or transfer initiator rights on the work baskets.
 The specified target work basket must be in the list of distribution targets for each work basket
 that contains one of the specified task instances.
 
 The action associated to this method is WorkBasketActions.DISTRIBUTE.
 
 This method is not supported in archive mode.

If a single transfer operation fails because any of the following exceptions has been thrown,
 then the result object contains the respective exception.
 Otherwise, the TaskException property is null.
 
com.ibm.task.api.IsNotDistributionTargetException
 com.ibm.task.api.TaskDoesNotExistException
 com.ibm.task.api.TaskNotInWorkBasketException
 com.ibm.task.api.WorkBasketNotAuthorizedException
 com.ibm.task.api.WrongTaskStateException
 
 If any of these exceptions is thrown, processing continues.
 If another exception is thrown, a rollback of the global transaction is enforced,
 and all transfers are undone.

Change History

Release
 Modification
 
7.0.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- getAllWorkItemsForWorkBasket
WorkItem[] getAllWorkItemsForWorkBasket(java.lang.String identifier)
                                        throws IdWrongFormatException,
                                               IdWrongTypeException,
                                               NotAuthorizedException,
                                               ObjectDoesNotExistException,
                                               WorkItemManagerException,
                                               WorkBasketNotEnabledException,
                                               UnexpectedFailureException,
                                               java.rmi.RemoteException,
                                               javax.ejb.EJBException
Returns all work item assignments associated to the specified work basket
  using a string representation of the work basket ID or the work basket name.
  
  The caller must have a work item for the specified work basket or be a
  work basket system administrator.
 
 The action associated to this method is WorkBasketActions.GETROLEINFO.
Parameters:identifier - The string representation of a work basket ID or the work basket name that is
    used to identify the work basket.
 
Returns:WorkItem[] -
    An array of work items. If there are no work items,
    an empty array is returned. Refer to WorkItem
    to view the work item properties.
 
Throws:
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
WorkItemManagerException
WorkBasketNotEnabledException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0 Feature Pack

- getAllWorkItemsForWorkBasket
WorkItem[] getAllWorkItemsForWorkBasket(WBID wbid)
                                        throws IdWrongFormatException,
                                               NotAuthorizedException,
                                               ObjectDoesNotExistException,
                                               WorkBasketNotEnabledException,
                                               WorkItemManagerException,
                                               UnexpectedFailureException,
                                               java.rmi.RemoteException,
                                               javax.ejb.EJBException
Returns all work item assignments associated to the specified work basket
  using the work basket ID.
  
  The caller must have a work item for the specified work basket or be a
  work basket system administrator.
 
 The action associated to this method is WorkBasketActions.GETROLEINFO.
Parameters:wbid - The object ID of the work basket thatis used to identify
    the work basket.
 
Returns:WorkItem[] -
    An array of work items. If there are no work items,
    an empty array is returned. Refer to WorkItem
    to view the work item properties.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
WorkBasketNotEnabledException
WorkItemManagerException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0 Feature Pack

- getAvailableActionFlagsForWorkBaskets
boolean[][] getAvailableActionFlagsForWorkBaskets(java.lang.String[] identifiers)
                                                  throws IdWrongFormatException,
                                                         IdWrongTypeException,
                                                         ObjectDoesNotExistException,
                                                         WorkBasketNotEnabledException,
                                                         UnexpectedFailureException,
                                                         java.rmi.RemoteException,
                                                         javax.ejb.EJBException
Returns the actions that can be called for the specified work baskets
 by the logged-on user
 using string representations of the work basket IDs or the work basket names.
 Refer to WorkBasketActions for possible actions.
Parameters:identifiers - An array of string representations of work basket IDs or work basket names.
 
Returns:boolean[][] -
    An array of actions that can be called for each specified work basket.
 The array contains a row per work basket and a column per possible action.
 An array entry thus indicates whether a possible action can be called for the work basket
 by the logged-on user.
 True states that the action can be called. False states that the action cannot be called.
 
 The work baskets appear in the same order as specified.
 Refer to WorkBasketActionIndex for index constants that can
 be used to access the columns of the two-dimensional array.
 
Throws:
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
WorkBasketNotEnabledException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0 Feature Pack

- getAvailableActionFlagsForWorkBaskets
boolean[][] getAvailableActionFlagsForWorkBaskets(WBID[] wbids)
                                                  throws IdWrongFormatException,
                                                         ObjectDoesNotExistException,
                                                         WorkBasketNotEnabledException,
                                                         UnexpectedFailureException,
                                                         java.rmi.RemoteException,
                                                         javax.ejb.EJBException
Returns the actions that can be called for the specified work baskets
 by the logged-on user using work basket IDs.
 Refer to WorkBasketActions for possible actions.
Parameters:wbids - An array of work basket IDs.
 
Returns:boolean[][] -
    An array of actions that can be called for each specified work basket.
 The array contains a row per work basket and a column per possible action.
 An array entry thus indicates whether a possible action can be called for the work basket
 by the logged-on user.
 True states that the action can be called. False states that the action cannot be called.
 
 The work baskets appear in the same order as specified.
 Refer to WorkBasketActionIndex for index constants that can
 be used to access the columns of the two-dimensional array.
 
Throws:
IdWrongFormatException
ObjectDoesNotExistException
WorkBasketNotEnabledException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0 Feature Pack

- getAvailableActionsForWorkBasket
int[] getAvailableActionsForWorkBasket(java.lang.String identifier)
                                       throws IdWrongFormatException,
                                              IdWrongTypeException,
                                              ObjectDoesNotExistException,
                                              WorkBasketNotEnabledException,
                                              UnexpectedFailureException,
                                              java.rmi.RemoteException,
                                              javax.ejb.EJBException
Returns the actions that can be called by the logged-on user
 for the specified work basket
 using a string representation of the work basket ID or the work basket name.
 Refer to WorkBasketActions for possible actions.
Parameters:identifier - The string representation of the work basket ID or the work basket name.
 
Returns:int[] -
    The set of possible actions.
    Returns an empty array if there are no available actions.
 
Throws:
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
WorkBasketNotEnabledException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0 Feature Pack

- getAvailableActionsForWorkBasket
int[] getAvailableActionsForWorkBasket(WBID wbid)
                                       throws IdWrongFormatException,
                                              ObjectDoesNotExistException,
                                              WorkBasketNotEnabledException,
                                              UnexpectedFailureException,
                                              java.rmi.RemoteException,
                                              javax.ejb.EJBException
Returns the actions that can be called by the logged-on user
 for the specified work basket
 using the work basket ID.
 Refer to WorkBasketActions for possible actions.
Parameters:wbid - The object ID of the work basket.
 
Returns:int[] -
    The set of possible actions.
    Returns an empty array if there are no available actions.
 
Throws:
IdWrongFormatException
ObjectDoesNotExistException
WorkBasketNotEnabledException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0 Feature Pack

- getDistributionTargets
java.util.List getDistributionTargets(java.lang.String identifier)
                                      throws IdWrongFormatException,
                                             IdWrongTypeException,
                                             NotAuthorizedException,
                                             ObjectDoesNotExistException,
                                             WorkBasketNotEnabledException,
                                             UnexpectedFailureException,
                                             java.rmi.RemoteException,
                                             javax.ejb.EJBException
Retrieves the distribution targets of the specified work basket
 using a string representation of the work basket ID or the work basket name.
 
 The caller must have distributor or transfer initiator rights on the specified work basket.
 
 The action associated to this method is WorkBasketActions.GETDISTRIBUTIONTARGETS.
Parameters:identifier - A string representation of the work basket ID or the work basket name. This is used
    to identify the work basket.
 
Returns:List -
    A list of WorkBasket objects that can be used as distribution targets.
    Note that all possible distribution targets are returned whether they can be
    used as distribution target by the logged-on user or not.
    
    The list is empty if there are no distribution targets for the specified work basket.
 
Throws:
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
WorkBasketNotEnabledException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0 Feature Pack

- getDistributionTargets
java.util.List getDistributionTargets(WBID wbid)
                                      throws IdWrongFormatException,
                                             NotAuthorizedException,
                                             ObjectDoesNotExistException,
                                             WorkBasketNotEnabledException,
                                             UnexpectedFailureException,
                                             java.rmi.RemoteException,
                                             javax.ejb.EJBException
Retrieves the distribution targets of the specified work basket
 using the work basket ID.
 
 The caller must have distributor or transfer initiator rights on the specified work basket.
 
 The action associated to this method is WorkBasketActions.GETDISTRIBUTIONTARGETS.
Parameters:wbid - The object ID of the work basket that is used to identify the work basket.
 
Returns:List -
    A list of WorkBasket objects that can be used as distribution targets.
    Note that all possible distribution targets are returned whether they can be
    used as distribution target by the logged-on user or not.
    
    The list is empty if there are no distribution targets for the specified work basket.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
WorkBasketNotEnabledException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0 Feature Pack

- getWorkBasket
WorkBasket getWorkBasket(java.lang.String identifier)
                         throws IdWrongFormatException,
                                IdWrongTypeException,
                                NotAuthorizedException,
                                ObjectDoesNotExistException,
                                WorkBasketNotEnabledException,
                                UnexpectedFailureException,
                                java.rmi.RemoteException,
                                javax.ejb.EJBException
Retrieves the specified work basket using a string
 representation of the work basket ID or the work basket name.
 
 The caller must have at least reader authority for the work basket.
 
 The action associated to this method is WorkBasketActions.GETWORKBASKET.
Parameters:identifier - A string representation of the work basket ID or the work basket name. This is used
    to identify the work basket to be retrieved.
 
Returns:WorkBasket -
    The work basket.
    Refer to WorkBasket to view the properties.
 
Throws:
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
WorkBasketNotEnabledException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0 Feature Pack

- getWorkBasket
WorkBasket getWorkBasket(WBID wbid)
                         throws IdWrongFormatException,
                                NotAuthorizedException,
                                ObjectDoesNotExistException,
                                WorkBasketNotEnabledException,
                                UnexpectedFailureException,
                                java.rmi.RemoteException,
                                javax.ejb.EJBException
Retrieves the specified work basket using the work basket ID.
 
 The caller must have at least reader authority for the work basket.
 
 The action associated to this method is WorkBasketActions.GETWORKBASKET.
Parameters:wbid - The object ID of the work basket to be retrieved.
 
Returns:WorkBasket -
    The work basket.
    Refer to WorkBasket to view the properties.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
WorkBasketNotEnabledException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0 Feature Pack

- getWorkBasketDefinition
WorkBasketDefinition getWorkBasketDefinition(java.lang.String identifier)
                                             throws IdWrongFormatException,
                                                    IdWrongTypeException,
                                                    NotAuthorizedException,
                                                    ObjectDoesNotExistException,
                                                    WorkBasketNotEnabledException,
                                                    UnexpectedFailureException,
                                                    java.rmi.RemoteException,
                                                    javax.ejb.EJBException
Retrieves the definition of the specified work basket using a string
 representation of the work basket ID or the work basket name.
  
  The caller must be the work basket system administrator.
 
 The action associated to this method is WorkBasketActions.GETWORKBASKETDEFINITION.
Parameters:identifier - A string representation of the work basket ID or the work basket name. This is used
    to identify the work basket.
 
Returns:WorkBasketDefinition -
    The work basket definition that is created from the specified work basket.
    Refer to WorkBasketDefinition to view the properties.
 
Throws:
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
WorkBasketNotEnabledException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0 Feature Pack

- getWorkBasketDefinition
WorkBasketDefinition getWorkBasketDefinition(WBID wbid)
                                             throws IdWrongFormatException,
                                                    NotAuthorizedException,
                                                    ObjectDoesNotExistException,
                                                    WorkBasketNotEnabledException,
                                                    UnexpectedFailureException,
                                                    java.rmi.RemoteException,
                                                    javax.ejb.EJBException
Retrieves the definition of the specified work basket using the work basket ID.
 
 The caller must be the work basket system administrator.
 
 The action associated to this method is WorkBasketActions.GETWORKBASKETDEFINITION.
Parameters:wbid - The object ID of the work basket.
 
Returns:WorkBasketDefinition -
    The work basket definition that is created from the specified work basket.
    Refer to WorkBasketDefinition to view the properties.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
WorkBasketNotEnabledException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0 Feature Pack

- getWorkItemsForWorkBasket
WorkItem[] getWorkItemsForWorkBasket(java.lang.String identifier)
                                     throws IdWrongFormatException,
                                            IdWrongTypeException,
                                            NotAuthorizedException,
                                            ObjectDoesNotExistException,
                                            WorkBasketNotEnabledException,
                                            WorkItemManagerException,
                                            UnexpectedFailureException,
                                            java.rmi.RemoteException,
                                            javax.ejb.EJBException
Returns the work item assignments for the logged-on user and the
  specified work basket using a string representation of the work basket ID or the work basket name.
  
  Note that a work basket system administrator is treated like any other user, that is,
  does only see the personally owned work items.
 
 The action associated to this method is WorkBasketActions.GETROLEINFO.
Parameters:identifier - The string representation of a work basket ID or the work basket name. The string is
    used to identify the work basket.
 
Returns:WorkItem[] -
    An array of work items. If there are no work items,
    an empty array is returned. Refer to WorkItem
    to view the work item properties.
 
Throws:
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
WorkBasketNotEnabledException
WorkItemManagerException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0 Feature Pack

- getWorkItemsForWorkBasket
WorkItem[] getWorkItemsForWorkBasket(WBID wbid)
                                     throws IdWrongFormatException,
                                            NotAuthorizedException,
                                            ObjectDoesNotExistException,
                                            WorkBasketNotEnabledException,
                                            WorkItemManagerException,
                                            UnexpectedFailureException,
                                            java.rmi.RemoteException,
                                            javax.ejb.EJBException
Returns the work item assignments for the logged-on user and the
  specified work basket using the work basket ID.
  
  Note that a work basket system administrator is treated like any other user, that is,
  does only see the personally owned work items.
 
 The action associated to this method is WorkBasketActions.GETROLEINFO.
Parameters:wbid - The object ID of the work basket that is used to identify the work basket.
 
Returns:WorkItem[] -
    An array of work items. If there are no work items,
    an empty array is returned. Refer to WorkItem
    to view the work item properties.
 
Throws:
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
WorkBasketNotEnabledException
WorkItemManagerException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0 Feature Pack

- removeAsDistributionTarget
java.util.List removeAsDistributionTarget(java.lang.String identifier)
                                          throws ArchiveUnsupportedOperationException,
                                                 IdWrongFormatException,
                                                 IdWrongTypeException,
                                                 ObjectDoesNotExistException,
                                                 WorkBasketNotEnabledException,
                                                 UnexpectedFailureException,
                                                 java.rmi.RemoteException,
                                                 javax.ejb.EJBException
Removes the specified work basket as a distribution target from all referencing work baskets
  using a string representation of the work basket ID or the work basket name.
  
  The caller must be the work basket system administrator.
 
 The action associated to this method is WorkBasketActions.UPDATE.
 
 This method is not supported in archive mode.
Parameters:identifier - A string representation of the work basket ID or the work basket name
    that is used to identify the work basket to be removed as distribution target.
 
Returns:List -
    A list of WorkBasketResult objects, one for each work basket that referenced the
 specified work basket. Refer to
 WorkBasketResult.
 
 The WorkBasketResult object states the object ID and name of the formerly referencing work basket.
 The TaskException property is not set, that is, is null.
 Returns an empty list when there is no work basket that referenced the specified one.
 
Throws:
ArchiveUnsupportedOperationException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
WorkBasketNotEnabledException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0 Feature Pack
 
Change History

Release
 Modification
 
7.0.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- removeAsDistributionTarget
java.util.List removeAsDistributionTarget(WBID wbid)
                                          throws ArchiveUnsupportedOperationException,
                                                 IdWrongFormatException,
                                                 ObjectDoesNotExistException,
                                                 WorkBasketNotEnabledException,
                                                 UnexpectedFailureException,
                                                 java.rmi.RemoteException,
                                                 javax.ejb.EJBException
Removes the specified work basket as a distribution target from all referencing work baskets
  
  The caller must be the work basket system administrator.
 
 The action associated to this method is WorkBasketActions.UPDATE.
 
 This method is not supported in archive mode.
Parameters:wbid - The work basket ID
    that is used to identify the work basket to be removed as distribution target.
 
Returns:List -
    A list of WorkBasketResult objects, one for each work basket that referenced the
 specified work basket. Refer to
 WorkBasketResult.
 
 The WorkBasketResult object states the object ID and name of the formerly referencing work basket.
 The TaskException property is not set, that is, is null.
 Returns an empty list when there is no work basket that referenced the specified one.
 
Throws:
ArchiveUnsupportedOperationException
IdWrongFormatException
ObjectDoesNotExistException
WorkBasketNotEnabledException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0 Feature Pack
 
Change History

Release
 Modification
 
7.0.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- transferTasksToWorkBasket java.util.List transferTasksToWorkBasket(java.lang.String[] tkiids, java.lang.String identifier, boolean cancelClaimIfNeeded) throws ArchiveUnsupportedOperationException , IdWrongFormatException , IdWrongTypeException , WorkBasketDoesNotExistException , WorkBasketNotAuthorizedException , WorkBasketNotEnabledException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Transfers the specified task instances to the specified work basket using string representations of the task instance and work basket IDs or the work basket name. The task instances must be in the ready state, or for invocation tasks, in the running state. Note that invocation task instances are also known as originating task instances. The task instances' read flags are set to false and the transferredToWorkBasket flags to true. The caller must be authorized to perform action TRANSFERFROMWORKBASKET for each work basket that contains one of the specified task instances and TRANSFERTOWORKBASKET for the specified target work basket. That is, the caller must have transfer initiator rights for the source work baskets and appender rights for the target work basket. The action associated to this method is WorkBasketActions.TRANSFERFROMWORKBASKET and WorkBasketActions.TRANSFERTOWORKBASKET . This method is not supported in archive mode. Parameters: tkiids - An array of string representations of task instance IDs that are used to identify the task instances. identifier - A string representation of the work basket ID or the work basket name. This is used to identify the work basket. cancelClaimIfNeeded - Specifies whether claiming of tasks should be cancelled. True states that the claim of a task should be cancelled, False states that the claim of a task should be kept, that is, transfer is prohibited. Returns: List - A list of TaskResult objects, one for every task instance specified. Refer to TaskResult . If a single transfer operation fails because any of the following exceptions has been thrown, then the result object contains the respective exception. Otherwise, the TaskException property is null. If any of these exceptions is thrown, processing continues. If another exception is thrown, a rollback of the global transaction is enforced, and all transfers are undone. Throws: ArchiveUnsupportedOperationException IdWrongFormatException IdWrongTypeException WorkBasketDoesNotExistException WorkBasketNotAuthorizedException WorkBasketNotEnabledException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 7.0 Feature Pack Change History Release Modification 7.0.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode.

#### transferTasksToWorkBasket

```
java.util.List transferTasksToWorkBasket(java.lang.String[] tkiids,
                                       java.lang.String identifier,
                                       boolean cancelClaimIfNeeded)
                                         throws ArchiveUnsupportedOperationException,
                                                IdWrongFormatException,
                                                IdWrongTypeException,
                                                WorkBasketDoesNotExistException,
                                                WorkBasketNotAuthorizedException,
                                                WorkBasketNotEnabledException,
                                                UnexpectedFailureException,
                                                java.rmi.RemoteException,
                                                javax.ejb.EJBException
```

The task instances must be in the ready state, or for invocation tasks, in the running state.
 Note that invocation task instances are also known as originating task instances.
 
 The task instances' read flags are set to false and the transferredToWorkBasket flags to true.
 
 The caller must be authorized to perform action
 TRANSFERFROMWORKBASKET for each work basket
 that contains one of the specified task instances and
 TRANSFERTOWORKBASKET for the specified target work basket.
 That is, the caller must have transfer initiator rights for the source work baskets and
 appender rights for the target work basket.
 
 The action associated to this method is WorkBasketActions.TRANSFERFROMWORKBASKET
 and WorkBasketActions.TRANSFERTOWORKBASKET.
 
 This method is not supported in archive mode.

If a single transfer operation fails because any of the following exceptions has been thrown,
 then the result object contains the respective exception.
 Otherwise, the TaskException property is null.
 
com.ibm.task.api.ApplicationVetoException
 com.ibm.task.api.TaskDoesNotExistException
 com.ibm.task.api.TaskNotInWorkBasketException
 com.ibm.task.api.WorkBasketNotAuthorizedException which is thrown when
 the caller does not have transfer initiator rights on the work basket that contains the task.
 com.ibm.task.api.WorkBasketDoesNotExistException which is thrown
 when the task is part of a work basket that does not exist.
 com.ibm.task.api.WrongTaskStateException
 
 If any of these exceptions is thrown, processing continues.
 If another exception is thrown, a rollback of the global transaction is enforced,
 and all transfers are undone.

Change History

Release
 Modification
 
7.0.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- transferTasksToWorkBasket java.util.List transferTasksToWorkBasket(TKIID [] tkiids, WBID wbid, boolean cancelClaimIfNeeded) throws ArchiveUnsupportedOperationException , IdWrongFormatException , WorkBasketDoesNotExistException , WorkBasketNotAuthorizedException , WorkBasketNotEnabledException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Transfers the specified task instances to the specified work basket using task instance and work basket IDs. The task instances must be in the ready state, or for invocation tasks, in the running state. Note that invocation task instances are also known as originating task instances. The task instances' read flags are set to false and the transferredToWorkBasket flags to true. The caller must be authorized to perform action TRANSFERFROMWORKBASKET for each work basket that contains one of the specified task instances and TRANSFERTOWORKBASKET for the specified target work basket. That is, the caller must have transfer initiator rights for the source work baskets and appender rights for the target work basket. The action associated to this method is WorkBasketActions.TRANSFERFROMWORKBASKET and WorkBasketActions.TRANSFERTOWORKBASKET . This method is not supported in archive mode. Parameters: tkiids - An array of task instance IDs. wbid - The work basket ID. cancelClaimIfNeeded - Specifies whether claiming of tasks should be cancelled. True states that the claim of a task should be cancelled, False states that the claim of a task should be kept, that is, transfer is prohibited. Returns: List - A list of TaskResult objects, one for every task instance specified. Refer to TaskResult . If a single transfer operation fails because any of the following exceptions has been thrown, then the result object contains the respective exception. Otherwise, the TaskException property is null. If any of these exceptions is thrown, processing continues. If another exception is thrown, a rollback of the global transaction is enforced, and all transfers are undone. Throws: ArchiveUnsupportedOperationException IdWrongFormatException WorkBasketDoesNotExistException WorkBasketNotAuthorizedException WorkBasketNotEnabledException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 7.0 Feature Pack Change History Release Modification 7.0.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode.

#### transferTasksToWorkBasket

```
java.util.List transferTasksToWorkBasket(TKIID[] tkiids,
                                       WBID wbid,
                                       boolean cancelClaimIfNeeded)
                                         throws ArchiveUnsupportedOperationException,
                                                IdWrongFormatException,
                                                WorkBasketDoesNotExistException,
                                                WorkBasketNotAuthorizedException,
                                                WorkBasketNotEnabledException,
                                                UnexpectedFailureException,
                                                java.rmi.RemoteException,
                                                javax.ejb.EJBException
```

The task instances must be in the ready state, or for invocation tasks, in the running state.
 Note that invocation task instances are also known as originating task instances.
 
 The task instances' read flags are set to false and the transferredToWorkBasket flags to true.
 
 The caller must be authorized to perform action
 TRANSFERFROMWORKBASKET for each work basket
 that contains one of the specified task instances and
 TRANSFERTOWORKBASKET for the specified target work basket.
 That is, the caller must have transfer initiator rights for the source work baskets and
 appender rights for the target work basket.
 
 The action associated to this method is WorkBasketActions.TRANSFERFROMWORKBASKET
 and WorkBasketActions.TRANSFERTOWORKBASKET.
 
 This method is not supported in archive mode.

If a single transfer operation fails because any of the following exceptions has been thrown,
 then the result object contains the respective exception.
 Otherwise, the TaskException property is null.
 
com.ibm.task.api.ApplicationVetoException
 com.ibm.task.api.TaskDoesNotExistException
 com.ibm.task.api.TaskNotInWorkBasketException
 com.ibm.task.api.WorkBasketNotAuthorizedException which is thrown when
 the caller does not have transfer initiator rights on the work basket that contains the task.
 com.ibm.task.api.WorkBasketDoesNotExistException which is thrown
 when the task is part of a work basket that does not exist.
 com.ibm.task.api.WrongTaskStateException
 
 If any of these exceptions is thrown, processing continues.
 If another exception is thrown, a rollback of the global transaction is enforced,
 and all transfers are undone.

Change History

Release
 Modification
 
7.0.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- updateWorkBasket
void updateWorkBasket(WorkBasketDefinition workBasketDefinition)
                      throws ArchiveUnsupportedOperationException,
                             CannotCreateWorkItemException,
                             InvalidAssignmentReasonException,
                             InvalidLengthException,
                             InvalidPropertyValueException,
                             NotAuthorizedException,
                             ObjectDoesNotExistException,
                             ParameterNullException,
                             WorkBasketNotEnabledException,
                             WorkItemManagerException,
                             UnexpectedFailureException,
                             java.rmi.RemoteException,
                             javax.ejb.EJBException
Updates a work basket with values from the specified work basket definition.
 
 The caller must be a work basket system administrator.
 
 The action associated to this method is WorkBasketActions.UPDATE.
 
 This method is not supported in archive mode.
Parameters:workBasketDefinition - The WorkBasketDefinition
  from which a work basket is to be updated.
 
Throws:
ArchiveUnsupportedOperationException
CannotCreateWorkItemException
InvalidAssignmentReasonException
InvalidLengthException
InvalidPropertyValueException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
WorkBasketNotEnabledException
WorkItemManagerException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0 Feature Pack
 
Change History

Release
 Modification
 
7.0.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- isWorkBasketSystemAdministrator
boolean isWorkBasketSystemAdministrator()
                                        throws java.rmi.RemoteException,
                                               javax.ejb.EJBException
States whether the logged-on user is a system administrator for work baskets.
    
    In general, authorization is granted to persons explicitly when a work basket is created
    or updated.
    Above that, special authority is granted to a person playing the role of a work basket
    system administrator. A work basket system administrator has all priviledges for work baskets.
 
Returns:boolean -
    boolean -
   True states that the logged-on user is a work basket system administrator.
   False states that the logged-on user is no work basket system administrator.
 
Throws:
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0 Feature Pack