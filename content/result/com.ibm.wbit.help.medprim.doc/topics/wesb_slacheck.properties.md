# SLA Check mediation primitive properties

## Registry Name

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | No                |
| Valid values   | StringNote:       |

## Endpoint

| Field detail   | Value and notes                                                                                                                                                                                                                                                                                     |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Required       | Yes                                                                                                                                                                                                                                                                                                 |
| Valid values   | XPathNote:                                                                                                                                                                                                                                                                                          |
| Default        | /headers/SMOHeader/Target/addressBy default, the endpoint is set to the address field of the Target in the service message object (SMO) header. Therefore, if an Endpoint Lookup mediation primitive is used before the SLA Check mediation primitive, no changes are needed to the Endpoint field. |

## Consumer ID

This
is an optional field, depending upon whether the associated artifacts
in the repository have the consumer identifier defined.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | No                |
| Valid values   | XPathNote:        |

## Context ID

This
is an optional field, depending upon whether the associated artifacts
in the repository have the context identifier defined.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | No                |
| Valid values   | XPathNote:        |

## Sample XML code

```
<node name="SLACheck1" type="SLACheck">
  <property name="registryName" value="myRegistry"/>
  <inputTerminal/>
  <outputTerminal name="accept">
    <wire targetNode="GatewayEndpointLookup1"/>
  </outputTerminal>
  <outputTerminal name="reject"/>
  <failTerminal/>
</node>
```