# Case configuration tool returns a
java.security.cert.CertificationException error

## Symptoms

When the Case configuration tool connects to a server
through an SSL or TLS connection, the server certificate is verified. The server certificate must be
issued by a trusted signer (signer must be in the truststore used by the Case configuration tool) for the host name that is used to connect to
the server.

If the certificate was not issued for the host name used in the connection attempt, upon
connection Case configuration tool might return an error
similar to this: java.security.cert.CertificationException:No name matching <some
hostname>.

Note that the host name is not necessarily the host name entered in the dialog, but may be the
result of a reverse lookup in DNS or the hosts file on the system that runs Case configuration tool.

## Resolving the problem

Ensure the certificate of the target server includes the host name that is used for the
connection attempt. The host name is part of the error message and might be retrieved from the hosts
file or a DNS reverse resolution on the system that runs  running Case configuration tool.

For web service connections, connect through a web server rather than accessing an individual
application server web container directly. Connecting through a web server ensures proper load
balancing and fail-over. Also, unlike the certificates used by individual application servers, the
SSL/TLS certificates used by a web server are often issued by a corporate certificate authority.

The certificate contains a "subject alternative name (SAN)" extension field that lists all the
host names and IP addresses for which the certificate can be used. By default, WebSphere-generated
certificates do not include the subject alternative name field, but instead specify a single valid
hostname in the "subject common name" field. If you must connect to the application server directly
and cannot use the host name specified in the certificate, you can use keytool that is shipped with
IBM SDK for Java to generate new certificates with subject alternative names.

- Default passwords are used for keystores and truststores.
- The Deployment Manager profile name is DmgrProfile.
- WebSphere is installed in /home/BPM/BPM8600.
- The WebSphere cell name is PSCell1.
- The WebSphere cell has a single node called Node1.
- Both deployment manager and Node1 are located on a host with the host name
some.host.name and IP address 10.1.2.3. Note that the value
of the SAN extension field is a comma-separated list of host names (prefixed by
dns:) and IP addresses (prefixed by ip:) that clients might use to
connect to the server. Multiple host names and IP addresses are allowed.
- Linux shell syntax is used for concatenating files. On Windows, use the copy
command with the /b parameter.

```
/home/BPM/BPM8600/java/jre/bin/keytool -certreq -alias default -storepass WebAS -keystore /home/BPM/BPM8600/profiles/DmgrProfile/config/cells/PSCell1/nodes/Node1/key.p12  -storetype PKCS12 > /home/BPM/temp/node1.csr

/home/BPM/BPM8600/java/jre/bin/keytool -certreq -alias default -storepass WebAS -keystore /home/BPM/BPM8600/profiles/DmgrProfile/config/cells/PSCell1/key.p12  -storetype PKCS12 > /home/BPM/temp/dmgr.csr

/home/BPM/BPM8600/java/jre/bin/keytool -gencert -alias root -keypass WebAS -storepass WebAS -storetype PKCS12 -keystore /home/BPM/BPM8600/profiles/DmgrProfile/config/cells/PSCell1/nodes/Dmgr/root-key.p12  -rfc -infile /home/BPM/temp/dmgr.csr -ext san=dns:some.host.name,ip:10.1.2.3 > /home/BPM/temp/dmgr.pem

/home/BPM/BPM8600/java/jre/bin/keytool -gencert -alias root -keypass WebAS -storepass WebAS -storetype PKCS12 -keystore /home/BPM/BPM8600/profiles/DmgrProfile/config/cells/PSCell1/nodes/Dmgr/root-key.p12  -rfc -infile /home/BPM/temp/node1.csr -ext san=dns:some.host.name,ip:10.1.2.3 > /home/BPM/temp/node1.pem

/home/BPM/BPM8600/java/jre/bin/keytool -exportcert -keystore /home/BPM/BPM8600/profiles/DmgrProfile/config/cells/PSCell1/trust.p12 -storetype PKCS12 -storepass WebAS -rfc -alias root > /home/BPM/temp/cell-signer.crt

cat  /home/BPM/temp/cell-signer.crt  /home/BPM/temp/dmgr.pem >>/home/BPM/temp/dmgrChain.pem
cat /home/BPM/temp/cell-signer.crt /home/BPM/temp/node1.pem >> /home/BPM/temp/node1Chain.pem
--copy /b /home/BPM/temp/cell-signer.crt+/home/BPM/temp/dmgr.pem /home/BPM/temp/dmgrChain.pem
--copy /b /home/BPM/temp/cell-signer.crt+/home/BPM/temp/node1.pem /home/BPM/temp/node1Chain.pem

/home/BPM/BPM8600/java/jre/bin/keytool -importcert -keystore /home/BPM/BPM8600/profiles/DmgrProfile/config/cells/PSCell1/nodes/Node1/key.p12 -storepass WebAS -storetype PKCS12 -alias default -file /home/BPM/temp/node1Chain.pem -noprompt

/home/BPM/BPM8600/java/jre/bin/keytool -importcert -keystore /home/BPM/BPM8600/profiles/DmgrProfile/config/cells/PSCell1/key.p12 -storepass WebAS -storetype PKCS12 -alias default -file /home/BPM/temp/dmgrChain.pem -noprompt
```

After regenerating certificates, a full resynchronization of the deployment manager and the
nodes is required. All the server JVMs (including deployment manager, node agents, and application
servers) must be restarted.