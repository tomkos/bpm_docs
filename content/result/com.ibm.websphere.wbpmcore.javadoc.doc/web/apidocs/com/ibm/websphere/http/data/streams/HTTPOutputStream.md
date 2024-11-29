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

## Interface HTTPOutputStream

- public interface HTTPOutputStream
An interface for the HTTP Output Stream used in the output communication between HTTP protocol and data binding.

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
write(byte[] outBuf)
Write an array of bytes to the stream.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - write
void write(byte[] outBuf)
           throws java.io.IOException
Write an array of bytes to the stream.  Bytes may be buffered for optimization.

  This method stores bytes from the array into an internal buffer for optimization.
 This buffer is then written to the underlying stream when the internal buffer is full.
Parameters:outBuf - An array of bytes to be written
Throws:
java.io.IOException - Thrown if an I/O problem occurs