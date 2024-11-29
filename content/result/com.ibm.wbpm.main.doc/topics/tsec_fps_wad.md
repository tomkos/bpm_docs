# Configuring Microsoft Active Directory Server user registry
for IBM® Process Federation
Server

## Procedure

1. Add the ldapRegistry-3.0 feature
to the featureManager section:
<!-- Enable features -->
<featureManager>
    <feature>ldapRegistry-3.0</feature>
</featureManager>
2. Specify the configuration information for Microsoft Active
Directory Server in the server.xml file.
The following code snippet is an example of an Microsoft Active Directory Server entry in the
server.xml
file:<ldapRegistry id="ldap" realm="SampleLdapADRealm"
    host="ldapserver.mycity.mycompany.com" port="389" ignoreCase="true"
    baseDN="cn=users,dc=adtest,dc=mycity,dc=mycompany,dc=com"
    bindDN="cn=testuser,cn=users,dc=adtest,dc=mycity,dc=mycompany,dc=com"
    bindPassword="testuserpwd"
    ldapType="Microsoft Active Directory"
    sslEnabled="true"
    sslRef="LDAPSSLSettings">
    <activedFilters
    userFilter="(&amp;(sAMAccountName=%v)(objectcategory=user))"
groupFilter="(&amp;(cn=%v)(objectcategory=group))"
   userIdMap="user:sAMAccountName"
    groupIdMap="*:cn"
    groupMemberIdMap="memberOf:member" >
</activedFilters>
    </ldapRegistry>

<ssl id="LDAPSSLSettings" keyStoreRef="LDAPKeyStore" trustStoreRef="LDAPTrustStore" />

<keyStore id="LDAPKeyStore" location="${server.config.dir}/LdapSSLKeyStore.jks"
          type="JKS" password="{xor}CDo9Hgw=" />
<keyStore id="LDAPTrustStore" location="${server.config.dir}/LdapSSLTrustStore.jks"
          type="JKS" password="{xor}CDo9Hgw=" />
3 Specify the configuration information for the federatedenvironment. Add a federatedRepository elementand specify values for the relevant configuration properties. The following code snippet is an example of a federatedRepository elementin the server.xml file:<federatedRepository> <primaryRealm name="ldap\_realm "> <participatingBaseEntry name="LDAP1\_BASE\_DN "/> <participatingBaseEntry name="LDAP2\_BASE\_DN "/> <uniqueGroupIdMapping inputProperty="uniqueName " outputProperty="uniqueName "/> </primaryRealm></federatedRepository> Note:

```
<federatedRepository>
   <primaryRealm name="ldap\_realm">
      <participatingBaseEntry name="LDAP1\_BASE\_DN"/>
      <participatingBaseEntry name="LDAP2\_BASE\_DN"/>
      <uniqueGroupIdMapping inputProperty="uniqueName" outputProperty="uniqueName"/>
   </primaryRealm>
</federatedRepository>
```

    - The name attribute of the participatingBaseEntry element
must be the same as the value of baseDN attribute
that is specified in the ldapRegistry element.

## What to do next