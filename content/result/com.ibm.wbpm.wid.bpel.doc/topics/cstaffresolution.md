<!-- image -->

# People resolution

- People directories for use with Business Process Choreographer

People directories store user information that is used for resolving queries that assign people to human tasks.
- People directory providers and configurations

Business Process Choreographer uses people directory providers as adapters for accessing people directories. You can configure virtual member manager, LDAP, the user registry, and the system people directory providers to retrieve user information.
- Transformation of people assignment criteria to people queries

When an application is deployed, people assignment criteria definitions are transformed into sets of queries that are specific to a people directory configuration. The resulting people queries are stored with the task template in the Business Process Choreographer database.