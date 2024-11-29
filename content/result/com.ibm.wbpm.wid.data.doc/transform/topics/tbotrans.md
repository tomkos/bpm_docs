<!-- image -->

# Transforming data using a business object map

- Business object maps

A business object map assigns values to target business objects based on values in source business objects. You can create and edit business objects maps using the business object map editor
- Business object map editor

IBM® Integration Designer's business object map editor is used to build and edit business object maps through a graphical interface.
- Creating business object maps in Integration Designer

You can create a business object map using the New Business Object Mapping wizard. A map between business objects establishes the correspondence between their fields, thereby permitting the exchange of data between them.
- Editing business object maps in Integration Designer

You can edit business object maps once they have been created in the business object map editor using either the graph view, table view, or properties view.
- Variables

Variables are used to prevent the same computation being performed several times as the variable allows you to store the values so that they can be used later.  A variable represents specific data or a value, and acts as a placeholder for that value. Unlike a constant value, which is fixed and unchanging, a variable can be repeatedly assigned different values. You assign a value to a variable and the variable maintains the value until you later assign a new value. Because of this flexibility, it is necessary for you to declare variables before you use them. Variables can be a source or target of a transform.
- Substitution groups

A substitution group is a construct in XML Schema (XSD) that allows data architects to create a set of elements that can be substituted for a head element.
- Mapping substitutable elements

A substitutable element is an XML element that declares another element to be its head element, by using the substitution group construct. The substitutable element can then be used instead of the head element. The substitutable element must be of the same type as or derived from a parent element. You can map a substitutable element in the business object map editor.
- Transform types in the business object map editor

The business object map editor supports the following mapping types, otherwise knows as transform types, to map business data inside of a business object.
- Automatic mapping

IBM Integration Designer supports the automatic mapping of similar fields.
- Reverse maps

A reverse map takes an existing business object map at a point in time and creates a new business object map with the inputs and outputs reversed. Any changes to the existing business object map made after the point in time will not be automatically reflected in the reverse map.
- SimpleContent support in the business object map editor

The business object map editor supports the use of complex type definitions with simple content in business objects.
- Sorting and filtering in a business object map

The business object map editor supports mappings between large business objects that may have hundreds of fields. You can sort and filter unnecessary fields when creating maps between large business objects to improve manageability.
- Mapping with XSD wildcards

You can use the business object map editor to map XSD wildcards (xsd:any, xsd:anyType, xsd:anyAttribute, and xsd:anySimpleType).
- Creating maps using the show change and event summaries

You can show the change and event summaries on business objects from the toolbar of the business object map editor.
- Troubleshooting the business object map

There are possible solutions for errors or issues that may occur when using the business object map editor.
- Writing Java code in the Custom, Custom Assign, and Custom Callout transforms

In the Details tab, you can construct Java™ code in one of the editors embedded in the Properties view.
- Considerations when using the business object map editor

There are a number of considerations when using the business object map editor.
- Limitations of the business object map editor

There are current limitations that you should be aware of when using the business object map editor.