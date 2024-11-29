# Configuring CORS for an external identity provider

## About this task

## Procedure

1. Create an xml snippet, such as
z\_Navigator.xml, in the configuration overrides directory
for Business Automation Navigator. For example:
/opt/ibm/wlp/usr/servers/defaultServer/configDropins/overrides/z\_Navigator.xml.
2 Configure a CORS settings for the endpoint(s) of the external identity provider in the new.xml file. For example:<server> <cors domain="/" allowedOrigins="xxxxx " allowedMethods="GET, DELETE, POST, HEAD, PUT, PATCH, OPTIONS" allowedHeaders="xxxxx " allowCredentials="true" maxAge="3600" /></server> where xxxxx is a list of the external identity providerendpoints. For more information, see:

```
<server>
  <cors
    domain="/"
    allowedOrigins="xxxxx"
    allowedMethods="GET, DELETE, POST, HEAD, PUT, PATCH, OPTIONS"
    allowedHeaders="xxxxx"
    allowCredentials="true"
    maxAge="3600" />
</server>
```

    - Configuring Cross Origin Resource Sharing on a Liberty
server
    - Cross-Origin Resource Sharing (cors)