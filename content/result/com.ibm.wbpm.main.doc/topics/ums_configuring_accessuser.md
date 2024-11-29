# Configuring access to user and group information (SCIM)

If you created your server configuration by using the ibmUserManagement:ibmUserManagement
template, the administrator role is already defined and the user specified
in the wlp/usr/servers/server\_name/configDropins/overrides/umsVariables.xml file
is assigned to that role. If you are upgrading from an earlier version
of the User Management Service,
you must add the administrator role to your User Management Service server configuration
as described in Creating a User Management Service server instance. In
both cases, you can create and add users to the administrator role,
for example, if you want fine-grained authorization control for the
OAuth 2.0, OpenID Connect, and SCIM features.

```
https://umshost:port/ibm/api/scim/Users/{id}
```

```
"name": {
        "formatted": "John Doe",
        "givenName": "John",
        "familyName": "Doe"
}
```

```
"name": {
        "formatted": "John Doe Doe",
        "givenName": "John Doe",
        "familyName": "Doe"
}
```

```
<attributeConfiguration> 
         <attribute name="givenName" propertyName="cn" syntax="String" entityType="PersonAccount" />
</attributeConfiguration>
```