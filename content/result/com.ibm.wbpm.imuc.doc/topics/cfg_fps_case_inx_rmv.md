# Rebuilding and stopping a case instances index

Follow those instructions to rebuild an index, or to stop the indexing of case
instances.

## Rebuilding a case index

```
https://<BAW\_hostname>:<BAW\_port>/<Business\_Automation\_Workflow\_External\_base\_URL>/CaseManager/CASEREST/v1/<TOS\_name>/index
```

- <BAW\_hostname> is the hostname where the Business Automation Workflow REST API is exposed.
- <BAW\_port> is the port on which the Business Automation Workflow REST API is exposed.
- <TOS\_name> is the symbolic name of the target object store.

```
curl -X POST -u admin https://mybaw.com:9443/CaseManager/CASEREST/v1/ABCD1234-EF56-AB12-34CD-ABCD1234EF5
```

## Stopping the indexing of case instances

```
ELASTICSEARCH\_ENDPOINT=https://my.elasticsearchOrOpensearch.host:port
```