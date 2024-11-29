# Using the curl command to access the indexers MBeans

- Querying all the MBean attributes for an indexer
- Querying a specific MBean attribute for an indexer
- Modifying a specific MBean attribute for an indexer
- Invoking an operation on an indexer MBean

## Querying all the MBean attributes for an indexer

- For BPD indexers:
curl –X GET -s -u user:password -k 'https://hostname:port/IBMJMXConnectorREST/mbeans/com.ibm.bpm.federation.server:name=indexerUniqueID,subtype=BpdIndexers,type=Indexers/attributes'
- For BPEL indexers:
curl –X GET -s -u user:password -k 'https://hostname:port/IBMJMXConnectorREST/mbeans/com.ibm.bpm.federation.server:name=indexerUniqueID,subtype=BpelIndexers,type=Indexers/attributes'

- user is the user name, and password is the password of a
Liberty user that has an administrative role.
- hostname is the Process Federation Server hostname.
- port is the HTTPS port.
- indexerUniqueID is the string based on the ID of the indexer and of the
federated system it refers to (for more information, see the MBean objectName
section in Monitoring and administering BPD indexers and Monitoring and administering BPEL indexers).

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

## Querying a specific MBean attribute for an indexer

- For BPD indexers:
curl –X GET -s -u user:password -k 'https://hostname:port/IBMJMXConnectorREST/mbeans/com.ibm.bpm.federation.server:name=indexerUniqueID,subtype=BpdIndexers,type=Indexers/attributes/attributeName'
- For BPEL indexers:
curl –X GET -s -u user:password -k 'https://hostname:port/IBMJMXConnectorREST/mbeans/com.ibm.bpm.federation.server:name=indexerUniqueID,subtype=BpelIndexers,type=Indexers/attributes/attributeName'

- user is the user name, and password is the password of a
Liberty user that has an administrative role.
- hostname is the Process Federation Server hostname.
- port is the HTTPS port.
- indexerUniqueID is the string based on the ID of the indexer and of the
federated system it refers to (for more information, see the MBean objectName
section in Monitoring and administering BPD indexers and Monitoring and administering BPEL indexers).
- attributeName is a valid attribute that is remotely accessible by the indexer
MBean.

```
{"value": attributeValue,"type": attributeType}
```

```
curl –X GET -s -u uid=admin,o=defaultWIMFileBasedRealm:admin -k 'https://pfsHost.com:9443/IBMJMXConnectorREST/mbeans/com.ibm.bpm.federation.server:name=bpd1.default-0,
subtype=BpdIndexers,type=Indexers/attributes/status'
{"value":"WAITING\_FOR\_NEXT\_CYCLE","type":"java.lang.String"}
```

- the MBean is not yet registered on Process Federation Server.
- the federated system ID refers to a federated system that does not exist or that is not
running.
- the attribute name does not exist

## Modifying a specific MBean attribute for an indexer

- For BPD indexers:
curl –X POST -s -u user:password –k
     -H 'Content-Type: application/json' 
     -d '[ { "name":attributeName, "value": { "value":newAttributeValue, "type":attributeType } } ]' 
'https://hostname:port/IBMJMXConnectorREST/mbeans/com.ibm.bpm.federation.server:name=indexerUniqueID,subtype=BpdIndexers,type=Indexers/attributes'
- For BPEL indexers:
curl –X POST -s -u user:password –k
     -H 'Content-Type: application/json' 
     -d '[ { "name":attributeName, "value": { "value":newAttributeValue, "type":attributeType } } ]' 
'https://hostname:port/IBMJMXConnectorREST/mbeans/com.ibm.bpm.federation.server:name=indexerUniqueID,subtype=BpelIndexers,type=Indexers/attributes'

- user is the user name, and password is the password of a
Liberty user that has an administrative role.
- attributeName is an attribute name that is remotely accessible by the indexer
MBean
- newAttributeValue is the new value to assign to the attribute.
- attributeType is the type of the attribute.
- hostname is the Process Federation Server hostname.
- port is the HTTPS port.
- indexerUniqueID is the string based on the ID of the indexer and of the
federated system it refers to (for more information, see the MBean objectName
section in Monitoring and administering BPD indexers and Monitoring and administering BPEL indexers).

```
[{"name":attributeName,"value":{"value":newAttributeValue,"type":attributeType}}]
```

```
curl -X POST -i  -u uid=admin,o=defaultWIMFileBasedRealm:admin -k 
-H 'Content-Type: application/json' 
-d '[ { "name":"scheduledSyncTasks", "value": { "value":"true", "type":"java.lang.Boolean" } } ]' 
'https://pfsHost.com:9443/IBMJMXConnectorREST/mbeans/com.ibm.bpm.federation.server:name=bpdl1,subtype=BpdIndexers,type=Indexers/attributes'
[{"name":"scheduledSyncTasks","value":{"value":"true","type":"java.lang.Boolean"}}]
```

- the MBean is not yet registered on Process Federation Server.
- the federated system ID refers to a federated system that does not exist or that is not
running.
- the attribute name does not exist

## Invoking an operation on an indexer MBean

- For BPD indexers:
curl –X POST -s -u user:password –k
     -H 'Content-Type: application/json' 
     -d '{"params": [ { "value": "",  "type":"java.lang.String" } ], "signature": []}' 
'https://hostname:port/IBMJMXConnectorREST/mbeans/com.ibm.bpm.federation.server:name=indexerUniqueID,subtype=BpdIndexers,type=Indexers/operations/operationName'
- For BPEL indexers:
curl –X POST -s -u user:password –k
     -H 'Content-Type: application/json' 
     -d '{"params": [ { "value": "",  "type":"java.lang.String" } ], "signature": []}' 
'https://hostname:port/IBMJMXConnectorREST/mbeans/com.ibm.bpm.federation.server:name=indexerUniqueID,subtype=BpelIndexers,type=Indexers/operations/operationName'

- user is the user name, and password is the password of a
Liberty user that has an administrative role.
- hostname is the Process Federation Server hostname.
- port is the HTTPS port.
- indexerUniqueID is the string based on the ID of the indexer and of the
federated system it refers to (for more information, see the MBean objectName
section in Monitoring and administering BPD indexers and Monitoring and administering BPEL indexers).
- operationName is the valid name of an operation.

```
{"value":returnedValue,"type":returnedValueType}
```

```
curl -X POST –s -u uid=admin,o=defaultWIMFileBasedRealm:admin -k 
-H 'Content-Type: application/json' -d '{"params": [ { "value": "",  "type":"java.lang.String" } ], "signature": 
[]}' 'https://pfsHost.com:9443/IBMJMXConnectorREST/mbeans/com.ibm.bpm.federation.server:name=bpdl1,subtype=BpdIndexers,type=Indexers/operations/runUnscheduledSyncTasks'
{"value":"status=acknowledged","type":"java.lang.String"}
```

```
{"value":null,"type":null}
```

- the MBean is not yet registered on Process Federation Server.
- the federated system ID refers to a federated system that does not exist or that is not
running.
- the operation name does not exist