# Granting table privileges to the JCA authentication alias user
ID

## About this task

Use
a schema name that is different from the JCA authentication alias
to prevent the alias user ID from having the authority to drop tables.
(The authority to drop tables is implicitly granted to the creator,
that is, the schema.) Note that it does not make sense to grant a
privilege like DBADM to the JCA authentication alias user ID because
DBADM also has the ability to drop tables.

```
GRANT ALL PRIVILEGES ON TABLE
cell.tablename TO userid/sqlid
```

where userid/sqlid is
the JCA authentication alias user ID.