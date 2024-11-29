# CMIS web service clients

When you access a content management system from a process
applicationworkflow automation by using Content Management Interoperability Service
(CMIS) integration, a web service client is used.

The CMIS web service client provides the required information for the functional interface,
whereas the content management system requires additional information. For example, the content
management system might require authentication, such as a user ID and password, or an LTPA token. As
a result, you must configure the web service client if the default options do not meet your
requirements.

The most common way to configure the web service client is to attach policy sets and bindings.
However, if your specific requirement of customization cannot be met using policy sets and bindings,
you can register your own JAX-WS handlers to be started as part of outbound calls.

- Attaching different policy sets or bindings to service references

To enable access to multiple CMIS web service providers, you can attach JAX-WS policy sets and bindings to the web service client in your workflow environment.
- Registering custom JAX-WS handlers

If your customization requirements cannot be met using policy sets and bindings, you can register your own JAX-WS handlers to be started as part of an IBM® Business Automation Workflow outbound call.