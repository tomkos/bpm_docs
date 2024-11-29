# Application migration and development considerations

## Error handling

- In eager XML parsing mode, those exceptions occur as soon as the
business object is parsed from the inbound XML stream.
- If lazy XML parsing mode is configured, the parsing exceptions
occur latently when the business object properties are accessed and
the portion of the XML that is ill-formed is parsed.

- Deploy an enterprise service bus on the edges to validate inbound
XML
- Author lazy error-detection logic at the point where business
object properties are accessed

## Exception stacks and messages

Because the
eager and lazy XML parsing modes have different underlying implementations,
stack traces thrown by the business object programming interfaces
and services have the same exception class name, but they might not
contain the same exception message or wrapped set of implementation-specific
exception classes.

## XML serialization format

The lazy XML parsing
mode provides a performance optimization that attempts to copy unmodified
XML from the inbound byte stream to the outbound byte stream upon
serialization.  The result is increased performance, but the serialization
format of the outbound XML byte stream might be different if the entire
business object was updated in lazy XML parsing mode or if it was
running in eager XML parsing mode.

Although the XML serialization
format might not be precisely syntactically equivalent, the semantic
value provided by the business object is equivalent independent of
the parsing modes, and XML can be safely passed between applications
running in different parsing modes with semantic equivalence.

## Business object instance validator

The lazy
XML parsing business object mode instance validator provides a higher
fidelity validation of business objects, particularly facet validation
of property values. Because of these improvements, the lazy parsing
mode instance validator catches additional issues that are not caught
in eager parsing mode and provides more detailed error messages.

## Version 602 XML Maps

Mediation flows originally
developed before WebSphere Integration Developer Version 6.1 might
contain Mapping primitives that use a map or stylesheet that cannot
run directly in lazy XML parsing mode. When an application is migrated
for use in lazy XML parsing mode, map files associated with Mapping
primitives can be automatically updated by the migration wizard to
run in the new mode. However, if a Mapping primitive refers directly
to a stylesheet that has been edited manually, the stylesheet is not
migrated and cannot run in lazy XML parsing mode.

## Private unpublished APIs

If an application
is taking advantage of unpublished, private, implementation-specific
business object programming interfaces, the application is likely
to fail compilation when the parsing mode is switched. In eager parsing
mode, these private interfaces are typically business object implementation
classes defined by the Eclipse Modeling Framework (EMF).

In
all cases, it is strongly recommend that private APIs be removed from
the application.

## Service Message Object EMF APIs

A mediation
component in IBM Integration Designer provides the ability to manipulate
message content using the Java™ classes
and interfaces provided in the com.ibm.websphere.sibx.smobo package.
In lazy XML parsing mode, the Java interfaces
in the com.ibm.websphere.sibx.smobo  package can still be used, but
methods that refer directly to Eclipse Modeling Framework (EMF) classes
and interfaces or that are inherited from EMF interfaces are likely
to fail.

The ServiceMessageObject and its contents cannot be
cast to EMF objects in lazy XML parsing mode.

## BOMode service

The BOMode service is used
to determine whether the currently executing XML parsing mode is eager
or lazy.

## Migration

All applications before version
7.0.0.0 are running in eager XML parsing mode. When they are runtime
migrated using the BPM runtime migration tools, they continue to run
in eager XML parsing mode.

To enable an application earlier
than version 7.0.0.0 to be configured to use the lazy XML parsing
mode, you first use Integration Designer to migrate
the artifacts of the application. After migration, you then configure
the application to use lazy XML parsing.

See Migrating source artifacts for
information on migrating artifacts in Integration Designer, and see Configuring the business object parsing mode of modules and libraries for information
on setting the parsing mode.