<!-- image -->

# The relationship service

The relationship service makes it possible to capture relationships
across different objects. Participants in the relationship are distinguished
by the roles they serve. For example, a Person object Joe can
have an ownership relationship with a Car object Subaru with license
plate XYZ 123.In this example, Joe participates in the relationship
with the role ownerwhile the car participates in the relationship
under the role owned object.

## Relationship and role definitions

Relationships
and roles are described in definitions that you design through the
graphical interface of the relationship editor tool in IBM® Integration
Designer.
The relationship definition is a template that describes what the
relationship should look like, identifying the roles each participant
in the relationship can assume. The role definition captures the structure
and constraint requirements for the participants. Relationship definitions
are stored as XML files that are deployed as part of a Java EE application
to a particular server.

## How relationships work

- IBM Integration
Designer component Java™ snippet invocations of the relationship
service APIs
- Relationship transformations in the IBM Integration
Designer business
object mapping service
- Using the relationship manager tool

The relationship and role instance data is saved in relationship
tables that are stored in the database in the default data source
that you specify when you configure the relationship service.

The
relationship service runs on each server at the cell level. The Relationship
Manager home page About section shows
the number of servers in the cell that are running relationship services;
the Relationships section shows each server name
that is running relationship services. Before working with relationship
instances, you need to select the server that has the instances of
the relationships and roles you want to manage.

Relationship
definitions that are contained in user-defined shared libraries will
be created in the server at startup time, even if those shared libraries
are not associated with any server or application. You can use the
relationship manager to manage these relationships.