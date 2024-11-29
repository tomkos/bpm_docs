<!-- image -->

# MBeans for Case retrievers

## MBean objectName

Every JMX MBean associated with a Case
retriever has an Object Name with a name. The syntax for the Object Name is
com.ibm.bpm.federation.server:type=Retrievers,subtype=CaseRetrievers,name=retrieverUniqueID.

retrieverUniqueID
is a string based on the ID of the Case retriever and of the federated system they refer to in the
Process Federation Server
server.xml file, and has the following format:
federatedSystemID.retrieverID.
federatedSystemID is the value of the id attribute of the ibmPfs\_federatedSystem element, and retrieverID is the value of the id attribute of the ibmPfs\_caseRetriever element.

If
no id attribute is specified for the Case retriever, then Liberty assigns a default
value with the format default-n, where n is a
positive integer that starts at 0. In that case, the retrieverUniqueID string
corresponds to the
federatedSystemID.default-n.

```
<ibmPfs\_federatedSystem  id="case" .../>
<ibmPfs\_caseRetriever federatedSystemRef="case1" .../>
```

## MBean attributes

| Attribute name            | Description                                                                                                                 | Nature    | Type             | Return value                                                                                                                                                                                |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------|-----------|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| connectionTimeout         | The maximum amount of time in milliseconds during which the retrieval service waits to connect to the federated system.     | Read only | Java.lang.String | An integer value                                                                                                                                                                            |
| readTimeout               | The maximum amount of time in milliseconds during which the retrieval service waits to read data from the federated system. | Read only | Java.lang.String | An integer value                                                                                                                                                                            |
| internalRestUrlPrefix     | The REST service URL that is used to communicate with the federated system.                                                 | Read only | Java.lang.String | An URL                                                                                                                                                                                      |
| federatedSystemInfo       | Information about the federated system.                                                                                     | Read only | Java.lang.String | {indexExists=boolean, allowedOrigins=[origins], launchListPriority=number, id=systemName}                                                                                                   |
| federatedSystemStatusInfo | Last known federated system status information.                                                                             | Read only | Java.util.List   | A list of items in the following format: {statusCode=status,statusTime=yyyy-MM-dd HH:MM:ss.SSS,user="username",version=federatedSystemVersion} [] if the retriever has not yet been called. |