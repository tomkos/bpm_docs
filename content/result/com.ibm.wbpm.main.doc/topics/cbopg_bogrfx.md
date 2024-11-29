<!-- image -->

# Modeling business graphs

- Business graph use models

Two primary use models represent the fundamental capabilities provided by the business graph: delta support and after image.
- Business graph model definition

To remain non-intrusive to an externally developed model of a business object, the business graph capability is wrapped around the original business object. A pattern named the templated business graph is used to wrap the original business object with the enriched business graph schema.
- Business graph model instance

The top-level business graph is represented in memory much the same as a business object, by an SDO 1.0 DataObject, specifically, the class commonj.sdo.DataObject.