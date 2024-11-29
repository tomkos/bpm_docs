<!-- image -->

# modifySCAImportHttpBinding command

- If a parameter is changed at the binding scope, the syntax should be:
<bindingName>newValue</bindingName>
- If a parameter is changed at the method scope, the syntax should be:
<methodName>newValue</methodName>

- A resource of an invalid type is specified.
- A resource is specified that does not exist.

## Location

Start the wsadmin scripting client from the install\_root/profiles/deployment\_manager\_profile/bin directory.

## Syntax

```
modifySCAImportHttpBinding
-moduleName moduleName
-import import\_name
[-applicationName applicationName]
[-endpointURL endpointURL]
[-endpointHttpMethod methodName]
[-endpointHttpVersion version]
[-authAlias authenticationAlias]
[-sslConfiguration configuration]
[-transferEncoding transferEncoding]
[-contentEncoding contentEncoding]
[-httpProxyHost hostName]
[-httpProxyPort portTitle]
[-httpNonProxyHosts hostTitle]
[-httpProxyCredential-AuthAlias aliasName]
[-httpsProxyHost hostName]
[-httpsProxyPort portTitle]
[-httpsNonProxyHosts hostTitle]
[-httpsProxyCredential-AuthAlias aliasName]
[-responseReadTimeout timeout]
[-connectionRetries connectionRetries]
```

## Required parameters

## Optional parameters

## Examples

The following example uses the modifySCAImportHttpBinding command to change
the number of connection retries of an HTTP import binding called Import1 in a module called MyMod
to 3.

```
AdminTask.modifySCAImportHttpBinding('[-moduleName MyMod 
-import Import1 -connectionRetries <Import1>3</Import1>]')
```

The following example uses tge modifySCAImportHttpBinding command to change
the number of connection retries of an HTTP import binding called Import1 in a module called MyMod
to 3.

```
AdminTask.modifySCAImportHttpBinding('[-moduleName MyMod 
-import Import1 -connectionRetries <method1>3</method1>]')
```