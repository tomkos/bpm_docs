<!-- image -->

# Advanced properties for service gateway

If you are using the service gateway with
an application that has web services bindings, you may need to configure
some additional fields.

## Export

To configure an export for
the service gateway follow these steps:

1. Select the Binding tab and expand Advanced
properties.
2. In the Function selector field, select
the function selector. A function selector determines the operation
that will invoked in the Service Component Architecture (SCA) application.
There will be only one choice.
3. In the Data format field, select the data
format transformation. A data format transformation transforms the
data format in a native environment to the data format expected by
an SCA application. For example, the incoming data from a web services
client might be in a text data format and the data is transformed
into an XML data format for the SCA application. This data format
transformation also works from the SCA application to the client.
There will be only one choice.
4. Save your configuration.

## Import

Configuring your import for the service
gateway is the same as configuring an export. However, there is no
function selector on the import. Only the data format transformation
selection is needed. There will be only one choice.