# Configuring single sign-on (SSO) for federated environments by using LTPA keys

## Before you begin

- Domains: The Process Federation Server and the
federated servers, including the server that hosts Process Portal, must be in the same domain.
- User registries for Process Federation Server andthe federated servers:
    - The user registries must be shared. Different federated environments can use different user
registries but you must configure these user registries on both Process Federation Server and the server
that hosts Process Portal or
Workplace, too. Restriction: You cannot mix LDAP servers with other authentication services, such as a basic
user registry or a custom user registry.
    - The user registries must use the same realm. The realm name must be the same as the one that you
set for Process Federation Server. To do so, in the WebSphere® Application
Server administration console, go
to Security > Global Security,
then, in the User account repository section, set your LDAP directory to use
a federated repository and name the realm ldap\_realm. For more information,
see the Federated repositories page of the WebSphere Application
Server documentation.
- LTPA key file:

- The keys are active.
- All the federated servers, including the server that hosts Process Portal or Workplace, share an LTPA key
file.
- System times: To avoid problems with LTPA expiry intervals, ensure that the system times on
Process Federation Server and each server in the
production environment are the same.

## About this task

## Procedure

1. Configure SSO for Process Federation Server
by uncommenting the following statement to the server.xml file:
<webAppSecurity allowLogoutPageRedirectToAnyHost="false" ssoDomainNames="domain.mycompany.com" ssoCookieName="LtpaToken2" ssoRequiresSSL="true" ssoUseDomainFromURL="true"/>To
ensure that the LTPA token cookies are propagated to all the federated systems, if you change the
default value of the ssoCookieName property, you must also change the value of the
propagateCookieNames property in all the ibmPfs\_bpdRetriever and
ibmPfs\_bpelRetriever elements in the server.xml file. For more
information, see Configuration properties for the Process Federation Server index.
2 Enable SSO for the federated servers, including the server that hosts Process Portal or Workplace .
    1. Log in to the administrative console.
    2. Open the Global security page by clicking
Security > Global security.
Expand Web and SIP security and click Single sign-on
(SSO).
    3 In the Single sign-on (SSO) window, configure the followingsettings:
        - Select Enabled.
        - Enable Requires SSL.
        - Set the domain name.
        - Save your updates.
3. Disable the automatic LTPA key generation on the federated servers.
Because the LTPA keys are shared between Process Federation Server and the
federated servers, automatic generation of keys causes the shared keys to become out of sync over
time. See WebSphere Application
Server:
Disabling automatic generation of Lightweight Third-Party Authentication keys
4 Share the LPTA key file among all the servers in the federatedprocess environment. Tip: To minimize the impact on existing environments that share LTPA keys, get and sharethe LTPA key file from one of the federated servers instead of sharing the Process Federation Server LTPA key. The instructions in thisstep assume that you are sharing a Business Automation Workflow orIBM BPM LTPA key.

1. Export the federated server LTPA key file from one of the servers by selecting Security > Global security > Authentication mechanisms and expiration > LTPA. Enter a password, which will be used to encrypt and
decrypt the keys, and the fully qualified key file name, and then click Export
keys.
2. If you have other federated servers that are not already configured for SSO with LTPA,
import the LTPA key file into each of the servers. 
In the administrative console, import the LTPA keys into each of these servers by selecting Security > Global security > Authentication mechanisms and expiration > LTPA. Enter the encryption password (the default password is
WebAS) and the fully qualified key file name, and then click Import
keys.
3. Save your changes and restart the federated servers.
4. Import the LTPA keys into Process Federation Server by
copying the key file to the pfs\_install\_root/usr/servers/server\_name/resources/security directory
and uncommenting the following entry to the server.xml file:
<ltpa keysFileName="pfs\_install\_root/usr/servers/server\_name/resources/security/yourLTPAKeysFileName.keys" keysPassword="keys\_Password"/>
5. Optional: Monitor the lpta.key file
so that changes to the key file can be dynamically reloaded by setting
a value for the monitorInterval attribute. 
In the following example, the lpta.key file
is checked every 5 seconds:<ltpa keysFileName="yourLTPAKeysFileName.keys" keysPassword="keys\_Password" expiration="120" monitorInterval="5s" />

## What to do next

1. From a web browser, go to a URL on any federated system or the server that hosts Process Portal or Workplace. For example, the
Process Portal URL:
https://bpm\_host.mycompany.com:9443/ProcessPortal. Import the
signer certificate if prompted to do so by the browser.Tip: Before you are directed to
Process Portal, you should
be prompted for your user ID and password the first time you access the URL.
2. From the same web browser, go to a URL on any other system in your federated environment, for
example, the Process Portal URL:
https://bpm\_host.mycompany.com:9443/ProcessPortal. Import the
signer certificate if prompted to do so by the browser.Tip: You should be automatically
directed to Process Portal without having to log in
again.
3. From the same web browser, go to a Process Federation Server URL, for example, the systems REST
service:
https://pfs\_host.mycompany.com:9443/rest/bpm/federated/v1/systems.
Import the signer certificate if prompted to do so by the browser.Tip: The REST service
request should complete without having to log in again.

If you are not prompted to log in at steps 2 and 3, SSO is working correctly.

If you
are prompted to log in at either step 2 or step 3, SSO is not working correctly. Verify the SSO
configuration and restart your server or Process Federation Server if you updated the configuration.
Before you verify SSO again, clear your browser cookies to remove the LTPA cookie that is used for
SSO.