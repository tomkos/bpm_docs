# Configuring single sign-on with LTPA for an IBM Content
Navigator or Content Platform Engine container

## Before you begin

- Ensure IBM Business Automation
Workflow, IBM Content
Navigator, and Content Platform Engine are configured with the same LDAP server and
share the same user registry.
- Ensure Business Automation Workflow, IBM Content
Navigator, and Content Platform Engine are under the same domain. Because the LTPA
token can't be shared across different domains, make sure that the host names for accessing Business Automation Workflow, IBM Content
Navigator, and Content Platform Engine have the same suffix.

## Procedure

1 Exchange certificates between Business Automation Workflow , IBM ContentNavigator , and the Content Platform Engine .
    1 Add IBM ContentNavigator andContent Platform Engine certificates to the Business Automation Workflow truststore.
        1. Log in to the IBM WebSphere® Application
Server admin
console.
        2. Go to Security > SSL certificate and key
management > Key stores and
certificates > CellDefaultTrustStore > Signer
certificates.
        3. Click Retrieve from port.
        4. Enter the host, port, and alias values for the Content Platform Engine container.
        5. Click Retrieve from port.
        6. Enter the host, port, and alias values for the IBM Content
Navigator container.
2 Add Business Automation Workflow certificates tothe IBM ContentNavigator and Content Platform Engine truststores.
    1. Log in into the WebSphere Application
Server admin console.
    2. Go to Security > SSL certificate and key
management > Key stores and
certificates > CellDefaultKeyStore > Personal
certificates.
    3. Select the default certificate option and click
Extract to extract the certificate.
    4. Specify where you want to save the certificate.
    5. Copy the extracted certificate to the Openshift environment that deploys IBM Content
Navigator or the Content Platform Engine.
    6. Create a secret with the certificate file by using the following command: kubectl create
secret generic baw-tls-secret --from-file=tls.crt=/ext/nfsshare/keystore/baw.cert
    7. Open the custom resource (CR) file that is used to deploy IBM Content
Navigator or the Content Platform Engine.
    8. Add the created baw-tls-secret  under
spec.shared\_configuration.trusted\_certificate\_list.
    9. Re-apply the CR file.
2 Exchange the LTPA token between Business Automation Workflow , IBM ContentNavigator , and the Content Platform Engine .

1. Log in to the WebSphere Application
Server admin
console.
2. Go to Security > Global
security > Authentication > LTPA.
3. Export the Business Automation Workflow LTPA
key.
4. Copy the exported LTPA key to the mapped persistent volume (icn\_cfgstore and
cpe\_cfgstore) path of IBM Content
Navigator and
Content Platform Engine. For example, the path might have the
format: /opt/cpit\_data/icn\_data/configDropins/overrides
5. Create a file named sso.xml to configure or overwrite the LTPA
settings for IBM Content
Navigator and the
Content Platform Engine. Ensure that the ssoDomainNames value
is the same as the value in the Business Automation Workflow
server. 
<server>
        <webAppSecurity ssoDomainNames="rtp.raleigh.ibm.com" ssoRequiresSSL="true" singleSignonEnabled="true" useAuthenticationDataForUnprotectedResource="true" useOnlyCustomCookeiName="true" ssoCookieName="LtpaToken2" /> 
        <ltpa monitorInterval="60s" keysPassword="passw0rd" keysFileName="/opt/ibm/wlp/usr/servers/defaultServer/configDropins/overrides/bawltpa.key" expiration="120m"/>
        <httpSession cookieHttpOnly="true" securityIntegrationEnabled="true"/>
</server>
6 Delete the IBM ContentNavigator instance and the Content Platform Engine pod. After they aredeleted, the pods are automatically redeployed.
    1. Log in to the Kubernetes admin console or OpenShift admin console.
    2. Find the IBM Content
Navigator instance and
Content Platform Engine pod instance, and delete them.
3 Enable SSO for Business Automation Workflow .

1. Log in to WebSphere Application
Server admin console.
2. Go to Security > Global
security > Authentication > Web and SIP
security > Single sign-on (SSO).
3. Make sure the Enabled and Requires SSL options are
selected.
4. Enter the same domain name as the setting for IBM Content
Navigator or the Content Platform Engine. For example, a domain name might look like:
rtp.raleigh.ibm.com
5. Click OK.
6. Save the changes and restart Business Automation Workflow.
4 Validate the SSO configuration. If you can access the Business Automation Workflow URL orContent Platform Engine URL without entering your user name andpassword, the SSO has been configured successfully.

1. Log in to IBM Content
Navigator by using the
credentials of an existing user from LDAP.
2. Open another browser tab and enter the Business Automation Workflow URL or Content Platform Engine URL.

If you can access the Business Automation Workflow URL or
Content Platform Engine URL without entering your user name and
password, the SSO has been configured successfully.