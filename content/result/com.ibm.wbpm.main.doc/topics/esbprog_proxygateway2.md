<!-- image -->

# Virtual services

## Network addressable endpoints for virtual services

```
http://localhost:9080/proxyGateway/sca/ProxyGatewayExport/VirtualServiceA
http://localhost:9080/proxyGateway/sca/ProxyGatewayExport/VirtualServiceB
...
```

The proxy gateway web service endpoint accepts messages based on a URL pattern instead of the
typical single URL pattern of a normal web service export.

```
http://localhost:9080/proxyGateway/sca/ProxyGatewayExport
```

```
http://localhost:9080/proxyGateway/sca/ProxyGatewayExport/*
```

## Virtual service WSDL generation

To create a web service client, you would normally retrieve the WSDL file for the service
provider, and pass it into the web service tool to generate a client stub. It might be difficult to
retrieve the WSDL from a service gateway because the WSDL that the client uses is a combination of
the WSDL for the gateway and the WSDL for the target service provider. For a dynamic or static
service gateway the creation of this WSDL file is a manual process: you must download the target
service provider WSDL, replace any policy information with the WSDL attached to the service gateway
export and then override the endpoint to that of the service gateway. This lets the service consumer
know that a service gateway is being used, and because a manual process was used to edit it, there
is a chance that mistakes have been made when it was edited.

```
<NORMAL-EXPORT-URL>/<VIRTUAL-SERVICE-NAME>?wsdl
```

```
http://localhost:9080/proxyGateway/sca/ProxyGatewayExport/VirtualServiceA?wsdl
```

## Virtual service endpoint resolution

Since the gateway is a proxy for multiple service providers, it is necessary to be able to
determine the type of message the gateway has received, and resolve this to a network addressable
endpoint. The proxy gateway handles this automatically using the dedicated URL and the information
in the built-in configuration store. The virtual service name is extracted ffrom the URL pattern and
passed to the built-in configuration store to resolve it to a network addressable endpoint.