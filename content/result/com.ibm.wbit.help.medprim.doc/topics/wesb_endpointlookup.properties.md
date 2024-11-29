# Endpoint Lookup mediation primitive properties

## Name portTypeName

Search the registry for services that
implement a particular portType, the name of which is specified by the Name
property.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | No                |
| Valid values   | StringNote:       |

## Namespace portTypeNamespace

Search the registry for services that
implement a particular portType, the namespace of which is specified by the
Namespace property. The Namespace can be specified in any
valid namespace format, for example, URI or URN.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | No                |
| Valid values   | StringNote:       |

## Registry
Name registryName

Identifies the WSRR definition to be used by
the Endpoint Lookup mediation primitive. A WSRR definition is created using the server
administrative console and provides connection information for a WSRR instance. At least one WSRR
definition needs to exist on the server that your SCA module is installed to. If the
Registry Name is absent then the default WSRR definition is used.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | No                |
| Valid values   | StringNote:       |

## Match Policy matchPolicy

If the registry has more than one service
matching your query, the Match Policy determines how many service endpoints
should be added to the message. It also determines whether the matching should select exact matches
or the latest compatible service versions.

| Match Policy      | First   | First     | All    | All       | All and Alternates   | All and Alternates   | Latest compatible   | Latest compatible   |
|-------------------|---------|-----------|--------|-----------|----------------------|----------------------|---------------------|---------------------|
| Output terminal   | out     | noMatch   | out    | noMatch   | out                  | noMatch              | out                 | noMatch             |
| Target            | update  | no action | clear  | no action | update               | no action            | update              | no action           |
| Primitive context | update  | no action | update | no action | update               | no action            | update              | no action           |
| Alternate targets | clear   | no action | clear  | no action | update               | no action            | clear               | no action           |

| Field detail   | Value and notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Required       | Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Valid values   | Return all matching endpoints 0   If the registry query returns matches, the following occurs: The SMO context is updated with registry information relating to all services returned by the registry.  The dynamic callout address, in the SMO header, is cleared.  The alternate targets list, in the SMO header, is cleared.    You must post-process the SMO to select a service endpoint for dynamic invocation.   Return first matching endpoint and set routing target 1   If the registry query returns matches, the following occurs: The dynamic callout address, in the SMO header, is updated with one service address from the results returned. The SMO context is updated with registry information relating to the address in the dynamic callout address.  The alternate targets list, in the SMO header, is cleared.     Return all matching endpoints and set alternate routing targets 2   If the registry query returns matches, the following occurs: The dynamic callout address, in the SMO header, is set with the first match. The alternate targets list, in the SMO header, is updated with the remaining matches.  All services found are also placed into the primitive context.     Return endpoint matching latest compatible version of SCA module-based services  3   If the registry query returns matches, the following occurs: The dynamic callout address, in the SMO header, is updated with one service address from the results returned. The SMO context is updated with registry information relating to the address in the dynamic callout address. The alternate targets list, in the SMO header, is cleared      Note: |
| Default        | Return first matching endpoint and set routing target                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

## Binding
Type bindingType

Search the registry for services that match a
specified binding type, WebServices and SCA bindings together, or any binding type.

| Field detail   | Value and notes                                                                                                          |
|----------------|--------------------------------------------------------------------------------------------------------------------------|
| Required       | Yes                                                                                                                      |
| Valid values   | All binding types 0  Web Services 1  MQ 2  MQ JMS 3  JMS 4  Generic JMS 5  HTTP 6  SCA 7  Web Services and SCA 8   Note: |
| Default        | Web Services and SCA                                                                                                     |

## Version portTypeVersion

The Version property
can be used in one of two ways. If you are using portTypes, this field holds the version of the
portType. However, if you are using versioned SCA modules, this field holds the version of the SCA
module.

If
you are using portTypes, the registry is searched for services that
implement a particular portType.

If you are using versioned
SCA modules, to do service-version-aware lookups, you must select
a Match Policy of Return endpoint matching
latest compatible service version. In addition, you must
set the Version property to be the version of the SCA module, and
set the Module property to the unversioned name of the SCA Module.
Optionally you can also set the Export property.

For
versioned SCA modules, the format of the Version property
is: V.R.M, where V is an integer version number, R is an integer release
number, and M is an integer modification number. The version supplied
can include one or more wildcard (*) characters. For example, a Version property
of 1.0.* will find the endpoint of the service
that has a version set to 1, a release set to 0, and the greatest
modification number. For further information, see: Matching
latest compatible service versions.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | No                |
| Valid values   | StringNote:       |

## Module moduleName

The SCA module name. Only used when the
Match Policy property is set to Return endpoint matching latest
compatible service version. Search the registry for SCA modules with a name that matches
the unversioned name of the specified Module.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | No                |
| Valid values   | StringNote:       |

## Export exportName

The SCA export name. Only used when the
Match Policy property is set to Return endpoint matching latest
compatible service version. Search the registry for SCA exports with a name that matches
the specified Export name.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | No                |
| Valid values   | StringNote:       |

## Classification
URIs classifications

Search for objects that match a particular
classification URI.

- If you want to extract endpoint information about exports that
use the default SCA binding then, in WSRR, you must specify any classifications
on the SCA Export objects that you want to retrieve. Make sure that
you put classifications on the SCA Exports and not on the SCA Export
documents.
- If you want to extract endpoint information about web services
then, in WSRR, you  must specify any classifications on the appropriate
WSDL Port objects. The WSDL Port objects must  implement a port type
that you describe using the Endpoint Lookup properties relating to
portType.

- Account
    - Identifier
    - Name
        - First name
        - Second name
- Address
    - First line of address
    - Second line of address

Specifying a classification of Address matches
any object classified as Address, First
line of address or Second line of address.

## User
Properties userProperties

Search the registry for services that are
annotated with user-defined properties.

- If you want to extract endpoint information about exports that
use the default SCA binding then, in WSRR, you must specify any user
properties on the SCA Export objects that you want to retrieve. Make
sure that you put user properties on the SCA Exports and not on the
SCA Export documents.
- If you want to extract endpoint information about web services
then, in WSRR, you  must specify any user properties on the appropriate
WSDL Port objects. The WSDL Port objects must  implement a port type
that you describe using the Endpoint Lookup properties relating to
portType.

| Field detail                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Value and notes   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| Name name The name of the user defined property. The valid type is String. Type type The type of the user-defined property. If the type is String, then what you specify as the Value is used as a literal, in the search query. If the type is XPath, then what you specify as the Value must be an XPath expression. The XPath expression must resolve to a unique leaf node in the inbound SMO. The value of the leaf node is used in the search query. Value value The value of the user defined property. This can be either a literal value or an XPath expression, depending upon the Type property. |                   |

## Considerations

Consider the following when
using the Endpoint Lookup mediation primitive:

- If the Use dynamic endpoint if set in the message header property
is not set in the callout node, the runtime environment does not use
the dynamic endpoint in /headers/SMOHeader/Target/address.
In this case, the runtime environment uses the default endpoint if
there is one, or throws an error.
- It is valid to specify only the Match Policy property.
In this case, the default registry is queried for all applicable services.
- All portType, Classification or User
Properties specified for an Endpoint Lookup mediation primitive
result in a query that combines all of these properties using a logical AND.
- If you want to use Classification URIs that
include white space characters, the correct URL encoding should be
used. For example, a single character space should be represented
as %20.
- White space characters provided in any of the Endpoint Lookup
mediation primitive properties are treated as literal characters.
They are not removed by the Endpoint Lookup mediation primitive when
querying the registry. For example, if you specify a Classification property
and the expected results are not returned from a query, ensure there
is no white space before or after the Classification URI.
- If you use the Return endpoint matching latest compatible
service version Match Policy to retrieve
SCA module export endpoints, the Module property
must be supplied.
- If you use the Return endpoint matching latest compatible
service version Match Policy to retrieve
manual endpoints, the Version Value property
must be manually entered for the Manual MQ/JMS/HTTP endpoint with
associated Interface in the WSRR console.
- If you use the Return endpoint matching latest compatible
service version Match Policy to retrieve
SCA module export endpoints, only the IBM Supplied Version Scheme
(IBM\_VRM) is supported.
- If you want to retrieve endpoints from WSDL that has SOAP 1.2
bindings, the WSRR definition must use the Version 6.2 web service
interface URL, which is generally: http://<server>:<port>/WSRR6\_2/services/WSRRCoreSDOPort.
However, if you call the Version 6.2 URL from a client generated for
a previous version of WSRR, the client might fail if it cannot correctly
process the data that is returned.
- If you want to retrieve manual endpoints or SCA module endpoints
with MQ, MQ JMS, JMS Generic JMS or HTTP export bindings, the WSRR
definition must use the Version 7.0 web service interface URL, which
is generally: http://WSRR7\_0/services/WSRRCoreSDOPort. However, if
you call the Version 7.0 URL from a client generated for a previous
version of WSRR, the client might fail if it cannot correctly process
the data that is returned.
- If you want to retrieve a manual endpoint for a Generic JMS service,
in the WSRR console, manually set the Binding Type property
to GenericJMS for the Manual JMS endpoint with associated Interface.
- If you want to retrieve a manual endpoint for an MQ JMS service,
in the WSRR console, manually set the Binding Type property
to MQJMS for the Manual MQ endpoint with associated Interface.

## Sample XML code

```
<node name="EndpointLookup" type="EndpointLookup">
  <property name="portTypeName" value="myInterface"/>
  <property name="portTypeNamespace" value="http://TestMod/myInterface"/>
  <property name="registryName" value="myRegistry"/>
  <property name="bindingType" value="1"/>
  <inputTerminal/>
  <outputTerminal>
    <wire targetNode="ServiceInvoke"/>
  </outputTerminal>
  <outputTerminal name="noMatch"/>
  <failTerminal/>
</node>
```