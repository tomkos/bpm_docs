- Overview
- Package
- Class
- Tree
- Deprecated
- Index
- Help

- Prev Package
- Next Package

- Frames
- No Frames

- All Classes

# Package com.ibm.casemgmt.api.deletecase

See: Description

- Class Summary 

Class
Description

CaseInstancesDeleterFromES
 

CloseCase

Represents the CloseCase class.

DeleteCaseDocumentsFromES
 

ProcessInstancesDeleter

## Package com.ibm.casemgmt.api.deletecase Description

The artifacts in case instances will be deleted in the following order,
  Processes associated with the activities. 
      If the process instance is active, It will be terminated before deletion.

 Activities. 
      If the activity is associated with a P8 workflow, the P8 workflow is deleted before deleting the activity.
      Activities in working state i.e the active activities will be promoted before deletion.

 Documents in the case folders. 
      If the document is referenced else where apart from the current case, 
      it will be unfiled and delete case result will contain the list of unfiled documents. 
      The document referenced only with in the current case will be deleted.

 Case Folder. 
      The case folders will be deleted from the Target Object store after the contents of the folder are deleted.

- Overview
- Package
- Class
- Tree
- Deprecated
- Index
- Help

- Prev Package
- Next Package

- Frames
- No Frames

- All Classes