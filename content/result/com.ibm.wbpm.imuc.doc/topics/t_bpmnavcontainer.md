# Configuring IBM Business Automation
Workflow with  an IBM Business Automation
Navigator container

Containers: 
If you are
running IBM® Business Automation
Navigator in a container, you can configure
IBM Business Automation
Workflow to work with your containerized
version.

Start with the instructions in Configuring IBM Business Automation
Workflow with an external IBM Content
Navigator until the steps send you to
this topic.

## Procedure

1. Use the same LDAP server in IBM Business Automation
Workflow
and in the IBM Business Automation
Navigator container. See Configure
IBM virtual member manager (VMM) Repositories with Content Platform Engine.
2. Configure IBM Business Automation
Workflow with the same
User Management Service (UMS) that IBM Business Automation
Navigator uses. See Configuring User Management Service.
3 Configure SSL between IBM Business AutomationWorkflow and theexternal IBM Business AutomationNavigator container operator.
    1. In the WebSphere® Application
Server administrative
console, go to SSL certificate and key management > Key
stores and certificates > CellDefaultTrustStore > Signer
certificates and export the  IBM Business Automation
Workflow certificate as a file named 
baw.cert.
    2. Copy baw.cert to the IBM Business Automation
Navigator container operator environment
and add this certification using the IBM Business Automation
Navigator operator TLS
setting. Follow the instructions in Exporting the operator root CA key and importing it into an external
service.
    3. Add IBM Business Automation
Navigator
root certification to IBM Business Automation
Workflow. Follow the
instructions in Importing the certificate of an external
service.