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

## Class LaunchStep

- java.lang.Object
    - com.ibm.casemgmt.api.tasks.LaunchStep

- public final class LaunchStep
extends java.lang.Object
Represents the step to launch a workflow of a task. A LaunchStep can be initialized as either a new launch 
 step or an in-progress launch step. A new launch step allocates a work object number from the server and retrieves 
 all information about the launch step, including parameters with default values.  
 
 An in-progress launch step is initialized only with information returned previously when the launch step was 
 initialized as a new launch step. For example, the operation to create a task may be broken up into multiple 
 requests to a web application. The first request initializes the launch step as a new launch step, and subsequent 
 requests initialize the launch step as an in-progress launch step.
  
 The previous information, used to initialize an in-progress launch step, includes the work object number that was 
 allocated initially. Any parameters in an in-progress launch step must be added by calling the addParameter
 method.

ID status:
ID review by David Newhall, 5/16/2012.

- ========== METHOD SUMMARY ===========
    - Method Summary All Methods Instance Methods Concrete Methods Modifier and Type Method and Description java.util.List<CaseMgmtProperty > fetchBusinessObjects (java.util.List<java.lang.String> selectedProperties) fetchBusinessObjects fetches Business Objects, if there are any. java.lang.String[] fetchDependentParameterChanges () If you modify any parameter that has the attribute hasDependentProperties() set as true, a round trip should be made to fetch any changes due to that modification. java.lang.String getAuthoredMapName () Obtains the authored map name. java.lang.Boolean getBusinessObjectParameterAccess (java.lang.String type, java.lang.String name) Get the access right permissions (read-oly or read-write) for the selected step BO paramter java.util.List<java.lang.String> getBusinessObjectsParameters (java.lang.String type) Returns the symbolic names of the business objects selected on this step. com.filenet.api.util.Id getCaseFolderId () Returns the Id of the Case folder, if this work item is associated with a Task of a Case. com.filenet.api.util.Id getCaseId () java.lang.String getComment () Returns a comment associated with this launch step. java.lang.String getExternalDataIdentifier () If the launch step is associated with a Case object that is configured with an external data server, this method returns the external data identifier appropriate for the current step parameter and case property values. java.lang.String getMapName () Obtains the map name. com.filenet.api.meta.PropertyDescription getNonStepPropertyDescription (java.lang.String name) Obtains a PropertyDescription corresponding to a non-step property. java.lang.String[] getNonStepPropertyNames () Obtains the non-step property names. java.lang.Object getNonStepPropertyValue (java.lang.String name) Obtains the value of a non-step property. StepParameter getParameter (java.lang.String name) Returns a StepParameter from the cache of parameters. java.lang.String[] getParameterAuthoredNames () Returns the array of authored names of the parameters currently contained in the parameter cache of this LaunchStep . StepParameter getParameterByAuthoredName (java.lang.String authName) Returns a StepParameter from the cache of parameters by its authored name. StepParameter getParameterBySymbolicName (java.lang.String propertyProvider, java.lang.String propertySymbolicName) Returns a StepParameter from the cache of parameters by its property provider and symbolic name. java.lang.String[] getParameterNames () Returns the array of names of the parameters currently contained in the parameter cache of this LaunchStep . java.lang.String[] getParameterSymbolicNames (java.lang.String propertyProvider) Returns the symbolic names of the parameters with a particular provider. java.lang.Object getParameterValue (java.lang.String name) Returns the parameter value of a StepParameter in the cache of parameters. java.lang.String getSelectedResponse () Retrieves the value of the selected response. java.lang.String getStepDescription () Returns the description of the step. int getStepId () Obtains the step id. java.lang.String getStepName () Obtains the step name. filenet.vw.api.VWStepProcessorInfo getStepProcessorInfo () Returns an object that describes the step processor information. java.lang.String[] getStepResponses () Retrieves the values of the possible responses. java.lang.String getSubject () Retrieves the subject that describes this launch step. java.lang.String getWorkflowName () Retrieves the workflow name. java.lang.String getWorkObjectNumber () Retrieves the work object number. boolean isNewLaunchStep () Indicates if this launch step was initialized as a new launch step. void setComment (java.lang.String comment) Specifies a comment associated with this launch step. void setExternalDataIdentifier (java.lang.String externDataIdent) Sets the current external data identifier. void setNonStepPropertyValue (java.lang.String name, java.lang.Object value) Specifies the value of a non-step property. void setParameterValue (java.lang.String name, java.lang.Object value) Sets the parameter value of a StepParameter in the cache of parameters. void setReferenceParameterValue (java.lang.String name, java.lang.Object value, int valueType) Sets a parameter value as a reference parameter. void setSelectedResponse (java.lang.String response) Sets the selected response to the passed-in String value. void setSubject (java.lang.String subject) Specifies a subject that describes this launch step.

### Method Summary

| Modifier and Type                        | Method and Description                                                                                                                                                                                                                                   |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| java.util.List<CaseMgmtProperty>         | fetchBusinessObjects(java.util.List<java.lang.String> selectedProperties) fetchBusinessObjects   fetches Business Objects, if there are any.                                                                                                             |
| java.lang.String[]                       | fetchDependentParameterChanges() If you modify any parameter that has the attribute hasDependentProperties()  set as true, a round trip should be made to fetch any changes due to that  modification.                                                   |
| java.lang.String                         | getAuthoredMapName() Obtains the authored map name.                                                                                                                                                                                                      |
| java.lang.Boolean                        | getBusinessObjectParameterAccess(java.lang.String type,                                 java.lang.String name) Get the access right permissions (read-oly or read-write) for the selected step BO paramter                                               |
| java.util.List<java.lang.String>         | getBusinessObjectsParameters(java.lang.String type) Returns the symbolic names of the business objects selected on this step.                                                                                                                            |
| com.filenet.api.util.Id                  | getCaseFolderId() Returns the Id of the Case folder, if this work item is associated with  a Task of a Case.                                                                                                                                             |
| com.filenet.api.util.Id                  | getCaseId()                                                                                                                                                                                                                                              |
| java.lang.String                         | getComment() Returns a comment associated with this launch step.                                                                                                                                                                                         |
| java.lang.String                         | getExternalDataIdentifier() If the launch step is associated with a Case object that is configured with  an external data server, this method returns the external data identifier  appropriate for the current step parameter and case property values. |
| java.lang.String                         | getMapName() Obtains the map name.                                                                                                                                                                                                                       |
| com.filenet.api.meta.PropertyDescription | getNonStepPropertyDescription(java.lang.String name) Obtains a PropertyDescription corresponding to a non-step property.                                                                                                                                 |
| java.lang.String[]                       | getNonStepPropertyNames() Obtains the non-step property names.                                                                                                                                                                                           |
| java.lang.Object                         | getNonStepPropertyValue(java.lang.String name) Obtains the value of a non-step property.                                                                                                                                                                 |
| StepParameter                            | getParameter(java.lang.String name) Returns a StepParameter from the cache of parameters.                                                                                                                                                                |
| java.lang.String[]                       | getParameterAuthoredNames() Returns the array of authored names of the parameters currently contained in the parameter cache of this   LaunchStep.                                                                                                       |
| StepParameter                            | getParameterByAuthoredName(java.lang.String authName) Returns a StepParameter from the cache of parameters by its authored name.                                                                                                                         |
| StepParameter                            | getParameterBySymbolicName(java.lang.String propertyProvider,                           java.lang.String propertySymbolicName) Returns a StepParameter from the cache of parameters by its property provider  and symbolic name.                         |
| java.lang.String[]                       | getParameterNames() Returns the array of names of the parameters currently contained in the parameter cache of this   LaunchStep.                                                                                                                        |
| java.lang.String[]                       | getParameterSymbolicNames(java.lang.String propertyProvider) Returns the symbolic names of the parameters with a particular provider.                                                                                                                    |
| java.lang.Object                         | getParameterValue(java.lang.String name) Returns the parameter value of a StepParameter in the cache of parameters.                                                                                                                                      |
| java.lang.String                         | getSelectedResponse() Retrieves the value of the selected response.                                                                                                                                                                                      |
| java.lang.String                         | getStepDescription() Returns the description of the step.                                                                                                                                                                                                |
| int                                      | getStepId() Obtains the step id.                                                                                                                                                                                                                         |
| java.lang.String                         | getStepName() Obtains the step name.                                                                                                                                                                                                                     |
| filenet.vw.api.VWStepProcessorInfo       | getStepProcessorInfo() Returns an object that describes the step processor information.                                                                                                                                                                  |
| java.lang.String[]                       | getStepResponses() Retrieves the values of the possible responses.                                                                                                                                                                                       |
| java.lang.String                         | getSubject() Retrieves the subject that describes this launch step.                                                                                                                                                                                      |
| java.lang.String                         | getWorkflowName() Retrieves the workflow name.                                                                                                                                                                                                           |
| java.lang.String                         | getWorkObjectNumber() Retrieves the work object number.                                                                                                                                                                                                  |
| boolean                                  | isNewLaunchStep() Indicates if this launch step was initialized as a new launch step.                                                                                                                                                                    |
| void                                     | setComment(java.lang.String comment) Specifies a comment associated with this launch step.                                                                                                                                                               |
| void                                     | setExternalDataIdentifier(java.lang.String externDataIdent) Sets the current external data identifier.                                                                                                                                                   |
| void                                     | setNonStepPropertyValue(java.lang.String name,                        java.lang.Object value) Specifies the value of a non-step property.                                                                                                                |
| void                                     | setParameterValue(java.lang.String name,                  java.lang.Object value) Sets the parameter value of a StepParameter in the cache of parameters.                                                                                                |
| void                                     | setReferenceParameterValue(java.lang.String name,                           java.lang.Object value,                           int valueType) Sets a parameter value as a reference parameter.                                                            |
| void                                     | setSelectedResponse(java.lang.String response) Sets the selected response to the passed-in String value.                                                                                                                                                 |
| void                                     | setSubject(java.lang.String subject) Specifies a subject that describes this launch step.                                                                                                                                                                |

- Methods inherited from class java.lang.Object
equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait