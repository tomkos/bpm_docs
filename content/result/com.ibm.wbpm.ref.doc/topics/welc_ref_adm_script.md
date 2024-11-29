# Commands (wsadmin scripting)

- If you are using a SOAP connection, a command can take longer to complete than the specified
SOAP timeout value. Although the command continues to run until it is finished, you might see the
exception java.net.SocketTimeoutException: Read timed out. To prevent this
exception, set a higher value for the com.ibm.SOAP.requestTimeout property in the
profile\_root/properties/soap.client.props file.
- Some wsadmin commands return multiple lines of information. If you are using Jython and the
command output is not formatted appropriately, add the print statement before the
command, as shown in the following example.
print AdminTask.BPMShowSnapshot('[-containerAcronym BILLDISP -containerSnapshotAcronym SS2.0.1 -containerTrackAcronym Main]')
- Use the following command to get detailed help on a particular
command:print AdminTask.help('command\_name')
- Many of the command reference pages contain examples. Because these are examples, they often
show the use of explicit values for things like user names, passwords, and server names. Be sure to
use the appropriate values for your environment when running these commands.
- If you are not connecting to the default profile, use the -profileName
profile\_name option.
- After running the command, save your changes to the master configuration using
AdminConfig.save().
- If the ClassNotFoundException: com.lombardisoftware.core.TeamWorksException
error occurs while the command is running, add the TeamWorksException class to
the wsadmin command class path. To do so, run the wsadmin
command with the classpath parameter, as follows: -wsadmin\_classpath
<BPM\_install\_dir>/bin/BPM/Lombardi/lib/svrcoreclnt.jar,
where <BPM\_install\_dir> is the directory where IBM® Business Automation Workflow is installed.

- addBPMSystem command

 Traditional: 
Use the addBPMSystem command to add an IBM Business Automation Workflow system with a Business Process Execution Language (BPEL) or business process definition (BPD) engine to the local IBM Business Automation Workflow federated API.
- addSCMConnectivityProvider command

 Traditional: 
Use the addSCMConnectivityProvider command to add a Service Connectivity Management (SCM) connectivity provider.
- BPMActivate command

 Traditional: 
This command activates a process application snapshot on the Workflow Center server or Workflow Server.
- BPMArchive command

 Traditional: 
This command archives a process application snapshot on the Workflow Center server.
- BPMArchiveProcessApplication command

 Traditional: 
This command archives a deactivated process application from the Workflow Center server.
- BPMArchiveToolkit command

 Traditional: 
This command archives a deactivated toolkit from the Workflow Center server.
- BPMCheckOrphanTokens command

 Traditional: 
Use the BPMCheckOrphanTokens command to detect the possibility of orphaned tokens before installing a new snapshot and identify whether to delete or move each token.
- BPMClearWSICache command

 Traditional: 
Use this command in Workflow Server to clear the web service integration cache of WSDL and XSD definitions when the WSDL of the web service provider changes during the lifecycle of the server or cluster. The server or cluster is the deployment target of the web service integration.
- BPMCreateOfflinePackage command

 Traditional: 
Use this command to create an installation package for a process application snapshot on the Workflow Center server. You cannot use the BPMCreateOfflinePackage command to set the migration plan.
- BPMCreateSnapshot command

 Traditional: 
Use this command to create snapshots for process applications or toolkits. You might want to run the command, for example, to automate the creation of an off-line backup of the current snapshots of your process applications and toolkits.
- BPMDeactivate command

 Traditional: 
This command deactivates an active snapshot.
- BPMDeleteDurableMessages command

 Traditional: 
The BPMDeleteDurableMessages command deletes old durable subscription messages from the LSW\_DUR\_MSG\_RECEIVED database table.
- BPMDeleteOnHoldEMTasks command

 Traditional: 
This command deletes Event Manager tasks that are on hold.
- BPMDeleteSnapshot command

 Traditional: 
Run  this command in connected mode against a Workflow Server instance to delete snapshots for process applications or toolkits. For example, you might want to run the command if an excessive number of snapshots is causing your system to slow down.
- BPMEPVHistoryCleanup command

 Traditional: 
To reduce the performance impact of having a large number of exposed process variables (EPVs), use this command to delete EPV values that are no longer required.
- BPMExport command

 Traditional: 
This command exports a process application or toolkit snapshot as a .twx file that you can import into a Workflow Center server.
- BPMExportInstallPackage command

 Traditional: 
This command creates a generic install package (.zip file) for a process application or case solution snapshot. The generic install package is not targeted at any specific workflow server.
- BPMExtractMigrationPolicy command

 Traditional: 
This command extracts the migration policy from Workflow Center.
- BPMExtractOfflinePackage command

 Traditional: 
This command extracts the process application snapshot installation package from Workflow Center. The package is a .zip file that contains a .twx file.
- BPMGetSnapshotAcronym command

 Traditional: 
This command retrieves the snapshot acronym of a snapshot.
- BPMGroupMembershipUpdateTask command

 Traditional: 
The BPMGroupMembershipUpdateTask command triggers synchronization of group membership by users between the WebSphere® Application Server user registry and the IBM Business Automation Workflow database. Use this command to update the LDAP group membership for the users that you specify on the command line.
- BPMGroupMembershipFullUpdateTask command

 Traditional: 
The BPMGroupMembershipFullUpdateTask command triggers synchronization of group membership by users between the WebSphere Application Server user registry and the IBM Business Automation Workflow database. Use the BPMGroupMembershipFullUpdateTask command to update the LDAP group membership of all users that are known to IBM Business Automation Workflow.
- BPMImport command

 Traditional: 
This command imports a workflow project into Workflow Center.
- BPMInstall command

 Traditional: 
This command installs a process application snapshot from a Workflow Center to a Workflow Server in a test or production environment.
- BPMInstallOfflinePackage command

 Traditional: 
This command uses a custom installation package to install a process application snapshot from Workflow Center to an offline workflow server.
- BPMInstallPackage command

 Traditional: 
This command installs a process application or case solution snapshot from Workflow Center to a workflow server, which involves importing and deploying a process application or case solution to the workflow server.
- BPMListOnHoldEMTasks command

 Traditional: 
The BPMListOnHoldEMTasks command lists Event Manager tasks that are on hold. You run the command by using the AdminTask object of the wsadmin scripting client.
- BPMListProcessApplications command

 Traditional: 
This command lists all process applications and toolkits on a Workflow Center server or Workflow Server.
- BPMListServers command

 Traditional: 
This command lists all the Workflow Server instances that are federated into Workflow Center.
- BPMMigrateInstances command

 Traditional: 
Use the BPMMigrateInstances command to run an instance migration.
- BPMProcessInstancesCleanup command (deprecated)

 Traditional: 
Use this command to delete business process definition (BPD) instance data and associated documents for a process application snapshot on IBM Workflow Server.
- BPMProcessInstancesPurge command

 Traditional: 
Use this command to delete business process definition (BPD) instance data and associated documents for a process application snapshot on Workflow Server.
- BPMProcessInstancesResumption command

 Traditional: 
Use this command to resume business process definition (BPD) instances that are in a suspended state on IBM Workflow Center and IBM Workflow Server.
- BPMRegenTheme command

 Traditional: 
 Running the BPMRegenTheme command updates the snapshots to use the updated CSS without requiring you to redeploy the snapshots.
- BPMRemoveProcessApplication command

 Traditional: 
This command removes an archived process application and all of its snapshots from the Workflow Center server.
- BPMRemoveToolkit command

 Traditional: 
This command removes a toolkit and all of its snapshots from the Workflow Center server.
- BPMReplayOnHoldEMTasks command

 Traditional: 
This command resumes Event Manager tasks that are on hold so that they can be scheduled by the Event Manager again.
- BPMRestore command

 Traditional: 
This command restores a process application snapshot that had previously been archived on the Workflow Center server.
- BPMSecurityUnlock command

 Traditional: 
Use the BPMSecurityUnlock command to unlock an application cluster member during server startup.
- BPMSetDefaultSnapshot command

 Traditional: 
Use the BPMSetDefaultSnapshot command to designate a default snapshot on Workflow Server.
- BPMSetECMServerProperties command

 Traditional: 
Use the BPMSetECMServerProperties command to set the connection information to an Enterprise Content Management (ECM) server for a specific snapshot.
- BPMSetEnvironmentVariable command

 Traditional: 
Use the BPMSetEnvironmentVariable command to set the value of an environment variable for a process app or toolkit.
- BPMSetILOGRulesServerProperties command

 Traditional: 
Use the BPMSetILOGRulesServerProperties command to set the connection information to an ILOG Rules server for a specific snapshot.
- BPMSetSAPServerProperties command

 Traditional: 
Use the BPMSetSAPServerProperties command to set the connection information to an SAP server for a specific snapshot.
- BPMSetWebServiceServerProperties command

 Traditional: 
Use the BPMSetWebServiceServerProperties command to set the connection information to a web service server for a specific snapshot.
- BPMShowInstallMessages command

 Traditional: 
This command returns detailed messages from the snapshot installation on Workflow Center or Workflow Server.
- BPMShowOrphanedToolkits command

 Traditional: 
This command returns a list of toolkit snapshots that are not referenced by other process applications or toolkits. You can use the list to delete the orphan snapshots on your server.
- BPMShowProcessApplication command

 Traditional: 
This command lists information about a process application on Workflow Center or Workflow Server.
- BPMShowServer command

 Traditional: 
This command lists information for a federated Workflow Server instance in Workflow Center.
- BPMShowSnapshot command

 Traditional: 
This command lists information about a process application or toolkit snapshot, or information about the tip if you are not working with a snapshot.
- BPMSnapshotCleanup command

 Traditional: 
Use the BPMSnapshotCleanup command to delete unnamed and archived snapshots of a process application or toolkit on a Workflow Center server.
- BPMStop command

 Traditional: 
This command stops the business-level application (BLA) associated with a snapshot that has already been deactivated on a workflow server. A BLA is a WebSphere Application Server configuration artifact that is created only for a snapshot that has advanced content generated in IBM Integration Designer.
- BPMSyncEnvironmentVariables command

 Traditional: 
Use the BPMSyncEnvironmentVariables command to copy environment variables between two snapshots.
- BPMSyncEPVValues command

 Traditional: 
Use the BPMSyncEPVValues command to copy exposed process values between two snapshots.
- BPMSyncExistingUsersTask command

 Traditional: 
Use the BPMSyncExistingUsersTask command to synchronize existing users between the WebSphere Application Server user registry and the IBM Business Automation Workflow database. This command updates information for existing users in the Business Automation Workflow database, but it does not import new users from the user registry into the database. You can also use this command to synchronize the user state for users in the Business Automation Workflow database with the user availability in the user registry. For example, if users were deleted from the user registry, the command marks these users as inactive in the Business Automation Workflow database.
- BPMSyncTeamBindings command

 Traditional: 
Use the BPMSyncTeamBindings command to copy teams between two snapshots.
- BPMTasksCleanup command

 Traditional: 
Use this command to delete completed tasks from running process instances on IBM Workflow Server and IBM Workflow Center.
- BPMUpdateDependency command

 Traditional: 
Use this command to update a process application or toolkit dependency on a toolkit. You might want to run the command, for example, to automate the update of dependencies on a toolkit.
- BPMUpdateFile command

 Traditional: 
Use the BPMUpdateFile command to update the contents of an existing file in your process application or toolkit. When the command runs, it creates a new version of the file at the tip of the branch.
- BPMUpdateInstallationInformation command

 Traditional: 
This command associates the generic installation package that is created by the BPMExportInstallPackage with a specific server so that you can install a snapshot onto that server.
- BPMUpdateSystemApp command

 Traditional: 
The BPMUpdateSystemApp command applies interim fixes to toolkits and process apps. This command must only be used if you are directed to use it by IBM Software Support or by the instructions in an interim fix file. Before running the command, read the instructions included with the interim fix.
- BPMUpdateTheme command

 Traditional: 
This command generates runtime CSS for a process application or toolkit snapshot using the theme definition of a source project.
- BPMUndeploy command

 Traditional: 
This command undeploys a process application snapshot from a server. It is available only if the snapshot contains advanced content generated in IBM Integration Designer and has a corresponding business-level application (BLA) deployed on the server.
- BPMUsersFullSyncTask command

 Traditional: 
Use the BPMUsersFullSyncTask command to import all the user information from the WebSphere Application Server user registry into the IBM Business Automation Workflow database. If the user registry contains new users, these users are created in the Business Automation Workflow database.
- BPMUsersSyncTask command

 Traditional: 
Use the BPMUsersSyncTask command to synchronize a set of specified users between the WebSphere Application Server user registry and the IBM Business Automation Workflow database. You can also use this command to create specific users in the IBM Business Automation Workflow database who are already available in the WebSphere Application Server user registry. If you specify a user who is not available in the user registry, the user is skipped.
- cleanupDocumentStoreEventSubscriptions command

 Traditional: 
The cleanupDocumentStoreEventSubscriptions command removes subscriptions to events where event subscriptions no longer exist.
- cleanupDocumentStoreProperties command

 Traditional: 
The cleanupDocumentStoreProperties command deletes all properties that are currently specified in the case and document classes for a specific application but are no longer used. (An unused property is one that is no longer referenced in any named snapshot or tip in any branch of a process application or toolkit.) After the properties are removed, the command also removes any unused property templates.
- clearBPMEndpointServiceCache command

 Traditional: 
Use the clearBPMEndpointServiceCache command to reset the endpoint service caches of all running servers, including the endpoint service configuration cache and the endpoint service URL cache. The command can help with problem determination because you can enable endpoint service tracing for a running server and still see where the configuration is read and how the URLs are constructed.
- configSCAAsyncRetryCount command

Use the configSCAAsyncRetryCount command to change asynchronous retry counts at run time.
- configureBPMTransportSecurity command

 Traditional: 
Use the configureBPMTransportSecurity command to list and toggle HTTPS protocol enforcement for a set of Business Automation Workflow URLs.
- correctDocumentStoreInstanceAuthorization command

 Traditional: 
Use the correctDocumentStoreInstanceAuthorization command to correct user and group authorizations for case, BPD, and team instances that reside on an external ECM server.
- createBPMCompatEndpoints command

 Traditional: 
Use the createBPMCompatEndpoints command to create the compatibility Business Automation Workflow endpoint objects that are required for compatibility with deprecated WebSphere Lombardi Edition scenarios. The compatibility endpoint objects include the LSW\_SERVLET, EXPOSED\_ITEMS, TASK\_REST\_API, and TASK\_TEMPLATE\_REST\_API objects, which can refer to virtual hosts.
- createObjectStoreForContent command

 Traditional: 
If you want to use case management, you must run the createObjectStoreForContent command to create the design object store, target object store, and other necessary items in the embedded Content Platform Engine. Run this command after you have created the deployment environment and started the server.
- createVersionedSCAModule command

This command creates a unique instance of an SCA module EAR file. The SCA module must have the sca.module.attributes file as part of its content. The sca.module.attributes file exists for all versioned SCA modules before IBM® Business Process Manager Advanced Version 8.0 and for all modules created with IBM® Integration Designer Version 8.0.
- createWSRRDefinition command

Use the createWSRRDefinition command to create a WSRR definition.
- createWXSDefinition command

Use the createWXSDefinition command to create a WebSphere eXtreme Scale (eXtreme Scale) definition.
- deleteBPMCompatEndpoints command

 Traditional: 
Use the deleteBPMCompatEndpoints command to delete unused compatibility Business Automation Workflow endpoint objects that were required for compatibility with deprecated WebSphere Lombardi Edition scenarios. The compatibility endpoint objects include the LSW\_SERVLET, EXPOSED\_ITEMS, TASK\_REST\_API, and TASK\_TEMPLATE\_REST\_API objects, which can refer to virtual hosts.
- deleteBPMEndpoint command

 Traditional: 
Use the deleteBPMEndpoint command to delete an Business Automation Workflow endpoint. In stand-alone environments, such as the unit test environment of Integration Designer, the value of the endpoint is set immediately when you run the command. In network deployment (ND) environments, the value of the endpoint is set when the next node synchronization occurs. For both stand-alone and ND environments, it is not necessary to restart the server or cluster after running the command.
- deleteBPMProperty command

 Traditional: 
Use the deleteBPMProperty command to delete an Business Automation Workflow custom property from the configuration repository.
- deleteBPMVirtualHost command

 Traditional: 
Use the deleteBPMVirtualHost command to delete an Business Automation Workflow virtual host.
- deleteSCADestinations.jacl script

Use the deleteSCADestinations.jacl script to remove Service Component Architecture (SCA) destinations associated with a particular module.
- deleteWSRRDefinition command

Use the deleteWSRRDefinition command to delete a WSRR definition that has been named or supplied as a target object.
- deleteWXSDefinition command

Use the deleteWXSDefinition command to delete a WebSphere eXtreme Scale(eXtreme Scale) definition that has been named.
- exportBusinessRuleArtifacts.jacl script

Use the exportBusinessRuleArtifacts.jacl script to export business 		rules and selector components to a compressed file using the command line.
- exportWASConfig.py script

 Traditional: 
Use the exportWASConfig.py script to export WebSphere Application Server configuration, in addition to the configuration exported by the BPMConfig –export or BPMConfig –migrate command.
- getBPMDefaultVirtualHost command

 Traditional: 
Use the getBPMDefaultVirtualHost command to get the Business Automation Workflow default virtual host.
- getBPMEndpoint command

 Traditional: 
Use the getBPMEndpoint command to display the attributes of an Business Automation Workflow endpoint.
- getBPMProperty command

 Traditional: 
Use the getBPMProperty command to get the value of an Business Automation Workflow custom property from the configuration repository.
- getBPMVirtualHost command

 Traditional: 
Use the getBPMVirtualHost command to display the attributes of an Business Automation Workflow virtual host.
- getDefaultWSRRDefinition command

Use the getDefaultWSRRDefinition command to return the current default WSRR definition. If no default is set (only if there are no WSRR definitions), it returns null.
- getDocumentStoreStatus command

 Traditional: 
Use the getDocumentStoreStatus command to return information about theBPM document store in IBM Business Automation Workflow. The command determines the availability of the BPM document store and returns detailed information about document migrations to the document store. It also returns information about whether the IBM\_BPM\_DocumentStore application is up-to-date in comparison to the authentication alias and the EAR file version.
- getDefaultWXSDefinition command

Use the getDefaultWXSDefinition command to return the current default WebSphere eXtreme Scale (eXtreme Scale) definition. If no default is set (that is, when there are no eXtreme Scale definitions), the command will return null.
- importBusinessRuleArtifacts.jacl script

Use the importBusinessRuleArtifacts.jacl script to import business rule artifacts from a compressed file using a command line.
- importSelectorArtifacts.jacl script

Use the importSelectorArtifacts.jacl script to import selector artifacts from a compressed file using a command line.
- importWASConfig.py script

 Traditional: 
Use the importWASConfig.py script to import WebSphere Application Server configuration that was exported from the source deployment environment, including data sources, authentication aliases, and Secure Sockets Layer (SSL) settings.
- installBusinessSpaceWidgets command

 Traditional: 
Use the installBusinessSpaceWidgets command to install, deploy and register widgets for use with the Business Space component.
- installHumanTaskManagementWidgets command

 Traditional: 
Use the installHumanTaskManagementWidgets command to install the human task management widgets application on an Business Automation Workflow server or cluster.
- isDefaultWSRRDefinition command

Use the isDefaultWSRRDefinition command to return true or false, depending on whether the specified WSRR definition is the current cell default.
- isDefaultWXSDefinition command

Use the isDefaultWXSDefinition command to return true or false, depending on whether the specified WebSphere eXtreme Scale (eXtreme Scale) definition is the current cell default.
- listBPMApiFederationDomains command

 Traditional: 
Use the listBPMApiFederationDomains command to list all federation domains for your environment.
- listSCAExports command

Use the listSCAExports command to list the exports of a Service Component Architecture (SCA) module.
- listSCAImports command

Use the listSCAImports command to list the imports of a Service Component Architecture (SCA) module.
- listSCAModules command

Use the listSCAModules command to list the SCA modules deployed to a cell.
- listSCMConnectivityProviders command

 Traditional: 
                                      Use the listSCMConnectivityProviders command to return a list of all the parameters for a Service Connectivity Management (SCM) connectivity providers that exist in the cell.
- listWSRRDefinitions command

Use the listWSRRDefinitions command to return a list of all the WSRR definitions that exist in the cell.
- listWXSDefinitions command

Use the listWXSDefinition command to return a list of all the WebSphere eXtreme Scale (eXtreme Scale) definitions that exist in the cell.
- maintainDocumentStoreAuthorization command

 Traditional: 
Use the maintainDocumentStoreAuthorization command to add or remove users and groups from the authorization role for managing and working with the BPM document store.
- maintainDocumentStoreTrace command

 Traditional: 
Use the maintainDocumentStoreTrace command to enable or disable tracing for an individual component or all components of the BPM document store.
- modifyBPMApiFederationDomain command

 Traditional: 
Use the modifyBPMApiFederationDomain command to add or remove targets from a federation domain using the addTarget and deleteTarget steps.
- modifySCAExportHttpBinding command

Use the modifySCAExportHttpBinding command to change the attributes of an HTTP export binding.
- modifySCAExportJMSBinding command

Use the modifySCAExportJMSBinding command to change the attributes of a JMS export binding. This command applies to JMS bindings, WebSphere MQ JMS bindings, and Generic JMS bindings.
- modifySCAExportMQBinding command

Use the modifySCAExportMQBinding command to change the attributes of a WebSphere MQ export binding.
- modifySCAImportEJBBinding command

Use the modifySCAImportEJBBinding command to modify the attributes of an Enterprise JavaBeans (EJB) import binding.
- modifySCAImportHttpBinding command

Use the modifySCAImportHttpBinding command to change the attributes of an HTTP import binding.
- modifySCAImportJMSBinding command

Use the modifySCAImportJMSBinding command to change the attributes of a JMS import binding. This applies to JMS bindings, WebSphere MQ JMS bindings, and Generic JMS bindings.
- modifySCAImportMQBinding command

Use the modifySCAImportMQBinding command to change the attributes of a WebSphere MQ import binding.
- modifySCAImportSCABinding command

Use the modifySCAImportSCABinding command to change attributes of Service Component Architecture (SCA) import bindings.
- modifySCAImportWSBinding command

Use the modifySCAImportWSBinding command to change the attributes of a web service import binding.
- modifySCAModuleProperty command

Use the modifySCAModuleProperty command to modify the property values for a specified Service Component Architecture (SCA) module.
- modifySCMConnectivityProvider command

 Traditional: 
                                      Use the modifySCMConnectivityProvider command to modify the details of a Service Connectivity Management (SCM) connectivity provider.
- modifyWSRRDefinition command

Use the modifyWSRRDefinition command to modify the details of a definition, given its name.
- modifyWXSDefinition command

Use the modifyWXSDefinition command to modify the details of a WebSphere eXtreme Scale (eXtreme Scale) definition, dependent on how the object that is being modified is identified.
- registerRESTServiceEndpoint command

 Traditional: 
Use the registerRESTServiceEndpoint command to register configured and enabled Representational State Transfer (REST) endpoints so that your team can use IBM Business Automation Workflow widgets.
- removeSCMConnectivityProvider command

 Traditional: 
                                      Use the removeSCMConnectivityProvider command to remove a Service Connectivity Management (SCM) connectivity provider.
- setBPMDefaultVirtualHost command

 Traditional: 
Use the setBPMDefaultVirtualHost command to set the Business Automation Workflow default virtual host.
- setBPMEndpoint command

 Traditional: 
Use the setBPMEndpoint command to create or update an Business Automation Workflow endpoint.
- setBPMExternalECM command

 Traditional: 
 Use the setBPMExternalECM command to configure IBM Business Automation Workflow to use an external Enterprise Content Management server.
- setBPMProperty command

 Traditional: 
Use the setBPMProperty command to set the value of an Business Automation Workflow custom property in the configuration repository.
- setBPMVirtualHost command

 Traditional: 
Use the setBPMVirtualHost command to create or update an Business Automation Workflow virtual host.
- setExternalNavigator command

 Traditional: 
Use the setExternalNavigator command to configure IBM Business Automation Workflow to use an external IBM Content Navigator.
- setWSRRDefinitionAsDefault command

Use the setWSRRDefinitionAsDefault command to set the named WSRR definition to be the default one.
- setWXSDefinitionAsDefault command

Use the setWXSDefinitionAsDefault command to set the named WebSphere eXtreme Scale (eXtreme Scale)  definition to be the default.
- showBPMExternalECM command

 Traditional: 
Use the showBPMExternalECM command to show the external Enterprise Content Management servers that are configured for IBM Business Automation Workflow.
- showSCAExport command

Use the showSCAExport command to display the attributes of a Service Component Architecture (SCA) module export.
- showSCAExportBinding command

Use the showSCAExportBinding command to display the attributes of Service Component Architecture (SCA) module export bindings.
- showSCAExportEJBBinding command

Use the showSCAExportEJBBinding command to show the attributes of an Enterprise JavaBeans (EJB) export binding.
- showSCAExportHttpBinding command

Use the showSCAExportHttpBinding command to show the attributes of an HTTP export binding.
- showSCAExportJMSBinding command

Use the showSCAExportJMSBinding command to show the attributes of a JMS export binding. This applies to JMS bindings, WebSphere MQ JMS bindings, and Generic JMS bindings.
- showSCAExportMQBinding command

Use the showSCAExportMQBinding command to show the attributes of a WebSphere MQ export binding.
- showSCAExportWSBinding command

Use the showSCAExportWSBinding command to show the attributes of a web service export binding.
- showSCAImport command

Use the showSCAImport command to display the attributes of a Service Component Architecture (SCA) module import.
- showSCAImportBinding command

Use the showSCAImportBinding command to display the attributes of Service Component Architecture (SCA) module import bindings.
- showSCAImportEJBBinding command

Use the showSCAImportEJBBinding command to show the attributes of an Enterprise JavaBeans (EJB) import binding.
- showSCAImportHttpBinding command

Use the showSCAImportHttpBinding command to show the attributes of an HTTP import binding.
- showSCAImportJMSBinding command

Use the showSCAImportJMSBinding command to show the attributes of a JMS import binding. This applies to JMS bindings, WebSphere MQ JMS bindings, and Generic JMS bindings.
- showSCAImportMQBinding command

Use the showSCAImportMQBinding command to show the attributes of a WebSphere MQ import binding.
- showSCAImportWSBinding command

Use the showSCAImportWSBinding command to show the attributes of a web service import binding.
- showSCAModule command

Use the showSCAModule command to display the attributes of a Service Component Architecture (SCA) module.
- showSCAModuleProperties command

Use the showSCAModuleProperties command to display the properties of a Service Component Architecture (SCA) module.
- showSCMConnectivityProvider command

 Traditional: 
                                      Use the showSCMConnectivityProvider command to return a list of all the parameters for a Service Connectivity Management (SCM) connectivity provider.
- showWSRRDefinition command

Use the showWSRRDefinition command to return a list of all the parameters for a WSRR definition, including the type of the connection and whether the definition is the default.
- showWXSDefinition command

Use the showWXSDefinition command to return a list of all the parameters for a WebSphere eXtreme Scale (eXtreme Scale) definition.
- startDocumentStoreMigration command

 Traditional: 
Use the startDocumentStoreMigration command to migrate Business Automation Workflow documents from the BPM database to the BPM document store in Business Automation Workflow or to an external ECM server.
- uninstallBusinessSpaceWidgets command

Use the uninstallBusinessSpaceWidgets command to remove widgets and widget definitions from the profile, including removing individual widget assets (application, catalog, endpoints, spaces, templates, help).
- updateBPMAliasesAndRunAsRolesPasswords command

 Traditional: 
When the password of the user defined in the file registry or external security provider is changed and the user ID is used by IBM Business Automation Workflow authentication aliases or RunAs roles of Business Automation Workflow applications, the password must be synchronized. The updateBPMAliasesAndRunAsRolesPasswords command enables this synchronization in one step.
- updateBPMConfig command

 Traditional: 
Use the updateBPMConfig command to create, update, delete, and append elements and attributes in the 100Custom.xml files.
- updateBPMExternalECM command

 Traditional: 
When you add or remove cluster members either on Business Automation Workflow or FileNet® Content Manager, use the updateBPMExternalECM command. This command reconciles the change from the old list of cluster members and servers to the new list of cluster members and servers. When you update the external Content Platform Engine, you must run the updateBPMExternalECM command to download the Content Platform Engine libraries on the Business Automation Workflow server. See the related topic  Updating the Content Platform Engine client connector files. You must run this command only if Business Automation Workflow is configured with an external ECM server.
- updateBusinessSpaceWidgets command

 Traditional: 
Use the updateBusinessSpaceWidgets command to update previously configured widgets and their endpoints, catalogs, templates, and help plugins.
- updateDocumentStoreApplication command

 Traditional: 
Use the updateDocumentStoreApplication command to check the status of the installed IBM\_BPM\_DocumentStore application in a deployment target. If the application is not current or the authentication alias used by the application does not match the one mapped in the EmbeddedECMTechnicalUser role, the application is updated.
- updateEndpointBindingsOnPortal command

 Traditional: 
Use the updateEndpointBindingsOnPortal command to create endpoint references on the WebSphere Portal application server so that your team can use the widgets on WebSphere Portal.
- updateRESTGatewayService command

 Traditional: 
Use the updateRESTGatewayService command to update a Representational State Transfer (REST) gateway service so that REST services are configured and enabled.
- validateSCAImportExportInformation command

This command validates import and export information associated with an SCA module. It takes an EAR file as input and validates that all expected exports exist on the bus.