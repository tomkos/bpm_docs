<!-- image -->

# Transformation of people assignment criteria to people queries

If you use virtual member manager as the people directory, you
need to change the predefined mappings in the transformation XSL file
only if you define custom people assignment criteria.

A transformation (XSLT) file contains the instructions for translating
the people assignment criteria. Each people directory configuration
is associated with a transformation file to generate people queries
that are specific to a particular repository. Each query can be run
by the appropriate people directory provider to obtain a list of user
IDs. The predefined queries that are available to a people directory
provider correspond to the calls that can be run by the provider,
and are therefore fixed.

- LDAPTransformation.xsl for the LDAP people directory provider
- VMMTransformation.xsl for the virtual member manager people directory
provider
- UserRegistryTransformation.xsl for the user registry people directory
provider
- SystemTransformation.xsl and EverybodyTransformation.xsl for the
system people directory provider

- On Linux® and
UNIX platforms,
these files are in the install\_root/ProcessChoreographer/Staff
directory.
- On Windows platforms, these files are in the
install\_root\ProcessChoreographer\Staff directory.

## People queries for a specific
people directory provider

- Combine query results so that the user IDs returned by the individualqueries are added to the current result list of user IDs. For example,the LDAP people directory provider allows the following predefinedqueries:
    - The list of user IDs for the group members of a specified group:<sldap:usersOfGroup groupDN="cn=group1,dc=mycomp" recursive="yes">
...
</sldap:usersOfGroup>
    - The distinguished name (DN) of the specified user:<sldap:user dn="uid=user1,dc=mycomp" .../>
    - A complex query can be constructed for a list of user IDs for
the members of a specified group, and the DN of a specified user:<sldap:staffQueries>
     <sldap:usersOfGroup groupDN="cn=group1,dc=mycomp" recursive="yes">
    ...
    </sldap:usersOfGroup>
    <sldap:user dn="uid=user1,dc=mycomp" .../>
</sldap:staffQueries>
- Remove query results from the current result list. For example,
the following snippet shows how to remove "user1" from the list of
IDs retrieved for the specified group members:<sldap:staffQueries>
     <sldap:usersOfGroup groupDN="cn=group1,dc=mycomp" recursive="yes">
    ...
    </sldap:usersOfGroup>
    <sldap:remove value="user1"/>
</sldap:staffQueries>
- Use the query results obtained from one query to influence the
behavior of a subsequent query. For example, in the following snippet,
two queries are performed. First, the value of the "manager" attribute
in the LDAP entry for the user "uid=user1,…" is retrieved and saved
in an intermediate variable "supervisor". This variable is then used
to look up the manager's LDAP entry and retrieve the associated user
ID. <sldap:staffQueries>
       <sldap:intermediateResult name="supervisor">
         <sldap:user dn="uid=user1,dc=mycomp" attribute="manager" ... />
       </sldap:intermediateResult>
      <sldap:user dn="%supervisor% .../>
</sldap:staffQueries>