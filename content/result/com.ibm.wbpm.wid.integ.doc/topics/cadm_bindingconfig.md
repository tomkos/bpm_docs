<!-- image -->

# Export and import binding configuration

In addition, you specify transport-specific information on bindings.
For example, for an HTTP binding, you specify the endpoint URL. For
the HTTP binding, the transport-specific information is described
in the Generating an HTTP import binding and Generating
an HTTP export binding topics. You can also find information about
other bindings in the documentation.

- Data format transformation in imports and exports

When an export or import binding is configured in IBM® Integration Designer, one of the configuration properties that you specify is the data format used by the binding.
- Function selectors in export bindings

A function selector is used to indicate which operation should be performed on the data for a request message. Function selectors are configured as part of an export binding.
- Fault handling

You can configure your import and export bindings to handle faults (for example, business exceptions) that occur during processing by specifying fault data handlers. You can set up a fault data handler at three levels-you can associate a fault data handler with a fault, with an operation, or for all operations with a binding.