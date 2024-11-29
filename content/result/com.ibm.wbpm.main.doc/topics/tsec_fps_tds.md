# Configuring IBM Security Directory
Suite user
registry for IBM Process Federation
Server

## Before you begin

## Procedure

1. Add the ldapRegistry-3.0 feature
to the featureManager section:
<!-- Enable features -->
<featureManager>
    <feature>ldapRegistry-3.0</feature>
</featureManager>
2. Specify the configuration information for IBM Security Directory
Suite in
the server.xml file.  The following
code snippet is an example of an IBM Security Directory
Suite entry
in the server.xml file: <ldapRegistry
     baseDN="LDAP1\_BASE\_DN,o=mycompany,c=us" 
     ldapType="IBM Security Directory Suite"
     port="ldap\_port" host="ldapserver.mycity.mycompany.com" id="ldap\_ID" 
     realm="ldap\_realm"
<ldapRegistry/>For more information about the configuration
properties that you can set for the IBM Security Directory
Suite,
see Configuring LDAP user registries in Liberty.
3 Specify the configuration information for the federatedenvironment. Add a federatedRepository elementand specify values for the relevant configuration properties. The following code snippet is an example of a federatedRepository elementin the server.xml file:<federatedRepository> <primaryRealm name="ldap\_realm "> <participatingBaseEntry name="LDAP1\_BASE\_DN "/> <participatingBaseEntry name="LDAP2\_BASE\_DN "/> <uniqueGroupIdMapping inputProperty="uniqueName " outputProperty="uniqueName "/> </primaryRealm></federatedRepository> Note: For more information about the configuration propertiesthat you can set for the federated repository, see Configuring LDAP user registries in Liberty .

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