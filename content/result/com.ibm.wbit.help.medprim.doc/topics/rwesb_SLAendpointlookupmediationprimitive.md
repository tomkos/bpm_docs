# SLA Endpoint Lookup mediation primitive

## Introduction

- Whether the consumer of the endpoint has a valid SLA for the endpoint
- Whether the particular SLA is active
- Whether the endpoint is online
- Whether the endpoint has a certain required classification; for
example, whether it is Production or Development.

The SLA Endpoint Lookup mediation primitive has one input
terminal (in), one fail terminal (fail),
and two output terminals (out and noMatch).
The in terminal is wired to accept a message
and the other terminals are wired to propagate a message. If the information
passed on the incoming message successfully finds a matching endpoint
in WSRR, the out terminal is fired. However,
if a matching endpoint is not found, the noMatch terminal
is fired.

## Usage

- Consumer Identifier. This field can be a
literal value, or can be passed as part of the message, and identifies
the consumer of the target endpoint. The consumer identifier is a
field in the CapabilityVersion, ProcessVersion, ApplicationVersion
or ServiceVersion representing the consumer of the target service.
For more information, see the WSRR documentation on the  Governance Enablement Profile.
- Context Identifier. This field can be a literal
value or can be passed as part of the message and identifies the context
under which the consumer's invocation of the target endpoint occurs.
The context identifier is a field on the SLA representing the agreement
between the consumer and provider of the target service. For more
information, see the WSRR documentation on the  Governance Enablement Profile.
- Endpoint Classification. This field  can
be a literal value, or can be passed as part of the message, and indicates
a refinement in the selection of the target endpoint. All endpoints
in WSRR can be classified. For example, they can be Test endpoints
or Production endpoints. This classification enables a more fine-grained
search. An example of a Production endpoint is http://www.ibm.com/xmlns/prod/serviceregistry/6/1/GovernanceProfileTaxonomy#Production.

Add extra parameters into the search to add further refinement
of the endpoint selection. Use the table of user defined parameters
under the Advanced tab for this purpose to
supply extra selection parameters. However, if you add extra parameters,
the named query installed on the WSRR system must be altered to match
these additions.

- Continue to use the same governance enablement profile you used
on a previous version of WSRR.
- Modify the named query on the supplied WSRR Version 8.0 profileby completing the following steps: The new named query is now active.
    1. Log onto the WSRR by using the web user interface.
    2. Change to the Configuration perspective.
    3. Go to Active Profile > Named
Queries.
    4. Select SLAEndpointLookup.
    5. Replace the <xpath> query with the
following code:<xpath>/WSRR/GenericObject[classifiedByAnyOf(.,
  'http://www.ibm.com/xmlns/prod/serviceregistry/profile/v6r3/GovernanceEnablementModel#CapabilityVersion') 
   and gep63\_consumes(.) and @gep63\_consumerIdentifier='%1']/      gep63\_consumes(.)[classifiedByAnyOf(.,
'http://www.ibm.com/xmlns/prod/serviceregistry/lifecycle/v6r3/LifecycleDefinition#SLAActive') 
   and @gep63\_contextIdentifier='%2']/gep63\_agreedEndpoints(.)/ gep63\_availableEndpoints(.)[classifiedByAnyOf(.,
'http://www.ibm.com/xmlns/prod/serviceregistry/lifecycle/v6r3/LifecycleDefinition#Online') and classifiedByAnyOf(.,'%3')]
</xpath>
    6. Select OK.

- SLA Endpoint Lookup mediation primitive properties

You can specify values for mediation primitive properties either by using the property fields in the IBM® Integration Designer user interface or by using an XML format. The property field names displayed in IBM Integration Designer are generally different from the property names used when building a mediation flow using XML code. In the following information, icons are used to identify each property name used in IBM Integration Designer and the corresponding XML name. (Where applicable, XML names that are required, but not shown in IBM Integration Designer, are also described.) Consult your WSRR Administrator for more information on which values to use for each of these parameters.