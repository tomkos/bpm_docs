# Referencing your own federated data repository

Instead of using Elasticsearch or OpenSearch as part of the stand-alone IBM Business Automation
Workflow on containers deployment,
you can decide to reference your own federated data repository.

- pfs\_configuration.elasticsearch.endpoint: the URL to access your
Elasticsearch service
- pfs\_configuration.elasticsearch.admin\_secret\_name: a secret containing the username and password that Process Federation Server will use to
access Elasticsearch. The keys expected in this secret are respectively username and password

```
pfs\_configuration:
      elasticsearch:
         endpoint: https://es\_host:9201
         admin\_secret\_name: demo-elasticsearch-admin-secret
         connect\_timeout: 10s
         read\_timeout: 30s
         thread\_count: 0
         max\_connection\_total: -1
         max\_connection\_per\_route: -1
```

For more information, see Defining a federated data repository for Process Federation
Server containers.