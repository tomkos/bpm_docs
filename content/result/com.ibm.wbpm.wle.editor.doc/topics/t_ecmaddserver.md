# Adding an Enterprise Content Management (ECM) server

## About this task

To add a server, follow these steps.

## Procedure

1. Select the Servers tab from the editor. You see the editor when
you first click Open in Designer from a newly created process application. Alternatively you can
select Process App Settings from the drop-down list on the toolbar in designer.
2. Under Servers, click +. Under
Details, enter a meaningful name for the server. From the drop-down list in
the Type field, select Enterprise Content Management
Server. Enter a meaningful description of the server in the
Description field. This field is optional. 
If you are working with the IBM® Process
Designer desktop editor,
under Servers, click Add to add a server
3 Enter the server configuration properties in the Default tab. If you are working with the IBM ProcessDesigner desktop editor,entering the server configuration properties is similar. However, the selection of the environmenttype is with a drop-down list.
    - The Default tab contains the server configuration properties of yourdefault environment type. You can have several environment types, which are added by clicking+ . The other environment types that you can add are as follows: You can modify the environment type after deployment by using theupdateBPMConfig administrative command. See Modifying the IBM Workflow Server environment type .
        - Development: The environment where you develop your services.
        - Test: The environment where you test your services.
        - Staging: The environment where you deploy your services for preproduction
testing.
        - Production: The environment where your services are deployed for use by
your organization.
- Host Name: The host name of the Enterprise Content Management server.
Specify an IP address or a host name and domain. For example:
myHost.labwide.ibm.com
- Port: The port number of the Enterprise Content Management server.
- Context Path : The path to the Content Management InteroperabilityServices (CMIS) web services application on the server. A connection must be established throughContent Management Interoperability Services (CMIS) by using the web services protocol rather thanthe Atom protocol.
    - The default CMIS context path is /fncmis and the port
is 9443.
- Secure Server: Select this option to specify whether you want your
service to be secure, that is, to use the Hypertext Transfer Protocol Secure (HTTPS) protocol. If
you select the HTTPS protocol, you must configure HTTPS security.
- Repository: The name of your repository. If you are using FileNet® Content
Manager as the ECM
server, the object store name is the CMIS repository name.
- User ID: The user ID to connect to the Enterprise Content Management
server.
- Password: The password of the user ID connecting to the Enterprise
Content Management server.
- Always Use This Connection Information: If selected, which is the
default, only this user ID and password are used for authentication. For example, a human service,
which your service is associated with when a Document List or Document Viewer is configured, also
has a user context. An administrator uses the Manage Users function to specify human service users.
Selecting this check box means this user ID and password overrides any other user information.
- ECM Document Authorization Service: A service that you create and select
if you want to check the permissions of a user. It is used by the Responsive Document Explorer,
Responsive Document List, and Responsive Document Viewer coach views from the Content Management
(SYSCM) toolkit when they perform operations that cannot be customized by using an Ajax service. It
is also used by the older heritage coach views of these controls. These operations are the creation,
update, and download of a document. The service is not used when you directly invoke the Content
Integration operations in the human service, Ajax service, and integration service editors.Important: To upload a document to the server, you must configure the ECM document
authorization service by creating a service and entering the following string in the script task:
tw.local.authorized=true;
- ECM Query Authorization Service: A service that you create and select if
you want to write custom logic to validate incoming CMIS queries associated with this server. This
service needs to be set when you select Always Use This Connection
Information. This service helps you in writing custom logic that validates the query and
runs the query that uses the validated query.Important:
To enable query validation for a server, you must configure the ECM query authorization service
by creating a service and write custom logic to validate incoming CMIS queries associated with this
server.
This service is executed when the Always Use This Connection Information
checkbox is selected. For example:var inquery = tw.local.inCmisQuery;
// Sample CMIS query
// SELECT cmis:objectId, cmis:name, cmis:lastModificationDate, cmis:versionLabel, cmis:contentStreamMimeType FROM  cmis:document WHERE IN\_FOLDER('idf\_088B1B67-1FF1-4A73-8E3A-8A52842A6B4B') ORDER BY cmis:name ASC
var folderId = null;// Parse and get the folderId from the CMIS query
if(inquery.indexOf("WHERE") != -1) {
    if(inquery.indexOf("IN\_FOLDER") != -1) {
        var start = inquery.indexOf("('") + 2;
        var end = inquery.indexOf("')");
        folderId = inquery.substring(start + "idf\_".length, end);
        folderId = "{" + folderId + "}";
    }
}
// For each server, one can have different validation logic
if(serverName == "ecm") {
    if(folderId != null) {
        // Fetch folder path using a JS API getECMFolderPath defined in the scope of a system namespace       
        var folderPath = tw.system.getECMFolderPath(serverName, folderId);
        if(folderPath != null && folderPath != "/") {
            // Check if the folder path is not Root (meaning access to all content under Root folder)           
             // You might have set a folder path such as /Invoices or /Receipts or any other custom folder under the Root as part of configuration setting in the ECM Coach Control. Check if the path matches. Here /Invoices or /Receipts is just an example. Please change it appropriately to your custom folder path           
            if(folderPath == "/Invoices" || folderPath == "/Receipts")
            {                
                 // Valid folder               
                 // Rebuild the cmis query or set the outCmisQuery to the inCmisQuery   
                 tw.local.outCmisQuery = tw.local.inCmisQuery;            
            }
        }
    }
}
- Event broadcasters: Specify a team whose content events are able to
trigger a document start event or precondition evaluation. The team must include the technical user
for this server. Content events will be processed only from these users.

If you are working with the IBM Process
Designer desktop editor,
entering the server configuration properties is similar. However, the selection of the environment
type is with a drop-down list.

4. Click Test Connection to confirm
the connection to the server works.
5. Click Save or Finish Editing.

## What to do next

- Enabling the creation, update, and download of ECM documents

Creating, updating, or downloading external Enterprise Content Management (ECM) documents is disabled by default. However, you can enable them, if it is required by your process applications, by adding the enable-document-authorization-security-service configuration setting to the 100Custom.xml files, clearing the Always use this connection information option in external ECM Server definitions, or creating a service that checks the permissions of a user.
- Disabling the ECM Query Authorization Service

The ECM Query Authorization Service is required and enabled by default, when Always use this connection information option in external ECM Server definitions is selected. However, if you would like to disable the ECM Query Authorization Service(s) for ECM servers for all process applications, you can disable the requirement for the ECM Query Authorization Service by adding the enable-query-authorization-security-service configuration setting in the 100Custom.xml files.