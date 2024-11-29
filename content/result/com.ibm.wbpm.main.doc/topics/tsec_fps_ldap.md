# Configuring LDAP user registries for Process Federation Server

## About this task

```
[ERROR   ] CWWKS3006E: A configuration exception has occurred. There are multiple available UserRegistry implementation services; the system cannot determine which to use.
```

```
[ERROR   ] CWIML4538E: The user registry operation could not be completed. More than one record exists for the u1 principal name in the configured user registries. The principal name must be unique across all the user registries.
[AUDIT   ] CWWKS1100A: Authentication did not succeed for user ID u1. An invalid user ID or password was specified.
```

## Procedure

To set up the user registry, add the ldapRegistry-3.0 feature
to the server.xml configuration file and specify
the configuration information for connecting to the LDAP server.

1. Open the server.xml configuration file for
editing.
By default, the configuration file is in the
pfs\_install\_root/usr/servers/server\_name directory on
Process Federation Server.
2. Add the ldapRegistry-3.0 feature
to the featureManager section:
<!-- Enable features -->
<featureManager>
    <feature>ldapRegistry-3.0</feature>
</featureManager>
3. Specify the configuration information for the LDAP server.
Add an ldapRegistry element for each LDAP server
in the federated environment and specify values for the relevant configuration
properties. The following code snippet is an example
of an LDAP server element in the server.xml file.
The entries in the Filters section depend on the
type of LDAP server that you are using.<ldapRegistry 
     baseDN="LDAP1\_BASE\_DN,o=mycompany,c=us" 
     ldapType="ldap\_server\_type"
     port="ldap\_port" host="ldapserver.mycity.mycompany.com" 
     id="ldap\_ID" realm="ldap\_realm">
     <ldap\_server\_typeFilters 
          userIdMap="*:uid"
          groupIdMap="*:cn"
          userFilter="(&amp;(uid=%v)(objectclass=ePerson))"
          groupFilter="(&amp;(cn=%v)(|(objectclass=groupOfNames)(objectclass=groupOfUniqueNames)(objectclass=groupOfURLs)))"
          groupMemberIdMap="mycompany-allGroups:member;mycompany-allGroups:uniqueMember;groupOfNames:member;groupOfUniqueNames:uniqueMember";
     />
</ldapRegistry>
If you have multiple LDAP servers
in your federated environment, add a federatedRepository section
with an allowOpIfRepoDown property to ensure
that Process Federation Server can
still authenticate users if one of the LDAP servers goes down. <federatedRepository>
   <primaryRealm name="LdapRegistry" allowOpIfRepoDown="true"> 
      <participatingBaseEntry name="IBM\_TDS\_BASE\_DN"/>
      <uniqueGroupIdMapping inputProperty="uniqueName" outputProperty="uniqueName"/> 
   </primaryRealm>
</federatedRepository>

## What to do next

- Configuring IBM Security Directory Suite user registry for IBM Process Federation Server

You can configure IBM Security Directory Suite user registry on Process Federation Server for user authentication.
- Configuring Microsoft Active Directory Server user registry for IBM Process Federation Server

You can configure Microsoft Active Server user registry on Process Federation Server for user authentication.