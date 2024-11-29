<!-- image -->

# Accessing the remote interface of the session bean

## About this task

## Procedure

1 Add a reference to the remote interface of the sessionbean to the application deployment descriptor. Add thereference to one of the following files: The reference to the remote home interface for process applicationsis shown in the following example:<ejb-ref> <ejb-ref-name>ejb/BusinessFlowManagerHome</ejb-ref-name> <ejb-ref-type>Session</ejb-ref-type> <home>com.ibm.bpe.api.BusinessFlowManagerHome</home> <remote>com.ibm.bpe.api.BusinessFlowManager</remote></ejb-ref> The reference to the remote home interfacefor task applications is shown in the following example:<ejb-ref> <ejb-ref-name>ejb/HumanTaskManagerHome</ejb-ref-name> <ejb-ref-type>Session</ejb-ref-type> <home>com.ibm.task.api.HumanTaskManagerHome</home> <remote>com.ibm.task.api.HumanTaskManager</remote></ejb-ref> If you use IBM® IntegrationDesigner toadd the EJB reference to the deployment descriptor, the binding forthe EJB reference is automatically created when the application isdeployed. For more information on adding EJB references, refer tothe Integration Designer documentation.
    - The application-client.xml file, for a Java™ Platform, Enterprise Edition
(Java EE) client application
    - The web.xml file, for a web application
    - The ejb-jar.xml file, for an Enterprise JavaBeans (EJB) application

```
<ejb-ref>
	<ejb-ref-name>ejb/BusinessFlowManagerHome</ejb-ref-name>
	<ejb-ref-type>Session</ejb-ref-type>
	<home>com.ibm.bpe.api.BusinessFlowManagerHome</home>
	<remote>com.ibm.bpe.api.BusinessFlowManager</remote>
</ejb-ref>
```

```
<ejb-ref>
	<ejb-ref-name>ejb/HumanTaskManagerHome</ejb-ref-name>
	<ejb-ref-type>Session</ejb-ref-type>
	<home>com.ibm.task.api.HumanTaskManagerHome</home>
	<remote>com.ibm.task.api.HumanTaskManager</remote>
</ejb-ref>
```

If you use IBM® Integration
Designer to
add the EJB reference to the deployment descriptor, the binding for
the EJB reference is automatically created when the application is
deployed. For more information on adding EJB references, refer to
the Integration Designer documentation.

2 Decide on how you are going to provide definitions of businessobjects. To work with business objects in a remote clientapplication, you need to have access to the corresponding schemasfor the business objects (XSD or WSDL files) that are used to interactwith a process or task. Access to these files can be provided in oneof the following ways:

To work with business objects in a remote client
application, you need to have access to the corresponding schemas
for the business objects (XSD or WSDL files) that are used to interact
with a process or task. Access to these files can be provided in one
of the following ways:

- If the client application does not run in a Java EE managed environment, package the files
with the client application's EAR file.
- If the client application is a web application or an EJB clientin a managed Java EE environment,either package the files with the client application's EAR file oruse remote artifact loading.
    1. Use the Business Process Choreographer EJB API createMessage and the ClientObjectWrapper.getObject methods
to load the remote business object definitions from the corresponding
application on the server transparently.
    2. Use the Service Data Object Programming API to create or read
a business object as part of an already instantiated business object.
Do this by using the commonj.sdo.DataObject.createDataObject or getDataObject methods on the DataObject interface.
    3. When you want to create a business object as the value for a business
object's property that is typed using the XML schema any or anyType, use the Business Object services
to create or read your business object. To do this, you must set the
remote artifact loader context to point to the application that the
schemas will be loaded from. Then you can use the appropriate Business
Object services.For example, create a business object, where "ApplicationName"
is the name of the application that contains your business object
definitions.BOFactory bofactory = (BOFactory) new 
   ServiceManager().locateService("com/ibm/websphere/bo/BOFactory");

com.ibm.wsspi.al.ALContext.setContext
   ("RALTemplateName", "ApplicationName");
try {
     DataObject dataObject = bofactory.create("uriName", "typeName" );
   } finally {
     com.ibm.wsspi.al.ALContext.unset();
   } 
For example, read XML input, where "ApplicationName"
is the name of the application that contains your business object
definitions.BOXMLSerializer serializerService =
  (BOXMLSerializer) new ServiceManager().locateService
    ("com/ibm/websphere/bo/BOXMLSerializer");
ByteArrayInputStream input = new ByteArrayInputStream(<?xml?>..);

com.ibm.wsspi.al.ALContext.setContext
          ("RALTemplateName", "ApplicationName");
try {
     BOXMLDocument document = serializerService.readXMLDocument(input);
     DataObject dataObject = document.getDataObject();
   } finally {
     com.ibm.wsspi.al.ALContext.unset();
   }
3. Locate the remote home interface of the session bean through
the Java Naming and Directory
Interface (JNDI).  The following example shows this
step for a process application:
// Obtain the default initial JNDI context
InitialContext initialContext = new InitialContext();

// Lookup the remote home interface of the BusinessFlowManager bean
Object result = 
       initialContext.lookup("java:comp/env/ejb/BusinessFlowManagerHome");

// Convert the lookup result to the proper type
   BusinessFlowManagerHome processHome = 
           (BusinessFlowManagerHome)javax.rmi.PortableRemoteObject.narrow
           (result,BusinessFlowManagerHome.class);
The remote home interface of the session bean contains
a create method for EJB objects. The method returns the remote
interface of the session bean.
4. Access the remote interface of the session bean. The following example shows this step for a process application:
BusinessFlowManager process = processHome.create();Access to the session bean does not guarantee that the caller
can perform all of the actions provided by the bean; the caller must
also be authorized for these actions. When an instance of the session
bean is created, a context is associated with the instance of the
session bean. The context contains the caller's principal ID, group
membership list, and indicates whether the caller has one of the Business
Process Choreographer Java EE
roles. The context is used to check the caller's authorization for
each call, even when administrative security is not set. If administrative
security is not set, the caller's principal ID has the value UNAUTHENTICATED.
5 Call the business functions exposed by the service interface. The following example shows this step for a process application: process.initiate("MyProcessModel",input); Calls fromapplications are run as transactions. A transaction is establishedand ended in one of the following ways: Tip: To prevent database lock conflicts, avoidrunning statements similar to the following in parallel:// Obtain user transaction interfaceUserTransaction transaction= (UserTransaction)initialContext.lookup("java:comp/UserTransaction");transaction.begin();//read the activity instance process.getActivityInstance(aiid); //claim the activity instanceprocess.claim(aiid); transaction.commit(); The getActivityInstance method and other read operations set a read lock. In this example,a read lock on the activity instance is upgraded to an update lockon the activity instance. This can result in a database deadlock whenthese transactions are run in parallel.

The following example shows this step for a process application:

```
process.initiate("MyProcessModel",input);
```

- Automatically by WebSphere® Application
Server (the deployment
descriptor specifies TX\_REQUIRED).
- Explicitly by the application. You can bundle application calls
into one transaction:// Obtain user transaction interface
UserTransaction transaction= 
       (UserTransaction)initialContext.lookup("java:comp/UserTransaction");

// Begin a transaction
transaction.begin();

// Applications calls ...

// On successful return, commit the transaction
transaction.commit();

```
// Obtain user transaction interface
UserTransaction transaction= 
       (UserTransaction)initialContext.lookup("java:comp/UserTransaction");

transaction.begin();

//read the activity instance 
process.getActivityInstance(aiid);     
//claim the activity instance
process.claim(aiid);               
     
transaction.commit();
```

## Example

Here is an example of how steps
3 through 5 might look for a task application.

```
//Obtain the default initial JNDI context
InitialContext initialContext = new InitialContext();

//Lookup the remote home interface of the HumanTaskManager bean
Object result = 
         initialContext.lookup("java:comp/env/ejb/HumanTaskManagerHome");

//Convert the lookup result to the proper type
HumanTaskManagerHome taskHome = 
           (HumanTaskManagerHome)javax.rmi.PortableRemoteObject.narrow
           (result,HumanTaskManagerHome.class);

...
//Access the remote interface of the session bean.
HumanTaskManager task = taskHome.create();

...
//Call the business functions exposed by the service interface
task.callTask(tkiid,input);
```