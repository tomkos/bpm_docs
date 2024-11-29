<!-- image -->

# People directory providers and configurations

The decision on which people directory provider to use depends
on the support that you need from people resolution. To exploit all
of the people assignment features offered by Business Process Choreographer,
use virtual member manager.

- Federated repository features, including the use of various repositories,
such as file and database repositories, LDAP directories, the property
extension repository, and the federation of repositories
- Email notification for escalations
- Substitution for absentees
- All of the predefined people assignment criteria

- Email notification for escalations
- All of the predefined people assignment criteria

- Minimum configuration of the people directory provider for Business Process Choreographer
because the repository is determined by the security realm for the application server
- A limited set of predefined people assignment criteria. The user registry people directory
provider can resolve users and groups, but not employee to manager relationships, user properties,
or email addresses.

All of the people directory configurations require that WebSphere Application
Server administrative
and application security are enabled.

Each of the people directory providers can be associated with one
or more people directory provider configurations. All of the configurations,
except the LDAP people directory provider, are ready to use. For the
virtual member manager people directory provider, the federated repositories
functionality must be configured in WebSphere Application
Server. For the
LDAP provider configuration, the required connection parameters must
be set. In addition, the transformation file for the LDAP provider
configuration must be customized.

Each of the configurations is uniquely identified by its Java™ Naming Directory (JNDI) name. The JNDI
names are the link between a task template definition and the people
directory configuration that is to be used for resolving the people
assignments to task roles. Use Integration Designer to specify the
configuration name for a task template. If you are defining tasks
at run time using the task creation API, you can specify the configuration
name directly in the API. Different task templates can reference different
people directory configurations.

After a task template is deployed, the people directory configuration
name is fixed for the lifetime of the deployed template. If you need
to change the people directory that is associated with the template,
use Integration Designer to change the JNDI name of the people directory
configuration that is defined for the task template definition, and
deploy the template again.