- Overview
- Package
- Class
- Tree
- Deprecated
- Index
- Help

- Prev Class
- Next Class

- Frames
- No Frames

- All Classes

- Summary:
- Nested |
- Field |
- Constr |
- Method

- Detail:
- Field |
- Constr |
- Method

## Interface WebServiceExportBinding

- All Superinterfaces:
ExportBinding

public interface WebServiceExportBinding
extends ExportBinding
Interface that represent the WebService binding information on a SCA export.
Since:
7.5.1.0

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description javax.xml.namespace.QName getPort () Method returns the QName of the port that belongs to the WebService binding of the export. javax.xml.namespace.QName getService () Method returns the QName of the service that belongs to the WebService binding of the export.

### Method Summary

| Modifier and Type         | Method and Description                                                                                       |
|---------------------------|--------------------------------------------------------------------------------------------------------------|
| javax.xml.namespace.QName | getPort() Method returns the QName of the port that belongs to the   WebService binding of the export.       |
| javax.xml.namespace.QName | getService() Method returns the QName of the service that belongs to the   WebService binding of the export. |

- Methods inherited from interface com.ibm.wsspi.sca.metadata.ExportBinding
getBindingType