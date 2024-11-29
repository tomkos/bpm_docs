# Enabling the creation, update, and download of ECM documents

Creating, updating, or downloading external
Enterprise Content Management (ECM) documents is disabled by default.
However, you can enable them, if it is required by your process applications,
by adding the enable-document-authorization-security-service configuration
setting to the 100Custom.xml files, clearing
the Always use this connection information option
in external ECM Server definitions, or creating a service that checks
the permissions of a user.

- You use the Document List or Document Viewer coach views to create,
update, or download the documents.
- You are using an external ECM server instead of the internal BPM document store.
- The properties of the ECM server definition have Always
use this connection information selected.

## Procedure

To enable the creation, update, and download of a
document, perform one of the following procedures:

- Add the following configuration setting to the 100Custom.xml file
in IBM® Workflow
Center or IBM Workflow
Server. 
  Note: Disabling the authorization service leads to security
vulnerabilities.

 <server>
   <!-- enable the document authorization security service -->
      <enable-document-authorization-security-service merge="replace">false</enable-document-authorization-security-service>
</server>
- For external ECM Server definitions within your process
applications and toolkits, clear the Always use this connection
information option, which causes IBM Business Automation
Workflow (BPM)
to propagate each user's context to the ECM server. Not
all ECM systems can share security context with Business Automation Workflow. To determine
whether you can use this option, see Authentication
scenarios.
- Create a service that checks the permissions of a user.Then, associate this service with each ECM server definition.
    1. Open the settings page for a process application or
toolkit that contains an ECM server definition, and go to the Servers tab.
    2. Select the ECM server from the
list, and scroll to the bottom of the Properties on
the left.
    3 For the External ECM Document AuthorizationService property, select New togenerate an empty service with the proper interface, or select anexisting service. The interface for this service musthave the following signature in the Variables tab: Inputparameters Output parameter

The interface for this service must
have the following signature in the Variables tab:

        - documentId (ECMID)
        - objectTypeId (ECMID)
        - action (String). The actions
available for creating, downloading, and updating external ECM documents
are ACTION\_CREATE\_DOCUMENT, ACTION\_GET\_DOCUMENT\_CONTENT,
and ACTION\_UPDATE\_DOCUMENT.
        - serverName (String)
        - authorized (Boolean)
4. Define the logic that uses one or more of the input
parameters to determine authorization for the action. The
service must return true if the user is authorized
for the action and false if the user is not authorized.
Your new service runs when a user creates, updates, or downloads a
document from a Document List coach view.
5. Click Save or Finish Editing.
6. Run a test to confirm the authorization logic that you
developed is working as you expect.
7. Create a snapshot for your changes when you are ready
to deploy them.