<!-- image -->

# Business Rule Group Properties

All properties are of type string and defined as name-value pairs. Each property can only be
defined once in a business rule group. For each property defined, it must have a value also defined.
The property value can be an empty string or zero in length, but not null. Setting a property to
null is the same as deleting the property.

The properties on a business rule group can also be accessed in a rule set or decision table at
run time. This allows a single value to be set at the business rule group to be used within multiple
rule sets or decision tables in the business rule group. Only those properties defined on the
business rule group are available to enclosed rule sets and decision tables.

There are two types of properties, system and user-defined. The number of system or user-defined
properties is not limited on a business rule group. The system properties are used to hold specific
component information such as the version of the rule model used in defining the rule logic. This
system information is exposed in properties to allow for query across these fields. The system
properties begin with a prefix IBMSystem and are read-only through the business rule group and
property classes. System properties cannot be added, changed or deleted. An example of a system
property is:

| Property Name    | Property Value   |
|------------------|------------------|
| IBMSystemVersion | 6.2.0            |

User-defined properties are available to be used for holding any customer specific information
and can also be used in queries for business rule groups. User-defined properties are available for
read-write.

The properties for a business rule group can be retrieved either individually or as a list
(PropertyList object). With the PropertyList, methods are provided for retrieving individual
properties and adding and removing user-defined properties.

Figure 1. Class diagram of Property and related classes

<!-- image -->