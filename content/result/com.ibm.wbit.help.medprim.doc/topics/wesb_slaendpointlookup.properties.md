# SLA Endpoint Lookup mediation primitive properties

## Registry Name

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | No                |
| Valid values   | StringNote:       |

## Consumer ID

The
SLA Endpoint Lookup mediation primitive uses the consumer identifier
to find the consumer in the SLA. Because most interactions will be
through web services and that the consumer identifier will not be
part of the message payload itself, the default value for this field
is /headers/SOAPHeader[name='GEPGatewayHeader']/value/consumerID.
The GEPGatewayHeader is a supplied schema specifically used for this
purpose; the XPath expression indicating that the value for the endpoint
classification should be taken from this particular field of a specific
SOAP header in the incoming message. You must enable the GEPGatewayHeader
in the mediation module dependencies section. This usage pattern can
be overridden with another XPath expression or literal value if necessary.

| Field detail   | Value and notes                                               |
|----------------|---------------------------------------------------------------|
| Required       | Yes                                                           |
| Valid values   | XPathNote:                                                    |
| Default        | /headers/SOAPHeader[name='GEPGatewayHeader']/value/consumerID |

## Context ID

The
SLA Endpoint Lookup mediation primitive uses the context identifier
to locate the exact SLA for a particular consumer.  Because most interactions
will be through web services and that the context identifier will
not be part of the message payload itself, the default value for this
field is /headers/SOAPHeader[name='GEPGatewayHeader']/value/contextID.
The GEPGatewayHeader is a supplied schema specifically used for this
purpose; the XPath expression indicating that the value for the context
identifier should be taken from this particular field of a specific
SOAP header in the incoming message. You must enable the GEPGatewayHeader
in the mediation module dependencies section. This usage pattern can
be overridden with another XPath expression or literal value if necessary.

| Field detail   | Value and notes                                              |
|----------------|--------------------------------------------------------------|
| Required       | Yes                                                          |
| Valid values   | XPathNote:                                                   |
| Default        | /headers/SOAPHeader[name='GEPGatewayHeader']/value/contextID |

## Endpoint Classification

The
SLA Endpoint Lookup mediation primitive uses this classification to
further refine the selection of endpoints associated with a particular
SLA.  Because most interactions will be through web services and that
the endpoint classification will not be part of the message payload
itself, the default value for this field is http://www.ibm.com/xmlns/prod/serviceregistry/6/1/GovernanceProfileTaxonomy#Development.
When deploying to different environments, change the default by using
the Promoted Properties function.

| Field detail   | Value and notes                                                                         |
|----------------|-----------------------------------------------------------------------------------------|
| Required       | Yes                                                                                     |
| Valid values   | XPathNote:                                                                              |
| Default        | http://www.ibm.com/xmlns/prod/serviceregistry/6/1/GovernanceProfileTaxonomy#Development |

## User Properties

| Field detail                                                                                                                                                                                                                                         | Value and notes   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| Value value The value of the parameter can be specified as either a literal or an XPath expression. Description description A description of the parameter. It is used solely for documentation, and plays no part in the selection of the endpoint. |                   |

## Sample XML
code

```
<node displayName="slaEndpointLookup" name="slaEndpointLookup" type="SLAEndpointLookup">
  <property name=registryName" value="myRegistry"/>
  <inputTerminal/>
  <outputTerminal>
    <wire targetNode="nextNode"/>
  </outputTerminal>
  <failTerminal/>
</node>
```