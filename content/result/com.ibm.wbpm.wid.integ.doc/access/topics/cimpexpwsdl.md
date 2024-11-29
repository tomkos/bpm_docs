<!-- image -->

# WSDL import and export files

If you need to use a WSDL file in a module, you can copy it to
the module. Alternately, you can copy the WSDL file to a library and,
in the module, set a dependency on the library so that you can use
the library's resources. If you try to drag a WSDL file from another
type of project, for example a web project, an error message prompts
you to copy the WSDL file to the module or library.

Interoperability and reuse are two good reasons to use the importing
and exporting WSDL file wizards in IBM® Integration
Designer instead
of any manual process.

## Interoperability

SOA projects by definition
integrate a wide spectrum of applications. Although these applications
are themselves defined as services, that is, they have an XML layer
of code that separates them from the actual implementation, even that
XML layer can have inconsistencies. These inconsistencies can lead
to interoperability problems. Typically, these interoperability problems
occur when enterprises are building their SOA applications with development
products from several vendors. One common difference is that some
vendors place the port type, that is, the interface in IBM Integration
Designer in
one file, and the types it references in separate schema files. Other
vendors place their schemas within the same file; a technique known
as inline schemas or inline business objects.

IBM Integration
Designer has
an import wizard that can extract a web service endpoint into a separate
file and extract inline schemas into separate schema files. You also
have the option of importing a WSDL file containing its web service
endpoint and inline schemas and extracting these elements later with
a refactoring wizard.

An export wizard can place an interface
and business objects inline, if they are in an external file and referenced
by the WSDL file. If an endpoint such as a port is defined in one
file and a port type (or interface) is defined in another file, then
this wizard can merge them also.

Using these importing, exporting,
and refactoring wizards, you can share WSDL files created in IBM Integration
Designer with
others in your organization regardless of the different development
environments. Conversely, you can share WSDL files and refactor WSDL
files produced by other tools from different vendors inside IBM Integration
Designer.

## Reuse

When you are working on large SOA
projects that share many modules among many developers, reuse can
play a significant role in reducing development time. On SOA projects,
sharing interfaces and business objects in libraries is a good programming
practice to minimize development time. The wizard supports and encourages
reuse. For example, the import wizard can extract a service endpoint
from a WSDL file, so that the port type can be reused. It can also
extract inline schemas so that the business objects can be reused.
The extracted business objects can themselves be extended and reused.

- Interoperability with services from other vendors

Web Services Description Language (WSDL) files are commonly shared amongst users working on service oriented architecture (SOA) projects. Different users use different software vendors. The vendors have different interpretations of the WSDL standard. This section describes some helpful wizards that ensure WSDL files you import are compatible with IBM Integration Designer editors and WSDL files you export are compatible with other software vendors.
- Importing WSDL or XSD files

Importing Web Services Description Language (WSDL) files or XML Schema Definition (XSD) files into a module or library through an import function are discussed.
- Exporting WSDL files

Exporting Web Services Description Language (WSDL) files from a module along with the options you can use at export time are discussed.
- WSDL binding styles

A Web Services Description Language (WSDL) binding can be created in several forms. For most purposes, document literal wrapped is the best binding style.