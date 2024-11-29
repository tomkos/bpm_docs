# Mediation policy patterns

The mediation policy processing model defines the result of processing
any combination of mediation policies. However, you can simplify the
implementation of mediation policies by following some basic rules
and patterns.

## Rules

- Have a single default mediation policy with no gate conditions.
This default mediation policy contains all module properties that
can be overridden, and is used when none of the conditional mediation
policies apply. When you export your Service Component Architecture
(SCA) module, WebSphere® Integration
Developer generates a default mediation policy for each property group
in your SCA module. Therefore, if you want to provide a dynamic override
for every dynamic property in your module, you can attach all the
default mediation policies to your SCA module. Note:  If
you attach all default mediation policies only to your SCA module,
all configuation is driven by mediation policies and any changes made
on the administrative console are ignored.
- Do not allow conflicts between mediation policies with gate conditions.

## Pattern one: Default mediation policies only

If
you want to provide a dynamic override for every dynamic property
in your module, when you administer WSRR you should attach all the
default mediation policies to your SCA module.

## Pattern two: Mutually exclusive gate conditions

- Have a single default mediation policy with no gate conditions
(the attachment has no conditions). This default mediation policy
contains all module properties that can be overridden, and is used
when none of the conditional mediation policies apply.
- Create gate conditions so that each gate condition represents
a distinct case; therefore, gate conditions are mutually exclusive,
and a maximum of one conditional mediation policy can be chosen. For
example, you could have one mediation policy with a gate condition
whose value is InsuranceType = "Gold", and another
mediation policy with a gate condition whose value is InsuranceType
= "Silver". For a particular message, the InsuranceType will
be either Silver or Gold, and the
appropriate mediation policy will be chosen.

## Example: Mutually exclusive gate conditions

The
following example shows three mediation policies attached to one module. Equally, the example could show three mediation policies
attached to one scope point of a target service. Two mediation
policies have a gate condition, and one mediation policy has no gate
conditions. The two mediation policies with a gate condition are mutually
exclusive.

- If the InsuranceType = "Gold", mediation policy
P1 is used.
- If the InsuranceType = "Silver", mediation policy
P2 is used and properties not mentioned by P2 are taken from mediation
policy P3.
- If the InsuranceType is neither Gold nor Silver,
mediation policy P3 is used.

Figure 1. Mutually exclusive gate conditions

<!-- image -->

## Pattern three: Distributing module properties to avoid
conflicts

- Have a single default mediation policy with no gate conditions
(the attachment has no conditions). This default mediation policy
is used when none of the conditional mediation policies apply.
- Create gate conditions so that more than one conditional mediation
policy might be used, but ensure that mediation policies that might
be merged have unique properties. For example, you could have one
mediation policy with a gate condition whose value is InsuranceType
= "Gold", another mediation policy with a gate condition
whose value is InsuranceType = "Silver", and yet
another mediation policy with a gate condition whose value is CustomerType
= "Student". For a particular message, the InsuranceType will
be either Silver or Gold, and the
appropriate mediation policy will be used. However, the mediation
policy associated with the gate condition CustomerType = "Student" might
need to be merged with the other conditional mediation policy; therefore,
it must contain unique module properties.

## Example: Distributing module properties to avoid conflicts

The
following example shows four mediation policies attached to one module. Equally, the example could show four mediation policies
attached to one scope point of a target service. Three mediation
policies have a gate condition, and one mediation policy has no gate
conditions. The conditional mediation policies that might be merged
have no overlapping module properties.

- If the InsuranceType = "Gold", mediation policy
P1 is used.
- If the InsuranceType = "Silver", mediation policy
P2 is used.
- If the CustomerType = "Student", mediation policy
P3 is used.
- If two conditional mediation policies are used, (either P1 andP3, or P2 and P3), no property appears more than once.
    - If P1 and P3 are used, Property\_A and Property\_B come
from P1 and Property\_C comes from P3.
    - If P2 and P3 are used, Property\_A comes from
P2, Property\_C comes from P3, and Property\_B comes
from P4.
- If no conditional mediation policies are used, mediation policy
P4 is used.

Figure 2. Distributing module properties to avoid conflicts

<!-- image -->