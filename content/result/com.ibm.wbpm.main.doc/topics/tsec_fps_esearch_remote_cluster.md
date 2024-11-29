# Securing communication between Process Federation Server and the
federated data repository

## Procedure

1. For SSL, import the Elasticsearch or OpenSearch server certificate to the Process Federation Server truststore by
using the standard IBM®
WebSphere® Application Server Liberty procedure.

For more information, see Adding trusted certificates in Liberty.
2. Use the endpoints property of the
ibmPfs\_remoteElasticsearch element in the server.xml
configuration file to specify the target URLs for the Elasticsearch or OpenSearch cluster
nodes.
3. Optional: 
If access to the Elasticsearch or OpenSearch cluster is secured through Basic authentication,
pass the credentials through the username and password
attributes of the ibmPfs\_remoteElasticsearch element.