<!-- image -->

# Factors affecting BPEL process interactions

- In a one-way operation, the completion of the service is not made
known to the invoking client. The service execution ends with the
successful invocation of the associated service.
- In a request-response operation, the completion of the service
is made known to the invoking client. The service execution ends when
the result of the service is made available to the invoking client.

- An SCA wire statically associates an SCA reference to the interface
of the invoked service. This is an SCA-level mechanism and it can
be applied if the client, the service, or both are implemented as
processes.
- An endpoint reference (EPR) can be assigned to a BPEL partner
link. The EPR determines the endpoint address of the service to be
invoked using the partner link. Thus, any service can be invoked dynamically
that complies with what SCA allows for dynamic service invocations,
for example, web service binding, MQ JMS binding, MQ binding, or an
SCA binding.
- A BPEL process template name can be set for a partner link that
is part of a BPEL process acting as an SCA client. The template name
uniquely determines the name of another BPEL process that is deployed
in the same server or cluster.