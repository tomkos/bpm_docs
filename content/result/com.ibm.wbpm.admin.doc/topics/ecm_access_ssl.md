# Accessing an Enterprise Content Management server using the
Secure Socket Layer (SSL)

## About this task

These steps show you how to set up a connection to an
Enterprise Content Management server using SSL.

## Procedure

1. Launch the Administrative console and log in to the Integrated
Solutions Console of the server running your IBM® Workflow
Center.
2. Navigate to Security > SSL certificate and key management > Key
stores and certificates > NodeDefaultTrustStore > Signer certificates.
3. Click Retrieve from port.
4. In the Host field, enter the hostname,
in the Port field enter the secure port number
and in the Alias field enter an alias name
for the Enterprise Content Management server you want to connect to.
5. Click Retrieve signer information.
Click Ok if the retrieval is successful.
6. Save your work and log out of the Integrated Solutions
Console. Restart your server if necessary.
7. When you add this secure server in your Process Apps Settings
page, use the host name and port that you used in the Integrated Solutions
Console. Select the Secure check box.