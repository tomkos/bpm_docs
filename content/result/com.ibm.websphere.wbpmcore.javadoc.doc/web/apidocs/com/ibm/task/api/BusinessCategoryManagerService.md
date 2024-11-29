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

## Interface BusinessCategoryManagerService

- All Known Subinterfaces:
HumanTaskManager, LocalBusinessCategoryManagerService, LocalHumanTaskManager

public interface BusinessCategoryManagerService
BusinessCategoryManagerService defines the business category methods that can be called by a local or remote client.

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

BCID
createBusinessCategory(BusinessCategoryDefinition businessCategoryDefinition)
Creates a business category from the specified business category definition.

BCID
createBusinessCategory(BusinessCategoryDefinition businessCategoryDefinition,
                      BCID parentBCID)
Creates a business category from the specified business category definition
 as a subcategory of the specified parent business category
 using the object ID of the parent business category.

BCID
createBusinessCategory(BusinessCategoryDefinition businessCategoryDefinition,
                      java.lang.String parentNameOrID)
Creates a business category from the specified business category definition
 as a subcategory of the specified parent business category
 using a string representation of the object ID of the parent business category or the business category name.

java.util.List
deleteBusinessCategory(BCID bcid,
                      boolean recursive)
Deletes the specified business category using the business category ID.

java.util.List
deleteBusinessCategory(java.lang.String identifier,
                      boolean recursive)
Deletes the specified business category
  using a string representation of the business category ID or the business category name.

WorkItem[]
getAllWorkItemsForBusinessCategory(BCID bcid)
Returns all work item assignments associated to specified business category
  using the business category ID.

WorkItem[]
getAllWorkItemsForBusinessCategory(java.lang.String identifier)
Returns all work item assignments associated to specified business category
  using a string representation of the business category ID or the business category name.

boolean[][]
getAvailableActionFlagsForBusinessCategories(BCID[] bcids)
Returns the actions that can be called for the specified business categories
 by the logged-on user using business category IDs.

boolean[][]
getAvailableActionFlagsForBusinessCategories(java.lang.String[] identifiers)
Returns the actions that can be called for the specified business categories
 by the logged-on user
 using string representations of the business category IDs or the business category names.

int[]
getAvailableActionsForBusinessCategory(BCID bcid)
Returns the actions that can be called by the logged-on user
 for the specified business category
 using the business category ID.

int[]
getAvailableActionsForBusinessCategory(java.lang.String identifier)
Returns the actions that can be called by the logged-on user
 for the specified business category
 using a string representation of the business category ID or the business category name.

BusinessCategory
getBusinessCategory(BCID bcid)
Retrieves the specified business category using the business category ID.

BusinessCategory
getBusinessCategory(java.lang.String identifier)
Retrieves the specified business category using a string
 representation of the business category ID or the business category name.

BusinessCategoryDefinition
getBusinessCategoryDefinition(BCID bcid)
Retrieves the definition of the specified business category using the business category ID.

BusinessCategoryDefinition
getBusinessCategoryDefinition(java.lang.String identifier)
Retrieves the definition of the specified business category using a string
 representation of the business category ID or the business category name.

WorkItem[]
getWorkItemsForBusinessCategory(BCID bcid)
Returns the work item assignments for the logged-on user and the
  specified business category using the business category ID.

WorkItem[]
getWorkItemsForBusinessCategory(java.lang.String identifier)
Returns the work item assignments for the logged-on user and the
  specified business category using a string representation of the business category ID or the business category name.

boolean
isBusinessCategorySystemAdministrator()
States whether the logged-on user is a system administrator for business categories.

java.util.List
setBusinessCategoryOnTasks(java.lang.String[] tkiids,
                          java.lang.String identifier)
Sets the business category of the specified tasks
 using string representations of the task instance or business category IDs or the business category name.

java.util.List
setBusinessCategoryOnTasks(TKIID[] tkiids,
                          BCID bcid)
Sets the business category of the specified tasks
 using the task instance and business category IDs.

void
setParentBusinessCategory(BCID bcid,
                         BCID parentBCID)
Sets the parent of the specified business category
 using business category IDs.

void
setParentBusinessCategory(java.lang.String identifier,
                         java.lang.String parentIdentifier)
Sets the parent of the specified business category using string
 representations of the business category IDs or the business category names.

java.util.List
setPriorityOfBusinessCategories(BCID[] bcids,
                               java.lang.Integer priority)
Sets the priority of the specified business categories
 using the business category IDs.

java.util.List
setPriorityOfBusinessCategories(java.lang.String[] identifier,
                               java.lang.Integer priority)
Sets the priority of the specified business categories
 using string representations of the business category IDs or the business category names.

void
updateBusinessCategory(BusinessCategoryDefinition businessCategoryDefinition)
Updates a business category with values from the specified business category definition.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - createBusinessCategory
BCID createBusinessCategory(BusinessCategoryDefinition businessCategoryDefinition)
                            throws ArchiveUnsupportedOperationException,
                                   BusinessCategoryAlreadyExistsException,
                                   BusinessCategoryNotEnabledException,
                                   CannotCreateWorkItemException,
                                   InvalidAssignmentReasonException,
                                   InvalidLengthException,
                                   InvalidPropertyValueException,
                                   NotAuthorizedException,
                                   ParameterNullException,
                                   UnexpectedFailureException,
                                   java.rmi.RemoteException,
                                   javax.ejb.EJBException
Creates a business category from the specified business category definition.
 
 The caller must be a business category system administrator.
 
 The action associated to this method is BusinessCategoryActions.CREATEBUSINESSCATEGORY.
 
 This method is not supported in archive mode.
Parameters:businessCategoryDefinition - The BusinessCategoryDefinition
  from which a business category is to be created.
 
Returns:BCID -
    The object ID of the business category created.
 
Throws:
ArchiveUnsupportedOperationException
BusinessCategoryAlreadyExistsException
BusinessCategoryNotEnabledException
CannotCreateWorkItemException
InvalidAssignmentReasonException
InvalidLengthException
InvalidPropertyValueException
NotAuthorizedException
ParameterNullException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0 Feature Pack
 
Change History

Release
 Modification
 
7.0.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
    - createBusinessCategory
BCID createBusinessCategory(BusinessCategoryDefinition businessCategoryDefinition,
                          java.lang.String parentNameOrID)
                            throws ArchiveUnsupportedOperationException,
                                   BusinessCategoryAlreadyExistsException,
                                   BusinessCategoryNotEnabledException,
                                   CannotCreateWorkItemException,
                                   IdWrongFormatException,
                                   IdWrongTypeException,
                                   InvalidAssignmentReasonException,
                                   InvalidLengthException,
                                   InvalidPropertyValueException,
                                   NotAuthorizedException,
                                   ObjectDoesNotExistException,
                                   ParameterNullException,
                                   UnexpectedFailureException,
                                   java.rmi.RemoteException,
                                   javax.ejb.EJBException
Creates a business category from the specified business category definition
 as a subcategory of the specified parent business category
 using a string representation of the object ID of the parent business category or the business category name.
 
 The caller must be a business category system administrator.
 
 The action associated to this method is BusinessCategoryActions.CREATEBUSINESSCATEGORY.
 
 This method is not supported in archive mode.
Parameters:businessCategoryDefinition - The BusinessCategoryDefinition
  from which a business category is to be created.parentNameOrID - The string representation of the business category object ID or
  the name of the business category that is to become
  the parent of the newly created business category.
  Note that business category names must conform to the XML NCName specification.
 
Returns:BCID -
    The object ID of the business category created.
 
Throws:
ArchiveUnsupportedOperationException
BusinessCategoryAlreadyExistsException
BusinessCategoryNotEnabledException
CannotCreateWorkItemException
IdWrongFormatException
IdWrongTypeException
InvalidAssignmentReasonException
InvalidLengthException
InvalidPropertyValueException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0 Feature Pack
 
Change History

Release
 Modification
 
7.0.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
    - createBusinessCategory
BCID createBusinessCategory(BusinessCategoryDefinition businessCategoryDefinition,
                          BCID parentBCID)
                            throws ArchiveUnsupportedOperationException,
                                   BusinessCategoryAlreadyExistsException,
                                   BusinessCategoryNotEnabledException,
                                   CannotCreateWorkItemException,
                                   IdWrongFormatException,
                                   InvalidAssignmentReasonException,
                                   InvalidLengthException,
                                   InvalidPropertyValueException,
                                   NotAuthorizedException,
                                   ObjectDoesNotExistException,
                                   ParameterNullException,
                                   UnexpectedFailureException,
                                   java.rmi.RemoteException,
                                   javax.ejb.EJBException
Creates a business category from the specified business category definition
 as a subcategory of the specified parent business category
 using the object ID of the parent business category.
 
 The caller must be a business category system administrator.
 
 The action associated to this method is BusinessCategoryActions.CREATEBUSINESSCATEGORY.
 
 This method is not supported in archive mode.
Parameters:businessCategoryDefinition - The BusinessCategoryDefinition
  from which a business category is to be created.parentBCID - The object ID of the business category that is to become
  the parent of the newly created business category.
 
Returns:BCID -
    The object ID of the business category created.
 
Throws:
ArchiveUnsupportedOperationException
BusinessCategoryAlreadyExistsException
BusinessCategoryNotEnabledException
CannotCreateWorkItemException
IdWrongFormatException
InvalidAssignmentReasonException
InvalidLengthException
InvalidPropertyValueException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0 Feature Pack
 
Change History

Release
 Modification
 
7.0.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.
    - deleteBusinessCategory
java.util.List deleteBusinessCategory(java.lang.String identifier,
                                    boolean recursive)
                                      throws BusinessCategoryHasChildrenException,
                                             BusinessCategoryInUseException,
                                             BusinessCategoryNotEnabledException,
                                             IdWrongFormatException,
                                             IdWrongTypeException,
                                             NotAuthorizedException,
                                             ObjectDoesNotExistException,
                                             UnexpectedFailureException,
                                             java.rmi.RemoteException,
                                             javax.ejb.EJBException
Deletes the specified business category
  using a string representation of the business category ID or the business category name.
  
  If the business category is a parent of another business category,
  then its sub-business categories must also be deleted.
  
  The caller must be the business category system administrator.
 
 The action associated to this method is BusinessCategoryActions.DELETEBUSINESSCATEGORY.
Parameters:identifier - A string representation of the business category ID or the business category name
    that is used to identify the business category.recursive - Specifies whether sub-business categories should be deleted together with the business category.
    True states that all sub-business categories should be deleted.
    False states that sub-business categories should not be deleted.
 
Returns:List -
    A list of BusinessCategoryResult objects, one for each business category deleted. Refer to
 BusinessCategoryResult.
 
 The BusinessCategoryResult object states the object ID and name of the business category deleted.
 The TaskException property is not set, that is, is null.
 If sub-business categories are not deleted together with the specified business category,
 the list contains a single entry.
 
Throws:
BusinessCategoryHasChildrenException
BusinessCategoryInUseException
BusinessCategoryNotEnabledException
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0 Feature Pack
    - deleteBusinessCategory
java.util.List deleteBusinessCategory(BCID bcid,
                                    boolean recursive)
                                      throws BusinessCategoryHasChildrenException,
                                             BusinessCategoryInUseException,
                                             BusinessCategoryNotEnabledException,
                                             IdWrongFormatException,
                                             NotAuthorizedException,
                                             ObjectDoesNotExistException,
                                             UnexpectedFailureException,
                                             java.rmi.RemoteException,
                                             javax.ejb.EJBException
Deletes the specified business category using the business category ID.
  
  If the business category is a parent of another business category,
  then its sub-business categories must also be deleted.
  
  The caller must be the business category system administrator.
 
 The action associated to this method is BusinessCategoryActions.DELETEBUSINESSCATEGORY.
Parameters:bcid - The business category ID that is used to identify the business category.recursive - Specifies whether sub-business categories should be deleted together with the business category.
    True states that all sub-business categories should be deleted.
    False states that sub-business categories should not be deleted.
 
Returns:List -
    A list of BusinessCategoryResult objects, one for each business category deleted. Refer to
 BusinessCategoryResult.
 
 The BusinessCategoryResult object states the object ID and name of the business category deleted.
 The TaskException property is not set, that is, is null.
 If sub-business categories are not deleted together with the specified business category,
 the list contains a single entry.
 
Throws:
BusinessCategoryHasChildrenException
BusinessCategoryInUseException
BusinessCategoryNotEnabledException
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0 Feature Pack
    - getAllWorkItemsForBusinessCategory
WorkItem[] getAllWorkItemsForBusinessCategory(java.lang.String identifier)
                                              throws BusinessCategoryNotEnabledException,
                                                     IdWrongFormatException,
                                                     IdWrongTypeException,
                                                     NotAuthorizedException,
                                                     ObjectDoesNotExistException,
                                                     WorkItemManagerException,
                                                     UnexpectedFailureException,
                                                     java.rmi.RemoteException,
                                                     javax.ejb.EJBException
Returns all work item assignments associated to specified business category
  using a string representation of the business category ID or the business category name.
  
  The caller must have a work item for the specified business category or be a
  business category system administrator.
 
 The action associated to this method is BusinessCategoryActions.GETROLEINFO.
Parameters:identifier - The string representation of a business category ID or the business category name that is
    used to identify the business category.
 
Returns:WorkItem[] -
    An array of work items. If there are no work items,
    an empty array is returned. Refer to WorkItem
    to view the work item properties.
 
Throws:
BusinessCategoryNotEnabledException
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
WorkItemManagerException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0 Feature Pack
    - getAllWorkItemsForBusinessCategory
WorkItem[] getAllWorkItemsForBusinessCategory(BCID bcid)
                                              throws BusinessCategoryNotEnabledException,
                                                     IdWrongFormatException,
                                                     NotAuthorizedException,
                                                     ObjectDoesNotExistException,
                                                     WorkItemManagerException,
                                                     UnexpectedFailureException,
                                                     java.rmi.RemoteException,
                                                     javax.ejb.EJBException
Returns all work item assignments associated to specified business category
  using the business category ID.
  
  The caller must have a work item for the specified business category or be a
  business category system administrator.
 
 The action associated to this method is BusinessCategoryActions.GETROLEINFO.
Parameters:bcid - The object ID of the business category that is used to identify
    the business category.
 
Returns:WorkItem[] -
    An array of work items. If there are no work items,
    an empty array is returned. Refer to WorkItem
    to view the work item properties.
 
Throws:
BusinessCategoryNotEnabledException
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
WorkItemManagerException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0 Feature Pack
    - getAvailableActionFlagsForBusinessCategories
boolean[][] getAvailableActionFlagsForBusinessCategories(java.lang.String[] identifiers)
                                                         throws BusinessCategoryNotEnabledException,
                                                                IdWrongFormatException,
                                                                IdWrongTypeException,
                                                                ObjectDoesNotExistException,
                                                                UnexpectedFailureException,
                                                                java.rmi.RemoteException,
                                                                javax.ejb.EJBException
Returns the actions that can be called for the specified business categories
 by the logged-on user
 using string representations of the business category IDs or the business category names.
 Refer to BusinessCategoryActions for possible actions.
Parameters:identifiers - An array of string representations of business category IDs or business category names.
 
Returns:boolean[][] -
    An array of actions that can be called for each specified business category.
 The array contains a row per business category and a column per possible action.
 An array entry thus indicates whether a possible action can be called for the business category
 by the logged-on user.
 True states that the action can be called. False states that the action cannot be called.
 
 The business categories appear in the same order as specified.
 Refer to BusinessCategoryActionIndex for index constants that should
 be used to access the columns of the two-dimensional array.
 
Throws:
BusinessCategoryNotEnabledException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0 Feature Pack
    - getAvailableActionFlagsForBusinessCategories
boolean[][] getAvailableActionFlagsForBusinessCategories(BCID[] bcids)
                                                         throws BusinessCategoryNotEnabledException,
                                                                IdWrongFormatException,
                                                                ObjectDoesNotExistException,
                                                                UnexpectedFailureException,
                                                                java.rmi.RemoteException,
                                                                javax.ejb.EJBException
Returns the actions that can be called for the specified business categories
 by the logged-on user using business category IDs.
 Refer to BusinessCategoryActions for possible actions.
Parameters:bcids - An array of business category IDs.
 
Returns:boolean[][] -
    An array of actions that can be called for each specified business category
 The array contains a row per business category and a column per possible action.
 An array entry thus indicates whether a possible action can be called for the business category.
 by the logged-on user.
 True states that the action can be called. False states that the action cannot be called.
 
 The work baskets appear in the same order as specified.
 Refer to BusinessCategoryActionIndex for index constants that should
 be used to access the columns of the two-dimensional array.
 
Throws:
BusinessCategoryNotEnabledException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0 Feature Pack
    - getAvailableActionsForBusinessCategory
int[] getAvailableActionsForBusinessCategory(java.lang.String identifier)
                                             throws BusinessCategoryNotEnabledException,
                                                    IdWrongFormatException,
                                                    IdWrongTypeException,
                                                    ObjectDoesNotExistException,
                                                    UnexpectedFailureException,
                                                    java.rmi.RemoteException,
                                                    javax.ejb.EJBException
Returns the actions that can be called by the logged-on user
 for the specified business category
 using a string representation of the business category ID or the business category name.
 Refer to BusinessCategoryActions for possible actions.
Parameters:identifier - The string representation of the business category ID or the business category name.
 
Returns:int[] -
    The set of possible actions.
    Returns an empty array if there are no available actions.
 
Throws:
BusinessCategoryNotEnabledException
IdWrongFormatException
IdWrongTypeException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0 Feature Pack
    - getAvailableActionsForBusinessCategory
int[] getAvailableActionsForBusinessCategory(BCID bcid)
                                             throws BusinessCategoryNotEnabledException,
                                                    IdWrongFormatException,
                                                    ObjectDoesNotExistException,
                                                    UnexpectedFailureException,
                                                    java.rmi.RemoteException,
                                                    javax.ejb.EJBException
Returns the actions that can be called by the logged-on user
 for the specified business category
 using the business category ID.
 Refer to BusinessCategoryActions for possible actions.
Parameters:bcid - The object ID of the business category.
 
Returns:int[] -
    The set of possible actions.
    Returns an empty array if there are no available actions.
 
Throws:
BusinessCategoryNotEnabledException
IdWrongFormatException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0 Feature Pack
    - getBusinessCategory
BusinessCategory getBusinessCategory(java.lang.String identifier)
                                     throws BusinessCategoryNotEnabledException,
                                            IdWrongFormatException,
                                            IdWrongTypeException,
                                            NotAuthorizedException,
                                            ObjectDoesNotExistException,
                                            UnexpectedFailureException,
                                            java.rmi.RemoteException,
                                            javax.ejb.EJBException
Retrieves the specified business category using a string
 representation of the business category ID or the business category name.
 
 The caller must have at least reader authority for the business category.
 
 The action associated to this method is BusinessCategoryActions.GETBUSINESSCATEGORY.
Parameters:identifier - A string representation of the business category ID or the business category name. This is used
    to identify the business category to be retrieved.
 
Returns:BusinessCategory -
    The business category.
    Refer to BusinessCategory to view the properties.
 
Throws:
BusinessCategoryNotEnabledException
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0 Feature Pack
    - getBusinessCategory
BusinessCategory getBusinessCategory(BCID bcid)
                                     throws BusinessCategoryNotEnabledException,
                                            IdWrongFormatException,
                                            NotAuthorizedException,
                                            ObjectDoesNotExistException,
                                            UnexpectedFailureException,
                                            java.rmi.RemoteException,
                                            javax.ejb.EJBException
Retrieves the specified business category using the business category ID.
 
 The caller must have at least reader authority for the business category.
 
 The action associated to this method is BusinessCategoryActions.GETBUSINESSCATEGORY.
Parameters:bcid - The object ID of the business category to be retrieved.
 
Returns:BusinessCategory -
    The business category.
    Refer to BusinessCategory to view the properties.
 
Throws:
BusinessCategoryNotEnabledException
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0 Feature Pack
    - getBusinessCategoryDefinition
BusinessCategoryDefinition getBusinessCategoryDefinition(java.lang.String identifier)
                                                         throws BusinessCategoryNotEnabledException,
                                                                IdWrongFormatException,
                                                                IdWrongTypeException,
                                                                NotAuthorizedException,
                                                                ObjectDoesNotExistException,
                                                                UnexpectedFailureException,
                                                                java.rmi.RemoteException,
                                                                javax.ejb.EJBException
Retrieves the definition of the specified business category using a string
 representation of the business category ID or the business category name.
 
 The caller must have at least reader authority for the business category.
 
 The action associated to this method is BusinessCategoryActions.GETBUSINESSCATEGORYDEFINITION.
Parameters:identifier - A string representation of the business category ID or the business category name. This is used
    to identify the business category.
 
Returns:BusinessCategoryDefinition -
    The business category definition that is created from the specified business category.
    Refer to BusinessCategoryDefinition to view the properties.
 
Throws:
BusinessCategoryNotEnabledException
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0 Feature Pack
    - getBusinessCategoryDefinition
BusinessCategoryDefinition getBusinessCategoryDefinition(BCID bcid)
                                                         throws BusinessCategoryNotEnabledException,
                                                                IdWrongFormatException,
                                                                NotAuthorizedException,
                                                                ObjectDoesNotExistException,
                                                                UnexpectedFailureException,
                                                                java.rmi.RemoteException,
                                                                javax.ejb.EJBException
Retrieves the definition of the specified business category using the business category ID.
 
 The caller must have at least reader authority for the business category.
 
 The action associated to this method is BusinessCategoryActions.GETBUSINESSCATEGORYDEFINITION.
Parameters:bcid - The object ID of the business category.
 
Returns:BusinessCategoryDefinition -
    The business category definition that is created from the specified business category.
    Refer to BusinessCategoryDefinition to view the properties.
 
Throws:
BusinessCategoryNotEnabledException
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0 Feature Pack
    - getWorkItemsForBusinessCategory
WorkItem[] getWorkItemsForBusinessCategory(java.lang.String identifier)
                                           throws BusinessCategoryNotEnabledException,
                                                  IdWrongFormatException,
                                                  IdWrongTypeException,
                                                  NotAuthorizedException,
                                                  ObjectDoesNotExistException,
                                                  WorkItemManagerException,
                                                  UnexpectedFailureException,
                                                  java.rmi.RemoteException,
                                                  javax.ejb.EJBException
Returns the work item assignments for the logged-on user and the
  specified business category using a string representation of the business category ID or the business category name.
  
  Note that a business category system administrator is treated like any other user, that is,
  does only see the personally owned work items.
 
 The action associated to this method is BusinessCategoryActions.GETROLEINFO.
Parameters:identifier - The string representation of a business category ID or the business category name. The string is
    used to identify the business category.
 
Returns:WorkItem[] -
    An array of work items. If there are no work items,
    an empty array is returned. Refer to WorkItem
    to view the work item properties.
 
Throws:
BusinessCategoryNotEnabledException
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
WorkItemManagerException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0 Feature Pack
    - getWorkItemsForBusinessCategory
WorkItem[] getWorkItemsForBusinessCategory(BCID bcid)
                                           throws BusinessCategoryNotEnabledException,
                                                  IdWrongFormatException,
                                                  NotAuthorizedException,
                                                  ObjectDoesNotExistException,
                                                  WorkItemManagerException,
                                                  UnexpectedFailureException,
                                                  java.rmi.RemoteException,
                                                  javax.ejb.EJBException
Returns the work item assignments for the logged-on user and the
  specified business category using the business category ID.
  
  Note that a business category system administrator is treated like any other user, that is,
  does only see the personally owned work items.
 
 The action associated to this method is BusinessCategoryActions.GETROLEINFO.
Parameters:bcid - The object ID of the business category that is used to identify the business category.
 
Returns:WorkItem[] -
    An array of work items. If there are no work items,
    an empty array is returned. Refer to WorkItem
    to view the work item properties.
 
Throws:
BusinessCategoryNotEnabledException
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
WorkItemManagerException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0 Feature Pack
    - setBusinessCategoryOnTasks java.util.List setBusinessCategoryOnTasks(java.lang.String[] tkiids, java.lang.String identifier) throws ArchiveUnsupportedOperationException , BusinessCategoryNotEnabledException , BusinessCategoryDoesNotExistException , IdWrongFormatException , IdWrongTypeException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Sets the business category of the specified tasks using string representations of the task instance or business category IDs or the business category name. The action associated to this method is TaskActions.UPDATE . This method is not supported in archive mode. Parameters: tkiids - An array of string representations of task instance IDs that are used to identify the task instances. identifier - A string representation of the business category or the business category name to identify the business category. Returns: List - A list of TaskResult objects, one for every task instance specified. Refer to TaskResult . If a single set operation fails because any of the following exceptions has been thrown, then the result object contains the respective exception. Otherwise, the TaskException property is null. If any of these exceptions is thrown, processing continues. If another exception is thrown, a rollback of the global transaction is enforced, and all set operations are undone. Throws: ArchiveUnsupportedOperationException BusinessCategoryNotEnabledException BusinessCategoryDoesNotExistException IdWrongFormatException IdWrongTypeException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 7.0 Feature Pack Change History Release Modification 7.0.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode.

#### setBusinessCategoryOnTasks

```
java.util.List setBusinessCategoryOnTasks(java.lang.String[] tkiids,
                                        java.lang.String identifier)
                                          throws ArchiveUnsupportedOperationException,
                                                 BusinessCategoryNotEnabledException,
                                                 BusinessCategoryDoesNotExistException,
                                                 IdWrongFormatException,
                                                 IdWrongTypeException,
                                                 UnexpectedFailureException,
                                                 java.rmi.RemoteException,
                                                 javax.ejb.EJBException
```

The action associated to this method is TaskActions.UPDATE.
 
 This method is not supported in archive mode.

If a single set operation fails because any of the following exceptions has been thrown,
 then the result object contains the respective exception.
 Otherwise, the TaskException property is null.
 
com.ibm.task.api.ApplicationVetoException
 com.ibm.task.api.NotAuthorizedException
 com.ibm.task.api.TaskDoesNotExistException
 com.ibm.task.api.PropertyVetoException
 com.ibm.task.api.WrongKindException
 com.ibm.task.api.WrongStateException
 
 If any of these exceptions is thrown, processing continues.
 If another exception is thrown, a rollback of the global transaction is enforced,
 and all set operations are undone.

Change History

Release
 Modification
 
7.0.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setBusinessCategoryOnTasks java.util.List setBusinessCategoryOnTasks(TKIID [] tkiids, BCID bcid) throws ArchiveUnsupportedOperationException , BusinessCategoryDoesNotExistException , BusinessCategoryNotEnabledException , IdWrongFormatException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Sets the business category of the specified tasks using the task instance and business category IDs. The action associated to this method is TaskActions.UPDATE . This method is not supported in archive mode. Parameters: tkiids - An array of task instance IDs. that are used to identify the task instances. bcid - The object ID of the business category to identify the business category. Returns: List - A list of TaskResult objects, one for every task instance specified. Refer to TaskResult . If a single set operation fails because any of the following exceptions has been thrown, then the result object contains the respective exception. Otherwise, the TaskException property is null. If any of these exceptions is thrown, processing continues. If another exception is thrown, a rollback of the global transaction is enforced, and all set operations are undone. Throws: ArchiveUnsupportedOperationException BusinessCategoryDoesNotExistException BusinessCategoryNotEnabledException IdWrongFormatException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 7.0 Feature Pack Change History Release Modification 7.0.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode.

#### setBusinessCategoryOnTasks

```
java.util.List setBusinessCategoryOnTasks(TKIID[] tkiids,
                                        BCID bcid)
                                          throws ArchiveUnsupportedOperationException,
                                                 BusinessCategoryDoesNotExistException,
                                                 BusinessCategoryNotEnabledException,
                                                 IdWrongFormatException,
                                                 UnexpectedFailureException,
                                                 java.rmi.RemoteException,
                                                 javax.ejb.EJBException
```

The action associated to this method is TaskActions.UPDATE.
 
 This method is not supported in archive mode.

If a single set operation fails because any of the following exceptions has been thrown,
 then the result object contains the respective exception.
 Otherwise, the TaskException property is null.
 
com.ibm.task.api.ApplicationVetoException
 com.ibm.task.api.NotAuthorizedException
 com.ibm.task.api.TaskDoesNotExistException
 com.ibm.task.api.PropertyVetoException
 com.ibm.task.api.WrongKindException
 com.ibm.task.api.WrongStateException
 
 If any of these exceptions is thrown, processing continues.
 If another exception is thrown, a rollback of the global transaction is enforced,
 and all set operations are undone.

Change History

Release
 Modification
 
7.0.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setParentBusinessCategory
void setParentBusinessCategory(java.lang.String identifier,
                             java.lang.String parentIdentifier)
                               throws ArchiveUnsupportedOperationException,
                                      BusinessCategoryNotEnabledException,
                                      BusinessCategoryParentCircularException,
                                      IdWrongFormatException,
                                      IdWrongTypeException,
                                      NotAuthorizedException,
                                      ObjectDoesNotExistException,
                                      UnexpectedFailureException,
                                      java.rmi.RemoteException,
                                      javax.ejb.EJBException
Sets the parent of the specified business category using string
 representations of the business category IDs or the business category names.
 
 The caller must be the business category system administrator.
 
 The action associated to this method is BusinessCategoryActions.UPDATE.
 
 This method is not supported in archive mode.
Parameters:identifier - A string representation of the business category ID or the business category name. This is used
    to identify the business category whose parent is to be set.parentIdentifier - A string representation of the business category ID or the business category name. This is used
    to identify the business category who is to become the parent.
    You can pass null to indicate that the business category specified by the identifier parameter
    is a root category.
 
Throws:
ArchiveUnsupportedOperationException
BusinessCategoryNotEnabledException
BusinessCategoryParentCircularException
IdWrongFormatException
IdWrongTypeException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0 Feature Pack
 
Change History

Release
 Modification
 
7.0.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setParentBusinessCategory
void setParentBusinessCategory(BCID bcid,
                             BCID parentBCID)
                               throws ArchiveUnsupportedOperationException,
                                      BusinessCategoryNotEnabledException,
                                      BusinessCategoryParentCircularException,
                                      IdWrongFormatException,
                                      NotAuthorizedException,
                                      ObjectDoesNotExistException,
                                      UnexpectedFailureException,
                                      java.rmi.RemoteException,
                                      javax.ejb.EJBException
Sets the parent of the specified business category
 using business category IDs.
 
 The caller must be the business category system administrator.
 
 The action associated to this method is BusinessCategoryActions.UPDATE.
 
 This method is not supported in archive mode.
Parameters:bcid - The object ID of the business category whose parent is to be set.parentBCID - The object ID of the business category who is to become the parent.
    You can pass null to indicate that the business category specified by the bcid parameter
    is a root category.
 
Throws:
ArchiveUnsupportedOperationException
BusinessCategoryNotEnabledException
BusinessCategoryParentCircularException
IdWrongFormatException
NotAuthorizedException
ObjectDoesNotExistException
UnexpectedFailureException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0 Feature Pack
 
Change History

Release
 Modification
 
7.0.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setPriorityOfBusinessCategories java.util.List setPriorityOfBusinessCategories(java.lang.String[] identifier, java.lang.Integer priority) throws ArchiveUnsupportedOperationException , BusinessCategoryNotEnabledException , IdWrongFormatException , IdWrongTypeException , InvalidPropertyValueException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Sets the priority of the specified business categories using string representations of the business category IDs or the business category names. The action associated to this method is BusinessCategoryActions.UPDATE . This method is not supported in archive mode. Parameters: identifier - An array of string representations of business category IDs or business category names that are used to identify the business categories. priority - The priority to be set. Returns: List - A list of BusinessCategoryResult objects, one for every business category specified. Refer to BusinessCategoryResult . If a single set operation fails because any of the following exceptions has been thrown, then the result object contains the respective exception. Otherwise, the TaskException property is null. If any of these exceptions is thrown, processing continues. If another exception is thrown, a rollback of the global transaction is enforced, and all set operations are undone. Throws: ArchiveUnsupportedOperationException BusinessCategoryNotEnabledException IdWrongFormatException IdWrongTypeException InvalidPropertyValueException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 7.0 Feature Pack Change History Release Modification 7.0.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode.

#### setPriorityOfBusinessCategories

```
java.util.List setPriorityOfBusinessCategories(java.lang.String[] identifier,
                                             java.lang.Integer priority)
                                               throws ArchiveUnsupportedOperationException,
                                                      BusinessCategoryNotEnabledException,
                                                      IdWrongFormatException,
                                                      IdWrongTypeException,
                                                      InvalidPropertyValueException,
                                                      UnexpectedFailureException,
                                                      java.rmi.RemoteException,
                                                      javax.ejb.EJBException
```

The action associated to this method is BusinessCategoryActions.UPDATE.
 
 This method is not supported in archive mode.

If a single set operation fails because any of the following exceptions has been thrown,
 then the result object contains the respective exception.
 Otherwise, the TaskException property is null.
 
com.ibm.task.api.NotAuthorizedException
 com.ibm.task.api.ObjectDoesNotExistException
 
 If any of these exceptions is thrown, processing continues.
 If another exception is thrown, a rollback of the global transaction is enforced,
 and all set operations are undone.

Change History

Release
 Modification
 
7.0.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- setPriorityOfBusinessCategories java.util.List setPriorityOfBusinessCategories(BCID [] bcids, java.lang.Integer priority) throws ArchiveUnsupportedOperationException , BusinessCategoryNotEnabledException , IdWrongFormatException , InvalidPropertyValueException , UnexpectedFailureException , java.rmi.RemoteException, javax.ejb.EJBException Sets the priority of the specified business categories using the business category IDs. The action associated to this method is BusinessCategoryActions.UPDATE . This method is not supported in archive mode. Parameters: bcids - An array of business category IDs that are used to identify the business categories. priority - The priority to be set. Returns: List - A list of BusinessCategoryResult objects, one for every business category specified. Refer to BusinessCategoryResult . If a single set operation fails because any of the following exceptions has been thrown, then the result object contains the respective exception. Otherwise, the TaskException property is null. If any of these exceptions is thrown, processing continues. If another exception is thrown, a rollback of the global transaction is enforced, and all set operations are undone. Throws: ArchiveUnsupportedOperationException BusinessCategoryNotEnabledException IdWrongFormatException InvalidPropertyValueException UnexpectedFailureException java.rmi.RemoteException javax.ejb.EJBException Since: 7.0 Feature Pack Change History Release Modification 7.0.0.3 Throws an ArchiveUnsupportedOperationException when called in archive mode.

#### setPriorityOfBusinessCategories

```
java.util.List setPriorityOfBusinessCategories(BCID[] bcids,
                                             java.lang.Integer priority)
                                               throws ArchiveUnsupportedOperationException,
                                                      BusinessCategoryNotEnabledException,
                                                      IdWrongFormatException,
                                                      InvalidPropertyValueException,
                                                      UnexpectedFailureException,
                                                      java.rmi.RemoteException,
                                                      javax.ejb.EJBException
```

The action associated to this method is BusinessCategoryActions.UPDATE.
 
 This method is not supported in archive mode.

If a single set operation fails because any of the following exceptions has been thrown,
 then the result object contains the respective exception.
 Otherwise, the TaskException property is null.
 
com.ibm.task.api.NotAuthorizedException
 com.ibm.task.api.ObjectDoesNotExistException
 
 If any of these exceptions is thrown, processing continues.
 If another exception is thrown, a rollback of the global transaction is enforced,
 and all set operations are undone.

Change History

Release
 Modification
 
7.0.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- updateBusinessCategory
void updateBusinessCategory(BusinessCategoryDefinition businessCategoryDefinition)
                            throws ArchiveUnsupportedOperationException,
                                   BusinessCategoryNotEnabledException,
                                   CannotCreateWorkItemException,
                                   InvalidAssignmentReasonException,
                                   InvalidLengthException,
                                   InvalidPropertyValueException,
                                   NotAuthorizedException,
                                   ObjectDoesNotExistException,
                                   ParameterNullException,
                                   UnexpectedFailureException,
                                   WorkItemManagerException,
                                   java.rmi.RemoteException,
                                   javax.ejb.EJBException
Updates a business category with values from the specified business category definition.
 
 The caller must be a business category system administrator.
 
 The action associated to this method is BusinessCategoryActions.UPDATE.
 
 This method is not supported in archive mode.
Parameters:businessCategoryDefinition - The BusinessCategoryDefinition
  from which a business category is to be updated.
 
Throws:
ArchiveUnsupportedOperationException
BusinessCategoryNotEnabledException
CannotCreateWorkItemException
InvalidAssignmentReasonException
InvalidLengthException
InvalidPropertyValueException
NotAuthorizedException
ObjectDoesNotExistException
ParameterNullException
UnexpectedFailureException
WorkItemManagerException
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0 Feature Pack
 
Change History

Release
 Modification
 
7.0.0.3
 
 Throws an ArchiveUnsupportedOperationException when called in archive mode.

- isBusinessCategorySystemAdministrator
boolean isBusinessCategorySystemAdministrator()
                                              throws java.rmi.RemoteException,
                                                     javax.ejb.EJBException
States whether the logged-on user is a system administrator for business categories.
    
    In general, authorization is granted to persons explicitly when a business category is created
    or updated.
    Above that, special authority is granted to a person playing the role of a business category
    system administrator. A business category system administrator has all priviledges for business categories.
 
Returns:boolean -
    boolean -
   True states that the logged-on user is a business category system administrator.
   False states that the logged-on user is no business category system administrator.
 
Throws:
java.rmi.RemoteException
javax.ejb.EJBExceptionSince:
7.0 Feature Pack