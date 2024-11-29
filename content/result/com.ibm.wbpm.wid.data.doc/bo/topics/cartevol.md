<!-- image -->

# Artifact evolution for business objects

A common business integration scenario is the reuse of business logic for evolving data. For example, you may have a specific business process that has been implemented as a business application within the IBM Integration
Designer environment. Business processes are constantly changing in accordance with new business requirements. The business data is provided to the business application as an XML Schema which is the data modeling technology used by IBM Integration
Designer. As the business requirements evolve, the XML Schema generation must also change.

Artifact evolution enables the integration of a new version of
XML Schema(s) into an existing business application with minimal manual
modifications to the dependent artifacts (some manual modification
cannot be avoided). Those modifications are a result of the potential
introduction of new business objects and new business object fields.
For example, you will need to update the existing business object
maps with new transforms associated with the new business object fields.
As well, you may need to create new business object maps to provide
mapping for the new business objects.

- Existing business object names changed
- Existing business object namespaces changed
- New business objects added
- Existing business objects removed
- New fields added to existing business objects
- Fields removed from existing business objects
- Business object field types changed
- Business object field names changed

Artifact evolution provides the means to propagate these changes
to all business object dependent artifacts like business object maps,
interfaces, interface maps, relationships, and so on.

- Creating artifact evolutions

Artifact evolutions can be created using the artifact evolution editor in IBM Integration Designer.