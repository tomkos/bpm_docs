<!-- image -->

# Proxy gateway widget

Each proxy group in the list includes information about the installed proxy gateways that are
associated with the group. When a proxy gateway is installed on a server, the proxy groups it
references are automatically added to the configuration store if they don't already exist. If you
uninstall a proxy gateway from the server, the proxy groups it is associated with are not deleted.
This prevents the unintentional loss of configuration data for the proxy group when no proxy gateway
applications are installed that reference it. You must delete the proxy group if it is no longer
needed.

- a proxy group is shared by multiple proxy gateways
- a proxy gateway has multiple proxy groups
- a proxy group exists without an associated proxy gateway

Figure 1. Proxy gateway widget in Business Space

<!-- image -->

- There are two proxy gateways: PGW1\_Gateway and PGW2\_Gateway.
- There are four proxy groups: PGW1ProxyGroup, PGW2ProxyGroup, PGW3ProxyGroup, PGWSharedGroup.
- The first row has a proxy group (PGW1ProxyGroup) that is associated with a single proxy gateway
(PGW1\_Gateway).
- The second row has a proxy group (PGWSharedGroup) shared by multiple proxy gateways
(PGW1\_Gateway, PGW2\_Gateway).
- Rows two and three illustrate a proxy gateway (PGW2\_Gateway) that is associated with multiple
proxy groups (PGWSharedGroup, PGW2ProxyGroup).
- The fourth row has a proxy group (PGW3ProxyGroup) without an associated proxy gateway.

## Using the proxy gateway widget

Figure 2. Select a proxy gateway widget

<!-- image -->

1. Select the relevant proxy group row in the table, which displays a pencil icon.
2. Click the  (pencil icon) which changes the widget to a new view where you can configure the virtual
services for the proxy group.
3. If the selected row is for a proxy group without an associated proxy gateway, a  (X icon) is visible where you can delete the proxy group.

When you create a new proxy group in the configuration store, there are no virtual services
defined. When you edit it for the first time, the panel shown in Figure 3 is displayed, where you must add a virtual service
by filling out the WSDL Location field.

Figure 3. Editing a new proxy group

<!-- image -->

```
http://localhost:9080/BankServiceProviderWeb/sca/accountExport1?wsdl
```

(If the service provider does not support the ?wsdl convention, the WSDL can be loaded from
another location such as a registry.)

You must then click Add Service, which opens the panel for defining a virtual service, as shown
in Figure 4.

Figure 4. Editing a new proxy group

<!-- image -->

1. Port Type - The WSDL port type for the virtual service.
2. Virtual Service Name - The key that is given to the URL of the export for the associated proxy
gateways to create a dedicated URL for the virtual service. You can change the generated value to
something more relevant. For example, the default value shown in the image is
accountExport1\_accountHttpService, which you can change to Account or AccountService.
3. Virtual Service URLs - Network addressable endpoints that are exposed for the virtual service
via the associated proxy gateways.
4. Endpoint URLs - An ordered list of network addressable endpoints that are used to forward
messages for this virtual service. These are available within the Target and AlternateTarget
elements of the SMO after a Gateway Endpoint Lookup mediation primitive.
5. Enable Virtual Service - must be selected if the virtual service will be available to a Gateway
Endpoint Lookup mediation primitive when it queries the built-in configuration store.
6. Advanced Service Properties - A series of user defined key value pairs associated with the
virtual service. These are available within the EndpointLookupContext of the SMO, after a Gateway
Endpoint Lookup mediation primitive.

When you click Save, the widget returns to the original list of virtual services associated with
the proxy group.