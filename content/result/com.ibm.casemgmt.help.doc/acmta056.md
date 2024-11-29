# Re-creating an IBM Business Automation
Workflow target object store in a
development environment

## Symptoms

The target object store might become corrupted or left
in an uncertain state during development activities.

## Resolving the problem

- IBM Administration Console for
Content Platform Engine
- General installation steps for Business Automation Workflow
- General installation and administration skills for the Content Platform Engine, Business Automation Workflow, and integrating
components that are configured on your system (such as Case History, Case Analyzer)

1. Back up your design object store database.
2. Use IBM
FileNet® Deployment Manager to export the
external solutions artifacts you want to keep. For more information, see Saving user-defined assets before you reset the test environment.
3 Note the properties of the target object store and the other components of the contentmanagement system that reference it. You need these property values to clean up resources andre-create components. For example, the following properties are important:
    - The names of servers, database instances, and database schemas.
    - The names of database connections and data sources.
    - Storage locations for tables, indexes, and large objects (LOBs) for the target object store and
workflow system data.
    - For the target object store, note the:
        - Symbolic name
        - user groups to which you grant administrative and basic access
        - Project area name
        - IBM Content
Navigator
desktop name
        - Case operations username and password
- Any add-ons that are added to the target object store. To determine the add-ons, log in to
IBM Administration Console for
Content Platform Engine, select the
target object store, click Actions, then click Install Add-on
Features. Note what add-ons are in the Installed add-on features list, then click
Cancel.
- For workflow systems, note the default locale, date/time mask, XSL/XSD base directory, workflow
system administration and configuration groups, process orchestration broker servlet URL, public
listener URLs, connection point name, and isolated region name.
- For Case Analyzer stores, note the event pruning schedule and publishing interval.

- For the target object store, note the:
    - Symbolic name
    - user groups to which you grant administrative and basic access
    - Project area name
    - IBM Content Navigator desktop name
    - Case operations username and password
4 Set the application server timeout values to at least 600 seconds.

1 Traditional on-premise: The following sample settings are for WebSphere® ApplicationServer Version 8.5.2:
    - Servers > Server
Types > WebSphere application servers > Configuration
tab > Container Settings > Container
Services > Transaction service > Total transaction lifetime
timeout
    - Servers > Server
Types > WebSphere application servers > Configuration
tab > Container Settings > Container
Services > Transaction service > Maximum transaction
lifetime timeout
    - Servers > Server
Types > WebSphere application servers > Configuration
tab > Container Settings > Container
Services > ORB service > Request
timeout
    - Servers > Server
Types > WebSphere application servers > Configuration
tab > Container Settings > Container
Services > ORB service > Locate request
timeoutNote: For WebSphere Application
Server Version 8.5.2, the maximum
value for the locate request timeout is 300.
    - Resources > JDBC > data sources >  [Content Engine or Case Manager data source name]  > Connection Pool properties > Connection timeout
    - Resources > JDBC > data sources >  [Content Engine or Case Manager XA data source name] > Connection Pool properties > Connection timeout
2. Containers: If you are running in IBM Cloud Pak for Business
Automation, tune this Liberty container setting:

- <server>
<transaction
clientInactivityTimeout=1800s 
propogatedOrBMTTranLifetimeTimeout=1800s 
totalTranLifetimeTimeout=1800s
/>
</server>
Related information: Tuning IBM
WebSphere Liberty for FileNet Content
Manager
components
5 Stop all but one Content Platform Engine node or replica

Stop all but one Content Platform Engine
node or replica

- Traditional on-premise - If the Content Platform Engine is running in an application
server cluster, stop all but one of the nodes.
- Containers - If multiple pods of Content Platform Engine are running, then reduce the
number of replicas to one.
6 In IBM Administration Console forContent Platform Engine , firstdelete all components that reference the target object store, including the connection points andworkflow systems, then delete the target object store. For information, see: Deleting an object store .Note the following information:

- The Deleting an object store topic does not provide a complete list of all the integrating
components that can reference an object store, such as Case Analyzer stores. If components exist
that reference the target object store, those components must be deleted before you can delete the
target object store.
- When you delete the case history store, you might get an error similar to the following error:
The case history store could not be deleted because of the following error: 
com.filenet.api.exception.EngineRuntimeException: FNCRE0066E: 
E\_UNEXPECTED\_EXCEPTION: An unexpected exception occurred. The unexpected 
exception is chained to this exception. Message was: null FNRAM9022
In this error
occurs, log in to IBM Administration Console for
Content Platform Engine, then select [ECM Domain Name] > Global
Configuration > Administration > Database
Connections > [target object store database
connection] . On the Properties tab, scroll to the
Event export Stores property. Verify that this value does not reference an event export store. The
property value must be either Event Export Stores, or <No items
found>.
7 In IBM Administration Console forContent Platform Engine , performthe following tasks:

- Navigate to the connection definition in the design object store that is associated with the
target object store: Object Stores >  [design object store name] > BrowseRoot Folder > IBM Case Manager > data sets > DevEnvReinitInfo > [connection definition name].
- Delete all the documents except DeployDataset. Do not change the DeployDataset document. Delete
the following documents (if they exist): CodeModules, DevEnvReinitManifest, DevEnvReinitStatus.
8. Log out of IBM Administration Console for
Content Platform Engine,
then stop IBM Administration Console for
Content Platform Engine and
any custom applications that might be accessing the target object store.
9 Stop Content Platform Engine

Stop Content Platform Engine

- Traditional on-premise - Stop the last Content Platform Engine node.
- Containers - For the Content Platform Engine pods, reduce the number of
replicas to zero.
10. For each of the deleted components that use a database, log in to the database administration
console and delete all the user tables in their schemas, leaving the system tables only. These
components include the workflow system and target object store. If any other deleted components have
database tables, delete those tables as well. For example, the Case Analyzer store is a component
that has database tables.Note: After you delete the target object store tables, you must also delete
the sequences that are associated with the target object store database schema. For more
information, see Deleting an object store.
11 Restart Content Platform Engine

Restart Content Platform Engine

- Traditional on-premise - Start the Content Platform Engine. In a clustered environment,
start all the nodes.
- Containers - For the Content Platform Engine pods, change the number of
replicas of your choice to one or greater.
12 To add an object, log in to IBM Administration Console forContent Platform Engine , select the ObjectStores node, and click New store.

- Use the same symbolic name as the original target object store.
- Reuse the database connection a targetd schema of the original target object store.
- The user group that you grant administrative access to must have Full Control access. The new
target object accesses the connection definition that is associated with the project area. The user
group that you grant basic access to must have View properties access to the connection definition.
- In the Select Add-ons window, click Default Application
Configuration. Do not select any more add-ons.
13 In IBM Administration Console forContent Platform Engine ,navigate to the connection definition Security tab:

1. Object Stores > [target object store name] > Browse > Root Folder > IBM Case Manager > data sets > DevEnvReinitInfo > [connection definition name] > Security
2. Verify that the target object store administrative and general (basic access) user groups have
security access (as described in the previous step). The user group that you grant administrative
access to must have Full Control. This object accesses only the connection definition that is
associated with the project area. The user group that you grant basic access to must have View
properties access to the connection definition.
14. In IBM Administration Console for
Content Platform Engine,
navigate to Object Stores > [target object store
name] > Administrative > Workflow
System. Click New to add a workflow
system.Note: You can reuse the same properties in the original workflow system, such as the database
storage locations (tables, index, LOB), connection point name, and region name.
15 Reconfigure the target object store by using one of the following methods:

- Case configuration tool - Traditional on-premise
    - For Development environment, see Preparing to run the case configuration tasks.
    - For Production environment, see Preparing to run the configuration tasks.
    - Run the following tasks:
        1. Configure the Case Management Object Stores. This step adds the target object store and
analytics add-ons.
        2. Register Project Area.
        3. Configure Business Rules.
- Case administration client

1. Convert to Target Object store.
2. Register Project Area.

- Container environments:
    1. Re-run {{case-init }}jobNote: This only applies to the default project area.
For additional project areas, use Case administration client.
16. In IBM Administration Console for
Content Platform Engine, add any
add-ons from the original target object store that still need to be added.
17. Deploy your workflow projects or case solutions.
18. Use FileNet Deployment
Manager to import
external solution artifacts that you want to keep.
19. Re-create any other integrating components that were deleted.