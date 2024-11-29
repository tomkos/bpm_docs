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

## Interface WebServiceImportBinding

- All Superinterfaces:
ImportBinding

public interface WebServiceImportBinding
extends ImportBinding
Interface that represent the WebService binding information on a SCA import.
Since:
7.5.1.0

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getEndpoint () Method returns the endpoint that belongs to the WebService binding of the import. javax.xml.namespace.QName getPort () Method returns the QName of the port that belongs to the WebService binding of the import. javax.xml.namespace.QName getService () Method returns the QName of the service that belongs to the WebService binding of the import.

### Method Summary

| Modifier and Type         | Method and Description                                                                                       |
|---------------------------|--------------------------------------------------------------------------------------------------------------|
| java.lang.String          | getEndpoint() Method returns the endpoint that belongs to the WebService binding of the   import.            |
| javax.xml.namespace.QName | getPort() Method returns the QName of the port that belongs to the   WebService binding of the import.       |
| javax.xml.namespace.QName | getService() Method returns the QName of the service that belongs to the   WebService binding of the import. |

- Methods inherited from interface com.ibm.wsspi.sca.metadata.ImportBinding
getBindingType