<!-- image -->

# Supported XSD and WSDL artifacts

## Business objects from imported XSD definitions

When
an XML schema is imported into a project, only certain artifacts are
rendered as business objects. The following lists show which artifacts
are supported at authoring time and at run time:

XSD artifacts
resulting in business objects at authoring time:

- Complex types defined at the root level
- Elements defined at the root level with anonymous complex types

- Simple types defined at the root level
- Elements defined at the root level with anonymous simple types

## Business objects from imported WSDL files

When
a WSDL definition that includes an inline XSD Schema is imported into
a project, only certain artifacts are rendered as business objects.
The following lists show which artifacts are supported at authoring
time and at run time:

Inline XSD artifacts resulting in business
objects at authoring time:

- Complex types defined at the root level
- Elements defined at the root level with anonymous complex types
AND the name of the element does not contain the names of any operations/messages
(as these could be doc-lit-wrapped elements which IBM Integration
Designer will
unwrap automatically)

- Simple types defined at the root level
- Elements defined at the root level with anonymous simple types

## Runtime business objects from XSD artifacts

These
artifacts result in business objects at run time:

- Complex types defined at the root level
- Elements defined at the root level with anonymous complex types
- Elements defined at the root level which reference a complex type

## Runtime business objects from WSDL files

These
artifacts result in business objects at run time:

- Complex types defined at the root level
- Elements defined at the root level with anonymous complex types
AND the name of the element does not contain the names of any operations/messages
(as these could be doc-lit-wrapped elements which IBM Integration
Designer will
unwrap automatically)
- Elements defined at the root level which reference a complex type

## XSD example (supported at authoring time)

This
example shows a project (XSDExamples) in the Business Integration
view with the business objects shown:

<!-- image -->

This shows the Customer.xsd file in the XSD Schema
editor:

<!-- image -->

| XSD support                                                       | XSD artifact in the above example   |
|-------------------------------------------------------------------|-------------------------------------|
| Complex types defined at the root level                           | Customer                            |
| Elements defined at the root level with anonymous complex types   | Address                             |
| Elements defined at the root level with user-defined simple types | addressNumber                       |

## WSDL example (supported at authoring time)

This
example shows a project (WSDL\_XSDExamples) in the Business Integration
view with the business objects shown:

<!-- image -->

This shows the CustomerInterface.wsdl file opened in
the WSDL editor:

<!-- image -->

| WSDL support                                                                                                                                                                                                                                            | Inline XSD Artifact in the above example   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| Complex types defined at the root level                                                                                                                                                                                                                 | Customer                                   |
| Elements defined at the root level with anonymous complex types AND the name of the element does not contain the names of any operations/messages (as these could be doc-lit-wrapped elements which IBM Integration Designer will unwrap automatically) | Address                                    |
| Elements defined at the root level with user-defined simple types                                                                                                                                                                                       | addressNumber                              |

## Runtime example

| Runtime support                                                                                          | XSD or Inline XSD artifact in the above examples   |
|----------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| All of the above	in examples 1 and 2 (except for addressNumber as simple types are not business objects) | See above (examples 1 and 2)                       |
| Elements defined at the root level which reference a complex type                                        | ACMECustomer (shown in examples 1 and 2)           |