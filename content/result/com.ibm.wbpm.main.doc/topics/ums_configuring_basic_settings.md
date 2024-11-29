# Specifying basic User Management Service configuration
settings

## Provide server configuration settings in the server.xml file

IBM®
WebSphere® Application Server Liberty servers
have a very flexible and dynamic configuration model. You can provide
all server configuration information in the server's server.xml file,
for example, C:\ums\wlp\usr\servers\serverName\server.xml,
where serverName is the name of the server.

```
<!-- configure variable values in configDropins/overrides/umsVariables.xml -->
```

This ssl\_keystore\_password
variable is used in SSL configuration in server.xml. If you do not want to use the default SSL
specification you must perform the configration by using the liberty server.xml. You can replace
this configuration in server.xml with your own SSL settings.

For more information about the
Liberty keystore, see keyStore - Keystore (keyStore).

```
<server>

    <variable name="hostname" value="localhost" />
    <variable name="http\_port" value="-1" />
    <variable name="https\_port" value="9443" />
    <variable name="external\_hostname" value="${hostname}" />

    <variable name="admin.user" value="adminUser" />
    <variable name="admin.password" value="password" />

    <variable name="ssl\_keystore\_password" value="keystorePassword" />

    <variable name="oidc.jwt.keystore.location" value="resources/security/key.p12" /> 
    <variable name="oidc.jwt.keystore.password" value="${ssl\_keystore\_password}" /> 
    <variable name="oidc.jwt.keystore.type" value="PKCS12" /> 
    <variable name="oidc.jwt.keyAliasName" value="default" />
 
    <variable name="db.type" value="derby" />

    <variable name="oauth.datasource.id" value="${db.type}OAuthDataSource" />
    <variable name="oauth.db.name" value="" />
    <variable name="oauth.db.hostname" value="" />
    <variable name="oauth.db.port" value="1521" />
    <variable name="oauth.db.user" value="" />
    <variable name="oauth.db.password" value="" />

</server>
```

```
<server>

    <variable name="hostname" value="localhost" />
    <variable name="http\_port" value="-1" />
    <variable name="https\_port" value="9443" />
    <variable name="external\_hostname" value="mypublicaddress.example.com" />
    <variable name="admin.user" value="adminUser" />
    <variable name="admin.password" value="password" />

    <variable name="ssl\_keystore\_password" value="keystorePassword" />
    
    <variable name="oidc.jwt.keystore.location" value="resources/security/jwtkey.p12" /> 
    <variable name="oidc.jwt.keystore.password" value="jktKeystorePassword" /> 
    <variable name="oidc.jwt.keystore.type" value="PKCS12" /> 
    <variable name="oidc.jwt.keyAliasName" value="default" />
 
    <variable name="db.type" value="oracle" />

    <variable name="oauth.datasource.id" value="${db.type}OAuthDataSource" />
    <variable name="oauth.db.name" value="ORCL" />
    <variable name="oauth.db.hostname" value="oracleserver.example.com" />
    <variable name="oauth.db.port" value="1521" />
    <variable name="oauth.db.user" value="UMSORCL" />
    <variable name="oauth.db.password" value="UMSORCLPassword" />

</server>
```

## Verify the basic configuration of the User Management
Server

```
server start serverName
```

```
server status serverName
```

```
server stop serverName
```

Next, perform Connecting a user registry.