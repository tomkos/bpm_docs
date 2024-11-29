<!-- image -->

# Managing relationship instances

You can view detailed
information for the selected relationship instance, including the relationship name, relationship
instance ID, property values, participating roles, and role instance values (role instance ID,
logical state, key attributes, and property values). You can view multiple roles
concurrently.

When a relationship instance is
no longer needed, you can delete it.

- Relationship instances which are created during the given period
get deleted (hard delete) from the database.
- Relationship instances which are activated get deleted (hard delete)
from the database.
- Relationship instances which are deactivated in the given time
period get activated.

If there are existing relationship instances in the
database, existing relationship instances and newly imported relationship
instances will be merged. If the relationship definition that you
are importing does not exist, a RelationshipUserException will be
thrown.

For more information on these tasks, see the relationship manager
online help.