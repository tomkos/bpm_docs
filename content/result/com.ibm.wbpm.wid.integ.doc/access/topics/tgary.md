<!-- image -->

# Interoperability with services from other vendors

## About this task

SOA projects by definition integrate a wide spectrum of
applications. Although these applications are themselves defined as
services, that is, they have an XML layer of code that separates them
from the actual implementation, even that XML layer can have inconsistencies.
These inconsistencies can lead to interoperability problems. Typically,
these interoperability problems appear when enterprises are building
their SOA applications with development products from several vendors.
One common difference is that some vendors place an interface in one
file and the references in that interface, that is, the schemas, in
separate files. Other vendors place their schemas within the same
file, a technique known as inline schemas.

Both types
of vendors are technically correct as they both comply with the formal
WSDL specification. Practically speaking, however, these two types
of WSDL files lead to aggravating interoperability problems that can
usually only be solved by manual workarounds.

If you are experiencing
this interoperability problem, IBM Integration
Designer has
some helpful wizards.

- Importing WSDL or XSD files lets you import WSDL files
into modules. IBM Integration
Designer editors
and wizards work with separate files for references in the interface.
If you import a WSDL file with inline schemas, the importing wizard
can extract your inline schemas to separate files at the time of the
import. Alternately, you can import the file and later extract the
inline schemas to separate files using the refactoring WSDL files
function.
- Exporting WSDL files lets
you export WSDL files from modules to the file system. Since you are
working with separate files for references in the interface while
working in IBM Integration
Designer,
when you export you have the option of merging these separate files
into the interface. You would use this function if you were sending
this file to a user who works with inline schemas.

## Related tasks

- Importing WSDL or XSD files
- Exporting WSDL files

## Related reference

- WSDL binding styles