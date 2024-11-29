# Updating IBM Business Automation
Workflow data sources

## Before you begin

## Procedure

To update Business Automation Workflow data
sources:

- To update properties for a non-Oracle data source, complete the following steps:
    1. Run the following BPMConfig command to export the existing
configuration and generate a configuration properties
file: BPMConfig -export -profile profile\_name [-de deployment\_environment\_name]If
there is only one deployment environment in the WebSphere cell, you can omit the
-de option. More information about the BPMConfig command is
found in the topic BPMConfig command-line utility.
    2. Open the generated configuration properties file in a text editor or in the IBM Business Automation
Workflow Configuration
Editor. See "Configuring your environment with the IBM Business Automation
Workflow Configuration
editor."
    3. Edit one or more of the following properties in the configuration properties
file: 
bpm.de.db.#.hostname=myHost
bpm.de.db.#.portNumber=myPortNumber
bpm.de.db.#.databaseName=myDatabase
    4. Save the file and run the following BPMConfig command:

BPMConfig -update -dataSource modified\_properties\_file
- To update properties for an Oracle data source, complete the following steps:

1. Run the following BPMConfig command to export the existing
incorrect configuration and generate a configuration properties
file: BPMConfig -export -profile profile\_name [-de deployment\_environment\_name]If
there is only one deployment environment in the WebSphere cell, you can omit the
-de option. More information about the BPMConfig command is
found in the topic BPMConfig command-line utility.
2. Open the generated configuration properties file in a text editor or in the IBM Business Automation
Workflow Configuration
Editor. See "Configuring your environment with the IBM Business Automation
Workflow Configuration
editor."
3. Locate the following properties in the configuration properties file: 
bpm.de.db.#.hostname=myHost
bpm.de.db.#.portNumber=myPortNumber
bpm.de.db.#.databaseName=serviceName
Note: If the Oracle database is accessed through the Single Client Access Name (SCAN) feature, then
the hostname, portNumber, and databaseName
properties are exported. The url property (described in the following step) is only
exported if a non-SCAN URL is configured, in which case the hostname and
portNumber properties will not be set.
4. Replace those properties with the following properties:
bpm.de.db.#.hostname=
bpm.de.db.#.portNumber=
bpm.de.db.#.databaseName=systemID
bpm.de.db.#.url=myURL //For example: jdbc:oracle:thin:@myHost:myPortNumber:systemIDIn
these properties, the hostname and portNumber properties are set
to empty strings because the url property is used instead. The value specified for
the databaseName property needs to be consistent with the service name or SID that
is specified for the url property.Note: If you want to configure a SCAN URL, then
set the hostname, portNumber, and databaseName
properties but do not set the url property. If you want to configure a non-SCAN
URL, then set the databaseName and url properties, but do not set
the hostname and portNumber properties. (You will need to add the
url property when you switch from using a SCAN URL to a non-SCAN
URL.)
5. Run the following BPMConfig command:

BPMConfig -update -dataSource modified\_properties\_file

## What to do next

When you move the database to a new server, the data sources are generally updated using the
BPMConfig command. However, BPMConfig does not update the
transaction log data sources. The data sources for transaction logs must be updated in the admin
console or using wsadmin commands. The target database requires XA and same user
privilege. See Configuring XA transactions for your database type, for example: Configuring XA transactions for Oracle in a network environment on Windows.

## Related information

- BPMConfig command-line utility