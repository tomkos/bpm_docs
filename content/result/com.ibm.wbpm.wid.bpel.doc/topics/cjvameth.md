<!-- image -->

# Using Java methods in
process snippets

Java coding methods are used
in process snippets to perform a variety of functions.

When you use a process snippet in a BPEL process, the Java code
does everything that you would normally do in an enterprise bean,
and using the same restrictions (for example, there is no thread handling).

- To compose an expression such as that used in transition conditions,
for each activity or timeout.
- Within a snippet activity.

- Partner links
- Correlation sets
- Custom properties
- Information about the state of the current process instance

You can access the snippet process variables the same way as you
would access them if they were local variables in the Java method.
You can use any BPEL variable in a snippet without the need to declare
it. There is no separate input or output data specified for a snippet
activity. In the case of more complex objects, XML-based schema types
can be mapped to corresponding Java types using predefined mapping
rules.

## Process Variables

1. You can initialize a process variable on the properties view details
tab when you select the variable in the BPEL process editor.
2. You can assign the WSDL message type, which is defined as an XML-schema.
In this case the message can either be handled in RPC style (where
the representation of the message is the corresponding Java class)
or in document/literal wrapped style (where a single-part message
of a primitive type is encapsulated in a commonj.sdo.DataObject).
3. Assign the XML schema directly to the variable. The primitive
types are mapped to the corresponding Java class. For example, xsd:int is
mapped to java.lang.Integer. Complex types are represented
by a commonj.sdo.DataObject.

For Java conditions
and expressions (including join conditions, transition conditions,
while conditions, and wait durations), the default access for BPEL
process variables is read-only. This means that changes to BPEL process
variables are discarded after the Java condition or expression is
evaluated. However, when the changes are discarded depends on the
data type (complex or boxed-primitive) and the process execution mode
(long-running or microflow). A common pitfall is a while condition
in which a counter is evaluated and then increased or decreased. This
action can fail because the default access for the BPEL process variables
used in the while condition is read-only.

Specifying the variables as read-only saves four unnecessary
database updates, including four unnecessary update events. The read-only
access also lowers the probability of database deadlocks. This can
be either done manually in the java code (see the following Code
Example section) or, as it would be recommended, using the
"Performance" property page (refer to the following Performance
property page section).

In some cases, conditions such
as the while condition (that evaluates a counter
and modifies it in one step) ensures that the BPEL process definition
can be kept more readable by specifying the counter BPEL process variable
as read/write access instead of separate the counter modification
of the evaluation.

```
// @bpe.readOnlyVariables names="<space separated list of BPEL Variables>"
```

```
// @bpe.readWriteVariables names="<space separated list of BPEL Variables>"
```

```
// @bpe.readWriteVariables names="LoopCounter Amount"
```

This
example specifies read/write access to two BPEL process variables, LoopCounter 
and Amount. You can place these pragmas at any position
in your Java code, but you need to specify them for each Java snippet,
condition, or expression separately. For better readability, list
these pragmas at the beginning of the Java code.

## Creating data objects

To create data objects
you need the BOFactory service. The following code
snippet shows how you can obtain the BOFactory service:

```
BOFactory boFactory = 
(BOFactory)ServiceManager.INSTANCE.locateService("com/ibm/websphere/bo/BOFactory");
```

To
create a nested data object, you can use the createDataObject method
of the DataObject class:

```
DataObject nested = Output.createDataObject("processBusinessObject");
```

You
can also create a data object using the create method of the BOFactory service.
You have to specify namespace and name so that the order of the parameters
matches the order that is used in the code sample:

```
MyBO = factory.create("http://JavaSnippets/bpc/samples","BO");
```

```
BOCopy copyService = 
(BOCopy)ServiceManager.INSTANCE.locateService("com/ibm/websphere/bo/BOCopy");
```

```
DataObject dataObject = copyService.copy(ProcessBusinessObject);
```

```
copyService.copyInto(ProcessBO, Output, "processBO");
```

## Java methods

The
following table provides a list of the available Java methods:

| Java method                                                                                                                                                          | Function                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| getServiceRefFromPartnerLink commonj.sdo.DataObject getServiceRefFromPartnerLink( String partnerLinkName, int role )                                                 | These methods can be used to either specify or retrieve the Service destination at the end of the named partner link. The role value must be one of: PARTNER\_LINK\_PARTNER\_ROLE PARTNER\_LINK\_MY\_ROLE  A DataObject is returned that contains an EndpointReference object with the name "EndpointReference".                                                                                                                                                                                                                                                                                                                                                                            |
| setServiceRefToPartnerLink void setServiceRefToPartnerLink( String partnerLinkName, commonj.sdo.DataObject serviceRef)                                               | These methods can be used to either specify or retrieve the Service destination at the end of the named partner link. The role value must be one of: PARTNER\_LINK\_PARTNER\_ROLE PARTNER\_LINK\_MY\_ROLE  A DataObject is returned that contains an EndpointReference object with the name "EndpointReference".                                                                                                                                                                                                                                                                                                                                                                            |
| getVariableProperty Object getVariableProperty( String variableName, QName propertyName )                                                                            | These methods either specify or return the value of a process variable's property. If either the property or the variable do not exist, a StandardFaultException of kind selection failure is thrown. If the value is not compatible to the type of the property, a StandardFaultException of kind mismatch assignment failure is thrown. Note: An alternative way to specify a process variable is on the details tab of the properties view when you select the variable in the BPEL process editor.                                                                                                                                                                                |
| setVariableProperty void setVariableProperty( String variableName, QName propertyName, Object value)                                                                 | These methods either specify or return the value of a process variable's property. If either the property or the variable do not exist, a StandardFaultException of kind selection failure is thrown. If the value is not compatible to the type of the property, a StandardFaultException of kind mismatch assignment failure is thrown. Note: An alternative way to specify a process variable is on the details tab of the properties view when you select the variable in the BPEL process editor.                                                                                                                                                                                |
| getCorrelationSetProperty Serializable getCorrelationSetProperty( String correlationSetName, QName propertyName )                                                    | This method can be used to retrieve the properties of correlation sets that are declared at the process level. If either the property with name propertyName or the correlation set with name correlationSetName do not exist, a StandardFaultException of kind "selection failure" is thrown.                                                                                                                                                                                                                                                                                                                                                                                        |
| getProcessCustomProperty String getProcessCustomProperty( String name)                                                                                               | Use these methods to access or define custom properties at the process level.The value for propertyName must be a valid NCName, and cannot be greater than 220 bytes in UTF-8 format. Not all functionality can be guaranteed for non NCNames.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| setProcessCustomProperty void   setProcessCustomProperty( String name, String value )                                                                                | Use these methods to access or define custom properties at the process level.The value for propertyName must be a valid NCName, and cannot be greater than 220 bytes in UTF-8 format. Not all functionality can be guaranteed for non NCNames.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| getActivityCustomProperty String getActivityCustomProperty( String activityName, String propertyName )                                                               | Use these methods to access or define custom properties at the activity level. If the activity does not exist, or activityName does not uniquely qualify an activity, a StandardFaultException of kind "selection failure" is thrown. If the value exceeds 254 bytes, an InvalidLengthException is thrown. The value for propertyName must be a valid NCName, and cannot be greater than 220 bytes in UTF-8 format. Not all functionality can be guaranteed for non NCNames.                                                                                                                                                                                                          |
| setActivityCustomProperty void setActivityCustomProperty( String activityName String propertyName, String value )                                                    | Use these methods to access or define custom properties at the activity level. If the activity does not exist, or activityName does not uniquely qualify an activity, a StandardFaultException of kind "selection failure" is thrown. If the value exceeds 254 bytes, an InvalidLengthException is thrown. The value for propertyName must be a valid NCName, and cannot be greater than 220 bytes in UTF-8 format. Not all functionality can be guaranteed for non NCNames.                                                                                                                                                                                                          |
| getLinkStatus boolean getLinkStatus(String linkName)                                                                                                                 | This method can be used in join conditions to access the state of the incoming links.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| activityInstance com.ibm.bpe.api.ActivityInstanceData activityInstance()                                                                                             | Use this method to return the current activity as an object in order to access its context                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| activityInstance com.ibm.bpe.api.ActivityInstanceData activityInstance( String activityName)                                                                         | Use this method to select an activity instance by its name.  To access an activity using this method, the activity must conform to the following restrictions:  The activity name must be unique within the scope of the process.   The activity must be a basic activity. If the activity is nested within an event handler, or forEach activity the Java code snippet that accesses the activity must be within the same event handler, or forEach activity. The activity must be a predecessor of the current Java code snippet (navigation-wise). The activity must be persisted in the database. That is, the attribute businessRelevant of the activity is to be set to "true". |
| processInstance com.ibm.bpe.api.ProcessInstanceData processInstance()                                                                                                | Use this method to return the current process as an object in order to access its context.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| raiseFault void raiseFault( QName faultName )  void raiseFault( QName faultName, String variableName )  void raiseFault( QName faultName, Serializable message )     | Use this method to raise a fault in the surrounding process.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| forceRollback void forceRollback( )                                                                                                                                  | Use this to cause the compensation of the microflow. This method will not work with long running processes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| BpelException  com.ibm.bpe.api.BpelException getCurrentFaultAsException()                                                                                            | Use this method to provide access to a Java exception within a fault handler.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| getServiceRefForProcessTemplate commonj.sdo.DataObject getServiceRefForProcessTemplate( String processTemplateName, String portTypeNamespace , String portTypeName ) | Returns a service reference to the port type portTypeNamespace, portTypeName of the process specified by processTemplateName. If multiple versions of a process template are available, the service reference is returned to the current valid version. Important:  Make sure that you added an export with an SCA binding for the corresponding process component in the Assembly editor. Otherwise, no service reference is returned. The getServiceRefForProcessTemplate() API always gets the newest (current) version of the parent process.                                                                                                                                     |

## Related concepts

- Replacement variables and context variables
- Using custom properties for human tasks
- Using event handlers

## Related tasks

- Modifying the properties of an activity
- Modifying the type of an activity
- Working with basic activities
- Working with structured activities
- Modeling human workflows