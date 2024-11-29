# Elasticsearch or OpenSearch fails to start

When it is configured to use GP2 block storage, the Elasticsearch pod might fail to start
if it cannot obtain node locks. You might see the following error:

```
[2023-07-18T17:26:56,256][ERROR][o.e.b.Elasticsearch      ] [workflow-elasticsearch-statefulset-0] fatal exception while booting Elasticsearch java.lang.IllegalStateException: failed to obtain node locks, tried [/usr/share/elasticsearch/data]; maybe these locations are not writable or multiple nodes were started on the same data path?
```

## Resolution

```
elasticsearch\_configuration:
  fs\_group: 0
```