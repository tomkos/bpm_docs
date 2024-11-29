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

## Class HTMConnection

- java.lang.Object
    - com.ibm.bpe.formrenderer.util.HTMConnection

- public class HTMConnection extends java.lang.Object Provides access to the HumanTaskManagerService API. The Human Task Manager API is rendered through an EJB. Use HTMConnection to initialize and configure references to the EJB. Use the following parameters to configure the connection: For example, the HTMConnection can be used as context for a Command .

```
public class HTMConnection
extends java.lang.Object
```

Provides access to the HumanTaskManagerService API.
 The Human Task Manager API is rendered through an EJB. Use HTMConnection
 to initialize and configure references to the EJB.

Use the following parameters to configure the connection:
 
 jndiName (mandatory): JNDI name for the EJB module.
 remote (optional): Defines whether the connection is made through a remote or local EJB interface.
       'TRUE' and 'FALSE' are valid values. Default is 'FALSE'.
 providerURL (optional): This parameter is used if the JNDI lookup for the EJB is not to be made
       against the local nameserver
 observer (optional): Defines whether the observer EJB is configured within BPCExplorer.
       'TRUE' and 'FALSE' are valid values. Default is 'FALSE'.

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
(C) Copyright IBM Corporation 2005, 2009.
    - Constructor Summary

Constructors 

Constructor and Description

HTMConnection()
Creates a new connection to the HumanTaskManagerService.
    - Method Summary Methods Modifier and Type Method and Description void close () Closes the connection to the process engine. protected void finalize () Ensures that the close() method is called before the object is disposed of by the garbage collector. HumanTaskManagerService getHumanTaskManagerService () Retrieves the HumanTaskManagerService bean. java.lang.String getJndiName () Gets the JNDI name for the Human Task Manager API EJB. java.lang.Boolean getObserver () Gets whether the observer EJB is configured within BPCExplorer. java.lang.String getProviderURL () Gets the URL to the service provider for the Human Task Manager API EJBs. java.lang.String getRemote () Gets whether the connection is to be made through a remote or local EJB interface. void setJndiName (java.lang.String newName) Sets the JNDI name for the Human Task Manager API EJB. void setObserver (java.lang.Boolean booleanValue) Sets whether the observer EJB is configured within BPCExplorer. void setProviderURL (java.lang.String url) Sets the URL to the service provider of the Human Task Manager API EJBs. void setRemote (java.lang.String booleanString) Sets whether the connection is to be made through a remote or local EJB interface.

### Method Summary

| Modifier and Type       | Method and Description                                                                                                       |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------|
| void                    | close() Closes the connection to the process engine.                                                                         |
| protected void          | finalize() Ensures that the close() method is called before  the object is disposed of by the garbage collector.             |
| HumanTaskManagerService | getHumanTaskManagerService() Retrieves the HumanTaskManagerService bean.                                                     |
| java.lang.String        | getJndiName() Gets the JNDI name for the Human Task Manager API EJB.                                                         |
| java.lang.Boolean       | getObserver() Gets whether the observer EJB is configured within BPCExplorer.                                                |
| java.lang.String        | getProviderURL() Gets the URL to the service provider for the Human Task Manager API EJBs.                                   |
| java.lang.String        | getRemote() Gets whether the connection is to be made through a remote or local EJB interface.                               |
| void                    | setJndiName(java.lang.String newName) Sets the JNDI name for the Human Task Manager API EJB.                                 |
| void                    | setObserver(java.lang.Boolean booleanValue) Sets whether the observer EJB is configured within BPCExplorer.                  |
| void                    | setProviderURL(java.lang.String url) Sets the URL to the service provider of the Human Task Manager API EJBs.                |
| void                    | setRemote(java.lang.String booleanString) Sets whether the connection is to be made through a remote or local EJB interface. |

- Methods inherited from class java.lang.Object
clone, equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait