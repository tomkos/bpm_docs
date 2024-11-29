<!-- image -->

# Relationships

When source and destination business objects contain equivalent
data that is represented differently, the transformation step employs
a relationship. A relationship establishes an association between
data from two or more business objects. Each business object is called
a participant in the relationship.  Each participant in a relationship
is distinguished from other participants based on the function (otherwise
known as role) they serve in the given relationship. Hence,
a relationship will contain a list of roles. The data that you typically
transform using relationships are ID numbers (such as order ID or
product ID) and other values represented as codes (such as country,
currency, or marital status).

For example, if a SAP application uses sequential integers for
Contact IDs, and Clarify application uses generated contact codes,
the SAP Contact number could be 806 and the Clarify
Contact Number may be generated as A100. To transfer
Contact ID data between these two applications, you can create a relationship
among the SAP application's contact business object, the generic
contact business object, and Clarify application's contact business
object based on the ID (Key).

- Car (Ferrari)
- Owner (John)

- John owns Ferrari
- Sara owns Mazda
- Bob owns Ferrari

## Relationship definitions

Relationships are important for mappings if no rule is
applicable to cover the mapping. For example, a product relationship of two different back-end
systems maps a product of System A to a product of System B. System A, however, has a different
indexing system for their products than System B. Therefore, a relationship is needed as a simple
mapping rule may not cover that particular mapping.

## Role definitions

A role describes how entities
can participate in a given relationship. That is, these role definitions
are used to capture structure and constraint requirements on participating
entities and their manner of participation. For example in an employment
relationship, the roles are employer and employee. A role has a set
of properties/attributes specified for its semantics.

Roles
have exactly one role object defined which represent the data
type. Each role may have one to several key attributes defined,
which represent attributes of the data type that are important for
the relationship.

These role definitions are used to capture
structure and constraint requirements for participating entities and
their manner of participation. For example, in a product relationship,
the roles would be the product of System A and the product of System
B. Each role would have defined the product number as an attribute
which uniquely identifies the product in the system.

## Relationship instance data

The
information in this topic deals with the pre-population of instance
data, which is used in the runtime environment. The pre-population
of instance data is used for lookup relationships which transform
data attributes according to a static mapping. For working on relationship
instance data, there is a property page in the relationship editor
for the relationship in case the relationship type is set to static
in the New Relationship wizard.

## Relationship definition versus relationship instance

## Role definition versus Role instance (Participant)

- Relationships in Network Deployment environments

Relationships can be used in Network Deployment (ND) environments without any extra configuration.