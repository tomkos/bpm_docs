# Completing configuration for Business Process Choreographer

If you have a Business Automation Workflow
deployment environment, you must perform some additional tasks before you start your
clusters.

Figure 1. Sample environment after the target is
started. The source environment is not running. The target can read
from the databases.

<!-- image -->

<!-- image -->

## Before you begin

You have successfully upgraded the Business
Process Choreographer database schema.

## About this task

Perform these tasks, if they apply to your environment, before you use IBM Business Automation Workflow in production.

## Procedure

1 Update the Human Task Manager email serviceconfiguration.
    1. Open the Human Task Manager configuration. Click Servers > Clusters > WebSphere
application server clusters > cluster\_name, where cluster\_name is the name
of the application cluster in your deployment environment. Under Business
Process Manager, expand Business Process Choreographer and
click Human Task Manager > Configuration.
    2. Note the E-mail session JNDI name.
    3. Verify the migrated Escalation URL prefix, Task URL
prefix, Administrator URL prefix, and Process Explorer
URL prefix settings. If necessary, update them according to your new environment.
    4. Click Resources > Mail > Mail Sessions.
    5. Locate the template mail session with the JNDI name
that was created for you (the one you found in step 1b).
    6. In the Outgoing Mail Properties section, update the Server, Protocol, User,
and Password settings according to your migration
source environment.
2. Apply any settings that were customized
for the  Business Process Choreographer Explorer. In the
administrative console, click Servers > Clusters > WebSphere application server
clusters >  cluster\_name . On the Configuration tab, in the Business Process
Manager section, expand Business Process Choreographer and
click Business Process Choreographer Explorer.
3. If you changed the mapping of Java EE roles for human tasks or BPEL
processes, ensure that you apply the same mappings. For more information about these
roles, see Security in human tasks and BPEL processes. For more information about changing the mappings, see
Assigning users and groups to roles and Assigning users to RunAs roles.
4 If you used people assignment before you migrated to IBM Business Automation Workflow , you must perform thefollowing actions:

1 Configure the same people directory provider that you used on themigration source.
    1. If you used the LDAP people
directory provider, perform the actions described in Configuring the LDAP people directory provider.Note: If you used
the BPMConfig command to migrate, the LDAP configuration was migrated from source
to target.
    2. If you used the Virtual Member Manager people directory provider, perform the actions described
in Configuring the Virtual Member Manager people directory provider.
2. If you applied any changes to the default XSL transformation files
(EverybodyTransformation.xsl, LDAPTransformation.xsl,
SystemTransformation.xsl, VMMTransformation.xsl, and
UserRegistryTransformation.xsl) that are in the
install\_root\ProcessChoreographer\Staff directory, then you
must reapply your changes to the IBM Business Automation Workflow versions of these
files after migration.  
In a network deployment environment, the transformation files must be available on the deployment
manager and on the managed nodes (if they are on different computers). Make sure that they all use
the same version of the transformation files.
To find the transformation files that you are using in the source environment, check the value of
the transformation file path that is specified in the people directory configuration. If the
transformation file path is
install\_root\ProcessChoreographer\Staff directory, you are
using the default files. Otherwise, you are using custom transformation files that you must manually
copy to the target environment and reconfigure in the people directory configuration.
Note: Custom XSL transformation files must be copied manually, depending on the exact value of the
transformation file path that is specified in the earlier version of the people directory
configuration (previously known as the staff plug-in configuration).
3 If you used the substitution feature and substitution informationis stored in one of the user repositories that are configured for VMM, you must add the newproperties for substitutionStartDate and substitutionEndDate toyour repository. The steps that you must perform depend on whetheryou store the substitution information in the VMM file registry or in the VMM property extensionregistry: For the VMM file registry: For the VMM property extension registry:

1. Add the substitutionStartDate and substitutionEndDate
properties to the definition of the PersonAccount entity type in the
wimxmlextension.xml file. In a network deployment environment, edit the file on the
deployment manager. The file is in
profile\_root\config\cells\cellName\wim\model.
Extend
the file to include the new
properties:<wim:propertySchema nsURI="http://www.ibm.com/websphere/wim" 
     dataType="STRING" multiValued="false" propertyName="substitutionStartDate">
    <wim:applicableEntityTypeNames>PersonAccount</wim:applicableEntityTypeNames>
</wim:propertySchema>

<wim:propertySchema nsURI="http://www.ibm.com/websphere/wim" 
     dataType="STRING" multiValued="false" propertyName="substitutionEndDate">
     <wim:applicableEntityTypeNames>PersonAccount</wim:applicableEntityTypeNames>
</wim:propertySchema>
2. The changes become effective after the deployment manager is restarted.

1. Check that the substitution properties isAbsent and substitutes are defined for the property extension repository. If they were
not defined before migration, no substitution information was stored in the VMM property extension
repository, and this migration step is not required. Change to the directory
install\_root\bin and enter the following commands in either
local mode or connected mode. In a network deployment environment, enter the commands on the
deployment
manager.
wsadmin -username admin -password adminPassWord
$AdminTask listIdMgrPropertyExtensions
2. Add the new properties substitutionStartDate and
substitutionEndDate to the property extension repository configuration by entering
the following commands:$AdminTask addIdMgrPropertyToEntityTypes 
   {-name substitutionStartDate 
    -dataType String 
    -isMultiValued false 
    -entityTypeNames PersonAccount 
    -repositoryIds LA}

$AdminTask addIdMgrPropertyToEntityTypes 
   {-name substitutionEndDate 
    -dataType String 
    -isMultiValued false 
    -entityTypeNames PersonAccount 
    -repositoryIds LA}
3. The changes become effective after the deployment manager is restarted.
4. Verify that the new properties were added to the property extension repository configuration by
entering the following command:$AdminTask
listIdMgrPropertyExtensions
5 Configure the REST API endpoints for the BusinessFlow Manager and Human Task Manager, update all references, and mapthe web modules to a web server.

1. Optional:
If you used Business Space to
access Business Process Choreographer, and you have not configured
it to use the federated REST APIs, you can do that configuration now.
To register the new endpoints with Business Space, using the
administrative console, click Servers > Clusters > WebSphere application server
clusters > cluster\_name, then in the Business Process Manager section,
click Business Space REST services endpoint registration and
verify that the entries for Process services and Task
services are correct.
2 If you migrated to a different computer, you must make surethat the REST API endpoint references for Business Process ChoreographerExplorer and Business Space point to the correct host name and portnumber of the server. In a clustered environment, if you use a proxyserver or HTTP server in front of several application servers, youcan achieve load balancing and high availability by directing theREST requests to that server.
    1 To change the context root for the REST API web modules, in theadministrative console:
        1. Click Applications > Application
Types > WebSphere enterprise applications > BPEContainer\_suffix > Context
Root for Web Modules, where suffix is
the cluster\_name where Business Process Choreographer
is configured.
        2. Make sure that the context root for the web module BFMRESTAPI is
correct and unique.
        3. Click Applications > Application
Types > WebSphere enterprise applications > TaskContainer\_suffix > Context Root for Web Modules
        4. Make sure that the context root for the web module HTMRESTAPI is
correct and unique.
2. To change the endpoint references for Business Process Choreographer
Explorer, click Servers > Clusters > WebSphere application server clusters > cluster\_name, then under Business Process Manager,
expand Business Process Choreographer, and
click Business Process Choreographer Explorer, then in the list of configured Business Process Choreographer
Explorer instances, click one instance to edit it and change the values
for Business Flow Manager REST API URL and Human
Task Manager REST API URL. Repeat this step as necessary
for the other instances.
3 To change the endpoint references for Business Space:
    1. To change the endpoint for the Business Flow
Manager, click Servers > Clusters > WebSphere application server clusters > cluster\_name, then under Business Process Manager,
expand Business Process Choreographer, and
click Business Flow Manager, and under Additional
Properties click REST Service Endpoint.
    2. To change the endpoint for the Human Task Manager,
click Servers > Clusters > WebSphere application server clusters > cluster\_name, then under Business Process Manager,
expand Business Process Choreographer, and
click Human Task Manager, and under Additional
Properties click REST Service Endpoint.
3 The JAX web services APIs were configured during migration. Youmight want to map the web modules to a web server and change the contextroot for the web modules of the JAX web services APIs. To changethe context root, in the administrative console:

1. Click Applications > Application
Types > WebSphere enterprise applications > BPEContainer\_suffix > Context
Root for Web Modules, where suffix is
the cluster\_name where Business Process Choreographer
is configured.
2. Make sure that the context root for the web module BFMJAXWSAPI is
correct and unique.
3. Click Applications > Application
Types > WebSphere enterprise applications > TaskContainer\_suffix > Context Root for Web Modules
4. Make sure that the context root for the web module HTMJAXWSAPI is
correct and unique.
6 Optional: Delete any old versionsof predefined human task applications. It is possible thatthe migration introduced new versions of the predefined human taskapplications, but because there might still be running instances ofthe old predefined human task applications, the old predefined humantask applications are not undeployed during migration. Therefore,it is possible that new and old versions of the predefined human taskapplications might exist in your system, and you should perform thefollowing actions:

1. To identify whether your system contains multiple versions
of the predefined human tasks, in the administrative console, click Applications > Application Types > WebSphere enterprise applications.
2 Locate all applications with names of the followingpatterns: Where nnn is the version number when the application was last updated, forexample 700 . If the newest version of these applicationslooks older than the current release, it just means that it did notchange since that version. The important thing is whether there aremultiple versions of these applications. cluster\_name is the name of the cluster.
    - HTM\_PredefinedTasks\_Vnnn\_cluster\_name.ear
    - HTM\_PredefinedTaskMsg\_Vnnn\_cluster\_name.ear
3. If there are multiple versions of the predefined human
tasks, make a note of the old versions. When there are
no old instances still running, you can delete all the old instances,
and then undeploy the old version of the applications. Undeploying
the old applications helps to reduce the server start time.
7. If you modified the faces-config-beans.xml configuration file
to specify thresholds for the queries for the Business Process Choreographer Explorer before you
migrated to IBM Business Automation Workflow, you must reapply the
changes. Only predefined views are affected by the settings in the
faces-config-beans.xml file. The thresholds for custom views are specified as part
of their definition.
8 If you use a generated JavaServer Faces (JSF)client for BPEL processes or human tasks, or if you created an applicationfor BPEL processes or human tasks using JSF components, and your serveris configured to use Apache MyFaces 2.0, you must replace the BusinessProcess Choreographer JAR files.

1. Import your application.
2 Replace the following files inthe WEB-INF/lib directory of your project: In Business Automation Workflow , all of these files are in thefollowingdirectory:install\_root \ProcessChoreographer\client
    - bfmclientmodel.jar
    - htmclientmodel.jar
    - bpcclientcore.jar
    - bpcjsfcomponents.jar
    - bpeapi.jar
    - taskapi.jar

```
install\_root\ProcessChoreographer\client
```

3 Optional: Remove the followingunnecessary files from the WEB-INF/lib directoryof your project if they are there:

- bpe137650.jar
- icu4j\_3\_4\_1.jar
- task137650.jar
4. Export your application.
9. Optional: You can improve the database
performance by activating shared work items. See the related
task link.
10. Optional: Retune your database
now or later.  For example, for DB2® databases, run REORG and RUNSTATS.
11. If you used the Business Process Choreographer Explorer reporting function, you
should be aware that it is not available anymore. The applications and resources for the reporting
function have not been created in the migration target environment. The reporting database was not
dropped though, and is still available when needed.
12. Perform Tuning.

## Related information

- Listing information about process and task templates
- Undeploying BPEL process and human task applications, using the administrative console
- Undeploying BPEL process and human task applications, using an administrative command
- Adding support for shared work items
- Removing redundant indexes