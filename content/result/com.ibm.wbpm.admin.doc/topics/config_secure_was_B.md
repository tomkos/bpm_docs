# Installing a signer certificate in IBM Workflow
Server trust
store

## Before you begin

Extract the signer certificate.

You must stop the IBM Workflow
Server if
it is running.

## Procedure

Complete the following steps to install the signer
certificate to the trust store for the IBM Workflow
Server:

1. Transfer the Distinguished Encoding Rules (DER) file from
the preceding procedure to a file system location that is accessible
to the IBM Workflow
Server. 
For example, you can use a shared drive.
2. On the IBM Workflow
Server host
system, go to install\_root/java/bin and
invoke ikeyman.
3. Click Key Database File > Open.
4. Set the value of Key database type to JKS.
5. Set the value of Location to install\_root/java/jre/lib/security.
6. Set the value of File Name to cacerts.
7. Click OK.
8. Provide a password. The default password is changeit.
9. Click Signer Certificates > Add.
10. Specify the location of the DER file, and then click OK.
11. Enter a label for the certificate, and then click OK.
12. Start IBM Workflow
Server.