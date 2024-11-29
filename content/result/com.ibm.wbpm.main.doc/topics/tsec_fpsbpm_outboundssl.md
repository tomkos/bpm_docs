# Securing outbound communications between Process Federation Server and federated systems

## Before you begin

- If your development or test environment communicates directly with a federated system, you canget the system signer certificate in one of the following ways:
    - Use the administrative console to extract the signer certificate. See Personal certificates collection.
    - Use the PFSSecurityUtility.py script to create a keystore and truststore that
are based on the signer certificate.
- If your development or test environment communicates with the federated system through an IBM
HTTP Server, get the signer certificate from the IBM HTTP Server by using the IKEYMAN utility. See
Securing with SSL communications.

## About this task

The Liberty
server.xml file contains the SSL configuration settings for Process Federation Server. The server.xml
that is provided as a template includes a default SSL configuration, and a default keystore. You can
configure a truststore for the signer certificates, so that communication can be secured with the
REST endpoints.

To manage the Process Federation Server truststore, use your JVM’s
keytool utility, or the IBM HTTP Server IKEYMAN utility.

## Procedure

1 Add the signer certificate for each federated system to the Process Federation Server truststore. In a development or test environment, use the Process Federation Server keystore as both the keystore andtruststore to simplify configuration. In a production environment, use a separate truststore. Useone of the following utilities to optionally create a new truststore and to import the signercertificate into your truststore:
    - Your JVM’s keytool utility
    - IBM HTTP Server IKEYMAN utility
    - In a development or test environment, you can use the PFSSecurityUtility.py script to create a combined Process Federation Server keystore and truststore that is based on the system certificate:
        1. Copy the script from the
pfs\_install\_root/ibmProcessFederationServer/wlp-ext/util
directory to a federated system and get the list of utility commands and
parameters:wsadmin -lang jython -host host\_name -port port\_number 
  -user user\_id -password user\_password 
  -f script\_path/PFSSecurityUtility.py help
        2. Use the createKeyStore command to create a combined keystore and truststore,
and a chained certificate that is signed by the root signer.
        3. Use the addSignerCertificate command for each additional federated system to
retrieve the root signer certificate, and add it to the combined keystore and truststore.
2 Update the Process Federation Server server.xml configurationfile to point to the truststore that you configured in step 1.

1. Open the server.xml configuration file for
editing.
By default, the configuration file is in the
pfs\_install\_root/usr/servers/server\_name directory on
Process Federation Server.

1. Update the keyStore element. 
Replace the default truststore values for the truststore filename
and password properties with the values that you configured in step
1.<keyStore id="defaultTrustStore"  
          location="pfs\_install\_root/usr/servers/server\_name/resources/security/new\_truststore\_filename"
           password="password" />