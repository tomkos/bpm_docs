# Configuring the federated data repository connection

## Before you begin

- OpenSearch 2.5.0 to 2.x
- Containers:  Elasticsearch 8.x - all versions. Note that versions prior to 8.x
are not supported.

- The federated data repository cluster must consist of at least three nodes so that it provides
high availability.
- The federated data repository API must be exposed on HTTPS, and basic authentication must be
enabled.

## About this task

To enable either BPD or case indexing, you must configure Business Automation Workflow to connect to the
federated data repository.

## Procedure

1 Create a file named<deploymentEnvironment> \_BAW\_federatedrepoclient.properties in the[BAW\_HOME] /profiles/<profileName> /config/cells/<cellName> folder, where
    - <deploymentEnvironment> is the deployment environment
name from the WebSphere console under
Server > Deployment
Environments.
    - <profileName> is the node profile name from the
WebSphere console under System
administration > Nodes. If your nodes are configured
with a deployment manager, use the deployment manager node name,
    - <cellName> is the cell name from the WebSphere
console under System
administration > Cell.
2. In the properties file, provide the configuration required by Business Automation Workflow to connect to the
federated data repository REST API. For example: 
endpoints=https://opensearch-node1:9200,https://opensearch-node2:9200,https://opensearch-node3:9200
authAlias=opensearchAuthAlias

The properties that you can set to configure the connection to the federated data
repository REST API are as follows.
Table 1. Properties for the
configuration of the federated data repository REST API connection

Property
Description
Required or optional
Default value

endpoints
A comma-separated list of URLs to the federated data repository cluster REST API. In
production topologies, to provide high availability, you must use at least two different URLs that
point to different nodes of the same federated date repository cluster.
Required
None

authAlias
The WebSphere authentication alias where you defined the credentials that Business Automation Workflow uses to authenticate when
it sends requests to the federated data repository REST API.
Required in production topologies.
Optional in development environments that
might communicate with an unsecured federated data repository.
None

connectTimeout
The maximum amount of time, in milliseconds, that Business Automation Workflow awaits to connect to the
federated data repository REST API.
Optional
10000

readTimeout
The maximum amount of time, in milliseconds, that Business Automation Workflow awaits for the federated
data repository REST API to respond.
Optional
30000

indexPrefix

Set the indexPrefix property only when you federate the Business Automation Workflow system from Process Federation Server that runs as
part of Cloud Pak for Business Automation or as
part of a stand-alone Business Automation Workflow deployment on containers.
In such case, set indexPrefix to "icp4ba-pfs".

Optional
None