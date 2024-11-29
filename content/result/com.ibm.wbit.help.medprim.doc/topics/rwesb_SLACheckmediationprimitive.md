# SLA Check mediation primitive

## Introduction

You can use the SLA Check mediation
primitive to check that a service level agreement (SLA) exists.

A
message that is being mediated can be routed to a target service.
Whether the consumer of this target service has a service level agreement
in place to use the service can be enforced using the SLA Check mediation
primitive, which checks that the correct SLA exists in WebSphere® Service Registry and Repository
(WSRR).

The SLA Check mediation primitive has one input terminal
(in), one fail terminal (fail),
and two output terminals (accept and reject).
The in terminal is wired to accept a message
and the other terminals are wired to propagate a message. If the information
passed on the incoming message is used to successfully find a matching
SLA in WSRR, the accept terminal is fired.
However, if a matching SLA is not found, the reject terminal
is fired.

## Usage

1. Endpoint.  This field can be a literal value, or can be passed
as part of the message, and identifies the target endpoint that the
consumer wants to call. This field is mandatory, if not set, the reject
terminal is fired.
2. Consumer Identifier. This field can be a literal value, or can
be passed as part of the message, and identifies the consumer of the
target endpoint. This is an optional field depending on whether the
relevant artifacts in WSRR have the identifier defined. If a value
is specified for the consumer identifier of the capability version
in WSRR, the value specified for the Consumer ID property must match
it exactly; if no value is specified then the Consumer Identifier
property must be left empty. For more information, see the WSRR documentation
about the governance enablement profile.
3. Context Identifier. This field can be a literal value or can be
passed as part of the message and identifies the context under which
the consumer's invocation of the target endpoint occurs.  If a value
is specified for the context identifier of the service level agreement
in WSRR, the value specified for the Context Identifier property must
match it exactly; if no value is specified then the Context ID property
must be left empty. This is an optional field depending on whether
the relevant artifacts in WSRR have the identifier defined. For more
information, see the WSRR documentation about the governance enablement
profile.

- Continue to use the same governance enablement profile you used
on a previous version of WSRR.
- Modify the named query on the supplied WSRR Version 8.0 profileby completing the following steps: The new named query is now active.
    1. Log onto the WSRR by using the web user interface.
    2. Change to the Configuration perspective.
    3. Go to Active Profile > Named
Queries.
    4. Select SLACheck.
    5. Replace the <xpath> query with the following
code:<xpath>/WSRR/GenericObject[classifiedByAnyOf(., 'http://www.ibm.com/xmlns/prod/serviceregistry/profile/v6r3/GovernanceEnablementModel#CapabilityVersion')and @gep63\_consumerIdentifier='%1']/
		gep63\_consumes(.)[@gep63\_contextIdentifier='%2' and gep63\_agreedEndpoints(.)/
		gep63\_availableEndpoints(.)[@name='%3']
</xpath>
    6. Select OK.

- SLA Check mediation primitive properties

You can specify values for mediation primitive properties either by using the property fields in the IBM® Integration Designer user interface or by using an XML format. The property field names displayed in IBM Integration Designer are generally different from the property names used when building a mediation flow using XML code. In the following information, icons are used to identify each property name used in IBM Integration Designer and the corresponding XML name. (Where applicable, XML names that are required, but not shown in IBM Integration Designer, are also described.)