<!-- image -->

# People directories for use with Business Process Choreographer

- The name that identifies a user profile and the login ID of a
user
- To exploit information that is related to the manager of a user,
the people directory should offer a corresponding attribute, by default
the manager attribute
- To exploit the email notification feature for escalations, the
people directory should offer user email addresses

- Federated repositories (also referred to as virtual member manager)This
is the default people directory that is supported by WebSphere® Application
Server. It provides
access to a variety of directory types, including Lightweight Directory
Access Protocol (LDAP) directories, database and file-based repositories,
and custom repositories. It also supports the federation of the repositories. 
Both
person and group information can be retrieved. The supported person
schema (PersonAccount entity type) includes properties for the name,
login identity, manager identity, and email address of a user. To
be available for people resolution, federated repositories must be
configured as the active security realm definition in WebSphere Application
Server.
- An LDAP directoryBusiness Process Choreographer can directly
access an LDAP directory for people resolution without using WebSphere Application
Server security.
To ensure consistency across people resolution (implemented by Business
Process Choreographer) and user authentication (implemented by WebSphere Application
Server security), WebSphere Application
Server security
must be configured to access the same LDAP directory server as the
one specified for people resolution in Business Process Choreographer. 
Depending
on the LDAP person schema that you use, the person-related information
includes the user name, identity, manager name, and email address.
To be available for people resolution, a Business Process Choreographer
people directory provider configuration is required.
- WebSphere Application
Server user
registryThe user registry is a subsystem of the application server
for retrieving user information. Business Process Choreographer can
use this user registry as a people directory. Business Process Choreographer
uses its own user registry people directory provider to access the WebSphere Application
Server user registry.