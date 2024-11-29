# Securing communications between Process Federation Server and
LDAP

## About this task

To manage the LDAP truststore, use your JVM’s
keytool utility, or the IBM HTTP Server IKEYMAN utility.

## Procedure

1. Create a new truststore or reuse the Process Federation Server default
truststore and import the signer certificate for the LDAP server.
2 Enable communication with an SSL-enabled LDAP server:
    1. Open the server.xml configuration file for
editing.
By default, the configuration file is in the
pfs\_install\_root/usr/servers/server\_name directory on
Process Federation Server.
    2. Configure the keystore and ssl elements
to refer to the truststore: <ssl id="LDAPSSLSettings" keyStoreRef="defaultKeyStore" trustStoreRef="LDAPTrustStore" />

...
<keyStore id="LDAPTrustStore" 
  location="pfs\_install\_root/usr/servers/server\_name/LdapSSLKeyStore.jks"
          type="JKS" 
  password="password" />
    3. Enable SSL on the ldapRegistry element,
and refer to the ssl configuration element:
<ldapRegistry ...
              ...
              sslEnabled="true" 
              sslRef="LDAPSSLSettings">
              ... 
  <ldapRegistry/>