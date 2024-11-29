# Promoted and dynamic properties

## Introduction

Certain properties lend themselves
to being administratively configured. Other properties are not suitable
for administrative configuration, typically because modifying them
affects the mediation flow in such a way that you need to redeploy
the module or mediation module. IBM Integration Designer lists the
properties you can choose to promote under the promoted properties
of a mediation primitive. You can also promote properties of the callout
node.

For mediation primitives contained in
a subflow, promoting a property results in the creation of a corresponding
property on each Subflow mediation primitive that refers to that subflow.
The property can then be promoted again until eventually it reaches
the top level request, response, or fault flow.

Any property
that you promote from a primitive in the top level request, response,
or fault flow is also a dynamic property. A dynamic property can be
overridden, at run time, using a mediation policy. Although you can
override promoted properties dynamically, you must always specify
a valid default value.

## Alias names

Promoted properties have an
alias name which, for a mediation primitive in the top level request,
response, or fault flow, is the name displayed on the runtime
administrative console. For a mediation primitive in a subflow, the
alias name is the name by which the property is known in the parent
flow. You can set the alias name and the alias value from IBM Integration
Designer. Multiple promoted properties can be given the same alias
name if they are of the same type. In one module or mediation
module, promoted properties that have the same alias name and group
use the same value.

Generally, you should choose a suitable
alias name for your promoted properties rather than accept the default
name: choosing a suitable name helps you identify properties at run
time. For example, suppose that you have a single mediation flow component
containing one Service Invoke mediation primitive in the request flow,
and one Service Invoke mediation primitive in the response flow. If
you accept the default alias names, you cannot distinguish between
the promoted properties of the two Service Invoke primitives in the
administrative console.

If you use a mediation policy, with
your mediation flow, the mediation policy must refer to a property
using its alias name.

## Property groups

Promoted properties belong
to a group, and are displayed in their group on the runtime administrative
console.

By default, the group name is the mediation flow component
name, but you can override the default group name.

At integration
time, you can use property groups to create collections of properties.
For example, suppose you have two mediation flow components in one
mediation module. If each component has a Message Logger primitive,
you could promote both of the Enabled properties
to the same group. If the two promoted properties have the same alias
name then, at run time, you could administer the Enabled properties
together.

Alternatively, two promoted properties can have the
same alias name but be in different groups. At run time, you could
then set the property values separately.

- Promoted properties table

Mediation primitives have properties, and some of these properties can be made visible to the runtime administrator by promoting them. This section shows the properties you can promote.
- Dynamic properties and mediation policies

Dynamic properties can be overridden, at run time, using mediation policies.