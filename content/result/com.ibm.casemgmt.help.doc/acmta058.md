# SSLHandshakeException error in the Case configuration tool

## Symptoms

When the Case configuration tool connects to a server by
using an SSL or a TLS connection, the certificate of that server is verified against the keystore
that is used by the Case configuration tool. To ensure that the
server certificate is authentic and that a malicious entity is not trying to impersonate the server,
you must add self-signed certificates to the JVM for the Case configuration tool. These certificates are required for https
connections.

```
javax.net.ssl.SSLHandshakeException: com.ibm.jsse2.util.j:
      PKIX path building failed:
    java.security.cert.CertPathBuilderException:
```

Because http connections are not encrypted, you do not need to add keys for certification
authority (CA) certificates that use an http connection.

## Resolving the problem

You might need to add certificates for the Content Platform Engine load balancer or server and the IBM® Content
Navigator load balancer or server. Before you
begin, ensure that Content Platform Engine and IBM Content
Navigator are already configured for SSL or TLS.

1 For each certificate that you need to add to the keystore, obtain the certificate from theserver to which the Case configuration tool is connecting.
    1. On the Content Platform Engine server, log in to the WebSphere Integrated Solutions Console.
    2. Click Security > SSL certificates and key management.
    3. Open the Signer Certificates page: 

Option
Description

WebSphere Application Server cluster configuration
Click Key stores and certificates > CellDefaultTrustStore > Signer certificates.

WebSphere stand-alone configuration
Click Key stores and certificates > NodeDefaultTrustStore > Signer certificates.
    4. Under Additional Properties, select Signer
certificates.
    5. Select the check box next to the certificate to export and click
Extract.
    6. Enter a name and the location where the extracted certificate file is to be stored, and then
click OK.
2 Add each certificate to the keystore for the Case configuration tool .

1. Start IBM Key Management by entering one of the following commands from the command line: 

Option
Description

AIX®, HPUX, HPUXi, Linux, Linux on System z®, Solaris
install\_root/java/sdk/jre/bin/ikeyman.sh

Windows
install\_root\java\sdk\jre\bin\ikeyman.bat
2. Click Keybase File > Open.
3. For the Key database type, select JKS.
4. Click Browse and navigate to
install\_root/java/sdk/jre/lib/security/cacerts.
5. Click OK.
6. Enter the password and click OK. The default password is
changeit.
7. Add the certificates that you exported in step 1 to the trust file for Case configuration tool .
8. Close IBM Key Management.