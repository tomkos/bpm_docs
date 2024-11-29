# Configuring IBM Business Automation
Workflow with a Content Platform Engine container

## About this task

- Case solutions that are deployed through Workflow Center and that have case
activities that are implemented as Business Automation Workflow local processes are
not supported.
- Content Management toolkit artifacts that are used in coaches do not work.

## Procedure

1. Use the same LDAP server in Business Automation Workflow and in the Content Platform Engine
container.
2. Configure Business Automation Workflow with the same UMS
that Content Platform Engine
uses. See Adding IBM Business Automation Workflow and IBM Federated Process Portal to use the User Management Service.
3 Configure the Secure Sockets Layer (SSL) between IBM Business AutomationWorkflow and the external Content Platform Engine container operator.
    1. In the WebSphere® Application
Server administrative console, go
to SSL certificate and key management > Key stores and
certificates > CellDefaultTrustStore > Signer
certificates and export the Business Automation Workflow certificate as a
file named  baw.cert.
    2. Copy baw.cert to the Content Platform Engine container operator
environment and add this certification by using the Content Platform Engine operator TLS
setting. Follow the instructions in Importing the certificate of an external service.
    3 Add the Content Platform Engine root certification toBusiness Automation Workflow .
        1. Export the Content Platform Engine
root certification. Follow the instructions in Exporting the operator root CA key and importing it into an external
service.
        2. Copy the Content Platform Engine
certificate that you have exported from the previous step to Business Automation Workflow server and import it
to Business Automation Workflow in

WebSphere
 administrative
console.
4. Configure a single sign-on for the Content Platform Engine. Follow the
instructions in Configuring single sign-on with
UMS.
5. Change the realm name of the Content Platform Engine
container to be the same as the realm name of IBM Business Automation
Workflow. Set the realmName in
the openidConnectClient configuration as described in step 6. Configure Open Id
Connect on the Content Platform Engine in Configuring users with an Identity Provider
(IDP).