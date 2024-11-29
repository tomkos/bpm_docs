<!-- image -->

# modifySCAExportHttpBinding command

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
modifySCAExportHttpBinding
-moduleName moduleName
-export export\_name
[-applicationName applicationName]
[-httpMethods methodName]
[-transferEncoding transferEncoding]
[-contentEncoding contentEncoding]
```

## Required parameters

## Optional parameters

## Examples

The following example uses modifySCAExportHttpBinding to change the transfer
encoding of an HTTP export binding called Export1 in a module called MyMod to
identity. In addition, the command changes httpMethod to type
"GET", sets pingable to "true", and sets ReturnCode to
400.

```
AdminTask.modifySCAExportHttpBinding('[-moduleName MyMod 
-export Export1 -transferEncoding <Export1>identity</Export1>
-httpMethods [<Export1><httpMethod type="GET" pingable="true">
<PingableSettings><ReturnCode>400</ReturnCode></PingableSettings>
</httpMethod></Export1>]]')
```

The following example uses modifySCAExportHttpBinding to change the transfer
encoding of an HTTP export binding called Export1 in a module called MyMod to
identity. In addition, the command changes httpMethod to type
"GET", sets pingable to "true", and sets ReturnCode to
400.

```
AdminTask.modifySCAExportHttpBinding('[-moduleName MyMod 
-export Export1 -transferEncoding <method1>identity</method1>
-httpMethods [<method1><httpMethod type="GET" pingable="true">
<PingableSettings><ReturnCode>400</ReturnCode></PingableSettings>
</httpMethod></method1>]]')
```