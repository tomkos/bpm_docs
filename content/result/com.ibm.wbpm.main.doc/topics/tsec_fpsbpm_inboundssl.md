# Securing inbound communications to Process Federation Server

## About this task

Inbound communication with Process Federation Server is
secured with Secured Sockets Layer (SSL) protocol. The web endpoints
that are made available in Process Federation Server,
for example, the Process Federation Server REST
services are configured to use SSL only.

The server.xml that
is provided as a template includes a default SSL configuration, and
a default keystore. When Process Federation Server starts
for the first time, it creates a JKS keystore and a self-signed certificate
in the keystore. Clients must be configured to trust the Process Federation Server certificate
signer.

In a production environment, replace the Process Federation Server default
self-signed certificate with a properly chained certificate that is
signed by a trusted certificate authority (CA). CA certificates are
more secure than the default certificate and they simplify configuration
because you can configure all clients to trust a common signer certificate.
In many cases, browsers will already trust the CA signer certificate,
which means that no additional certificate configuration is required
for browser clients to connect to Process Federation Server.
To manage the Process Federation Server keystore
and certificates, use your JVM’s keytool utility, or the IBM
HTTP Server IKEYMAN utility.

## Procedure

Because the Process Federation Server web
endpoints redirect HTTP request to HTTPS, you can disable HTTP access.
You can then enable and configure the Secure Sockets Layer (SSL) protocol
in the server.xml file.

1 Disable HTTP access to Process Federation Server .
    1. Open the server.xml configuration file for
editing.
By default, the configuration file is in the
pfs\_install\_root/usr/servers/server\_name directory on
Process Federation Server.
    2. In the httpEndpoint element, set the
value of the httpPort property to -1 and
ensure that an HTTPS port is configured.
2 Enable the SSL protocol on inbound communicationwith Process Federation Server inthe server.xml file. SSL communicationrequires the ssl-1.0 feature to be enabled. Thisfeature is automatically enabled with the ibmPfs:federationServer-1.0 feature.

1. If you don't use the ibmPfs:federationServer-1.0 feature,
add the ssl-1.0 feature to the featureManager section.
<featureManager>
   <feature>ssl-1.0</feature>
</featureManager>
2. Verify the SSL configuration entry:  <ssl id="defaultSSLConfig" keyStoreRef="defaultKeyStore" trustStoreRef="defaultTrustStore" sslProtocol="TLS"/>
If you have multiple SSL configurations in your server.xml file,
you must specify which configuration is the default one to be used
for inbound communications:<sslDefault sslRef="defaultSSLConfig"/>
3. Verify the keystore entry: <keyStore id="defaultKeyStore"  
          location="pfs\_install\_root/usr/servers/server\_name/resources/security/key.jks"
           password="password" />
Tip: Use the Liberty profile
security utility to encode passwords. 
If the key.jks file
does not exist, the server creates it when it starts. If the server
creates the keystore file, it also creates the certificate inside
it. The certificate is a self-signed certificate that is valid for
365 days. The CN value of the certificate's subjectDN parameter
is the host name of the computer where the server is running, and
the signature algorithm is SHA1withRSA.In
a production environment, ensure that the Process Federation Server certificate
is a properly chained certificate that is signed by a trusted certificate
authority (CA). To manage the Process Federation Server keystore
and certificates, use your JVM’s keytool utility, or the IBM
HTTP Server IKEYMAN utility.
4. Add the truststore entry: <keyStore id="defaultTrustStore"  
          location="pfs\_install\_root/usr/servers/server\_name/resources/security/key.jks"
           password="password" />
The truststore is not used for inbound
communications, but it is used for securing outbound communications.
3 Optional: Configure IBM HTTP Server for SSLand to trust the Process Federation Server signercertificate.

1. Configure IBM HTTP Server for SSL. See Securing with SSL communications.
2. Configure the IBM HTTP Server to trust the Process Federation Server signer
certificate, by importing the signer certificate into the IBM HTTP
Server truststore. For production environments, use a CA certificate.
See Storing a certificate authority certificate.