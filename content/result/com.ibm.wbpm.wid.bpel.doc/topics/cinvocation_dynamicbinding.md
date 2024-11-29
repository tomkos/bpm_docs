<!-- image -->

# Dynamic binding between BPEL processes and services

The services with which a BPEL process interacts are modeled as
partner links in the process model. Before operations on a partner
service can be invoked using a partner link, the binding and communication
data for the partner service must be available. The relevant information
about a partner service is usually set as part of business process
deployment.

The Service Component Architecture (SCA) reference that corresponds
to the BPEL partner link can be left unwired. In this case, the binding
that is used for the invocation defaults to an SCA or a web service
binding, depending on the endpoint address URL. Alternatively, the
SCA reference can be prewired to an SCA Import. In this case, the
binding and any quality of service specifications are obtained from
the SCA Import and only the service endpoint address is overwritten
by the endpoint reference.

- For a microflow, the service is invoked synchronously
- For a long-running process, the service is invoked asynchronously