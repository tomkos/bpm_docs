<!-- image -->

# Dynamic endpoint example URIs

## SOAP/HTTP

```
http://host:port/moduleName/sca/exportName
```

```
http://host:port/service
```

## SOAP/JMS

```
The URI format in the case of an export with a web service binding, is as follows: 
jms:/queue?destination=jms/WSjmsExport&connectionFactory=jms/WSjmsExportQCF&targetService=WS
```

```
jms:/queue?destination=<destName>&connectionFactory=<factory>&targetservice=<service>
```

## SCA default binding example

```
sca://moduleName/exportName
```