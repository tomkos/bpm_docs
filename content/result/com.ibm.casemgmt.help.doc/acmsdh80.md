# Adding and modifying business objects

## About this task

You can create a business object as a child of an existing business object. The child inherits
all the properties that are defined for the parent business object.

You can also reuse business objects that are defined for other solutions. Reused business objects
can be edited only in the original source solution.

## Procedure

To add or modify a business object from the solution home page:

1. Click the Business Objects tab.
2 Create a business object or modify an existing object. Option Description To add a business object To add a business object as a subclass of an existing business object Tip: To view the properties that a business object inherits from a parent businessobject, select the Show inherited properties check box on theProperties tab for the child business object. To modify an existing business object Click the business object name in the list.

| Option                                                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-----------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| To add a business object                                              | Click Add Business Object > New. Enter a name and a description for the business object. The Unique Identifier field is updated as you enter the name for the business object. You cannot change the unique identifier after you click OK. If you do not want this business object to be used as a property type, select the Do not use this business object as a property type check box. Click OK.                                                                                                                                                                                                                                                                               |
| To add a business object as a subclass of an existing business object | Select the parent business object from the list of business objects. Click Add Business Object > New subclass. Enter a name and a description for the business object. The Unique Identifier field is updated as you enter the name for the business object. You cannot change the unique identifier after you click OK. If you do not want this business object to be used as a property type, select the Do not use this business object as a property type check box. Click OK.  Tip: To view the properties that a business object inherits from a parent business object, select the Show inherited properties check box on the Properties tab for the child business object. |
| To modify an existing  business object                                | Click the business object name in the list.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

3. On the Properties tab, add or modify the properties that define this
business object.
4. Optional: 
Select a property from the title list to uniquely identify instances of
this business object.

A business object is a subclass of the Content Platform Engine
DependentObject class. An object that is instantiated from a subclass of the
DependentObject class is a dependent object, which is non-addressable. A
dependent object does not possess a unique identifier by which it can be referenced and; therefore,
can be identified only by value. The title field identifies this value.
Tip: IBM® Business Automation
Workflow does not check at run time to ensure
that the business object title is unique. However, you can write a script to validate this
information. For information about scripts to validate data, see ICM Data Validation When Adding New Cases.
If a business object is not referenced at run time, you do not need to set a title. You might not
set a title for a parent business object that is never used as a property type. However, if you do
set a title, the children inherit that title. You can override that inherited title by selecting a
different property for a child business object.

## What to do next

- In an expression for the A property condition is met option in a task
precondition
- In an in-basket
- In a business rule
- As a document property

Like other case properties, a business object property is added to the default view for any case
type in which the property is used. A business object property is presented in a table in which each
column represents a property that is contained in the business object.

- Business objects

At times, you need a collection of properties to represent a single solution entity. If a case contains multiple instances of such a solution entity, you can use a business object, which is a structured data type that represents a solution entity as a collection of properties. You can then assign that business object as the data type of a multivalued property. For example, to represent a person who is covered by an insurance policy, you need properties for given name, surname, ID, birth date, relation to policy holder, and similar information. You create a business object, Insured Party, with these properties.