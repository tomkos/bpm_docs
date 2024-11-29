<!-- image -->

# Adding virtual services to proxy groups

## Before you begin

1. Use IBM Integration Designer to create a proxy gateway. Use the wizard to create a proxy gateway
module, which is an SCA module containing a Gateway Endpoint Lookup mediation primitive.
2. Deploy the proxy gateway module to Process Server.
3. Create a business space containing the Proxy Gateway widget.

## About this task

A proxy gateway is a module that receives web service requests and forwards them to an endpoint
defined in a proxy group. Proxy groups contain virtual services that you map to real service
endpoints. A virtual service can have one or more endpoints associated with it.

When you create your proxy gateway module, you define the proxy groups for the module. After you
deploy your proxy gateway module, you can use the Proxy Gateway widget to add virtual services to
the proxy groups. The virtual service information is stored in the built-in configuration store that
exists in Process Server.

When the proxy gateway processes a client request, the virtual service name used to look up the
endpoints must match the virtual service name in the client request. If you create a proxy gateway
module with the default type of routing, which is URL-based, and use the URL available in the
resolved WSDL, then the routing of the request occurs automatically. If you create a proxy gateway
module with XPath-based routing, ensure that the message location you specify contains the correct
virtual service name.

## Procedure

1. Log in to your business space and open the page that contains the Proxy
Gateway widget.
2. From the Proxy Gateway widget, select the Proxy
Group that you want to work with. 
Click the pencil icon at the end of the relevant row. 
The Proxy Gateway widget is refreshed. If the configuration store
contains virtual services for the proxy group, the virtual services are displayed. If a virtual
service is associated with more than one endpoint, only the first endpoint is displayed in the
table.
3 Add a virtual service.
    1. Enter the location of the WSDL that describes the virtual service. 
 The WSDL might be stored in WebSphere® Service
Registry and Repository (WSRR) or another repository. When the widget is refreshed, the service name
in the WSDL is used to populate the Virtual Service Name field.
    2 Click Add Service The Proxy Gateway widget is refreshed and shows the followinginformation: Note: If your WSDL document describes multiple WSDL services, the ProxyGateway widget imports the first WSDL service only.
        - Port Type: The WSDL portType of the virtual service.
        - Virtual Service Name: The name of the virtual service that is stored in
the configuration store. The default name is entered for you, and is based on the service name in
the WSDL you specified.
        - Virtual Service URLs :
            - Proxy Gateway: The name of the proxy gateway module.
            - Endpoint: The endpoint of the virtual service.
    - Enable Virtual Service: A check box that indicates whether you can send
messages to the virtual service. By default, virtual services are enabled.
    - Endpoint URLs: One or more network-addressable endpoints to which a
message can be forwarded. If you define a list of endpoints, you can determine the order in which
the services are tried. You determine the order by moving the endpoints up and down in the list.
    - Advanced Service Properties : If you need to do special processing, for aparticular virtual service, you might use the Advanced Service Properties . TheAdvanced Service Properties are key-value pairs that you want to be accessiblein the mediation flow, after the Gateway Endpoint Lookup mediation primitive. For example, you mightwant to specify the location of the XSL style sheet that relates to this virtual service. At runtime, the key-value pairs are stored in the EndpointLookupContext of the service message object (SMO).
        - Name: The name of the key.
        - Value: The value of the key.
4. Optional: 
Add another endpoint to the virtual service by clicking Add Endpoint.
5. Optional: 
Delete one of the endpoints defined for the virtual service by clicking the cross icon at the
end of the relevant row.
6. Save the endpoint information.

## Results

The new virtual service is added to the built-in configuration store, and the Proxy
Gateway widget is refreshed.

## What to do next

1. Retrieve the WSDL that your client uses to call a virtual service. You can obtain the WSDL by
entering the endpoint of the virtual service URL in a web browser, and appending the string:
?wsdl. For example, http://zzz/Gold?wsdl, where
http://zzz/ is the address of the proxy gateway and Gold is the
name of the virtual service. Note: The endpoint of the virtual service URL is specified in the
Endpoint field, under the Virtual Service URLs heading.
2. Use your client to access the proxy gateway. The proxy gateway routes your request to the real
service associated with the virtual service.