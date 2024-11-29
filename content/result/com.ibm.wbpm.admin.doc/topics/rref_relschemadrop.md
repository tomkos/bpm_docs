<!-- image -->

# RelationshipDatabaseSchemaDrop script

Use the RelationshipDatabaseSchemaDrop.py script
to remove all relationship database artifacts that are associated
with a relationship, including all database artifacts and instance
data that are associated with the roles defined for that relationship.

The RelationshipDatabaseSchemaDrop.py script
is located in the WPS\_HOME/util/RelService directory.

Make
sure that wsadmin is connected to the server (in
a stand-alone environment) or to the deployment manager (in a Network
Deployment environment).

## Required parameter

## Example

```
wsadmin -f ${WPS\_HOME}/util/RelService/RelServicRelationshipDatabaseSchemaDrop.py http://RelationshipSample/
CountryRelationship
```