# Configuring single sign-on with LTPA for an external IBM Business Automation
Navigator

## Procedure

To configure single sign-on for an external Business Automation Navigator, complete the following steps:

1. Ensure that Business Automation Navigator is installed on
WebSphere® Application
Server v8.5 or higher.
2 Configure access to a shared user repository. Both IBM Business Automation Workflow and Business Automation Navigator must have access to the same set of users.Therefore, configure both cells to access the same user repository (such as a Lightweight DirectoryAccess Protocol (LDAP) directory). To configure access to a shared user repository, follow thesesteps: There is no need to remove or disable any file-based registries on the two systems. Theregistries can still be useful for administrative functions. Note, however, that users and groupsfrom file-based registries cannot be used in Business Automation Workflow case applications. In the WebSphereadministrative console of both systems, select Users and Groups > Manage Users and search for the Business Automation Workflow userID that you are going to define as the ECM administrative user. Verify that the user ID is uniqueand it is in the shared user repository.
    1. In the WebSphere administrative console on both systems, select Security > Global Security. The Global Security page opens.
    2 In the Available realm definitions drop-down list, select one of theseoptions:
        - If Business Automation Navigator is configured with a federated
repository, select Federated Repositories and then click
Configure. The Federated Repositories page opens.
        - If Business Automation Navigator is
configured with a stand-alone LDAP (deprecated for Business Automation Workflow), select
Standalone LDAP and then click Configure. The
Standalone LDAP page opens.
3. Configure your shared user repository with matching user and group attributes.
4. Test your LDAP connection. See Configuring Content Platform
Engine application server authentication (LDAP) settings.
5. If the realm names of Business Automation Workflow and Business Automation Navigator are different (for example, because you set
different active realm definitions), make certain that in each cell the realm of the other cell is
trusted. From the navigation panel, click Security > Global security. Under RMI/IIOP security, click CSIv2 inbound
communications. Click Trusted authentication realms - inbound.
Select Trust realms as indicated below. Click Add external
realm and add the realm of the remote cell. Click Apply.

In the WebSphere
administrative console of both systems, select Users and Groups > Manage Users and search for the Business Automation Workflow user
ID that you are going to define as the ECM administrative user. Verify that the user ID is unique
and it is in the shared user repository.

3 Configure single sign-on with Lightweight Third-Party Authentication (LTPA) keys. Because alluser IDs are shared, users that are authenticated in either one of the systems don't need toauthenticate again when they connect to the other system. If you are adding a Business Automation Navigator system to an existing Business Automation Workflow installation, you can export the LTPA keys fromthe Business Automation Workflow system. Then, you can import themto the Business Automation Navigator system. You can also import andexport the LTPA keys the other way around. These substeps follow the first approach. You might want to increase the number of active keys that WebSphere ApplicationServer returns when the server queries for keys for aparticular key set. When you import keys into the cell, active keys are overwritten. The replacedkeys become the historic keys. WebSphere keeps, by default, a maximum of 2 keys in the cell. Thismaximum means that, with a second import, the original key of the cell is paged out. For reliabilityreasons, you might want to keep these keys. You are successful in establishing single sign-on (SSO) between the two systems when you can login to one administrative console and then access the other administrative console without having tolog in again. Log in to the WebSphere ApplicationServer administrative console where you exported the LTPA key. In your browser's address bar, enter the URLfor the WebSphere ApplicationServer administrative console where youimported the LTPA key. If the administrative console opens without requiring you to log in, yousuccessfully set up SSO. The previous test for a successful single sign-on works only if the administrative user for bothcells is identical. An alternate test is to log on to two URLs with an ordinary user from the sharedrepository; that is, a user without additional administration rights in both cells. For example, inBusiness Automation Workflow , log in to the /ProcessPortal URL witha user from shared repository. Then, in a new browser tab, specify the URL for the AdministrationConsole for Business Automation Navigator . Note: Using localhost, ashort host name, or the IP address in place of the host name does not work. Single sign-on requiresthat the browser pass LTPA cookies to the WebSphere ApplicationServer server. These cookies contain the fully qualified host name that must match the specified SSOdomain name.

You might want to increase the number of active keys that WebSphere Application
Server returns when the server queries for keys for a
particular key set. When you import keys into the cell, active keys are overwritten. The replaced
keys become the historic keys. WebSphere keeps, by default, a maximum of 2 keys in the cell. This
maximum means that, with a second import, the original key of the cell is paged out. For reliability
reasons, you might want to keep these keys.

1. Select Global security, expand Web and SIP
security, select Single sign-on (SSO). Make sure that
Enabled is checked and specify a common domain name on both servers.
The domain name is case-sensitive and should be lowercase.
2. In the WebSphere administrative console of the Business Automation Workflow server, select Security > Global Security. The Global Security page opens.
3. Click the LTPA link. The LTPA page opens.
4. Export the LTPA keys to a file. Use an arbitrary password.
5. Copy the exported file to a location that can be shared with the Business Automation Navigator system.
6. In the WebSphere administrative console on the Business Automation Navigator system, select Security > Global Security. The Global Security page opens.
7. Click the LTPA link. The LTPA page opens.
8. Import the exported LTPA keys. Use the same password that was used for the export.
9. Still on the Global Security page, select Administrative
authentication and make sure Only use the active application authentication
mechanism is checked.
10. Restart each WebSphere Application
Server.

You are successful in establishing single sign-on (SSO) between the two systems when you can log
in to one administrative console and then access the other administrative console without having to
log in again. Log in to the WebSphere Application
Server
administrative console where you exported the LTPA key. In your browser's address bar, enter the URL
for the WebSphere Application
Server administrative console where you
imported the LTPA key. If the administrative console opens without requiring you to log in, you
successfully set up SSO.

4 Update the ECM system to support SSL. The default installation of Business Automation Workflow uses SSL. The default installation of Business Automation Navigator uses TCP-IP without SSL. Update the Business Automation Navigator system to support SSL by completing thefollowing substeps:

1. In the WebSphere administrative console on the Business Automation Navigator system, select Security
> Global Security. The Global Security page opens.
2. Expand the RMI/IIOP security section. A list of inbound and
outbound links is displayed.
3. Click each inbound and outbound link, and then in the Transport
drop-down list, select either SSL-required or
SSL-supported.
5 On both the Business Automation Workflow and Business Automation Navigator systems, configure SSL to exchange SSLcertificates in both directions between the servers by completing the following substeps:

1. In the WebSphere administrative console, select Security > SSL certificate and key management. The SSL certificate and key management page opens.
2. Select the Key stores and certificates link. The Key stores and
certificates page opens.
3. Select NodeDefaultTrustStore (for Base Server) or
CellDefaultTrustStore (if on a Network Deployment cell).
4. Either extract the certificate to a file and copy it to the other system to add, or use the
Retrieve from port button to connect and retrieve the certificate. For
details on retrieving from the port, see Configuring cross-cell security for IBM Workflow Center.