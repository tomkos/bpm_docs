# Configuring a custom user registry for IBM® Process Federation
Server

## Before you begin

```
uid=%user security name%, %base dn%
```

## Procedure

1. Convert the implementation class for your custom user registry to an OSGi
service. For more information, see Developing a custom user registry for the Liberty profile.
2. Package the custom user registry as an OSGi bundle and
export the UserRegistry service. For more information,
see Creating a service bundle.
3. Create a feature manifest file to include the OSGi bundle.
4. Install the feature on Process Federation Server.
5. Enable the feature on the server by adding the feature
name to the server.xml file. For
example, if your feature is called usr:customRegistrySample-1.0, the server.xml file
contains the following entry:<featureManager>
   ...
   <feature>usr:customRegistrySample-1.0</feature>
</featureManager>