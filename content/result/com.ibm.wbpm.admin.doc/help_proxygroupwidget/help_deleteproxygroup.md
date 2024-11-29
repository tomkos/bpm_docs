<!-- image -->

# Deleting proxy groups from the built-in store

## Before you begin

1. Use IBM Integration Designer to create a proxy gateway. Use the wizard to create a proxy gateway
module, which is an SCA module containing a Gateway Endpoint Lookup mediation primitive.
2. Install the proxy gateway module to Process Server.
3. Create a business space containing the Proxy Gateway widget.
4. Uninstall the proxy gateway module.

## About this task

A proxy gateway is a module that receives web service requests and forwards them to an endpoint
defined in a proxy group.

When you create a proxy gateway module, you define the proxy groups for the module. When you
install your proxy gateway module, if the proxy groups do not exist in the built-in configuration
store, they are automatically created.

When you uninstall your proxy gateway module, the proxy groups are not automatically deleted from
the built-in configuration store. You must use the Proxy Gateway widget to delete the proxy groups
and associated virtual services.

## Procedure

1. Log in to your business space and open the page that contains the Proxy
Gateway widget.
2. From the Proxy Gateway widget, delete a proxy group that has no associated
proxy gateway. 
Click the cross icon at the end of the relevant row.

## Results

The proxy group is removed from the built-in configuration store, and the Proxy
Gateway widget is refreshed.