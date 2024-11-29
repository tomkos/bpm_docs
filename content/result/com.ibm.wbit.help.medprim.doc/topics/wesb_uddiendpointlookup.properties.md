# UDDI Endpoint Lookup mediation primitive properties

## Registry
Name registryName

Identifies the definition to be used by
the UDDI Endpoint Lookup mediation primitive. A definition is created using the server
administrative console and provides connection information for a UDDI instance. At least one UDDI
definition needs to exist on the server that your SCA module is installed to.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | No                |
| Valid values   | StringNote:       |

## Match Policy
matchPolicy

If no match is found during a registry query, regardless of the match policy, the
noMatch output terminal is fired and the original input SMO is propagated.

| Match Policy      | First   | First     | All    | All       | All and Alternates   | All and Alternates   |
|-------------------|---------|-----------|--------|-----------|----------------------|----------------------|
| Output terminal   | out     | noMatch   | out    | noMatch   | out                  | noMatch              |
| Target            | update  | no action | clear  | no action | update               | no action            |
| Primitive context | update  | no action | update | no action | update               | no action            |
| Alternate targets | clear   | no action | clear  | no action | update               | no action            |

- If the registry query returns matches, the following occurs:
    - The SMO context is updated with registry information relating to all services returned by the
registry.
    - The dynamic callout address, in the SMO header, is cleared.
    - The alternate targets list, in the SMO header, is cleared.
- You must post-process the SMO to select a service endpoint for dynamic calling.

- If the registry query returns matches, the following occurs:
    - The dynamic callout address, in the SMO header, is updated with one service address from the
results returned.
    - The SMO context is updated with registry information relating to the address in the dynamic
callout address.
    - The alternate targets list, in the SMO header, is cleared.

- If the registry query returns matches, the following occurs:
    - The dynamic callout address, in the SMO header, is set with the first match.
    - The alternate targets list, in the SMO header, is updated with the remaining matches.
    - All services found are also placed into the primitive context.

## Business
Name businessName

The name of the business to search
for.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | No                |
| Valid values   | StringNote:       |

## Technical
Model Names technicalModels

The name of the technical model to
search for. This property is optional, with a valid type of String.

The
maximum number of TModels which UDDI can check that a given Service
supports is 64, and 5 by default, as determined by the configuration
parameter that has been set.

## Service
Name serviceName

The name of the service to search
for.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | No                |
| Valid values   | StringNote:       |

## Find
Qualifiers findQualifiers

A
list of find qualifiers (as specified in the UDDI specification).
This property is optional.

## Considerations

- If the Use dynamic endpoint if set in the message header property
is not set in the callout node, the runtime environment does not use
the dynamic endpoint in /headers/SMOHeader/Target/address.
In this case, the runtime environment uses the default endpoint if
there is one, or throws an error.
- The previous information only applies to UDDI Servers that support the UDDI version 3
specification.

## Sample XML code

```
<node name="UDDIEndpointLookup" type="UDDIEndpointLookup">
  <property name="registryName" value="myRegistry"/>
  <property name="businessName" value="myBusinessName"/>
  <table name="technicalModels">
    <row>
      <property name="technicalModel" value="myTechnicalModel"/>
    </row>
  </table>
  <property name="serviceName" value="myServiceName"/>
  <table name="findQualifiers">
    <row>
      <property name="findQualifier" value="myFindQualifier"/>
    </row>
  </table>
  <inputTerminal/>
  <outputTerminal>
    <wire targetNode="SLACheck1"/>
  </outputTerminal>
  <outputTerminal name="noMatch"/>
  <failTerminal/>
</node>
```