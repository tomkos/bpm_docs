# Declaring the federated data repository in server.xml

## About this task

Process Federation Server
uses a remote Elasticsearch or OpenSearch cluster to provide the federated data repository, a
distributed index that contains data extracted in real time from the federated systems databases.
The distributed index ensures that users have fast access to federated data, and relieves business
process management systems from expensive queries. Process Federation Server creates an
Elasticsearch or OpenSearch index for each server in the federated environment, and offers a common
REST-based query service that provides data to Process Federation Server clients, such
as federated Process Portal
and Workplace.

## Procedure

1. Open the Process Federation Server
server.xml configuration file for editing.

By default, you can find it on Process Federation Server in the
pfs\_install\_root/usr/servers/server\_name directory.
2 Add an ibmPfs\_remoteElasticsearch configuration element. Set the enabled attribute to true , and specify theendpoints as in the following examples. For information about the properties that you can set, see Configuration properties for the federated datarepository . Note: Elasticsearch and OpenSearch automatic index creation is controlled by theaction.auto\_create\_index setting. By default, this setting is set totrue , which allows any index to be created automatically. The remote Elasticsearchor OpenSearch cluster used by Process Federation Server must beconfigured to prevent automatic index creation. The documentation of this setting can be foundhere:
    - where authentication to the Elasticsearch or OpenSearch service is not
required:<ibmPfs\_remoteElasticsearch
        enabled="true"
        endpoints="http[s]://my.elasticsearchOrOpensearch.host:port/optional/path[,http[s]://myother.elasticsearchOrOpensearch.host:otherport/optional/path]"/>
    - where authentication to the Elasticsearch or OpenSearch service is
required:<ibmPfs\_remoteElasticsearch
        enabled="true"
        endpoints="http[s]://my.elasticsearchOrOpensearch.host:port/optional/path[,http[s]://myother.elasticsearchOrOpensearch.host:otherport/optional/path]"
        username="user"
        password="password"/>
    - For Elasticsearch:
https://www.elastic.co/guide/en/elasticsearch/reference/8.4/docs-index\_.html#index-creation
    - For Opensearch:
https://opensearch.org/docs/2.5/api-reference/cluster-api/cluster-settings/

## What to do next

- Configuration properties for the federated data repository

The ibmPfs\_remoteElasticsearch element within the server.xml file contains the configuration properties for the federated data repository.