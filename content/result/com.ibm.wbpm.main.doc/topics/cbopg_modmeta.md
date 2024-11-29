<!-- image -->

# Modeling business object type metadata

The business object framework provides a mechanism that enables:

- Metadata to be mixed into a business object in a consistent, and relatively non-intrusive
fashion
- A prescriptive policy for developers to define complex annotation structures
- A prescriptive policy for business object developers and deployers to annotate a business object
with instance metadata that conforms to the predefined complex annotation structures
- A set of APIs for transforming the annotations at run time into a simple to use DataObject
structure

- The first role is that of the business object type metadata designer. This role designs the
metadata structure. For example, the business object framework plays this role and defines a couple
of metadata characteristics for annotating a business object. It is expected that adapters such as
PeopleSoft, Siebel, and SAP, play the role of the metadata designer to annotate the business object
with application-specific information.
- The second role is the business object designer or deployer. This role uses the structure of the
business object type metadata, and the policy defined by the business object type metadata
framework, to annotate the business object definitions with metadata.
- If the business object is annotated correctly, the third role can use the business object
metadata APIs to validate and inspect the metadata at run time, and turn it into a navigable and
useful DataObject graph structure.

- Compound primary key and foreign key property definitions
- Top-level supported verb metadata annotations

For more details, refer to these other topics.

- Representing business object type metadata

The business object framework defines a mechanism by which business object type metadata can be mixed into either a top down, or externally developed, imported schema.
- Designing business object type metadata

You can design a metadata structure to house the business object metadata.
- Annotating a business object definition

You can use the syntax supported by the business object framework to annotate a business object definition.
- Converting annotation into DataObjects

The business object framework provides the capability to transform annotations into a usable DataObject structure.