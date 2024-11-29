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

## Class DeployedSolution

- java.lang.Object
    - com.ibm.casemgmt.api.DeployedSolution

- public final class DeployedSolution
extends java.lang.Object
Represents a deployed solution in the case management system. To obtain an instance
 of DeployedSolution, use one of the factory methods, getFetchlessInstance 
 or fetchInstance.  A list of deployed solutions can be obtained by
 calling the fetchSolutions method.
 
 If an instance if fetched by calling the fetchInstance method, the method
 verifies that the referenced object store and solution name represent
 a valid solution in the system, and if not, throws an exception. If
 the getFetchlessInstance() method is called, no such verification 
 occurs, but an exception may be thrown later if a method is called that requires that the
 identifiers used to reference the solution are valid.
 
 Much of the information returned by DeployedSolution is managed by a cache internal
 to the Case Java API. All of the information can be obtained whether the
 instance was obtained in a fetched or a fetchless manner, but the
 fetchInstance method just performs an initial check to ensure
 that the referenced case type is valid.

ID status:
ID review by David Newhall

- ========== METHOD SUMMARY ===========
    - Method Summary All Methods Static Methods Instance Methods Concrete Methods Modifier and Type Method and Description static DeployedSolution fetchInstance (ObjectStoreReference objStoreRef, java.lang.String solutionName) A factory method that returns an instance of DeployedSolution . static java.util.List<DeployedSolution > fetchSolutions (java.lang.String ceUri, java.lang.String mashupSrvUri) A factory method that returns a list of deployed solutions. static java.util.List<DeployedSolution > fetchSolutions (java.lang.String ceUri, java.lang.String[] objectStoreNameArray) A factory method that returns a list of deployed solutions. java.util.List<java.lang.String> getAppSpaceNames () java.util.List<CaseType > getCaseTypes () Returns the list of CaseType objects representing the case types deployed with this solution. java.util.Date getDateLastModified () Returns the last modified date of the solution folder. SolutionDeploymentStatus getDeploymentStatus () Returns the deployment status of this solution. java.lang.String getDescription () Returns the textual description. java.util.List<DocumentType > getDocumentTypes () Returns the list of DocumentType objects representing the document types deployed with this solution. static DeployedSolution getFetchlessInstance (ObjectStoreReference objStoreRef, java.lang.String solutionName) A factory method that returns an instance of DeployedSolution without verifying that the identifiers used to reference the object store and solution represent a valid deployed solution. com.filenet.api.util.Id getFolderId () Returns the ID of the deployed solution. java.lang.String getMashupServerURI () Returns the mashup server URI for this deployed solution. ObjectStoreReference getObjectStoreReference () Returns an ObjectStoreReference that represents a reference to the Content Engine object store where this solution is deployed. java.lang.String getPEConnectionPoint () Returns the name of the Process Engine (PE) connection point configured for this solution. java.lang.String getPrefix () Returns the prefix associated with this solution java.util.List<java.lang.String> getRoles () java.lang.String getSolutionDisplayName () Returns the solution display name associated with this solution java.util.Map<java.lang.String,java.lang.String> getSolutionLayouts () Returns a string array containing the solution layouts specified in this deployed solution. java.util.Map<java.lang.String,java.lang.String> getSolutionLayoutsDisplayName () Returns a string array containing the solution layouts display name in this deployed solution. java.lang.String getSolutionName () Returns the name of the solution. java.lang.String[] getStaticPages (java.lang.String roleName) Returns a string array containing the static pages name for the role specified in this deployed solution. filenet.vw.api.VWSession getVWSession () A convenience method to obtain a VWSession that is appropriate for this solution. java.lang.String getWebAppId () Returns the web application ID for the deployed solution.

### Method Summary

| Modifier and Type                                | Method and Description                                                                                                                                                                                                                                                                                |
|--------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static DeployedSolution                          | fetchInstance(ObjectStoreReference objStoreRef,              java.lang.String solutionName) A factory method that returns an instance of DeployedSolution.                                                                                                                                            |
| static java.util.List<DeployedSolution>          | fetchSolutions(java.lang.String ceUri,               java.lang.String mashupSrvUri) A factory method that returns a list of deployed solutions.                                                                                                                                                       |
| static java.util.List<DeployedSolution>          | fetchSolutions(java.lang.String ceUri,               java.lang.String[] objectStoreNameArray) A factory method that returns a list of deployed solutions.                                                                                                                                             |
| java.util.List<java.lang.String>                 | getAppSpaceNames()                                                                                                                                                                                                                                                                                    |
| java.util.List<CaseType>                         | getCaseTypes() Returns the list of CaseType objects representing the case types deployed  with this solution.                                                                                                                                                                                         |
| java.util.Date                                   | getDateLastModified() Returns the last modified date of the solution folder.                                                                                                                                                                                                                          |
| SolutionDeploymentStatus                         | getDeploymentStatus() Returns the deployment status of this solution.                                                                                                                                                                                                                                 |
| java.lang.String                                 | getDescription() Returns the textual description.                                                                                                                                                                                                                                                     |
| java.util.List<DocumentType>                     | getDocumentTypes() Returns the list of DocumentType objects representing the document types  deployed with this solution.                                                                                                                                                                             |
| static DeployedSolution                          | getFetchlessInstance(ObjectStoreReference objStoreRef,                     java.lang.String solutionName) A factory method that returns an instance of DeployedSolution  without verifying that the identifiers used to reference  the object store and solution represent a valid deployed solution. |
| com.filenet.api.util.Id                          | getFolderId() Returns the ID of the deployed solution.                                                                                                                                                                                                                                                |
| java.lang.String                                 | getMashupServerURI() Returns the mashup server URI for this deployed solution.                                                                                                                                                                                                                        |
| ObjectStoreReference                             | getObjectStoreReference() Returns an ObjectStoreReference that represents a reference to   the Content Engine object store where this solution is deployed.                                                                                                                                           |
| java.lang.String                                 | getPEConnectionPoint() Returns the name of the Process Engine (PE) connection point configured for this solution.                                                                                                                                                                                     |
| java.lang.String                                 | getPrefix() Returns the prefix associated with this solution                                                                                                                                                                                                                                          |
| java.util.List<java.lang.String>                 | getRoles()                                                                                                                                                                                                                                                                                            |
| java.lang.String                                 | getSolutionDisplayName() Returns the solution display name associated with this solution                                                                                                                                                                                                              |
| java.util.Map<java.lang.String,java.lang.String> | getSolutionLayouts() Returns a string array containing the solution layouts specified in this deployed solution.                                                                                                                                                                                      |
| java.util.Map<java.lang.String,java.lang.String> | getSolutionLayoutsDisplayName() Returns a string array containing the solution layouts display name in this deployed solution.                                                                                                                                                                        |
| java.lang.String                                 | getSolutionName() Returns the name of the solution.                                                                                                                                                                                                                                                   |
| java.lang.String[]                               | getStaticPages(java.lang.String roleName) Returns a string array containing the static pages name for the role specified in this deployed solution.                                                                                                                                                   |
| filenet.vw.api.VWSession                         | getVWSession() A convenience method to obtain a VWSession that is appropriate for this solution.                                                                                                                                                                                                      |
| java.lang.String                                 | getWebAppId() Returns the web application ID for the deployed solution.                                                                                                                                                                                                                               |

- Methods inherited from class java.lang.Object
equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait