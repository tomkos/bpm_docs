# Troubleshooting Business Automation Workflow administration

- Configuring integration with IBM Business Automation Workflow fails

User names longer than 35 characters cause the Configure case integration with IBM Business Automation Workflow task to fail.
- Unreadable characters for non-English locales in the Case configuration tool on AIX

 Traditional:  Unreadable characters might occur in the Case configuration tool when it is started with a locale other than English on AIX®.
- Case management configuration fails because the case management add-ons cannot be installed

 Traditional:  If you use a load balancer URL when you configure case management, the Case configuration tool might fail to install the case management add-ons.
- Registration of the IBM Business Automation Workflow plug-in fails

 Traditional:  After you configure the case management and then attempt to register the IBM® Business Automation Workflow plug-in, the registration fails.
- Case configuration tool does not create the baw and bawadmin desktops

 Traditional:  If you use a load balancer URL when you configure Business Automation Workflow for case management, the Case configuration tool might not create the baw and bawadmin desktops.
- Display issues with Case configuration tool

 Traditional:  You might encounter display issues with drop-down lists if you are using Case configuration tool on Red Hat Enterprise Linux® with OpenText Exceed (formerly, Hummingbird Exceed).
- SSLHandshakeException error in the Case configuration tool

 Traditional:  The Case configuration tool can connect to a server by using a Security Socket Layer (SSL) or Transport Layer Security (TLS) connection. However, the Case configuration tool returns an SSLHandshakeException error if the SSL signer or TLS signer is not added to the keystore.
- Case configuration tool returns a java.security.cert.CertificationException error

 Traditional:  The Case configuration tool can connect to a server by using a Security Socket Layer (SSL) or Transport Layer Security (TLS) connection. However, the configuration tool might return a java.security.cert.CertificationException error if the server certificate was not issued for the host name that is used for the connection.
- Solution export problems

Various problems can occur when you export a solution from IBM Business Automation Workflow.
- Solution import problems

Problems might occur when you import a solution into IBM Business Automation Workflow or when you deploy a solution.
- Removing invalid principal mappings after a solution is imported

After you import a solution, you receive a message that the imported solution includes principal mappings that cannot be displayed.
- Unable to access the role assignment page from the Deploy Solution task

 Traditional:  The Assign Roles button on the Deploy Solution task accesses the Case Client URL. If your browser type is not compatible, the Case configuration tool cannot start the embedded browser.
- Deleting a case

When you delete a case, you delete the case folder and the associated activity and process items, but some related artifacts and associated case, workflow, or process data remain in the system.
- Removing a case type

When you remove a case type, you must also remove the case type folder structure.
- Work items for a deployed solution whose name exceeds 58 characters do not display in a personal in-basket

When you enter the solution name in the Case configuration tool or in Case Builder, ensure that the name is 58 characters or fewer. Otherwise, the work items will not display in a personal in-basket after the solution is deployed.
- Solution deployment fails with a Content Platform Engine views error

Your solution deployment fails if the length of your solution name, role name, case type name, or field name exceeds the limit of the database view name that is set by the Content Platform Engine database. This issue is specific to Oracle databases.
- Deployment of rules fails during solution deployment in IBM Business Automation Workflow

 Traditional:  In a Business Automation Workflow environment that uses an external IBM FileNet® P8 Content Platform Engine, embedded rule deployment fails when you deploy your case management solution.
- Online deployment of a solution snapshot fails after adding or changing a security manifest

When you log in to Workflow Center and deploy online a case solution snapshot to the workflow server, the deployment is actually performed internally on the workflow server by a configured system user (e.g. ECMoC\_Service\_Account). If you deploy a solution snapshot and then log into the IBM Content Navigator bawadmin desktop on the workflow server and apply or modify a security manifest, the Content Platform Engine (CPE) folder permissions are changed. If you do not add the configured system user to the security manifest, the next time that you deploy a solution snapshot online from Workflow Center to the workflow server, the deployment will fail. This is because the configured system user will not have the authority to perform deployment operations for the CPE folders.
- Solution assets changed in Case Builder cannot be viewed in Case Client after redeployment

Case Client users cannot see changes to assets that were recently added or modified by using Case Builder.
- Removing proxy documents that are associated with external documents

When you unfile an external document from a case, the associated proxy document is not removed from the case management object store. To remove the proxy document, manually delete it from Content Platform Engine by using IBM Administration Console for Content Platform Engine.
- Cannot reassign work items in the All Assigned Work in-basket

To reassign work items in the All Assigned Work in-basket, your role must have the appropriate permissions.
- Messages and annotations in the viewer are not displayed in the browser locale or are displayed incorrectly

 Traditional:  When you view documents by using Case Client, the messages and annotations in the viewer are not displayed in the locale in which the browser is set, or they are displayed incorrectly.
- Unlocking a locked work item

A work item can get locked if a user does not complete the work item and does not go back to complete the item, or if a user closes the browser before completing the work item.
- Long-string properties that are reused in case type searches might have invalid operators

A search in Case Client that uses long string properties might have invalid operators that are causing the Case Client search to fail.
- Adding workflow groups to a step in IBM FileNet Process Designer can cause validation errors in Step Designer

You see validation errors in Step Designer for a workflow that validated successfully in IBM FileNet Process Designer.
- Changing the saved solution locale after solution deployment

If you deploy a solution under the wrong locale the first time that you deploy it, the wrong solution locale is saved to the target object store for that solution. To resolve the problem, you must manually change the solution properties in the target object store.
- Problems occur when you import solutions with IBM FileNet Deployment Manager

Various problems can occur when you use FileNet Deployment Manager to import solution assets into IBM Business Automation Workflow.
- Troubleshooting CA eTrust SiteMinder single sign-on configuration

 Traditional:  The Register Project Area task in the workflow Case configuration tool fails and displays an error message stating that an error occurred while running Register Target Environment.
- Cannot copy solutions that contain rule steps in a production environment

In a production environment, when you try to copy a solution that contains a workflow with a rule step you receive a message that the solution cannot be validated because no definition was found for the ICM\_RuleOperations queue.
- Cannot deploy a solution with business rules if transaction timeout value is too low

 Traditional:  You cannot deploy a solution that contains business rules if the transaction timeout setting of the application server for Content Platform Engine is too low.
- Rule steps do not run if processing timeout value is too low

Rule steps might not run if the processing timeout value for the rules component queue is too low.
- Troubleshooting business rule errors

You might receive errors that are related to business rules when you deploy or run IBM Business Automation Workflow.
- Troubleshooting case history table lock escalation errors

If table lock escalation errors occur when case history data is processed, you can bypass new errors by increasing the size of the log file for the case history database and increasing the maximum number of table locks.
- Database deadlock issue with large solution deployments

When you try to deploy a large solution, a database deadlock error might be generated in the IBM FileNet P8 server error log.
- Event payloads can contain model objects that are not fully retrieved

Event payloads can sometimes contain sparse model objects that are not fully retrieved.
- Improve performance at case creation time by limiting subfolder structure

To improve performance at case creation time, limit the predefined subfolder structure in your case design to 10 or fewer subfolders. The more subfolders that are in a predefined subfolder structure, the longer case creation can take. To reduce the time that it takes to create a case, limit the complexity of your predefined folder structure.
- Case administration client does not remove all files that are related to the package

To completely remove a custom widgets package, you must manually delete some additional files after you use the Case administration client to delete the package.
- Supporting external documents in production environments

To support external documents in a production environment, you must update security settings in the Administration Console for Content Platform Engine.
- Older versions of an audit or security configuration in the Case administration client might not be re-imported

You cannot roll back an audit or security configuration to an older version by using the Case administration client to re-import the older configuration if a newer configuration exists in the same environment.
- EAR file for custom widget package isn't deployed

 Traditional:  You can use the Case administration client to register a custom widget package.
- Case configuration tool task fails with 414 error

 Traditional:  Running the Register Target Environment configuration task in an environment with Oracle HTTP Server results in a 414 Request-URI Too Large error.
- Configuring the object stores failed

 Traditional:  If configuring the object stores fails, you can either re-tune your database or increase the database transaction timeouts.
- Troubleshooting ECMException ObjectStore.get\_RootFolder returns null

If incomplete information about the FileNet P8 object stores is cached, users might encounter errors when using IBM CMIS for FileNet Content Manager.
- Re-creating an IBM Business Automation Workflow target object store in a development environment

If the development target object store for IBM Business Automation Workflow is corrupted or unusable, you can re-create it.
- Configure Box Collaboration task fails in a distributed environment when the date/time is not synchronized

 Traditional:  In a distributed or cluster environment, the Configure Box Collaboration task does not run if the system time is not synchronized with the internet time.
- Auto stage completion fails in Case Builder with WSIloginModule

 Traditional:  Auto stage never goes to complete state. The problem can be resolved by removing WSIloginModule.