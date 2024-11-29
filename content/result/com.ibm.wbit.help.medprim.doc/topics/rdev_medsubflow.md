# Mediation subflows

## Introduction

A mediation subflow is created
with IBM® Integration
Designer and
consists of a set of mediation primitives wired together in the same
way as for a request or response flow. The mediation subflow is defined
as integration logic inside a mediation module. The logic encapsulated
inside the subflow can be started as part of any request or response
flow inside the module and can be reused in the module multiple times.
Alternatively, a mediation subflow can be defined in a library and
reused in multiple mediation modules that are dependent on that library.

## Details

IBM Integration
Designer is
used to define a mediation subflow inside the integration logic of
either a mediation module or dependent library. Unlike a request or
response flow, the inputs and outputs of a subflow are not tied to
specific interfaces. Instead, a subflow defines a number of in and
out nodes representing the inputs and outputs of the flow. These nodes
might or might not have message types associated with them. A subflow
is then started from a request or response flow via a Subflow mediation
primitive. Multiple Subflow mediation primitives can be associated
with the same subflow. The input and output terminals of the Subflow
mediation primitive correspond to the in and out nodes inside the
subflow. The Subflow mediation primitive also has a fail terminal
which is invoked should an error occur during the execution of the
subflow.

A subflow can contain the same mediation primitives
as a request or response flow with the exception of the Policy Resolution
mediation primitive which can only be used inside a top-level request
or response flow. In particular, a subflow can contain Subflow mediation
primitives allowing the nesting of one subflow inside another. Properties
on mediation primitives inside a subflow can be promoted in which
case they then appear as promotable properties on the associated Subflow
mediation primitives. If these properties need to be modified at run
time then they must be promoted up the hierarchy of Subflow mediation
primitives until they are promoted inside the top-level request or
response flow at which point they will appear as module properties.

In
a similar manner, Service Invoke mediation primitives inside a subflow
can define references to callout from inside the subflow invocation.
A Subflow mediation primitive associated with the subflow then performs
the mapping of the reference used by the Service Invoke mediation
primitive to a reference available in the module.

## Usage

Mediation subflows are used to encapsulate
integration logic. The following list gives some potential reasons
for wanting to perform this encapsulation:

- To reduce complexity of the request or response flows when viewed
in the Mediation Flow Editor.
- To enable reuse of integration logic on multiple parallel paths
through a mediation flow.
- To enable reuse of integration logic between request and response
flows inside a mediation module.
- To enable reuse of integration logic across mediation modules
by extracting the common logic to a subflow in a library.

## Properties

A mediation subflow is given
a name and namespace on creation. When a Subflow mediation primitive
is added to a flow, a mediation subflow is selected by this name and
namespace from those available in the current modules and its dependent
libraries.

Any promoted properties on mediation primitives
inside the subflow become properties of the Subflow mediation primitive.
This properties can be given new values allowing a subflow to be used
in multiple places with different values. Alternatively, the properties
can be promoted again until they reach the module level at which point
they can be modified at run time. When promoting properties from the
Subflow mediation primitive the original alias name can be retained
allowing a property on all instance of a subflow to me modified together.
Alternatively, a new alias name can be given each time enabling the
properties of each subflow instance to be overridden independently.

The names of any references contained inside the subflow
are also surfaced on the Subflow mediation primitive so that they
can be mapped to references available inside the mediation module
where the subflow is being used.

## Considerations

Correlation, transient and
shared context are propagated from the parent flow to a subflow and
back to the parent but there is currently no mechanism to define the
type of a context on a subflow. Consequently, a subflow should use
the Set Message Type mediation primitive to type a context before
use. Dynamic context is not propagated from a parent flow to a subflow
as the property names referred to by the context are those at the
module level not those applicable to the subflow.

Any Service
Invoke mediation primitives inside a subflow are required to wait
for a service response when the flow component is invoked asynchronously
with callback.