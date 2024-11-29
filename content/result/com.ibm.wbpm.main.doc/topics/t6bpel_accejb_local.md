<!-- image -->

# Accessing the local interface of the session bean

## About this task

## Procedure

1 Add a reference to the local interface of the session beanto the application deployment descriptor. Add the referenceto one of the following files: The reference to the local home interface for process applicationsis shown in the following example:<ejb-local-ref> <ejb-ref-name>ejb/LocalBusinessFlowManagerHome</ejb-ref-name> <ejb-ref-type>Session</ejb-ref-type> <local-home>com.ibm.bpe.api.LocalBusinessFlowManagerHome</local-home> <local>com.ibm.bpe.api.LocalBusinessFlowManager</local></ejb-local-ref> The reference to the local homeinterface for task applications is shown in the following example:<ejb-local-ref> <ejb-ref-name>ejb/LocalHumanTaskManagerHome</ejb-ref-name> <ejb-ref-type>Session</ejb-ref-type> <local-home>com.ibm.task.api.LocalHumanTaskManagerHome</local-home> <local>com.ibm.task.api.LocalHumanTaskManager</local></ejb-local-ref> If you use IBM® IntegrationDesigner toadd the EJB reference to the deployment descriptor, the binding forthe EJB reference is automatically created when the application isdeployed. For more information on adding EJB references, refer tothe Integration Designer documentation.
    - The application-client.xml file, for a  Java™ Platform, Enterprise Edition
(Java EE) client application
    - The web.xml file, for a web application
    - The ejb-jar.xml file, for an Enterprise JavaBeans (EJB) application

```
<ejb-local-ref>
	<ejb-ref-name>ejb/LocalBusinessFlowManagerHome</ejb-ref-name>
	<ejb-ref-type>Session</ejb-ref-type>
	<local-home>com.ibm.bpe.api.LocalBusinessFlowManagerHome</local-home>
	<local>com.ibm.bpe.api.LocalBusinessFlowManager</local>
</ejb-local-ref>
```

```
<ejb-local-ref>
	<ejb-ref-name>ejb/LocalHumanTaskManagerHome</ejb-ref-name>
	<ejb-ref-type>Session</ejb-ref-type>
	<local-home>com.ibm.task.api.LocalHumanTaskManagerHome</local-home>
	<local>com.ibm.task.api.LocalHumanTaskManager</local>
</ejb-local-ref>
```

If you use IBM® Integration
Designer to
add the EJB reference to the deployment descriptor, the binding for
the EJB reference is automatically created when the application is
deployed. For more information on adding EJB references, refer to
the Integration Designer documentation.

2. Locate the local home interface of the session bean through
the Java Naming and Directory
Interface (JNDI).  The following example shows this
step for a process application:
// Obtain the default initial JNDI context
InitialContext initialContext = new InitialContext();

// Lookup the local home interface of the BusinessFlowManager bean
 
 LocalBusinessFlowManagerHome processHome = 
      (LocalBusinessFlowManagerHome)initialContext.lookup
      ("java:comp/env/ejb/LocalBusinessFlowManagerHome");
The local home interface of the session
bean contains a create method for EJB objects. The method returns
the local interface of the session bean.
3. Access the local interface of the session bean. The
following example shows this step for a process application:
LocalBusinessFlowManager process = processHome.create();Access
to the session bean does not guarantee that the caller can perform
all of the actions provided by the bean; the caller must also be authorized
for these actions. When an instance of the session bean is created,
a context is associated with the instance of the session bean. The
context contains the caller's principal ID, group membership list,
and indicates whether the caller has one of the Business Process Choreographer Java EE roles. The context is used
to check the caller's authorization for each call, even when administrative
security is not set. If administrative security is not set, the caller's
principal ID has the value UNAUTHENTICATED.
4 Call the business functions exposed by the service interface. The following example shows this step for a process application: process.initiate("MyProcessModel",input); Callsfrom applications are run as transactions. A transaction is establishedand ended in one of the following ways: Tip: To prevent database deadlocks, avoid runningstatements similar to the following in parallel:// Obtain user transaction interfaceUserTransaction transaction= (UserTransaction)initialContext.lookup("java:comp/UserTransaction");transaction.begin();//read the activity instance process.getActivityInstance(aiid); //claim the activity instanceprocess.claim(aiid); transaction.commit(); The getActivityInstance methodand other read operations set a read lock. In this example, a readlock on the activity instance is upgraded to an update lock on theactivity instance. This can result in a database deadlock when thesetransactions are run in parallel

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
2 through 4 might look for a task application.

```
//Obtain the default initial JNDI context
InitialContext initialContext = new InitialContext();

//Lookup the local home interface of the HumanTaskManager bean
LocalHumanTaskManagerHome taskHome = 
        (LocalHumanTaskManagerHome)initialContext.lookup
        ("java:comp/env/ejb/LocalHumanTaskManagerHome");

...
//Access the local interface of the session bean
LocalHumanTaskManager task = taskHome.create();

...
//Call the business functions exposed by the service interface
task.callTask(tkiid,input);
```