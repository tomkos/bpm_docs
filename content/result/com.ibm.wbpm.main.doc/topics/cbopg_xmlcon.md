<!-- image -->

# Supported XSD and WSDL artifacts

## Business objects from imported XSD definitions

When an XML schema is imported into a project, only certain artifacts are rendered as business
objects. The following lists show which artifacts are supported at authoring time and at run
time:

XSD artifacts resulting in business objects at authoring time:

- Complex types defined at the root level
- Elements defined at the root level with anonymous complex types

- Simple types defined at the root level
- Elements defined at the root level with anonymous simple types

## Business objects from imported WSDL files

When a WSDL definition that includes an inline XSD schema is imported into a project, only
certain artifacts are rendered as business objects. The following lists show which artifacts are
supported at authoring time and at run time:

Inline XSD artifacts resulting in business objects at authoring time:

- Complex types defined at the root level
- Elements defined at the root level with anonymous complex types AND the name of the element does
not contain the names of any operations/messages (as these elements could be doc-lit-wrapped
elements which IBM Integration
Designer unwraps automatically)

- Simple types defined at the root level
- Elements defined at the root level with anonymous simple types

## Run time business objects from XSD artifacts

These artifacts result in business objects at run time:

- Complex types defined at the root level
- Elements defined at the root level with anonymous complex types
- Elements defined at the root level which reference a complex type

## Run time business objects from WSDL files

These artifacts result in business objects at run time:

- Complex types defined at the root level
- Elements defined at the root level with anonymous complex types AND the name of the element does
not contain the names of any operations/messages (as these elements could be doc-lit-wrapped
elements which IBM Integration
Designer unwraps automatically)
- Elements defined at the root level which reference a complex type