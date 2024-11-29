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

## Class BFMConnection

- java.lang.Object
    - com.ibm.bpe.clientmodel.BFMConnection

- public class BFMConnection extends java.lang.Object The BFMConnection class provides access to the BusinessFlowManagerService API. The API is rendered through an EJB. Use BFMConnection to initialize and configure the reference to the EJB. Use the following parameters to configure the connection: For example, the BFMConnection can be used as context for a Command .

```
public class BFMConnection
extends java.lang.Object
```

The BFMConnection class provides access to the BusinessFlowManagerService API.
 The API is rendered through an EJB. Use BFMConnection to initialize and
 configure the reference to the EJB.

Use the following parameters to configure the connection:
 
jndiName (mandatory): JNDI name for the EJB module.
remote (optional): Defines whether the connection is to be made through a remote ('TRUE') or local ('FALSE') EJB interface.
  'TRUE' and 'FALSE' are valid values; the default value is 'FALSE'.
 providerURL (optional): This parameter is used if the JNDI lookup for the EJB is not to be performed
       against the local name server
 observer (optional): Deprecated - The reporting feature is no longer supported. 
         This value is ignored and always 'FALSE'.

 For example, the BFMConnection can be used as context for a Command.

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
(C) Copyright IBM Corporation 2005, 2012.
    - Constructor Summary

Constructors 

Constructor and Description

BFMConnection()
Creates a new connection to the BusinessFlowManagerService.
    - Method Summary Methods Modifier and Type Method and Description void close () Closes the connection to the process engine. protected void finalize () BusinessFlowManagerService getBusinessFlowManagerService () Retrieves the BusinessFlowManagerService bean. java.lang.String getJndiName () Gets the JNDI name for the API EJB. java.lang.Boolean getObserver () Deprecated. As of version 8.0.1, the reporting feature is no longer supported. This method always returns false. java.lang.String getProviderURL () Gets the URL to the service provider for the Business Process Choreographer API beans. java.lang.String getRemote () Whether the connection is through a remote or local EJB interface. java.lang.Object retrieve (OID id) Retrieves a ProcessTemplateData, ProcessInstanceData or ActivityInstanceData object by its identifier void setJndiName (java.lang.String newName) Set the JNDI name for the API EJB. void setObserver (java.lang.Boolean booleanValue) Deprecated. As of version 8.0.1, the reporting feature is no longer supported. This value is ignored. void setProviderURL (java.lang.String url) Sets the URL to the service provider of the Business Process Choreographer beans. void setRemote (java.lang.String booleanString) Sets whether the connection is to be made through a remote or local EJB interface.

### Method Summary

| Modifier and Type          | Method and Description                                                                                                                             |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| void                       | close() Closes the connection to the process engine.                                                                                               |
| protected void             | finalize()                                                                                                                                         |
| BusinessFlowManagerService | getBusinessFlowManagerService() Retrieves the BusinessFlowManagerService bean.                                                                     |
| java.lang.String           | getJndiName() Gets the JNDI name for the API EJB.                                                                                                  |
| java.lang.Boolean          | getObserver() Deprecated.  As of version 8.0.1, the reporting feature is no longer supported. This method always returns false.                    |
| java.lang.String           | getProviderURL() Gets the URL to the service provider for the Business Process Choreographer API beans.                                            |
| java.lang.String           | getRemote() Whether the connection is through a remote or local EJB interface.                                                                     |
| java.lang.Object           | retrieve(OID id) Retrieves a ProcessTemplateData, ProcessInstanceData  or ActivityInstanceData object by its identifier                            |
| void                       | setJndiName(java.lang.String newName) Set the JNDI name for the API EJB.                                                                           |
| void                       | setObserver(java.lang.Boolean booleanValue) Deprecated.  As of version 8.0.1, the reporting feature is no longer supported. This value is ignored. |
| void                       | setProviderURL(java.lang.String url) Sets the URL to the service provider of the Business Process Choreographer beans.                             |
| void                       | setRemote(java.lang.String booleanString) Sets whether the connection is to be made through a remote or local EJB interface.                       |

- Methods inherited from class java.lang.Object
clone, equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait