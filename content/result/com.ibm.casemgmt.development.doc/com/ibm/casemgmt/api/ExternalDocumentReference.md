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

## Class ExternalDocumentReference

- java.lang.Object
    - com.ibm.casemgmt.api.ExternalDocumentReference

- public final class ExternalDocumentReference
extends java.lang.Object
Represents a reference to an external document filed in a Case folder or a sub-folder
 of a Case.  References to external documents that are filed in the same Case folder or
 sub-folder share a single proxy document which is multi-filed into each folder.  This class
 takes care of locating the existing proxy document, if any, and filing that same document
 into a different folder, or creating a new proxy document if none exists.

- ========== METHOD SUMMARY ===========
    - Method Summary All Methods Static Methods Instance Methods Concrete Methods Modifier and Type Method and Description com.filenet.api.core.BatchItemHandle addToBatch (com.filenet.api.core.UpdatingBatch ub) Adds the changes represented by this instance to an UpdatingBatch instance. static ExternalDocumentReference createPendingFromAttachment (ObjectStoreReference objStore, filenet.vw.api.VWAttachment att, com.filenet.api.util.Id folderId) A factory method that constructs an ExternalDocumentReference instance representing a new filing of a reference to an external document, using a VWAttachment representing the external document. static ExternalDocumentReference createPendingInstance (ObjectStoreReference objStore, com.filenet.api.util.Id parentFolderId, java.lang.String externalDocName, java.lang.String externalDocId, java.lang.String externalRepositoryInfo, int externalRepositoryType) A factory method that constructs an ExternalDocumentReference instance representing a new filing of a reference to an external document. static ExternalDocumentReference getFetchlessFromAttachment (ObjectStoreReference objStore, filenet.vw.api.VWAttachment att, com.filenet.api.util.Id caseId) Factory method that constructs an ExternalDocumentReference instance representing a reference to an external document in a Case. com.filenet.api.util.Id getProxyDocumentId () Retrieves the Id of the proxy document that references the external document. com.filenet.api.util.Id getProxyDocumentVsId () Retrieves the version series Id of the proxy document that references the external document. boolean isFilePending () Indicates that a new filing of an external document reference is pending by this ExternalDocumentReference instance. boolean isUnfilePending () Indicates that an unfiling of a current filing of an external document reference is pending by this ExernalDocumentReference instance. void refreshFromBatch (com.filenet.api.core.UpdatingBatch ub, com.filenet.api.core.BatchItemHandle bih) Refreshes this object after a batch execution. void save (com.filenet.api.constants.RefreshMode mode) Saves this ExternalDocumentReference instance, saving the file or unfile operation that is pending. boolean setUnfiled (com.filenet.api.util.Id folderId) Flags the External Document Reference as needing to be unfiled from the parent folder specified when the reference object was created.

### Method Summary

| Modifier and Type                    | Method and Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| com.filenet.api.core.BatchItemHandle | addToBatch(com.filenet.api.core.UpdatingBatch ub) Adds the changes represented by this instance to an UpdatingBatch instance.                                                                                                                                                                                                                                                                                                                                                          |
| static ExternalDocumentReference     | createPendingFromAttachment(ObjectStoreReference objStore,                            filenet.vw.api.VWAttachment att,                            com.filenet.api.util.Id folderId) A factory method that constructs an ExternalDocumentReference instance representing a new filing of a reference to  an external document, using a VWAttachment representing the external document.                                                                                                 |
| static ExternalDocumentReference     | createPendingInstance(ObjectStoreReference objStore,                      com.filenet.api.util.Id parentFolderId,                      java.lang.String externalDocName,                      java.lang.String externalDocId,                      java.lang.String externalRepositoryInfo,                      int externalRepositoryType) A factory method that constructs an ExternalDocumentReference instance representing a new filing of a reference to  an external document. |
| static ExternalDocumentReference     | getFetchlessFromAttachment(ObjectStoreReference objStore,                           filenet.vw.api.VWAttachment att,                           com.filenet.api.util.Id caseId) Factory method that constructs an ExternalDocumentReference instance representing a reference  to an external document in a Case.                                                                                                                                                                       |
| com.filenet.api.util.Id              | getProxyDocumentId() Retrieves the Id of the proxy document that references the external document.                                                                                                                                                                                                                                                                                                                                                                                     |
| com.filenet.api.util.Id              | getProxyDocumentVsId() Retrieves the version series Id of the proxy document that references the external document.                                                                                                                                                                                                                                                                                                                                                                    |
| boolean                              | isFilePending() Indicates that a new filing of an external document reference is pending  by this ExternalDocumentReference instance.                                                                                                                                                                                                                                                                                                                                                  |
| boolean                              | isUnfilePending() Indicates that an unfiling of a current filing of an external document reference is pending by this ExernalDocumentReference instance.                                                                                                                                                                                                                                                                                                                               |
| void                                 | refreshFromBatch(com.filenet.api.core.UpdatingBatch ub,                 com.filenet.api.core.BatchItemHandle bih) Refreshes this object after a batch execution.                                                                                                                                                                                                                                                                                                                       |
| void                                 | save(com.filenet.api.constants.RefreshMode mode) Saves this ExternalDocumentReference instance, saving the file or unfile operation  that is pending.                                                                                                                                                                                                                                                                                                                                  |
| boolean                              | setUnfiled(com.filenet.api.util.Id folderId) Flags the External Document Reference as needing to be unfiled from the  parent folder specified when the reference object was created.                                                                                                                                                                                                                                                                                                   |

- Methods inherited from class java.lang.Object
equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait