<!-- image -->

# Identity relationships versus non-identity relationships

In an identity relationship there is a unique mapping between the key attributes
of Role A to the key attributes of Role B within the same instance.
Instance means the instance of role data in the relationship service
runtime environment (essentially a table containing data - instances are one
row of that table).

There are also combined keys allowed in identity relationships.
Combined keys are represented by several key attributes defined for one role.
An exception for combined keys is the managed role of the identity relationship.
The managed role of the identity relationship must have only one key attribute
defined, there are no combined keys allowed for the managed role.

During the creation of the relationships, the differences are not overtly
apparent. You do not need a managed role for a non-identity relationship and
it is also not recommended to use a managed role. The main difference is that
during runtime the mapping of the key attribute values is not unique. This
means the key attribute LastName in Role A may have the value "Doe"
specified, which will be mapped to key attribute GivenName in Role B with
the values "John", "Mary", "George".
This would be a one-to-many mapping. In non-identity relationships, there
are also combined keys allowed as in identity relationships.