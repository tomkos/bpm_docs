# Policy Resolution mediation primitive properties

## Registry Name registryName

Identifies the WSRR definition to be used by
the Policy Resolution mediation primitive. A WSRR definition is created using the server
administrative console and provides connection information for a WSRR instance. At least one WSRR
definition needs to exist on the server on which your SCA module is installed. If you do not specify
a value for the Registry Name, the default registry (WSRR definition) is
used.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | No                |
| Valid values   | StringNote:       |

## Policy Scope scope

Defines the scope of any mediation
policies.

| Field detail   | Value and notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Required       | Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Valid values   | Module 0 If you set the Policy Scope property to Module, the Policy Resolution primitive retrieves mediation policies that are attached to an SCA module object, in WSRR. When you load an SCA module into WSRR, the registry creates an SCA module document, and an SCA module object to which you can attach mediation policies. Target Service 1 If you set the Policy Scope to Target Service, the Policy Resolution primitive retrieves mediation policies that are attached to WSRR objects representing the target service. When you load a WSDL document into WSRR, the registry creates objects for any service, port, binding, portType, operation, and message elements described by the WSDL. You can attach mediation policies to any of these objects except message objects.When you load an SCA module into WSRR the registry creates objects for the module and any exports and imports defined in the module. You can attach mediation policies to exports, the interface portType and operations that are linked to the export. You can also attach mediation policies to the WSRR objects "Manual HTTP Endpoint with associated Interface", "Manual JMS Endpoint with associated Interface" and "Manual MQ Endpoint with associated Interface", and the interface portType and operations that are linked to these Manual Endpoints. Note: Use an Endpoint Lookup mediation primitive to determine the exact target service, before retrieving mediation policies associated with the target service.   Intersection of Module and Target Service 2 If you set the Policy Scope to Intersection, the Policy Resolution primitive retrieves mediation policies that are attached to both the module and the target service, in WSRR; combining both scopes into a single mediation policy that meets the requirements of both.  Note: |
| Default        | Module                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

## Conditions conditions

| Field detail                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Value and notes   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| Policy condition name name The name of a condition that a mediation policy must have. Conditions allow different mediation policies to apply in different contexts. At run time, the conditions must be satisfied before a conditional mediation policy can be used. Note: In WSRR, you must specify the conditions on the policy attachment objects.   XPath xpath The XPath location from which the runtime environment gets the mediation policy condition. For example, if an XPath is set to /body/input/customerName and the associated Policy condition name is Customer, the runtime environment sets the value of Customer to whatever it finds at /body/input/customerName. Comment comment Any comments that you want to be saved with the mediation flow component. |                   |

## Propagate mediation policy to response
flow propagate

Defines whether the mediation policy selected
on the request flow is propagated to the response flow. By default the mediation policy is not
propagated to the response flow. You can propagate the mediation policy to the response flow by
selecting the check box.

| Field detail   | Value and notes   |
|----------------|-------------------|
| Required       | Yes               |
| Valid values   | BooleanNote:      |
| Default        | false             |

## Classification URIs classifications

A set of classification names, expressed
as a list of URIs.

1. In the navigation pane of the WSRR web user interface, click Service Documents > Policy Documents.
2. In the content pane, click a mediation policy document.
3. Click Edit Classifications.
4. If your policy document does not have the classification whose URI you
want, select the check box of the classification that you want and click Add
>>>.
5. Select (highlight) the classification whose URI you want, and the URI appears in the table at
the end of the page.
6. Click Cancel. Do not add governance classifications
using the Edit Classifications method.

At run time, any Classification you specify in IBM Integration
Designer must be found on a
suitable mediation policy in WSRR. WSRR has many classification systems, including lifecycle
classifications that can be used for governance.

- If you want to use WSRR governance you must make the appropriate WSRR policy documents governed.
Then you can move the policy documents, and any associated policies, through the lifecycle
classifications. However, if you want to use classifications that are not related to governance, you
must specify the classifications on the WSRR policies that you want to retrieve, not on the policy
documents.
- Mediation policies, in WSRR, have two classifications that are used for internal processing:
WESB Mediation Policy and WS Policy Framework 1.5. Do not
edit or delete these classifications, or move them to IBM Integration
Designer.

If you specify one classification in the Policy Resolution primitive and two classifications in
WSRR, then the mediation policy can be returned, assuming the names match. For example, if the
Policy Resolution primitive specified a classification of Test and the WSRR
policy object specified classifications of Test and
Managed, then the mediation policy would match the query. However, if the
Policy Resolution primitive specified classifications of Test and
Managed but the WSRR policy object only specified a classification of
Managed, then the mediation policy would not match the query.

WSRR defines classification systems using the Web Ontology Language (OWL), in which each
classifier is a class and has a URI. OWL implements a simple hierarchical system. For example, a
bank account could start with the following details:

- Account
    - Identifier
    - Name
        - First name
        - Second name
- Address
    - First line of address
    - Second line of address

Specifying a classification of Address matches any object classified as
Address, First line of address or Second
line of address.

## Considerations

- White space characters provided in any of the Policy Resolution
mediation primitive properties are treated as literal characters.
They are not removed by the Policy Resolution mediation primitive
when querying the registry.
- Policy Resolution mediation primitives cannot be used in subflows. Properties on mediation
primitives in subflows need to be promoted to the highest-level request, response, or fault flow
before they can be modified by a Policy Resolution mediation primitive.

## Sample XML code

```
<node name="PolicyResolution" type="PolicyResolution">
  <property name="registryName" value="myRegistry"/>
  <table name="conditions">
    <row>
      <property name="name" value="condition1"/>
      <property name="xpath" value="/body/myRequestMsg/person/name"/>
      <property name="comment" value="Name of person requesting service"/>
    </row>
  </table>
  <inputTerminal/>
  <outputTerminal>
    <wire targetNode="endAggregation"/>
  </outputTerminal>
  <outputTerminal name="policyError"/>
  <failTerminal/>
</node>
```