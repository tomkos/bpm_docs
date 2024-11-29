# The ums-teams-deployment pods do not start

```
workflow-...-ums-teams-deployment-...   0/1     Running     ...                              
workflow-...-ums-teams-deployment-...   0/1     Running     ...
```

This message means that the database is wrongly initialized. The UMS Teams Pods search the
database tables in the default schema of the database. If the database has no default schema, the
tables are not found. The UMS Teams Pods connect to the database with a database user as specified
in the custom resource. To know how to set a default schema for that database user, refer to the
documentation of your database provider.