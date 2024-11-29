# Configuring the user registry

## About this task

The default installation of IBM® Business Automation Workflow provides a federated
repository that contains the WebSphere® Application
Server file registry.

- You must search for users by the user ID in stand-alone LDAP user repositories (deprecated).
Searching for users by user first name or last name is not supported in this configuration.
- If you are using Active Directory as a user repository, and you search for a user name that
contains a letter with a diacritical mark, the search ignores the diacritical mark and returns all
user names that contain the character, regardless of whether the character has a diacritical mark.
For example, a search on user names that contain the letter e with an accent mark returns not
just those user names, but also user names that include e with any other accent mark or
e with no accent mark.

- The connection with an embedded Enterprise Content Management (ECM) system might be lost if
users are deleted and re-created. Refer to Administering the technical
user for the BPM document store.
- If you are using Active Directory as a user repository, and perform the step of changing the
mapping of the Federated Repository uid property to use the user repository
userPrincipalName attribute instead of the default samAccountName
attribute, you must set the following JVM
argument.-Dcom.filenet.security.vmmProvider.upnAsUserShortName=true For more
information, see Configuring the JVM.

## Procedure

1. Log in to the WebSphere Application
Server administrative
console.
2. Click Security > Global
security.
3. Under User account repository, select Federated
repositories from the list of Available realm
definitions.
4. Click Configure.
5. Under Related items, click Manage
repositories.
6. Click Add >  LDAP
Repository and specify parameters for the provider that you want to add.
For example, to add Microsoft Active Directory, specify
values such as the following examples: 
Table 1.  Parameters for adding a provider

Parameter
Example values

Repository identifier
SALOMLDAP // change to suit

Directory type
Microsoft Windows Active Directory

Primary host name
10.1.5.18

Bind distinguished name
cn=LDAP\_USER,CN=Users,DC=COMPANYQA,DC=com

Bind password
pwsaaswp
7. Click OK and then Save.
8. On the Federated repositories page, click Add
Base entry to Realm and specify values such as the following
examples: 
Table 2.  Parameters for adding a base
entry to a realm

Base entry name
Example values

Distinguished name of a base entry that uniquely
identifies this set of entries in the realm
cn=Users,DC=COMPANYQA,DC=com

Distinguished name of a base entry in this repository
cn=Users,DC=COMPANYQA,DC=com
9. Click OK and then Save.
If your external security provider (LDAP) contains many entries, you must increase the maximum
number of search results in federated repositories. A full synchronization queries all entries in
LDAP. This process is limited by the maximum search value in the wimconfig.xml.
In WebSphere Application Server, the default maximum search results are 4500 entries. This value is
not the maximum number of LDAP users or groups that WebSphere Application Server can handle; rather,
it is the maximum number that is returned based on the configuration value in the
wimconfig.xml file. Check the SystemOut.log file for the
CWWIM1018E error code. If you have this issue, you can increase the maximum search results in the
wimconfig.xml file as described in the MaxResultsExceededException occurs during LDAP repository search topic in
the WebSphere Application Server Information Center. After the change, restart the Business Automation Workflow servers, then complete a
full synchronization.
10. On the Global Security page, click Set as current and
then click Apply.
11. Shut down all Business Automation Workflow servers.
For a network deployment environment, you must shut down all
of the servers, node agents, and deployment manager.
12. Make sure that no duplicate users exist in the WebSphere Application
Server file registry and the
security provider that you just added. If duplicate users exist, errors occur when you run IBM Business Automation Workflow product
components.
13. Although you do not necessarily need to set any Virtual Member Manager (VMM) properties, you
can use the 100Custom.xml file to set one or more of the VMM properties in the
following table (if the properties are applicable to your environment).  Business Automation Workflow interacts with IBM
WebSphere Application Server level APIs referred to as Virtual Member Manager (VMM), which expose
access to user, group and membership data. The following settings allow you to fine-tune which of
the VMM properties should be used for what purpose, for example which property holds the user's
displayname. They also allow enabling optional post processing of data that is
obtained from these fields, in case your underlying user registry exposed data in unusual formats.
The default settings work in most environments. Modify any of these settings only if you are not
satisfied with, for example - display names for end users or you were told by support to enable
post-processing for unusual data format.

Table 3. IBM Business Automation Workflow VMM
properties

Property
100Custom.xml structure
Description

user-full-name-prop

<common merge="mergeChildren">
 <security>
  <vmm-options>
   <user-full-name-prop>cn
   </user-full-name-prop>
  </vmm-options>
 </security>
</common>

The LDAP displayname attribute is no longer automatically retrieved for use
as the fullName by IBM Business Automation Workflow. A user's full name is
now derived from the LDAP cn attribute. However, if you still want to derive a
user's full name from the displayname attribute, you can use the
user-full-name-prop property.
The default value for this property is cn. For more information about this
property, see the topic Retrieving a user's full name in an easier-to-read format.

user-email-prop

<common merge="mergeChildren">
  <security>
    <vmm-options>
      <user-email-prop>mail</user-email-prop>
    </vmm-options>
  </security>
</common>

Specifies the name of the property in federated repositories that is considered the email of a
user. This property can be mapped to an attribute with different names in multiple connected
repositories. 
The default value for this property is mail. 

user-phone-prop

<common merge="mergeChildren">
  <security>
    <vmm-options>
      <user-phone-prop>telephoneNumber</user-phone-prop>
    </vmm-options>
  </security>
</common>

Specifies the name of the property in federated repositories that is considered the phone number
of a user. This property can be mapped to an attribute with different names in multiple connected
repositories. 
The default value for this property is telephoneNumber. 

normalize-whitespaces-for-distinguished-names-prop

<common merge="mergeChildren">
 <security>
  <vmm-options>
   <normalize-whitespaces-for-distinguished-names-prop>true
   </normalize-whitespaces-for-distinguished-names-prop>
  </vmm-options>
 </security>
</common>

Enables or disables the action of detecting and removing white spaces in distinguished names
in a VMM LDAP repository.The default value for this property is true. For
more information about this property, see the topic Configuring IBM Business Automation Workflow to handle white space and letter case variations in the LDAP server

normalize-case-for-distinguished-names-prop

<common merge="mergeChildren">
 <security>
  <vmm-options>
   <normalize-case-for-distinguished-names-prop>INSQL
   </normalize-case-for-distinguished-names-prop>
  </vmm-options>
 </security>
</common>

Enables or disables the action of normalizing capitalization in distinguished names in a
Virtual VMM LDAP repository.The default value for this property is INSQL.
For more information about this property, see the topic Configuring IBM Business Automation Workflow to handle white space and letter case variations in the LDAP server

group-user-member-prop

<common merge="mergeChildren">
 <security>
  <vmm-options>
   <group-user-member-prop>groupusermember
   </group-user-member-prop>
  </vmm-options>
 </security>
</common>

Configures IBM Business Automation Workflow and VMM by using a group membership property that reflects all users in a
group.There is no default value for this property. For more information about this property, see
the topic Configuring IBM Business Automation Workflow and VMM by using a group membership property that reflects all users in a group.

group-member-prop

<common merge="mergeChildren">
 <security>
  <vmm-options>
   <group-member-prop>groupmember
   </group-member-prop>
  </vmm-options>
 </security>
</common>

Configures IBM Business Automation Workflow and VMM by using a group membership property that reflects direct users in
a group. 
There is no default value for this property. For more information about this property, see the
topic Configuring IBM Business Automation Workflow and VMM by using a group membership property that reflects direct users in a group.

group-name-prop

<common merge="mergeChildren">
 <security>
  <vmm-options>
   <group-name-prop>cn
   </group-name-prop>
  </vmm-options>
 </security>
</common>

Specifies the name of the property in federated repositories that is considered the group
name. This property can be mapped to an attribute with different names in multiple connected
repositories. The default value for this property is cn.

user-id-prop

<common merge="mergeChildren">
 <security>
  <vmm-options>
   <user-id-prop>principalName
   </user-id-prop>
  </vmm-options>
 </security>
</common>

Specifies the name of the property in federated repositories that is considered the user ID.
The default value for this property is principalName. The default value
automatically maps to the first login property in each of the federated repositories. This is the
correct value, but the value is still configurable for compatibility with an earlier
version.

threshold-for-existing-user-retrieval-mode

<common merge="mergeChildren">
 <security>
  <vmm-options>
   <threshold-for-existing-user-retrieval-mode>1000
   </threshold-for-existing-user-retrieval-mode>
  </vmm-options>
 </security>
</common>

Determines whether calls to VMM are done for each user or as one call for all users.The
default value for this property is 1000, which indicates 1000 available
users. For more information about this property, see the topic Synchronizing users.

Additional information about LDAP properties is found in the topic Security configuration properties. For information about the attributes in the user registry that
are replicated and the elements of the registry that must be unique and stable, see the topic Synchronizing users and groups.
14 Start all Business Automation Workflow servers. For a network deployment environment, you must restart all of the servers, node agents, anddeployment manager.If you have configured a server cluster for yourruntime environment, stop and restart all servers in the cluster. Note: Make sure especially when federating user registries that group short names are unique across alluser registries. A user registry might contain multiple groups with the same short name. This canhappen especially when multiple user registries (such as multiple LDAP servers or multiple branchesin the same LDAP server) are federated.For example, you might have two LDAP groups. Both are represented by their short name "contractors". Such groups cannot be used withthe product it requires group short names to be unique. Therefore, the group will not be importedinto the product database and permissions (or team memberships) related to these groups will notwork. There is a way to reconfigure the mapping between federated repositories and userregistry so that access to group names via the UserRegistry interface can access a different LDAPattribute. This is available in the WebSphere administrative console at Global security > Federatedrepositories > User repository attribute mapping (see WebSphere Application Server8.5.5.x) . This reconfiguration causes inconsistencies as access to group names via theFederated Repositories interface continues to read its default attributes. The only supportedconfiguration is unique short names and working with short names as group names. If you have aunique attribute for your group entity in LDAP, you can map that as short name to federatedrepositories property "cn" as described in Manually configuring a LightweightDirectory Access Protocol repository in a federated repositoryconfiguration

If you have configured a server cluster for your
runtime environment, stop and restart all servers in the cluster.

For example, you might have two LDAP groups.

    - cn=contractors,ou=services,ou=Groups,dc=example,dc=local
    - cn=contractors,ou=engineering,ou=Groups,dc=example,dc=local

Both are represented by their short name "contractors".

Such groups cannot be used with
the product it requires group short names to be unique. Therefore, the group will not be imported
into the product database and permissions (or team memberships) related to these groups will not
work.

There is a way to reconfigure the mapping between federated repositories and user
registry so that access to group names via the UserRegistry interface can access a different LDAP
attribute. This is available in the WebSphere administrative console at Global security > Federated
repositories > User repository attribute mapping (see WebSphere Application Server
8.5.5.x). This reconfiguration causes inconsistencies as access to group names via the
Federated Repositories interface continues to read its default attributes.

The only supported
configuration is unique short names and working with short names as group names.

If you have a
unique attribute for your group entity in LDAP, you can map that as short name to federated
repositories property "cn" as described in Manually configuring a Lightweight
Directory Access Protocol repository in a federated repository
configuration