<!-- image -->

# Creating Mapping transformations

## Before you begin

## About this task

<!-- image -->

The Mapping transformation primitive
uses a map file that contains the information required to map between
two message types. You can select an existing map, and optionally
edit it, or create a new one using the XML Map Editor. An XSL file
is automatically generated for the map file and used at run time.

Note: If
you create a map and set its input and output types, the types you
have selected will be present at the input and output terminals of
the primitive regardless of the wiring. The same applies when using
a previously created map. To reset the input or output message type,
right-click the terminal and select Reset Message Type.
The map will have to be recreated because it is not refactored when
the terminal type changes.

- Creating an XML map in a Mapping transformation primitive

Use the XML map editor to create an XML map between the input and output message. When the mapping has been created, an XSL style sheet will be generated to perform the transformation at run time. If you want to create a new XML map for a Mapping transformation primitive but an XML map already exists, you can use the Properties view of the mediation flow editor to create the new XML map and simultaneously choose whether to have the existing XML map overridden, deleted, or retained.
- Using an existing XML map

You can use an existing XML map and generate a style sheet from it.
- Migrating an XML Map

In IBM® Integration Designer 6.1 and the versions that follow, the Mapping transformation primitive has a new XML map editor. Before you can edit XML maps that were created in a prior version of IBM Integration Designer, you must migrate them to the new format.
- Troubleshooting: warning on Mapping transformation primitive

Changing the correlation, transient or shared context results in a warning marker on a Mapping transformation primitive, and this type of warning message in the problems view: CWZMU0046E: The correlation context type on the in terminal of the Mapping1 primitive does not match the empty type.