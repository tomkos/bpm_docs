# Indexing case instances

## Before you begin

Complete configuring the connection to the federated data repository, as described in Configuring the federated data repository connection.

## About this task

After case federation is enabled, an administrator or operator needs to trigger the rebuild of
the federated data repository index for the historical case instances to be indexed. The first
indexing must be done before a case management system is registered to Process Federation Server. Subsequent
full reindexing is rarely needed, but you can initiate full reindexing if you find that the index is
not up to date. Case instances that have the following properties are indexed:

- Fixed well-known metadata properties
- Business properties (case properties) that are defined in the Search or Summary views of the
case solution, except business objects.

## Procedure

To index case instances, complete the following steps:

1. Create an environment variable in your system with
following settings: 
ELASTICSEARCH\_ENDPOINT=https://my.elasticsearchOrOpensearch.host:port
2. Start the Case configuration tool, select
Enable case indexing in the Configure Case integration with IBM
Business Automation Workflow
task, and run the task. For more information, see Configure the case integration
with Business Automation Workflow in
Running the configuration tasks.
3 Perform a POST request to the following URL: https://<BAW\_hostname> :<BAW\_port> /<Business\_Automation\_Workflow\_External\_base\_URL> /CaseManager/CASEREST/v1/<TOS\_name> /index where Forexample:curl -X POST -u admin https://mybaw.com:9443/CaseManager/CASEREST/v1/ABCD1234-EF56-AB12-34CD-ABCD1234EF56/index

```
https://<BAW\_hostname>:<BAW\_port>/<Business\_Automation\_Workflow\_External\_base\_URL>/CaseManager/CASEREST/v1/<TOS\_name>/index
```

    - <BAW\_hostname> is the hostname where the Business Automation Workflow REST API is exposed.
    - <BAW\_port> is the port on which the Business Automation Workflow REST API is exposed.
    - <TOS\_name> is the symbolic name of the target object
store.

```
curl -X POST -u admin https://mybaw.com:9443/CaseManager/CASEREST/v1/ABCD1234-EF56-AB12-34CD-ABCD1234EF56/index
```

4. To perform partial reindexing, use the syntax and URL described
earlier, but also specify the following parameter (where UTC\_time is the time
that is specified in UTC): 
{"skipCaseInstancesNotModifiedSince" : "UTC\_time"}

For example,
{"skipCaseInstancesNotModifiedSince" : "2020-09-05 12:00:00"}
Partial reindexing is automatically performed in certain situations: for example,
when you add a case property in case summary or case search views and then redeploy. In this
particular situation, all the case instances under the case type are reindexed to capture the values
of the new fields for the case instances. However, you might want to manually
perform partial reindexing by using the skipCaseInstancesNotModifiedSince
parameter in certain situations. For example, when index inconsistencies are suspected after a
disaster recovery.

## What to do next

- Rebuilding and stopping a case instances index

Follow those instructions to rebuild an index, or to stop the indexing of case instances.