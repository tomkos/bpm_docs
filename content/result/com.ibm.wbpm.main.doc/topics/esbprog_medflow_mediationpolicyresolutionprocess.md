<!-- image -->

# The mediation policy resolution process

<!-- image -->

A mediation flow, built in IBM® Integration
Designer, contains a Policy Resolution
mediation primitive and some downstream mediation primitives with promoted properties. A
.ear file is generated from the mediation module and deployed to IBM Business Automation Workflow. The .ear file is also imported into WSRR and
mediation policy gate conditions are applied to the properties. When a message passes through the
mediation flow, at the Policy Resolution mediation primitive WSRR is checked to see whether any
policy documents associated with the mediation module have gate conditions that apply to some aspect
the current message. If so, information about the properties and the values to be set are extracted
from the policy document and written into the dynamic property context area of the SMO. Any
downstream mediation primitives that have promoted properties that correspond to items in the
dynamic property context area of the SMO will be updated with the appropriate values.

## Policy Resolution mediation primitive settings

You can use several parameters to configure the Policy Resolution mediation primitive.

The default behavior for the Policy Resolution mediation primitive module is to
search for mediation policies that are attached to the module containing the Policy Resolution
mediation primitive. The mediation flow module containing the Policy Resolution mediation primitive
must be exported as a .ear file and loaded into WSRR as an SCA module for the
function to work.

An alternative use is for the mediation primitive to search for mediation policies attached to a
Target Service; that is, a service to which the mediation containing the Policy
Resolution mediation primitive is going to call out. Information about the target service must be
loaded into WSRR and the service must have mediation policies attached to it.

You can load target service information into WSRR in several ways. One way is by using WSDLs that
describe the service or by loading an SCA module. In Target Service mode the Policy Resolution
mediation primitive looks at the /headers/SMOHeader/Target area of the SMO to
determine which entity to check for policy attachments. Although you can set this area of the SMO
manually (using a Message Element Setter mediation primitive), it is generally set by a Lookup
mediation primitive (such as an Endpoint Lookup, Gateway Endpoint Lookup or SLA Endpoint Lookup),
which obtains the target information for the current message context from WSRR.

There are three different scopes that policies can be attached to within the Target Service
scope. A policy can be attached to the whole service, it can be attached to a particular endpoint
(the port of a WSDL) or it can be attached to a particular operation.

If both Module and Target Service policies are available in WSRR then the mediation primitive can
use the Intersection of Module and Target Service, which combines both module and
target service mediation policies.

You can create policy conditions to apply mediation policies based on the message context. By
creating policy conditions you specify a part of the message whose value is then used to evaluate a
gate condition, the result of which determines whether a specific mediation policy must
be applied in this particular message context. The gate condition is created in WSRR and is applied
to a policy attachment on the SCA module. To create a policy condition first specify a policy
condition name. Creating a policy condition is important because it is the name that will be
used in the gate condition in WSRR.

A downstream mediation primitive might have a promoted property with an
Alias
LogRoot and Alias value
/body to specify how much of a message to log. This policy condition becomes
the default policy document for the mediation module when it is loaded into WSRR.

In WSRR you can create a policy document that sets the value of the downstream promoted property
LogRoot to a value of /body/custRequest/Customer. This
new policy can then be attached to the SCA module containing the Policy Resolution Mediation
primitive, which has been loaded into WSRR. A gate condition can be added to this policy attachment
with a condition CustomerType="Premium".

The gate condition checks the value associated with the condition name
CustomerType, which in this case is the message value at
/body/custRequest/Customer/type, against the value given in the gate
condition definition ("Premium"). If the condition evaluates to
true then this policy can be applied; if not, the policy is not
applicable in this context.

For this example, a message containing the body
/body/custRequest/Customer/type="Premium" would cause a downstream
mediation primitive with a promoted property called LogRoot to take the value
/body/custRequest/Customer, but for other messages the
LogRoot promoted property would take the value
/body.

WSRR can be used to govern the way that services are used. For example, a service might go
through lifecycle phases Development, Test and
Production, and WSRR can apply these lifecycle classifications to the service
during the appropriate phase. WSRR can then apply rules about how the service is to be used based on
the current classification. Classifications can be applied to policy documents in the same way.

The classifications are encoded as URIs. For example:

Development:
http://www.ibm.com/xmlns/prod/serviceregistry/6/1/GovernanceProfileTaxonomy#Development

Test:
http://www.ibm.com/xmlns/prod/serviceregistry/6/1/GovernanceProfileTaxonomy#Test

Production:
http://www.ibm.com/xmlns/prod/serviceregistry/6/1/GovernanceProfileTaxonomy#Production

For example, in the policy resolution mediation primitive you can add the Classification URI for
the lifecycle phase Development. This means that the mediation primitive
obtains policies from the policy document only if it also has the Development
classification attached to it.