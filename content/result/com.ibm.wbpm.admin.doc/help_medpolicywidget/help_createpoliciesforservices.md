<!-- image -->

# Services: Creating mediation policies for services

## Before you begin

1. Use IBM Integration Designer to create a module containing a Policy Resolution mediation
primitive.
2. Deploy the module to Process Server.
3. Ensure that Process Server has a definition for the WSRR that you want to use.
4. In WSRR, load the enterprise archive (EAR) file containing your module. Also, load the WSDL
documents for the services that you want to attach mediation policies to.
5. Create a business space that contains the administration widgets you need, including the
Service Browser and Mediation Policy Administration
widgets.

## About this task

You can control service requests dynamically by using mediation policies to override module
properties at run time. Such mediation policies are stored in WSRR. You can define one or more
mediation policies for services used by your module, and each mediation policy can override one or
more module properties. Optionally, you can create one or more gate conditions on each policy
attachment. When service requests are processed, gate conditions are compared to the condition
values in the message. All the gate conditions must be met before an associated mediation policy can
be used.

## Procedure

1. Log in to your business space and navigate to the space that you created for administering
services.
2. From the Service Browser widget, if the correct WSRR definition is not
displayed select the correct WSRR definition. 
If your application server has definitions for more than one instance of WSRR, you can display
the services that are defined on each WSRR. 
 The list of services is refreshed.
3 Select the level at which you want to create a mediation policy. You can attach a mediation policy at the level of the service, endpoint, or operation. The Mediation Policy Administration widget is refreshed. Thefollowing information is displayed:
    - The name of the service, endpoint, or operation that you selected.
    - The WSRR definition that you selected.
    - Any policy attachments that exist for the service, endpoint, or operation that you selected.
4. Enter the name of the New policy attachment. 
Policy attachments associate a mediation policy with a target service. In WSRR, the mediation
policy and the policy attachment are separate objects.
5. Click Create
The Mediation Policy Administration widget is refreshed. You can now
specify the group of properties you want to work with, and the name of the new mediation policy.
6. Select a Group name. 
Each group contains module properties. Select the group whose property values you want to
override.
7. Enter a name in the New policy field. 
This is the name of the mediation policy you want to create and attach to the service,
endpoint, or operation.
8. Click Next

The Mediation Policy Administration widget is refreshed. You can now add
assertions and gate conditions. Note: You cannot edit assertions in a business space after you
create a mediation policy. Therefore, you must add all the assertions that you require before you
save the mediation policy.
9 Define one or more assertions. Assertions are module properties that the mediation policy can override. In WSRR, the moduleproperties that you want to override appear as policy assertions. Note: The widget requires eachpolicy attachment to have at least one assertion.

1. Select a Property name. 
The name is the alias name of the property. The alias name identifies the property in the
mediation flow.
2. Enter a suitable value in the Value field; for example,
All or 10 or
/body/input/address.
When available, the policy value takes precedence at run time. If a policy is not found, or is
unsuitable, the runtime environment uses the promoted property value.
3. Click Add Assertion.
10 Optional: Define one or more gate conditions. Gate conditions must be met before the policy can be used. In WSRR, gate conditions are userproperties on the policy attachment object.

1. Enter a gate condition name in the Gate condition name field.
The name of a gate condition is always prefixed with the string
medGate\_.
2 Enter a gate condition value in the Value field. The gate condition value is made up of the following parts: policy conditionname , operation and gate value .
    - The policy condition name you enter must map to a Policy condition
name in the module.
    - The operation can be: = , != ,
> , < , <= or
>= .
    - The gate value is the value being compared, for example, country =
France.
3. Click Add Gate Condition.
11. Optional: 
If you want to delete an assertion or gate condition, click the delete icon of the appropriate
assertion or gate condition.
If you hover over an assertion or gate condition, the delete icon, a cross, appears at the end
of the row.
12. Click Save.

## Results