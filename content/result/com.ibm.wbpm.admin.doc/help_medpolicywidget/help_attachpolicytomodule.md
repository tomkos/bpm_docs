<!-- image -->

# Modules: Attaching existing mediation policies to modules

## Before you begin

1. Use IBM Integration Designer to create a module containing a Policy Resolution mediation
primitive.
2. Deploy the module to Process Server.
3. Ensure that Process Server has a definition for the WSRR that you want to use.
4. Load the enterprise archive (EAR) file, containing your module, into WSRR.
5. Create a business space that contains the Module Browser widget and the
Mediation Policy Administration widget.

## About this task

You can control service requests dynamically by using mediation policies to override module
properties at run time. Such mediation policies are stored in WSRR. You can define one or more
mediation policies for your module, and each mediation policy can override one or more module
properties. Optionally, you can create one or more gate conditions on each policy attachment. When
service requests are processed, gate conditions are compared to the condition values in the message.
All the gate conditions must be met before an associated mediation policy can be used.

## Procedure

1. Log in to your business space and navigate to the space that you created for administering
mediation policies associated with modules.
2. From the Module Browser widget, select Mediation
Policies.
The Mediation Policy Administration widget is refreshed. If there
are existing policy attachments they are displayed.
3. If you have more than one WSRR definition, select the definition used by your module.
4. Enter the name of the New policy attachment. 
Mediation policy attachments associate a mediation policy with a module. In WSRR, the
mediation policy and policy attachment are separate objects.
5. Click Create
The Mediation Policy Administration widget is refreshed. You can now
specify the group of properties you want to work with, and the name of an existing mediation policy
for that group.
6. Select a Group name. 
Each group contains module properties. Select the group whose property values you want to
override.
7. Click Use existing.
8. Select a mediation policy from the Select a policy menu. 
 The mediation policies displayed depend on the group you selected.
9. Click Next
The Mediation Policy Administration widget is refreshed. You can now add
gate conditions. Note: You cannot edit mediation policy assertions after you create a mediation
policy in a business space. However, because gate conditions exist on the mediation policy
attachment, you can add gate conditions when you create a new policy attachment.
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
11. Click Save.

## Results

In WSRR, a policy attachment is created that associates the selected mediation policy with the
selected module.

The Mediation Policy Administration widget is refreshed, and the new policy
attachment is added to the list of policy attachments.