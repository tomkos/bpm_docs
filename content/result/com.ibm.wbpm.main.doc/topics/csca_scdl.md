<!-- image -->

# Service Component Definition Language

The various artifact types that exist in SCA were designed to support some of the basic
requirements of this service-oriented architecture. To start with, SCA needs a mechanism for
defining a basic service component. Once there is a mechanism for defining service components, it is
important to be able to make these services available to clients both inside or outside of the
current SCA module. In addition to this, a construct designed to import and reference services
external to the current SCA module must exist. Finally, SCA provides constructs for composing
services and modules into larger applications.

SCDL definitions are organized across several files. For example, in a credit approval
application, we can store the SCDL for the interface and implementation in a file called
CreditApproval.component. References can be included in the
CreditApproval.component file (inline) or in a separate
sca.references file located in the module root. Any stand-alone reference is
placed in the sca.references file. Stand-alone references can be used by
non-SCA artifacts (JSP) within the same SCA module to invoke the SCA component.

| Artifact           | SCDL Definition                                                                                                                                                          |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Module Definition  | Contained in the sca.module file at the root SCA project JAR                                                                                                             |
| Service Components | A module can contain 0..n service definitions Each component definition is contained in a <SERVICE\_NAME>.component file                                                  |
| Imports            | A module can contain 0..n import definitions Each import definition is contained in a <IMPORT\_NAME>.import file                                                          |
| Exports            | A module can contain 0..n export definitions Each export definition is contained in a <EXPORT\_NAME>.export file                                                          |
| References         | Two types of references Inline (contained within a service component definition) Stand-alone   Each component definition is contained in a <SERVICE\_NAME>.reference file |
| Other Artifacts    | Other artifacts include: Java™ Classes, WSDL files, Other Artifacts XSD files, BPEL.                                                                                     |

When building an SCA application, IBM® Integration
Designer takes care of generating the appropriate SCDL definitions. However, a basic familiarity with SCDL
can help you to understand the overall architecture and assist when debugging applications.

- Module definition

Service Component Architecture (SCA) defines a standard deployment model for packaging components into a service module. The sca.module file contains the definition of the module.
- Component definition

The service component definition is included in a file called <SERVICE\_NAME>.component. SCA components with their associated dependencies can be defined and packaged together into deployable units.
- Import definition

The import definition is included in a file called <IMPORT\_NAME>.import. SCA imports allow clients in an SCA module to access services that are outside the current SCA module.
- Export definition

The export definition is included in a file called <EXPORT\_NAME>.export. SCA exports provide access to service components defined in an SCA module for use by clients outside of the current SCA module.
- Reference definition

SCA and non-SCA clients calling a service component need a reference to that service in order to invoke it. You can define either a stand-alone reference in the sca.reference file or an inline reference within a service composition definition.

<!-- image -->