<!-- image -->

# Creating relationships

A relationship establishes an association between data from two
or more data types. Each data type is represented as a role in
the relationship. Each role in a relationship is distinguished from
other roles based on the function that they serve in the given relationship.
This means that several roles ultimately contribute to build the relationship.

The following topics provide the concepts and step-by-step instructions
for creating relationships.

- Relationships

A relationship correlates at least two or more semantically equivalent business objects, which are represented in different physical formats.
- The relationship service

The relationship service maintains relationships and roles in the system. It manages relationship and role definitions and metadata and makes it possible to specify the definition of a relationship and manipulate the instances derived from the definition.
- Relationship models

Relationships are created by defining model data. There are primarily two different data models that are used within the relationship editor: relationship models and relationship instance models. The relationship models are stored in .rel and .role  files and the relationship instance models are stored in .ri files (.ri files are not visible in the Business Integration view, they can only be seen in the Physical Resources view).
- Relationship editor

IBM® Integration Designer's relationship editor enables building and editing relationships and their attributes through a graphical interface.
- Identity relationships versus non-identity relationships

There are two different types of relationships: identity and non-identity relationships. An identity relationship is a one-to-one relationship. There must be one managed role defined in the identity relationship, which represents the generic data type and is managed by the relationship service. A non-identity relationship differs slightly from the identity relationship. The non-identity relationship is also called a relationship one-to-many or many-to-many relationship.
- Creating relationships using the New Relationship wizard

Use the New Relationship wizard to create a relationship.
- Working with comma-separated values (CSV) data

The relationship editor supports the import and export of data in a comma-separated values (CSV) file format, such as data that has been created or stored in an Excel file.
- Defining roles

In the relationship editor, there are three property pages available for the role. The Description page handles general detailed information about the role. The Details page displays the type of the role. The Properties page allows you to define user defined properties.
- Role objects

Role objects are the reference of the role to the data type. In the relationship editor, there is one property page (Description page) available for the role object.
- Adding key attributes

In the relationship editor, there is one property page available (Details page) for the key attributes.
- Adding user defined properties

To edit user defined properties, there is the Properties page in the Properties View for the relationship or role object.
- Adding, editing and removing instance data

Working on the pre-population of instance data for the relationship can be done on the Instance Data property page of the relationship. This page is only available on a relationship with a static mapping. A static relationship must have at least one set of values defined for a transformation mapping. The set consists of instance data objects, representing the relationship instances. Each instance data object may have none, one, or several role instances defined depending on the type of relationship. A one-to-one relationship will always have one role instance for each role in the model defined in each instance data object. In the one-to-many and many-to-many relationship there might be none, one, or several role instances defined for each role in the model in each instance data object. You can define user defined property values for each instance data object (representing the relationship) as well as for each role instance object if there are any user defined properties defined in the model. For each role instance you must also define the key attribute values.
- Static relationships

A static relationship is used when to map data from one application to the other and to define the values for the mapping during the definition time of the relationship (for example, for state codes).  In one application the state code may be "California", while in another application it may be "CA". A static relationship is created between these two pieces of data indicating that they are equivalent. The participant data that these types of relationships contain have values that do not change frequently. These relationships exist for both identity relationships and the non-identity relationships.
- Launching the Relationship Manager

In IBM Integration Designer, you can use the Relationship Manager tool of the IBM Integration Designer runtime environment to create, manipulate, and view relationship runtime instances.
- Relationship service APIs

Relationships can be invoked programmatically through the relationship service APIs, within or outside of business object maps.