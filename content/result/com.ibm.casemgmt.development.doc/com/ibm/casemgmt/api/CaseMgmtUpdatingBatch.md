- Overview
- Package
- Class
- Tree
- Deprecated
- Index
- Help

- Prev Class
- Next Class

- Frames
- No Frames

- All Classes

- Summary:
- Nested |
- Field |
- Constr |
- Method

- Detail:
- Field |
- Constr |
- Method

## Class CaseMgmtUpdatingBatch

- java.lang.Object
    - com.ibm.casemgmt.api.CaseMgmtUpdatingBatch

- public class CaseMgmtUpdatingBatch
extends java.lang.Object
Submits changes to Case Management objects in a batch.  One round-trip to the server
 is made to submit the changes for multiple objects.  This class directly handles the
 changes for Case, Task and ExternalDocumentReference Case Java API objects.
 
 Internally, an UpdatingBatch instance from the IBM Content Engine Java
 API is managed, collecting each change to be submitted to the server.

- ========== METHOD SUMMARY ===========
    - Method Summary All Methods Static Methods Instance Methods Concrete Methods Modifier and Type Method and Description com.filenet.api.core.BatchItemHandle add (Case c) Adds the changes for a Case object to the batch. com.filenet.api.core.BatchItemHandle add (ExternalDocumentReference extDoc) Adds the changes for an ExternalDocumentReference object to the batch. com.filenet.api.core.BatchItemHandle add (Task t) Adds the changes for a Task object to the batch. static CaseMgmtUpdatingBatch createUpdatingBatchInstance (DomainReference domain, com.filenet.api.constants.RefreshMode refresh) Factory method that creates a new CaseMgmtUpdatingBatch instance. boolean hasPendingExecute () Indicates if the batch has yet to be executed. void updateBatch () Executes the changes for all of the objects added to the batch.

### Method Summary

| Modifier and Type                    | Method and Description                                                                                                                                                                          |
|--------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| com.filenet.api.core.BatchItemHandle | add(Case c) Adds the changes for a Case object to the batch.                                                                                                                                    |
| com.filenet.api.core.BatchItemHandle | add(ExternalDocumentReference extDoc) Adds the changes for an ExternalDocumentReference object to the batch.                                                                                    |
| com.filenet.api.core.BatchItemHandle | add(Task t) Adds the changes for a Task object to the batch.                                                                                                                                    |
| static CaseMgmtUpdatingBatch         | createUpdatingBatchInstance(DomainReference domain,                            com.filenet.api.constants.RefreshMode refresh) Factory method that creates a new CaseMgmtUpdatingBatch instance. |
| boolean                              | hasPendingExecute() Indicates if the batch has yet to be executed.                                                                                                                              |
| void                                 | updateBatch() Executes the changes for all of the objects added to the batch.                                                                                                                   |

- Methods inherited from class java.lang.Object
equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait