<!-- image -->

# Displaying proxy groups

## Before you begin

1. Use IBM Integration Designer to create a proxy gateway. Use the wizard to create a proxy gateway
module, which is an SCA module containing a Gateway Endpoint Lookup mediation primitive.
2. Deploy the proxy gateway module to Process Server.
3. Create a business space containing the Proxy Gateway widget.

## About this task

A proxy gateway is a module that receives web service requests and forwards them to an endpoint
defined in a proxy group. Proxy groups contain virtual services that you map to real
service endpoints. A virtual service can have one or more endpoints associated with it.

## Procedure

1. Log in to your business space and open the page that contains the Proxy
Gateway widget. 
The Proxy Gateway widget lists the proxy gateways and proxy groups
that are installed on your system.
2. From the Proxy Gateway widget, select the Proxy
Group whose details you want to display by clicking the pencil icon. 
The Proxy Gateway widget is refreshed.

## Results

- Enabled: An icon indicates whether you can send messages to the virtual
service. On another panel, you can enable or disable virtual services.
- Virtual Service: The name of a proxy service. You can associate a virtual
service with one or more existing service endpoints.
- Endpoint: One or more existing service endpoints that are associated with
the virtual service.

## What to do next