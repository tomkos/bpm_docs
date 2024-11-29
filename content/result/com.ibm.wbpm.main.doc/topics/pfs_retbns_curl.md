# Using the curl command to access the retriever MBeans

- Querying all the MBean attributes for a retriever
- Querying a specific MBean attribute for a retriever

## Querying all the MBean attributes for a retriever

- For BPD
retrievers:curl –X GET -s -u user:password -k 'https://hostname:port/IBMJMXConnectorREST/mbeans/com.ibm.bpm.federation.server:name=retrieverUniqueID,subtype=BpdRetrievers,type=Retrievers/attributes’
- For BPEL
retrievers:curl –X GET -s -u user:password -k 'https://hostnameport/IBMJMXConnectorREST/mbeans/com.ibm.bpm.federation.server:name=retrieverUniqueID,subtype=BpelRetrievers,type=Retrievers/attributes’

- user is the user name, and password is the password of a
Liberty user that has an administrative role.
- hostname is the Process Federation Server hostname.
- port is the HTTPS port.
- retrieverUniqueID is the string based on the ID of the retriever and of the
federated system it refers to (for more information, see the MBean objectName section in MBeans for BPD retrievers and MBeans for BPEL retrievers.)

```
[
{"name": attributeName1,"value":{"value":attributeValue1,"type":attributeType1}},
{"name": attributeName2,"value":{"value":attributeValue2,"type": attributeType2}},
 …
]
```

- the MBean is not yet registered on Process Federation Server.
- the federated system ID refers to a federated system that does not exist, or that is not
running.

## Querying a specific MBean attribute for a retriever

- For BPD retrievers:
curl –X GET -s -u user:password -k 'https://hostname:port/IBMJMXConnectorREST/mbeans/com.ibm.bpm.federation.server:name=retrieverUniqueID,subtype=BpdRetrievers,type=Retrievers/attributes/attributeName'
- For BPEL retrievers:
curl –X GET -s -u user:password -k 'https://hostname:port/IBMJMXConnectorREST/mbeans/com.ibm.bpm.federation.server:name=retrieverUniqueID,subtype=BpelRetrievers,type=Retrievers/attributes/attributeName'

- user is the user name, and password is the password of a
Liberty user that has an administrative role.
- hostname is the Process Federation Server hostname.
- port is the HTTPS port.
- attributeName is a valid attribute that is remotely accessible by the
retriever MBean.

```
{"value": attributeValue,"type": attributeType}
```

```
curl –X GET -s -u uid=admin,o=defaultWIMFileBasedRealm:admin -k 'https://pfsHost.com:9443/IBMJMXConnectorREST/mbeans/com.ibm.bpm.federation.server:name=bpd1.default-0,
subtype=BpdRetrievers,type=Retrievers/attributes/connectionTimeout'
{"value":"10000","type":"java.lang.String"}’
```

- the MBean is not yet registered on Process Federation Server.
- the federated system ID refers to a federated system that does not exist or that is not
running.
- the attribute name does not exist