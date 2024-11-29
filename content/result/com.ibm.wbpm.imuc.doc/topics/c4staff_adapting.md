<!-- image -->

# Adapting the LDAP transformation file

- The LDAP object class for group entries is groupOfName.
- The group entry attribute that contains the member distinguished
names (DNs) for the group is member.
- The LDAP object class for person entries is inetOrgPerson.
- The attribute that contains the login ID in a person entry is uid.
- The person entry attribute that contains their email address is mail.
- The person entry attribute containing the distinguished name of
the manager of a person is manager.

If your LDAP schema uses name for object class and attribute names
that are different from those listed, you perform the following steps.

1 Make a copy of the standard transformation file for LDAP, andgive it another name, for example, myLDAPTransformation.xsl .The standard XSL transformation for LDAP is located in:
    - install\_root/ProcessChoreographer/Staff/LDAPTransformation.xsl.
    - install\_root\ProcessChoreographer\Staff\LDAPTransformation.xsl.
2. In the copy of the file, change the names of the object classes
and attributes to match the names used by your LDAP schema. For most
situations, you can change the settings for all people assignment
criteria by editing the variable declaration part of the file:  <xsl:variable name="DefaultGroupClass">groupOfNames</xsl:variable>
  <xsl:variable name="DefaultGroupClassMemberAttribute">member</xsl:variable>
  
  <xsl:variable name="DefaultPersonClass">inetOrgPerson</xsl:variable>
  <xsl:variable name="DefaultUserIDAttribute">uid</xsl:variable>
  <xsl:variable name="DefaultMailAttribute">mail</xsl:variable>  
  <xsl:variable name="DefaultManagerAttribute">manager</xsl:variable>
CAUTION: Do not modify the
original version of the standard transformation file because it might
be overwritten without warning when you apply a service pack or fix
pack.
You can apply changes within the XSL templates that
transform the individual staff assignment criteria, as illustrated
in the following examples.

## Example: GroupMembers

```
<sldap:usersOfGroup>
...

<sldap:attribute>
<xsl:attribute name="name">uniqueMember</xsl:attribute>
<xsl:attribute name="objectclass">groupOfUniqueNames</xsl:attribute>
<xsl:attribute name="usage">recursive</xsl:attribute>
</sldap:attribute> 

...
<sldap:attribute>
<xsl:attribute name="name">cn</xsl:attribute>
<xsl:attribute name="objectclass">inetOrgPerson</xsl:attribute>
<xsl:attribute name="usage">simple</xsl:attribute>
</sldap:attribute>
...
<sldap:resultObject>
<xsl:attribute name="objectclass">groupOfUniqueNames</xsl:attribute> 
<xsl:attribute name="usage">recursive</xsl:attribute> 
<sldap:resultAttribute>
<xsl:attribute name="name">uniqueMember</xsl:attribute> 
<xsl:attribute name="destination">intermediate</xsl:attribute>
</sldap:resultAttribute> 
</sldap:resultObject>

<sldap:resultObject>
<xsl:attribute name="objectclass"><xsl:value-of select="$DefaultPersonClass"/></xsl:attribute>
<xsl:attribute name="usage">simple</xsl:attribute>

<sldap:resultAttribute>
<xsl:attribute name="name">cn</xsl:attribute>
<xsl:attribute name="destination">userID</xsl:attribute>
</sldap:resultAttribute> 
<sldap:resultAttribute>
<xsl:attribute name="name"><xsl:value-of select="$DefaultMailAttribute"/></xsl:attribute>
<xsl:attribute name="destination">eMailAddress</xsl:attribute>
</sldap:resultAttribute> 
<sldap:resultAttribute>
<xsl:attribute name="name"><xsl:value-of select="$DefaultLocaleAttribute"/></xsl:attribute>
<xsl:attribute name="destination">preferredLocale</xsl:attribute>
</sldap:resultAttribute> 
</sldap:resultObject>

</sldap:usersOfGroup>
```

## Example: GroupMembersWithoutFilteredUsers

```
<sldap:StaffQueries>
<sldap:usersOfGroup>
...
</sldap:usersOfGroup>

<sldap:intermediateResult> 
<xsl:attribute name="name">filteredusers</xsl:attribute>
<sldap:search>
<xsl:attribute name="filter">
<xsl:value-of select="staff:parameter[@id='FilterAttribute']"/>
  >=
<xsl:value-of select="staff:parameter[@id='FilterValue']"/>
</xsl:attribute> 
...
<sldap:search>
...

</sldap:intermediateResult>
...
</sldap:StaffQueries>
```

## Example: GroupSearch

```
<sldap:StaffQueries>
...
<sldap:search>
<xsl:attribute name="filter">
(&
...
<xsl:if test="staff:parameter[@id='MyType']!="">
(<xsl:value-of select="$GS\_Type"/>=
<xsl:value-of select=staff:parameter[@id='Type']"/>)
</xsl:if>
)
...
</xsl:attribute>

<sldap:attribute> 
<xsl:attribute name="name">myuid</xsl:attribute>
<xsl:attribute name="objectclass">mypersonclass</xsl:attribute>
<xsl:attribute name="usage">simple</xsl:attribute>
</sldap:attribute> 
... 
<sldap:resultObject>
<xsl:attribute name="objectclass">mypersonclass</xsl:attribute>
<xsl:attribute name="usage">simple</xsl:attribute>

<sldap:resultAttribute>
<xsl:attribute name="name">myuid</xsl:attribute>
<xsl:attribute name="destination">userID</xsl:attribute>
</sldap:resultAttribute> 
<sldap:resultAttribute>
<xsl:attribute name="name"><xsl:value-of select="$DefaultMailAttribute"/></xsl:attribute>
<xsl:attribute name="destination">eMailAddress</xsl:attribute>
</sldap:resultAttribute> 
<sldap:resultAttribute>
<xsl:attribute name="name"><xsl:value-of select="$DefaultLocaleAttribute"/></xsl:attribute>
<xsl:attribute name="destination">preferredLocale</xsl:attribute>
</sldap:resultAttribute> 
</sldap:resultObject> 

<sldap:search>
</sldap:StaffQueries>
```

## Example: Manager of Employee

```
<sldap:StaffQueries>

<sldap:intermediateResult>
...
<sldap:user>
...
<xsl:attribute name="name">managerentry</xsl:attribute>
...
<sldap:resultObject>
<xsl:attribute name="objectclass"><xsl:value-of select="$DefaultPersonClass"/></xsl:attribute>
<xsl:attribute name="usage">simple</xsl:attribute>

<sldap:resultAttribute>
<xsl:attribute name="name">managerentry</xsl:attribute>
<xsl:attribute name="destination">intermediate</xsl:attribute>
</sldap:resultAttribute>
</sldap:resultObject> 
</sldap:user>
</sldap:intermediateResult>

<sldap:user>
...
<xsl:attribute name="name">name</xsl:attribute>
...
<sldap:resultObject>
<xsl:attribute name="objectclass"><xsl:value-of select="$DefaultPersonClass"/></xsl:attribute>
<xsl:attribute name="usage">simple</xsl:attribute>

<sldap:resultAttribute>
<xsl:attribute name="name">name</xsl:attribute>
<xsl:attribute name="destination">userID</xsl:attribute>
</sldap:resultAttribute> 
<sldap:resultAttribute>
<xsl:attribute name="name"><xsl:value-of select="$DefaultMailAttribute"/></xsl:attribute>
<xsl:attribute name="destination">eMailAddress</xsl:attribute>
</sldap:resultAttribute> 
<sldap:resultAttribute>
<xsl:attribute name="name"><xsl:value-of select="$DefaultLocaleAttribute"/></xsl:attribute>
<xsl:attribute name="destination">preferredLocale</xsl:attribute>
</sldap:resultAttribute> 
</sldap:resultObject> 

</sldap:user>
</sldap:StaffQueries>
```

## Example: PersonSearch

```
<sldap:StaffQueries>
...
<sldap:search>
<xsl:attribute name="filter">
(&
...
<xsl:if test="staff:parameter[@id='MyAttribute']!="">
(<xsl:value-of select="$PS\_UserID"/>=
<xsl:value-of select=staff:parameter[@id='UserID']"/>)
)
</xsl:if>
...
</xsl:attribute>

<sldap:attribute> 
<xsl:attribute name="name">myuid</xsl:attribute>
<xsl:attribute name="objectclass">mypersonclass</xsl:attribute>
<xsl:attribute name="usage">simple</xsl:attribute>
</sldap:attribute> 
...
<sldap:resultObject>
<xsl:attribute name="objectclass">mypersonclass</xsl:attribute>
<xsl:attribute name="usage">simple</xsl:attribute>

<sldap:resultAttribute>
<xsl:attribute name="name">myuid</xsl:attribute>
<xsl:attribute name="destination">userID</xsl:attribute>
</sldap:resultAttribute> 
<sldap:resultAttribute>
<xsl:attribute name="name"><xsl:value-of select="$DefaultMailAttribute"/></xsl:attribute>
<xsl:attribute name="destination">eMailAddress</xsl:attribute>
</sldap:resultAttribute> 
<sldap:resultAttribute>
<xsl:attribute name="name"><xsl:value-of select="$DefaultLocaleAttribute"/></xsl:attribute>
<xsl:attribute name="destination">preferredLocale</xsl:attribute>
</sldap:resultAttribute> 
</sldap:resultObject>
</sldap:search>
</sldap:StaffQueries>
```

## Example: Users

```
<sldap:user>
...
<xsl:attribute name="attribute">myuid</xsl:attribute>
<xsl:attribute name="objectclass">mypersonclass</xsl:attribute>

<sldap:resultObject>
<xsl:attribute name="objectclass">mypersonclass</xsl:attribute>
<xsl:attribute name="usage">simple</xsl:attribute>

<sldap:resultAttribute>
<xsl:attribute name="name">myuid</xsl:attribute>
<xsl:attribute name="destination">userID</xsl:attribute>
</sldap:resultAttribute> 
<sldap:resultAttribute>
<xsl:attribute name="name"><xsl:value-of select="$DefaultMailAttribute"/></xsl:attribute>
<xsl:attribute name="destination">eMailAddress</xsl:attribute>
</sldap:resultAttribute> 
<sldap:resultAttribute>
<xsl:attribute name="name"><xsl:value-of select="$DefaultLocaleAttribute"/></xsl:attribute>
<xsl:attribute name="destination">preferredLocale</xsl:attribute>
</sldap:resultAttribute> 
</sldap:resultObject> 

</sldap:user>
```