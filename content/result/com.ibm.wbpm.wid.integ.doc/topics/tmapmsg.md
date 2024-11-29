<!-- image -->

# Transforming messages

## About this task

In the mediation flow you can map Business Objects using either business object maps or XSLT style sheets.
Business object maps can be used with either the Business Object Map primitive or the Mapping primitive. XSL style sheets can 
be used with the Mapping primitive. The Business Object Map primitive uses the Business Object Map
editor to create mappings. The Mapping primitive uses the XML Map editor to create XML mappings. You can choose to generate XSLT or business object maps from the XML maps.

If a message has weakly typed fields, ie fields of xsd:any, xsd:anyType, and xsd:anySimpleType, they must be converted
to a strong type in order to effectively map them in the business object and
XML map editors. You can use the setMessageType primitive to convert the weakly
typed fields to strongly typed fields.

- XML maps versus business object maps
- Mapping interfaces in mediation flows

You can easily map interfaces and their operations in a mediation flow by using a template in the mediation flow editor. The operation map template provides functionality similar to the deprecated interface maps created in the interface map editor.
- Mapping weakly typed elements using the set message type mediation primitive

When you want to work with weakly typed elements such as xsd:any, xsd:anyType and xsd:anySimpleType, use the Set Message Type mediation primitive. You can also use the primitive to access elements in substitution groups, and to cast a concrete type to another concrete type as long as the types are related, such as from an int type to a double.
- Creating Mapping transformations

When the message types of source and target operations do not match, you need to transform the source message type so that the target operation can receive it and you do this with the Mapping transformation primitive which uses a map file to map source and target message types.
- Using the Business Object Map primitive

To enable data to exchange between differently structured business objects, you map those business objects in the business object map editor using the Business Object Map primitive.