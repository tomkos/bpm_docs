# The Process Federation Server server.xml configuration file

## Configurable elements in the server.xml file

- authorization-roles
- basicRegistry
- datasource
- feature
- featureManager
- federatedRepository
- fileset
- httpEndpoint
- ibmPfs\_bpdIndexer
- ibmPfs\_bpdRetriever
- ibmPfs\_bpelIndexer
- ibmPfs\_bpelRetriever
- ibmPfs\_caseRetriever
- ibmPfs\_remoteElasticsearch
- ibmPfs\_federatedPersistence
- ibmPfs\_federatedSystem
- ibmPfs\_launchableEntity
- ibmPfs\_restConfig
- interceptors
- keyStore
- ldapRegistry
- library
- logging
- ltpa
- participatingBaseEntry
- pluginConfiguration
- primaryRealm
- security-role
- ssl
- sslDefault
- trustAssociation
- uniqueGroupIdMapping
- webAppSecurity

## Elements specific to Process Federation Server

For more information about this element and its attributes, see Configuration properties for the Process Federation Server index.

For specific configurations and usage, also see Enabling indexing of BPD-related data in a federated environment and Adding a Business Automation Workflow system to the federated environment.

Back to top

For more information about this element and its attributes, see Configuration properties for the Process Federation Server index.

For specific configurations and usage, also see Third-party authentication in federated process environments,
Enabling indexing of BPD-related data in a federated environment, Adding a Business Automation Workflow system to the federated environment, and Maintaining the Process Federation Server index.

Back to top

For more information about this element and its attributes, see Configuration properties for the Process Federation Server index.

For specific configurations and usage, also see Enabling indexing of BPEL-related data in a federated environment and Adding a Business Automation Workflow system to the federated environment.

Back to top

For more information about this element and its attributes, see Configuration properties for the Process Federation Server index.

For specific configurations and usage, also see Enabling indexing of BPEL-related data in a federated environment and Adding a Business Automation Workflow system to the federated environment.

Back to top

For more information about this element and its attributes, see Configuration properties for the Process Federation Server index.

For specific configurations and usage, also see Adding a Business Automation Workflow system to the federated environment.

Back to top

For more information about this element and its attributes, see Configuration properties for a remote Elasticsearch service.

Back to top

- Draft comment: amadelin those attributes are documented inhttp://bidoc.canlab.ibm.com:9080/support/knowledgecenter/SSFPJS\_8.5.7/com.ibm.wbpm.main.doc/topics/cfg\_fps\_database.html.Delete them from there and point to this ref topic instead? Or duplicateinfo? schemaName
    - Description: The name of the schema that contains the database tables. The name must be the same
as the name that was used when the Process Federation Server tables were created.
    - Default value: FEDERATED
    - Required: false
    - Data type: string
- dataSourceRef

- Description: The data source ID for the Process Federation Server database instance. This property
refers to the data source ID set in the <datasource id> attribute.
- Required: true
- Data type: string

For specific configurations and usage, also see Configuring the Process Federation Server database.

Back to top

For more information about this element and its attributes, see Configuration properties for the Process Federation Server index.

For specific configurations and usage, also see Enabling indexing of BPD-related data in a federated environment, Enabling indexing of BPEL-related data in a federated environment, Adding a Business Automation Workflow system to the federated environment, Federation considerations for dashboards, processes, and services in Process Portal, Configuring allowed origins for Process Portal .

Back to top

For more information about this element and its attributes, see Federation considerations for dashboards, processes, and services in Process Portal.

Back to top

For more information about this element and its attributes, see Configuration properties for the Process Federation Server index.

Back to top

## Generic  elements configurable for Process Federation Server

For specific configurations and usage, also see Configuring LDAP user registries for Process Federation Server, Configuring a custom user registry for Process Federation Server , Securing inbound communications to Process Federation Server .

Back to top

For specific configurations and usage, also see Configuring LDAP user registries for Process Federation Server, Configuring a custom user registry for Process Federation Server , Securing inbound communications to Process Federation Server .

Back to top

For specific configuration and usage, also see Securing inbound communications to Process Federation Server .

Back to top

For specific configurations and usage, also see Logging and tracing for Process Federation Server.

Back to top

For specific configurations and usage, also see Securing outbound communications between Process Federation Server and federated systems, Securing inbound communications to Process Federation Server , Securing communications between Process Federation Server and LDAP.

Back to top

For specific configurations and usage, also see Securing inbound communications to Process Federation Server , Securing communications between Process Federation Server and LDAP.

Back to top

For specific configurations and usage, also see Securing inbound communications to Process Federation Server .

Back to top

For specific configurations and usage, also see Configuring a basic user registry for Process Federation Server .

Back to top

For specific configurations and usage, also see Configuring LDAP user registries for Process Federation Server, Securing communications between Process Federation Server and LDAP.

Back to top

For specific configurations and usage, also see Configuring LDAP user registries for Process Federation Server.

Back to top

For specific configurations and usage, also see Configuring LDAP user registries for Process Federation Server.

Back to top

For specific configurations and usage, also see Configuring LDAP user registries for Process Federation Server.

Back to top

For specific configurations and usage, also see Configuring LDAP user registries for Process Federation Server.

Back to top

For specific configurations and usage, also see Configuring SSO for federated environments by using LTPA keys.

Back to top

For specific configurations and usage, also see Validating the Process Federation Server and federated environment configuration .

Back to top

For specific configurations and usage, also see Validating the Process Federation Server and federated environment configuration .

Back to top

For specific configurations and usage, also see Configuring the Process Federation Server database, Configuring single sign-on for federated environments by using a custom trust association interceptor (TAI), Enabling indexing of BPD-related data in a federated environment, Enabling indexing of BPEL-related data in a federated environment.

Back to top

For specific configurations and usage, also see Configuring the Process Federation Server database, Enabling indexing of BPD-related data in a federated environment, Enabling indexing of BPEL-related data in a federated environment.

Back to top

For specific configurations and usage, also see Configuring the Process Federation Server database, Enabling indexing of BPD-related data in a federated environment, Enabling indexing of BPEL-related data in a federated environment, Adding a Business Automation Workflow system to the federated environment, Configuring secure access to DB2 databases in federated environments, Configuring secure access to Oracle databases in federated environments,
Configuring secure access to SQL Server databases in federated environments.

Back to top

For specific configurations and usage, also see Configuring SSO for federated environments by using LTPA keys.

Back to top

For specific configurations and usage, also see Configuring single sign-on for federated environments by using a custom trust association interceptor (TAI).

Back to top

For specific configurations and usage, also see Configuring single sign-on for federated environments by using a custom trust association interceptor (TAI).

Back to top

For specific usage, also see Configuring IBM HTTP Server for federated environments.

Back to top