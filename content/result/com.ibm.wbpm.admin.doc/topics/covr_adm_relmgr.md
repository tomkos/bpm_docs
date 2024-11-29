<!-- image -->

# The relationship manager

## What is the relationship manager?

The relationship
manager allows you to configure, query, view, and perform operations
on relationship runtime data, including roles and their data. You
create relationship definitions with the relationship editor. At run
time, instances of the relationships are populated with the data that
associates information from different applications. This relationship
instance data is created when the maps or other IBM® Business Automation Workflow components
run and need a relationship instance. The relationship service exposes
a set of application programming interfaces (API's) to retrieve relationship
metadata and to create, retrieve, and manipulate the instance data.
The data is stored in the relationship tables that are specified in
the relationship definition. The relationship manager provides a graphical
user interface to interact with the relationships and relationship
instances.

For each relationship instance, the relationship manager can display a hierarchical listing of
its roles. Each role in the relationship has instance data, properties, and key attributes. The
relationship tree also provides detailed information about each of the roles in the relationship
instance, such as the type of entity, its value, and the date it was last modified. A relationship
instance ID is automatically generated when the relationship instance is saved in the relationship
table. The relationship manager displays this instance ID at the highest level of the relationship
tree.

## Using the relationship manager

- Browse and inspect the values for existing relationships
- Create and delete relationship instances
- Modify the contents of a relationship instance, such as adding
and deleting role instances
- Edit the data of a relationship role instance, including role
properties and logical state
- Roll back relationship instance data
- Activate and deactivate role instances
- Get role instances, given the key attribute, start and end date,
and property value
- Export an existing static relationship instance (from one platform)
to an RI or CSV file, then use the relationship manager to import
the RI or CSV file into a new environment (a different platform from
the first)
- Recover from problems if they occur. For example, when corrupted
or inconsistent data from a source application has been sent to the
generic and destination application relationship table, you can use
the relationship manager to rollback the data to a point in time when
you know the data is reliable

For more information about performing these tasks, see
the relationship manager online help.

## Displaying the relationship manager

Display
the relationship manager in the administrative console, by clicking Integration Applications > Relationship
Manager. From there, click Relationships to
view a list of relationships in the system, including the relationship
name, display name, and static and identity attributes. You can also
view detailed information for a selected role, including the relationship
name, role name, display name, property values, keys, role object
type, and managed attribute setting.