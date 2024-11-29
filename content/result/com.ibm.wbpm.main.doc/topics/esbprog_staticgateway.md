<!-- image -->

# Static service gateway pattern

Figure 1. Static service gateway pattern

<!-- image -->

To create a web service client, you retrieve the WSDL file for the service provider, and pass it
into the web service tool to generate a client stub. For a static service gateway the creation of
this WSDL file is a manual process, where you must download the target service provider WSDL,
replace any policy information with that attached to the service gateway export and then override
the endpoint to that of the service gateway.

- Example scenario