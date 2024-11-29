# Accessing an IBM Business Automation
Workflow server using the
Secure Sockets Layer (SSL) (deprecated)

## About this task

These steps show you how to set up a connection to an IBM Business Automation
Workflow server
using SSL.

## Procedure

1. Launch the Administrative console and log in to the IBM
Integration Solutions Console of the server running your IBM Workflow
Center.
2. For stand-alone servers, navigate to Security > SSL certificate and key management > Key stores and certificates > NodeDefaultTrustStore > Signer certificates. 

In a Network Deployment (ND) environment, the truststore is called CellDefaultTrustStore.
3. Click Retrieve from port.
4. In the Host field, enter the hostname,
in the Port field enter the secure port number
and in the Alias field enter an alias name
for the IBM Business Automation
Workflow server you want to connect to.
5. Click Retrieve signer information. Verify that the retrieved information is the expected signer certificate
of your Case Manager server. Click Ok if the
retrieval is successful.
6. In a Network Deployment (ND) environment, make certain
all nodes are synchronized. Save your work and log out of the IBM
Solutions Console.
7. When you add this secure server in your process app settings
page, use the host name and port that you used in the IBM Solutions
Console. Click the Secure check box.