# Example: mediation policy conditions

## Introduction

In order to implement the correct
mediation policy at run time, you need to understand how the properties
specified by the Policy Resolution mediation primitive interact with
the values of a particular message and the objects in the registry.

## Policy Resolution conditions

You can specify
mediation policy conditions in the Policy Resolution mediation primitive.
You specify where the mediation policy condition values are found
in the message, by providing XPath expressions.

| Mediation policy condition name   | XPath                     |
|-----------------------------------|---------------------------|
| InsuranceType                     | /body/input/insuranceType |
| Continents                        | /body/input/continents    |
| Days                              | /body/input/numberOfDays  |

## Registry conditions

In the registry, you
can load objects such as SCA modules and mediation policy documents.
When a mediation policy document specifies the objects to which it
applies (in this case an SCA module) WSRR creates a policy attachment
document. After a policy attachment document has been created you
can add user properties to it, and the runtime environment interprets
some of the user properties as necessary conditions. Only user properties
that begin with the string medGate\_ are used as conditions.

Figure 1. Example registry
conditions

<!-- image -->

## Runtime conditions

| Policy condition name   | XPath                     | Value in message   |
|-------------------------|---------------------------|--------------------|
| InsuranceType           | /body/input/insuranceType | Gold               |
| Continents              | /body/input/continents    | Europe             |
| Days                    | /body/input/numberOfDays  | 28                 |

| Mediation policy name   | Mediation policy condition   | Mediation policy condition met by the example message?   | All mediation policy conditions met by message?   |
|-------------------------|------------------------------|----------------------------------------------------------|---------------------------------------------------|
| P1                      | Continents = Asia            | No                                                       | No                                                |
| P1                      | Days > 14                    | Yes                                                      | No                                                |
| P2                      | Continents = Europe          | Yes                                                      | Yes                                               |
| P2                      | Days > 14                    | Yes                                                      | Yes                                               |
| P3                      | InsuranceType = Gold         | Yes                                                      | Yes                                               |