# Adding and managing properties

## About this task

In Case Builder, you have the
flexibility to generate new properties or reuse existing ones from the target object store. Reused
properties remain unchanged and retain their original configuration throughout the solution
deployment process. You can select from a range of reusable properties and apply sorting or
filtering based on criteria such as name, unique ID, or type.

- Adding properties to a case solution
- Adding properties to a case type, document class, or task
- Adding one or more task preconditions
- Deleting case properties

## Adding properties to a case solution

### About this task

### Procedure

1 In the solution page, click Data > PropertyDefinitions , then click Add Property and selecteither New or Reuse Property . Note:
    - You
can reuse String, Integer, Boolean, Float, and DateTime type properties. You cannot reuse a property
that is of type Business Object. You cannot use multi-value properties that are configured as unique
and unordered or as hierarchical choice lists.
    - To reduce the amount of space that is
used by properties, reuse existing properties as much as possible. When you select
Reuse Property, you can select one or more properties that exist in Content Platform Engine.
    - If necessary, create new properties. To reduce the amount of space that is used by properties,
see the tips in Minimize database row sizes.
2. Define property values. The displayed property value fields vary based on the
property type. Single properties have default values, and certain property types, such as float and
integer properties, have specific minimum and maximum values. If no default value is assigned to a
Boolean property in the solution design, the corresponding case instance Boolean property is without
a value or has the value of None. This condition holds true even if a
default value is not designated for a Boolean property in the solution design.
3. Optional: If the types are a match, when you designate a property as a choice
list, the choice list of a reused property can be added to the solution.  
To create a new choice list, on the Properties page, click Manage
Choice Lists and define choice list values. IBM® Business Automation
Workflow does not prevent you from
entering duplicate values in a choice list. For example, assume you add First
as a choice item and assign the value as 1. You then add
Primary as another choice item and assign the value as
1. In Case Builder, both
First and Primary appear in the choice list.

Restriction: If the solution was created from a template that included a choice list,
the choice list is read-only. You cannot change the choice list. You can create a new choice list
with the same or different values.
If you modify a choice list in the original solution where it was created and then
redeploy the solution. It transmits the changes to other solutions by using the same choice list.
When the solution designer opens the solution in Case Builder, they receive a prompt to
synchronize the choice list with the updated version that is redeployed to the target object
store.
4. Optional: Without going to solution level, you can add a choice list, at the
case level.  To create a quick choice list, on the Properties page,
click Manage Choice Lists > Add Choice
List and define choice list values.
Note: You cannot edit the existing choice lists. You can add a single choice list and that gets
automatically set in the choice list drop-down.
After a choice list is added by using Add Choice List, that
choice list is auto-selected in the property wrapper choice list drop-down.

## Adding properties to a case type, document class, or task

### About this task

### Procedure

1. Click Add Property and then select an existing property that is
defined for the solution, reuse a property, or create a new one.
2. Define property values. The property value fields that are displayed depend on
the type of the property. For example, single properties can have a default property value. Some
properties, like float and integer properties, can have minimum and maximum values. If you edit a
property that existed in the solution, any values that you enter here apply only to this case type
or document class. For example, you can override the default value that was set at the solution
level.On the Views page, you can designate a caseworker property
as the Case Title Property. The chosen property is of string or integer data
type, a single value property, and not hidden. In cases where no case property is assigned, the
Case ID automatically serves as the default Case Title
Property.

## Adding one or more task preconditions

### Procedure

1. When you create or edit a task, click the Preconditions
tab.
2. Select a precondition type. Depending on the task, you can select: 

A case property is updated
To configure this precondition, select a property in the Case properties
list.
A document is filed in the case
To configure this precondition, select Any document class or select one
or more types in the Document classes list. You can make this task
repeatable.
A property condition is met
To complete this precondition, click Add Condition to select a case
property that can be included in an expression. For example, you can set a precondition for the
claim value property so that if the claim value exceeds a specific value, then the fraud assessment
task starts.
3. To add another precondition in which a property condition must be met, click
Add Condition. You can add other conditions, such as the AND or OR
conditions.

## Deleting case properties

### About this task

You need to delete properties that are not used in a solution. Keeping unused properties in
elements like case types, activities, and in-baskets can confuse users and can cause database table
limit issues during solution deployment. For more information, see How to plan
project area or target environments appropriately for solution deployment to avoid column
limitations on database tables.

### Procedure

1. Before you delete a property at the solution level, ensure that you have removed the
property from individual pages, in-baskets, case types, etc. The Case Builder automatically verifies whether
properties are used in pages, in-baskets, case types, etc., before allowing the deletion of the
property at the solution level.
2. Delete the properties in Case Builder by clicking the
Remove icon for each property.
3. If the property was added to either a workflow or configuration in relation to a 
FileNet®
 workflow system that is done
outside of Case Builder. Use FileNet Process
Designer to open the solution
and delete the property (data fields) from the queues, in-baskets, and workflows. For more
information, see Case Type Selection.
4. Validate, save, and close the solution after you make the required changes.

### What to do next

When creating your solution, avoid displaying long string properties from Content Platform Engine in the Search
View of a case type if you are reusing them. Including long string properties in the
Search View can lead to errors for caseworkers when searching using these
properties. Long string properties support only the operators begins with,
ends with, contains, is empty, and
is not empty. If a caseworker uses a different operator in the client, the
search fails.