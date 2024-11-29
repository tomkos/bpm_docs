<!-- image -->

# Planning for the people directory provider

## Procedure

1 If you are going to use human tasks, decide which peopledirectory providers you will use: Virtual member manager (VMM) people directory provider The VMM people directory provider is ready to use federated repositories (also known as virtualmember manager) as is preconfigured for WebSphere®security - using a file repository. If you want to use a different user repository with federatedrepositories, you will need to reconfigure federated repositories. The VMM people directory providersupports all Business Process Choreographer people assignment features including substitution. Itrelies on the features provided by federated repositories, such as support for different repositorytypes, such as LDAP, database, file based, and property extension repository. To use the VMMpeople directory provider requires that you have configured federated repositories for WebSphere ApplicationServer security. You can associate federated repositories withone or more user repositories, based on a file, LDAP, or a database.Formore information about this, see Managing the realm in a federated repository configuration . Lightweight Directory Access Protocol (LDAP) people directoryprovider This people directory provider must be configured before you canuse it. Perform the planning in step 2 . System people directory provider This people directory provider can be used without configuringit. Do not use this provider for a production system, it is only intendedfor application development testing. User registry people directory provider This people directory provider can be used without configuringit. Depending on the WebSphere security realm definition, the user registry can use one of thefollowing repositories:

To use the VMM
people directory provider requires that you have configured federated repositories for WebSphere Application
Server security. You can associate federated repositories with
one or more user repositories, based on a file, LDAP, or a database.
For
more information about this, see Managing the realm in a federated repository configuration.

    - Federated repository - which can use the following repositories:
        - File registry
        - One or more LDAPs
        - One or more databases
- Stand-alone LDAP (deprecated)
- Stand-alone custom (deprecated)
- Local operating system (deprecated)
2 If you are going to use the Lightweight DirectoryAccess Protocol (LDAP), plan the following items.

1. You might need to customize your own version of the LDAPTransformation.xsl file. For the location of that
file and a list of properties that you might need to customize, see Configuring the LDAP people directory provider.
2. Plan the following LDAP custom properties: 

LDAP plug-in property
Required or optional
Description

AuthenticationAlias
Optional
The authentication alias used to
connect to LDAP, for example, mycomputer/My LDAP Alias. You must define this alias in the administrative console by clicking Security > Secure administration, applications,
and infrastructure  > Java Authentication and
Authorization Service  > J2C Authentication Data. If this alias is not set or if AuthenticationType is not set to simple then an anonymous logon to
the LDAP server is used.

AuthenticationType
Optional
If this property is set to simple, for simple authentication, then the AuthenticationAlias parameter is required. Otherwise, if
it is not set, anonymous authentication is used.

BaseDN
Required
The base distinguished name (DN)
for all LDAP search operations, for example, o=mycompany,
c=us. To specify the directory root, specify an empty
string using two single quotation marks, ''.

CasesentivenessForObjectclasses
Optional
Determines whether the names of LDAP object
classes are case-sensitive. 

ContextFactory
Required
Sets the Java™ Naming and Directory Interface (JNDI) context
factory, for example, com.sun.jndi.ldap.LdapCtxFactory

ProviderURL
Required
This web address must point to
the LDAP JNDI directory server and port. The format must be in normal
JNDI syntax, for example, ldap://localhost:389. For
SSL connections, use the LDAP's URL. For a high availability configuration,
where you have two or more LDAP servers that maintain mirrored data,
plan to specify a URL for each LDAP server and use the space character
to separate them.

SearchScope
Required
The default search scope for all
search operations. Determines how deep to search beneath the baseDN
property. Specify one of the following values: objectScope, onelevelScope, or subtreeScope

additionalParameterName1-5 and additionalParameterValue1-5
Optional
Use these name-value pairs to set
up to five arbitrary JNDI properties for the connection to the LDAP
server.
3 If you are going to use the virtual membermanager, plan the following items.

1. You might need to customize your own version of the VMMTransformation.xsl file. For the location
of that file and a list of properties that you might need to customize,
refer to Configuring the Virtual Member Manager people directory provider.
4 If you want to use people substitution, consider the followingguidelines:

- You must use the VMM people directory provider. The LDAP, system,
and user registry people directory providers do not support people
substitution.
- If you are going to use people substitution in a production environment,
plan to use the VMM Property Extension Repository to store the substitution
information. The Property Extension Repository and, implicitly, the
selected database must be unique and accessible from within the whole
cell. As the BPEDB database is not necessarily unique within a cell,
BPEDB cannot be used. You can use the common database, WPSRCDB, to
host the Property Extension Repository, however, for a production
environment, it is recommended to use a database that is independent
of other Workflow Server databases.
- To use people substitution in a single-server test environment,
you can store people substitution information in the internal file
registry that is configured for federated repositories.
5. If you will use people assignment for human
tasks, and you will use a Lightweight Directory Access Protocol (LDAP)
people directory provider that uses simple authentication, plan a
Java Authentication and Authorization Service (JAAS) alias and an
associated user ID that will be used to connect to the LDAP server.
If the LDAP server uses anonymous authentication this alias and user
ID are not required. 
Table 1. Planning
the alias and user ID for the LDAP server

User ID or role
When the user ID is used
What the alias and user ID are used for
Which rights the user ID must have

LDAP plug-in property: AuthenticationAlias
Run time
The alias is used to retrieve the user ID
that is used to connect to the LDAP server. You specify this alias
ID when customizing the properties for the LDAP plug-in, for example mycomputer/My LDAP Alias.
The JAAS alias must be associated with the LDAP
user ID. 

LDAP user ID
Run time
This user ID is used to connect to the LDAP
server.
If the LDAP server uses simple authentication,
this user ID must be able to connect to the LDAP server. This user
ID is either a short name or a distinguished name (DN). If the LDAP
server requires a DN you cannot use the short name.

## Results