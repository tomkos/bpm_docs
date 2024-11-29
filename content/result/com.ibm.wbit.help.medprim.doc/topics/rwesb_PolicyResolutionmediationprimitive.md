# Policy Resolution mediation primitive

## Introduction

You can use the Policy Resolution
mediation primitive to retrieve mediation policies from a WSRR registry,
and control mediation primitives that come later in the flow. The
registry can be local or remote.

The Policy Resolution primitive
lets you retrieve mediation policies associated with the current Service
Component Architecture (SCA) module. You can also retrieve mediation
policies associated with a target service used by the mediation flow.
If you want to retrieve mediation policies associated with a target
service, add an Endpoint Lookup primitive to the mediation flow before
the Policy Resolution primitive. The Endpoint Lookup primitive selects
the target service and the Policy Resolution primitive retrieves mediation
policies attached to the target service.

## Details

If valid mediation policies are
found in the registry, their contents can be used to override the dynamic
properties of mediation primitives that come after the Policy
Resolution primitive. If a mediation flow contains the Policy Resolution
primitive, any promoted property that is in the top-level request,
response, or fault flow is a dynamic property. Mediation policies
contain the equivalent of promoted property groups, names, and values,
and must conform to the Web Services Policy Framework (WS-Policy).

- If you set the Policy Scope property to Module,
then the Policy Resolution primitive retrieves mediation policies
that are attached to an SCA module object, in WSRR.
- If you set the Policy Scope to Target
Service, then the Policy Resolution primitive retrieves
mediation policies that are attached to WSRR objects representing
the target service. When you load a WSDL document into WSRR, the registry
creates objects for any service, port, binding, portType, operation,
and message element described by the WSDL. When you load an SCA
module into WSRR the registry creates objects for the module and any
exports and imports defined in the module. The term target
service encompasses all the relevant definitions included in
a WSDL description and SCA exports. Generally, you should
choose one point at which to attach mediation policies, for example,
you might choose to attach policies to service objects or operation
objects. Note: The runtime environment supports mediation policies
attached to service, port, binding, portType ,
and operation objects defined in WSDL documents. However,
the runtime environment does not support mediation policies attached
to message objects. For SCA modules, the runtime environment
supports mediation policies attached to exports, the interface portType,
and operations that are linked to the export. The runtime environment
also supports mediation policies attached to the WSRR objects Manual
HTTP Endpoint with associated Interface, Manual JMS Endpoint
with associated Interfaceand Manual MQ Endpoint with associated
Interface, and the interface portType and operations that are
linked to these Manual Endpoints.
- If you set the Policy Scope to Intersection,
then the Policy Resolution primitive retrieves mediation policies
that are attached to both the module and the target service, in WSRR.
The Policy Resolution primitive combines both scopes into a single
mediation policy that meets the requirements of both. If the intersection
processing cannot find a policy that meets both requirements, the policyError terminal
is fired.

## SMO details

If there are mediation policies
attached to either the current module or to the target service, they
are analyzed according to the mediation policy processing model. The
resulting property information is copied to the SMO at location /context/dynamicProperty.
For each property, the /context/dynamicProperty location
stores the group, name, and value. The property group and name are
compared to dynamic properties in later mediation primitives. When
a match occurs, the value of the dynamic property is overridden. For
example, you create a module that contains one mediation flow component,
and the component contains two mediation primitives: a Policy Resolution
primitive followed by a Mapping mediation primitive. If you promote
the Mapping primitive property, Mapping file,
you can override the value at run time, using mediation policies in
your registry.

Any dynamic properties not overridden by mediation
policies take the values shown on the administrative console. However,
the administrative console values are not stored in the /context/dynamicProperty location.

- The Endpoint Lookup primitive updates the Target field of the
SMO to indicate the target service for the flow, then the Policy Resolution
primitive retrieves the mediation policies associated with the target
service. The Endpoint Lookup primitive puts the target service details
in the SMO at location /headers/SMOHeader/Target,
and the Policy Resolution primitive uses this information.
- If the Endpoint Lookup primitive provides alternate target services,
you can use one of them as your target service provided you move the
appropriate object to the correct location in the SMO. The Endpoint
Lookup primitive puts alternate target services at location /headers/SMOHeader/AlternateTarget.
If you want the Policy Resolution primitive to use an alternate target
service, you must move a complete AlternateTarget object
to the SMO location /headers/SMOHeader/Target. To
move the AlternateTarget object requires you to insert
another mediation primitive, between the Endpoint Lookup primitive
and the Policy Resolution primitive. Typically, you might insert a
Custom Mediation primitive.
- Do not change the fields inside the Target or AlternateTarget objects
because these fields are used by the Policy Resolution primitive.
The primitive uses these fields to locate the mediation policies belonging
to the target service.

## Mediation policy conditions

- In IBM Integration Designer, set an XPath expression in the XPath property.
The XPath expression is used by the runtime environment to find the
value of the condition. You can specify more than one XPath expression.
- For each XPath expression, provide a condition name using the Policy
condition name property.
- In WSRR, create a gate condition using the Policy condition
name property. For example, if you create a Policy
condition name called InsuranceType,
you could create a gate condition called medGate\_Condition1 with
a value of InsuranceType = Gold. For more information
on creating mediation policies and gate conditions, see the tutorials
referred to at the end of this topic.

## WSRR

Before you use the Policy Resolution
mediation primitive you might need to add SCA modules, WSDL documents,
mediation policies, and mediation policy attachment documents to your
WSRR registry. You can create mediation
policies using WSRR, directly. Alternatively, you can create mediation
policies using Business Space widgets, and the widgets create the
mediation policies in WSRR. IBM Process Server includes Business Space
widgets for creating mediation policies.

To retrieve mediation
policies for the current module, the details of your SCA module must
exist in the appropriate registry. When you load an SCA module into
WSRR, the registry creates an SCA module document. The registry also
creates an SCA module object to which you can attach mediation policies.

When
you export an SCA module containing a Policy Resolution mediation
primitive, Integration Designer generates a default mediation policy
for each property group in your SCA module. For example, if your SCA
module contains three property groups, Integration Designer generates
three default mediation policies each containing all the dynamic properties
belonging to one group. The default mediation policies represent the
values given to all dynamic properties, at development time. Although
Integration Designer generates default mediation policies, it does
not attach them to the SCA module. You must decide how to use the
default mediation policies. If you load an EAR file containing your
SCA module into WSRR, the registry creates an SCA module document
and loads any default mediation policies. If you create your own mediation
policies, they must refer to the group and alias names of your dynamic
properties.

- Because mediation policies override module properties, the policy
creation process needs module information even if the policy is going
to be attached to a target service. If you load your SCA modules onto
a different WSRR instance to your WSDL documents, you might need to
copy a suitable policy from one WSRR instance to the other.
- The Web Services Policy Framework specifies that policies can
exist at different levels of the target service. The WS-Policy Framework
calls these levels the policy subject. The levels are:
service, endpoint, operation, and message. The endpoint level contains
port, binding, and portType. In the interests of simplicity, you should
attach mediation policies to either port or binding or portType; not
to multiple types of object. If you use
the Mediation Policy Administration widget, any mediation policies
you attach to the endpoint subject are attached to the portType.
- WSRR creates two types of operation objects: portType operation
objects and binding operation objects. For a particular endpoint,
use the operation type that is relevant to you, do not use both types. If you use the Mediation Policy Administration
widget, any mediation policies you attach to the operation subject
are attached to the operation portType.

When
you have the mediation policies you need, you can attach them to your
SCA module or your target service. If you want to specify
gate conditions on a mediation policy, you must specify them on the
policy attachment in WSRR.

If you want to use WSRR governance
you must make your WSRR policy document governed. Then you can move
the policy document, and any associated policies, through the lifecycle
classifications. If you want to use classifications that are not related
to governance, you must add classifications to the WSRR policy, not
the policy document. In WSRR, there is a default governance lifecycle,
but you can define your own. If you want to filter mediation policies
according to particular WSRR classifications, including lifecycle
classifications, you must also define the classifications on the Policy
Resolution primitive.

## Usage

Using mediation policies, you can
develop new service interactions that achieve greater levels of flexibility
and administrative control. In addition, you can get new value out
of existing systems by adjusting message flows according to the context
in which they occur.

When you design your mediation flow, any
mediation primitive that occurs after the Policy Resolution primitive
can have its dynamic properties overridden, using values from mediation
policies. However, you must specify a valid default value for every
property you want to override. Generally, you put a Policy Resolution
primitive at the start of the flow, except when you need other
mediation primitives, typically the Endpoint Lookup primitive.

- Use mediation policies to activate or deactivate properties. For
example, you could turn off message filtering by unsetting the Enabled property
of the Message Filter primitive.
- Use conditional mediation policies, which apply when particular
conditions exist. For example, you apply different message transformations
depending on different customer types: one transformation for gold
customers and another transformation for silver customers. The mediation
policies will contain a different value for the Mapping primitive Mapping
File property, depending on the customer type.

WSRR has many classification systems, including lifecycle
classifications, and you can select mediation policies based on their
WSRR classification. Lifecycle classifications allow you to impose
governance on your policies, or create your own classification systems.

- Policy Resolution mediation primitive properties

You can specify values for mediation primitive properties either by using the property fields in the IBM® Integration Designer user interface or by using an XML format. The property field names displayed in IBM Integration Designer are generally different from the property names used when building a mediation flow using XML code. In the following information, icons are used to identify each property name used in IBM Integration Designer and the corresponding XML name. (Where applicable, XML names that are required, but not shown in IBM Integration Designer, are also described.)
- Mediation policy patterns

Mediation policy patterns can simplify the implementation of mediation policies. This topic describes some basic patterns to use with mediation policies.
- Mediation policy processing model

The mediation policy processing model explains the conditions under which information is taken from mediation policies and applied to message flows.
- Example: mediation policy conditions

This example shows you how the Policy Resolution mediation primitive and the registry files interact.