<!-- image -->

# Inline schemas

The following XML
code fragment has an inline schema called Employee, which is used
within the WSDL file.

<!-- image -->

The WSDL
file with this inline schema can be opened and used by the interface
editor as shown in the following image:

<!-- image -->

The data type defined
within an inline schema can be used in the same WSDL, but cannot be
used in another new interface.  If you create a new interface and
use the inline schemas in existing WSDL files, the interface editor
will not show those types in the new interface. A workaround for this
problem is to copy the inline schema from the existing WSDL file to
the new WSDL file.