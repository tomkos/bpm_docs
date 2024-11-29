<!-- image -->

# Transforming data

XML maps support mapping between source and target objects. XSL
stylesheets that are generated from XML maps are used in Mapping
primitives in mediation flow components. XML Maps can be stored in
modules, mediation modules, and libraries. However, the root XML Map
that is used by a Mapping primitive must be stored in
the same module as the Mapping primitive. XML maps that
are used as submaps in a root XML map can be stored in modules and
libraries.

Business object maps support mappings between source and target
business objects. Business object maps can be stored in modules, mediation
modules, and libraries.

The following topics provide information on XML maps and business
object maps.

- XML maps versus business object maps

You can perform the same data transformations using either XML maps or business object maps. How do you decide which one to use? In general, use an XML map in a Mapping primitive. However, in some specific situations, you need to use a business object map.
- Mapping weakly typed elements

When you want to work with weakly typed elements such as xsd:any, xsd:anyType and xsd:anySimpleType, use the Set Message Type mediation primitive in a mediation flow. You can also use the primitive to access elements in substitution groups, and to cast a concrete type to another concrete type as long as the types are related, such as from an int type to a double.
- Organizing data maps in the data map catalog

The data map catalog is a facility to organize data maps, for example xml maps and business object maps. You can view all of your data maps together within a defined scope.
- Transforming data using XML maps

When you are integrating services, you almost always need to transform the data into a format that the receiving service can process. You can use the XML map editor to create an XML map between input and output data. An XSL style sheet is generated from the XML map and performs the transformation at run time.
- Transforming data using a business object map

When you are integrating services, you almost always need to transform the data into a format that the receiving service can process. You can use the business object map editor to create a business object map between input and output business objects. Business object maps can be used in business processes, mediation flows and can be inserted between components in a module.