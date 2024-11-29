# Dynamic properties and mediation policies

## Introduction

Any property that you promote
on a mediation primitive is also a dynamic property, so
long as the property is in the top-level request, response, or fault
flow. Dynamic properties can be overridden, at run time, using
mediation policies in a registry. Although you can override promoted
properties dynamically, you must always specify a valid default value.

Promoted
properties have a group name, an alias name, a type, and value: all
of which you can set from WebSphere® Integration Designer.
Multiple promoted properties can be given the same alias name if they
are of the same type. You can see the promoted properties on the runtime
administrative console, and you can set the property values administratively.

When
you use mediation policies, the property group name is used to construct
the mediation policy namespace, and the alias name must map to an
assertion name in the mediation policy. For example, suppose a property
has an alias name of beforeRequestTransform and
a group of stockQuoteGroup. The mediation policy
refers to the property with the name beforeRequestTransform,
and uses the group stockQuoteGroup as the namespace
of the mediation policy assertion.

## SMO context

After mediation policy information
has been retrieved from the registry, the runtime environment stores
it in the dynamicProperty context of the service message object (SMO).
The information in the dynamicProperty context can be used to override
the values of promoted properties that come later in the flow.

| Element   | Value   | Description                                      |
|-----------|---------|--------------------------------------------------|
| group     | String  | The group name of the property to be overridden. |
| name      | String  | The alias name of the property to be overridden. |
| value     | String  | The value to be used.                            |
| type      | String  | The property type.                               |

## How to
override properties

1 From IBM Integration Designer:
    1. Promote the property you want to override.
    2. Set the elements of the property. Pay particular attention to
the group and the alias name.
    3. Add a Policy Resolution mediation primitive to your mediation
flow. Add it before the mediation primitive whose property you want
to override.
    4. If you want to retrieve
mediation policies for a target service, you should add an Endpoint
Lookup primitive to the mediation flow, before the Policy Resolution
primitive.
    5. Export the EAR file containing your Service Component Architecture
(SCA) module.
2 From WSRR:

1. Load the EAR file containing your SCA module. The registry creates
an SCA module document and object, and loads any default mediation
policies.
2. If you want to attach mediation
policies to target services, rather than to SCA modules, load the
WSDL document that represents your target services. The registry creates
objects for any service, port, binding, portType, operation, and message
elements described by the WSDL; you can attach mediation policies
to some of these objects. Tip: The runtime environment
supports mediation policies attached to service, port, binding, and
portType objects. However, the runtime environment does not support
mediation policies attached to operation or message objects.
3. If the default mediation
policies do not meet your requirements, create a suitable mediation
policy.
4. Attach a mediation policy to your SCA module
object or to an object associated with your WSDL.
3 From the administrative console:

1. Import the EAR file containing the SCA module.
2. Ensure that the server is using the correct registry instance.

When available, the mediation policy values take precedence
at run time. If a mediation policy is not found, or is unsuitable,
the runtime environment uses the promoted property values shown on
the administrative console.

If the dynamic override fails for
a particular mediation primitive, the fail terminal of that mediation
primitive is fired. A dynamic override can fail for a number of reasons.
For example, if you try to override the XSL stylesheet of the Mapping
mediation primitive, but the stylesheet cannot be found at run time.

## How to override properties using
a custom mediation

You can override a promoted property
without using WSRR by creating a custom mediation. In this example,
the Async timeout property of a Service Invoke primitive is
changed, determined by a value in the input message. The property
change applies only to the single invocation of the mediation primitive.

1. Set up your mediation flow to have your custom mediation wired
to a Service Invoke mediation primitive. The custom mediation must
be positioned before any primitive being dynamically configured by
it in the mediation flow.
2 In the Service Invoke mediation primitive, navigate to Properties > Promotable Properties . Promote the Async timeout property by updatingthe fields:
    1. Select the Promoted check box.
    2. Set the alias to ServiceInvoke1.asyncTimeout.
    3. Set the group to MyModule.
3. In the custom mediation, set the property dynamically by selecting Properties > Details and entering the following code sample:PropertyType property = ServiceMessageObjectFactory.INSTANCE.createPropertyType();
// The alias for the promoted property for the async timeout of the service invoke
property.setName("ServiceInvoke1.asyncTimeout");
// Use the new value for the async timeout (in seconds) from the specified location in the message.
property.setValue(((DataObject)smo).get("/body/operation1/input1/field1"));
DynamicPropertySetType dynamicPropertySet = ServiceMessageObjectFactory.INSTANCE.createDynamicPropertySetType();
// The group of the promoted property
dynamicPropertySet.setGroup("MyModule");
dynamicPropertySet.getProperties().add(property);

DynamicPropertyContextType dynamicPropertyContext = ServiceMessageObjectFactory.INSTANCE.createDynamicPropertyContextType();

dynamicPropertyContext.getPropertySets().add(dynamicPropertySet);

smo.getContext().setDynamicProperty(dynamicPropertyContext);Tip: All the property values are loaded as Strings. However,
an integer must still be entered as a whole number.