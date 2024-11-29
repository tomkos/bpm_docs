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

## Interface BOPrinter

- public interface BOPrinter
Print the Business Object content or Business Object type information for human reading.
 Note: The output format may be changed in future release, so use
 this for debugging or tracing purpose only.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary

Methods 

Modifier and Type
Method and Description

void
print(commonj.sdo.ChangeSummary changeSummary,
     java.io.OutputStream out)
Print ChangeSummary content to specified output stream.

void
print(commonj.sdo.DataObject dataObject,
     java.io.OutputStream out)
Print Business Object content to specified output stream.

void
print(commonj.sdo.Type type,
     java.io.OutputStream out)
Print Business Object type to specified output stream.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - print
void print(commonj.sdo.DataObject dataObject,
         java.io.OutputStream out)
           throws java.io.IOException
Print Business Object content to specified output stream.
Parameters:dataObject - the Business Object to be printed outout - the output stream
Throws:
java.io.IOException
    - print
void print(commonj.sdo.Type type,
         java.io.OutputStream out)
           throws java.io.IOException
Print Business Object type to specified output stream.
Parameters:type - the Business Object type to be printed out.out - the output stream
Throws:
java.io.IOException
    - print
void print(commonj.sdo.ChangeSummary changeSummary,
         java.io.OutputStream out)
           throws java.io.IOException
Print ChangeSummary content to specified output stream.
Parameters:changeSummary - the Change Summary to be printed out.out - the output stream
Throws:
java.io.IOException