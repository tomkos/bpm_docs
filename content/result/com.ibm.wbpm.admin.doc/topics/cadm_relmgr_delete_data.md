<!-- image -->

# Removing relationship instance data from the repository

When you install an application containing relationships, the server
creates the corresponding database schema objects including tables,
indexes, sequences, and stored procedures. At run time, the tables
are populated with the relationship instance data. If you uninstall
the application that contains relationships, the tables and instance
data are not removed from the database. The next time the application
is installed, any new static relationship data in the application
is not populated, and if the relationship definition is changed, the
relationship table is not recreated. This can result in errors.

If you reinstall the application with the same relationship, the
old schema is reused. However, if the relationship or role definition
is modified in such a way that makes it incompatible with the existing
schema, the relationship service throws an exception and terminates
the installation of the relationship. The logs show the following
exception and message:

```
RelationshipServiceException("table <tablename> already exists, but the table schema is different from current role definition")
```

The solution for this problem is to remove the existing relationship
schema artifacts manually (using the tools supplied by the database
platform of your repository), and then to reinstall the application.

- RelationshipDatabaseSchemaDrop script

Use the RelationshipDatabaseSchemaDrop.py script to remove all relationship database artifacts that are associated with a relationship, including all database artifacts and instance data that are associated with the roles defined for that relationship.
- Using database tools to remove relationship instance data from the repository

You can use database tools to manually delete all of the database artifacts that comprise a relationship, including tables, stored procedures, and sequences.