# Mediation policy processing model

## Introduction

The mediation
policy model describes how the runtime environment calculates the effective mediation
policy for a particular scope, and when the runtime environment applies
intersection rules. For a summary of the Web Services Policy
1.5 Framework terminology, see the end of this topic.

1. If the Policy Resolution primitive has a Policy Scope property
of Module or Intersection,
the runtime environment calculates the effective policy for the SCA
module. To calculate the effective policy, the runtime environment
must merge the mediation policies that belong to the
module.
2 If the Policy Resolution primitive has a Policy Scope propertyof Target Service or Intersection ,the runtime environment calculates the effective policy for the targetservice. To calculate the effective policy, the runtime environmentmust merge the mediation policies that belong to thetarget service.Note: If you want to use more than one WSRR objecttype to represent the target service, you should always attach mediationpolicies to the most granular scope point. For example, because aportType can apply to more than one binding, any mediation policiesyou attach to the portType should contain assertions that are bindingindependent. Be aware that by using more than one WSRR object typeto represent the target service, you can significantly increase thelevel of complexity. The Web Services Policy 1.5 framework statesthat an effective policy is calculated for each policy subject ,and the effective policies are then merged. Therefore, if you definemediation policies for all the target service scope points that aresupported, the runtime environment would take the following actions:
    1. Calculate the effective policy for the endpoint policy subject,
by merging the mediation policies attached to the port, binding, and
portType objects.
    2. Calculate the effective policy for the service policy subject,
by merging the mediation policies attached to the service object.
    3. Merge the effective policy of the endpoint policy subject with
the effective policy of the service policy subject. If property values
conflict, the effective policy of the endpoint policy subject takes
precedence.
3. If the Policy Resolution primitive has a Policy Scope property
of Intersection, the runtime environment applies
policy intersection rules to determine if the two effective policies
are compatible (according to the Web Services Policy 1.5 framework).

## Hierarchy of mediation policies

1. Mediation policies with gate conditions have the highest precedence.
Therefore, property values defined by these mediation policies have
the highest precedence. Note: Before a mediation policy with gate
conditions can be further evaluated, all of the gate conditions must
be met.
2. Mediation policies without gate conditions have a lower precedence.
Therefore, property values defined by these mediation policies have
a lower precedence.

Administrative console values are used if there is no
suitable property in a mediation policy.

## Merging mediation policies

If multiple mediation
policies (at the same precedence) contain the same dynamic property,
the mediation policies are merged. In this case, the value of the
property must be the same in all the merged mediation policies. Any
mismatch is termed a policy error, which means that there is no mediation
policy for that policy merge.

1 Process the highest-precedence mediation policies.
    1. Merge the mediation policies.
    2 If any property occurs in multiple mediation policies, the valueof the property must be the same in all mediation policies.
        - If there are no property mismatches, the values of the properties
are stored in the service message object (SMO).
        - If there are property mismatches, no properties from this precedence-level
are used. Note: Policy processing continues to the lower-precedence
mediation policies, but when that processing is complete the output
will be sent to the policyError terminal.
2 Process the lower-precedence mediation policies.

1. Merge the mediation policies.
2 If any property occurs in multiple mediation policies, the valueof the property must be the same in all mediation policies.
    - If there are no property mismatches, the values of the properties
are stored in the SMO, unless they have already been set by the highest-precedence
mediation policies.
    - If there are property mismatches, no properties from this precedence-level
are used. Note: If a property has been successfully set in the highest-precedence
policies, but it causes a mismatch in the lower-precedence policies,
the normal rules apply. Because there has been a policy merge error,
no mediation policies from the lower-precedence level are used; the
output will be sent to the policyError terminal.
The value from the highest-precedence policies is used.

Any dynamic property that has not been assigned a value
from a mediation policy document, is assigned the value shown by the
administrative console.

## Example: Successful merge

The following
example shows a successful merge of mediation policies, attached to
an SCA module.

- Property\_1
- Property\_2
- Property\_3
- Property\_4
- Property\_5

- Policy\_X, with associated conditions
- Policy\_XX, with associated conditions
- Policy\_Y, with no associated conditions

| Mediation policy precedence                | Mediation policy name                      | Promoted property: alias name   | Promoted property: value   | Use this promoted property value   | Merged mediation policy values   | Properties used for message flow   |
|--------------------------------------------|--------------------------------------------|---------------------------------|----------------------------|------------------------------------|----------------------------------|------------------------------------|
| Highest precedence: with conditions        | Policy\_X                                   | Property\_1                      | A                          | Yes                                | Property\_1 = A                   | Property\_1 = A                     |
| Highest precedence: with conditions        | Policy\_X                                   | Property\_2                      | B                          | Yes                                | Property\_2 = B                   | Property\_2 = B                     |
| Highest precedence: with conditions        | Policy\_XX                                  | Property\_3                      | C                          | Yes                                | Property\_3 = C                   | Property\_3 = C                     |
| Lower precedence: without conditions       | Policy\_Y                                   | Property\_1                      | D                          | No                                 |                                  |                                    |
| Lower precedence: without conditions       | Policy\_Y                                   | Property\_4                      | E                          | Yes                                | Property\_4 = E                   | Property\_4 = E                     |
| Administrative console promoted properties | Administrative console promoted properties | Property\_1                      | F                          | No                                 |                                  |                                    |
| Administrative console promoted properties | Administrative console promoted properties | Property\_2                      | G                          | No                                 |                                  |                                    |
| Administrative console promoted properties | Administrative console promoted properties | Property\_3                      | H                          | No                                 |                                  |                                    |
| Administrative console promoted properties | Administrative console promoted properties | Property\_4                      | I                          | No                                 |                                  |                                    |
| Administrative console promoted properties | Administrative console promoted properties | Property\_5                      | J                          | Yes                                |                                  | Property\_5 = J                     |

## Example: Unsuccessful merge

The following
example shows an unsuccessful merge of mediation policies, attached
to an SCA module.

- Property\_1
- Property\_2
- Property\_3
- Property\_4
- Property\_5

- Policy\_X, with associated conditions
- Policy\_XX, with associated conditions
- Policy\_XXX, with associated conditions
- Policy\_Y, with no associated conditions

| Mediation policy precedence                | Mediation policy name                      | Promoted property: alias name   | Promoted property: value   | Use this promoted property value   | Merged mediation policy values   | Properties used for message flow   |
|--------------------------------------------|--------------------------------------------|---------------------------------|----------------------------|------------------------------------|----------------------------------|------------------------------------|
| Highest precedence: with conditions        | Policy\_X                                   | Property\_1                      | A                          | No                                 |                                  |                                    |
| Highest precedence: with conditions        | Policy\_X                                   | Property\_2                      | B                          | No                                 |                                  |                                    |
| Highest precedence: with conditions        | Policy\_XX                                  | Property\_1                      | C                          | No                                 |                                  |                                    |
| Highest precedence: with conditions        | Policy\_XXX                                 | Property\_3                      | D                          | No                                 |                                  |                                    |
| Lower precedence: without conditions       | Policy\_Y                                   | Property\_1                      | D                          | Yes                                | Property\_1 = D                   | Property\_1 = D                     |
| Lower precedence: without conditions       | Policy\_Y                                   | Property\_4                      | E                          | Yes                                | Property\_4 = E                   | Property\_4 = E                     |
| Administrative console promoted properties | Administrative console promoted properties | Property\_1                      | F                          | No                                 |                                  |                                    |
| Administrative console promoted properties | Administrative console promoted properties | Property\_2                      | G                          | Yes                                |                                  | Property\_2 = G                     |
| Administrative console promoted properties | Administrative console promoted properties | Property\_3                      | H                          | Yes                                |                                  | Property\_3 = H                     |
| Administrative console promoted properties | Administrative console promoted properties | Property\_4                      | I                          | No                                 |                                  |                                    |
| Administrative console promoted properties | Administrative console promoted properties | Property\_5                      | J                          | Yes                                |                                  | Property\_5 = J                     |

## Terminology

Web services
policy terminology is described in the Web Services Policy 1.5
Framework and in the Web Services Policy 1.5 Attachment;
in addition, the mediation policy model uses some further terms.

- Module
- Service
- Port
- Binding
- PortType