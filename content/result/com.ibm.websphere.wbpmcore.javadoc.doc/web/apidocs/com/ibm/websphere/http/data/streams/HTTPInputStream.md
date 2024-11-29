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

## Interface HTTPInputStream

- public interface HTTPInputStream
An interface for the HTTP Input Stream used in the input communication between HTTP protocol and data binding.

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

int
read(byte[] inBuf,
    int off,
    int len)
Read bytes into a byte array.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - read int read(byte[] inBuf, int off, int len) throws java.io.IOException Read bytes into a byte array. This method reads bytes into the array until one of the following conditions is met: Parameters: inBuf - byte array input buffer off - offset to begin storing bytes in inBuf len - maximum number of bytes to read Returns: The number of bytes actually read, or -1 if the end of the stream is reached Throws: java.io.IOException - Thrown if an I/O problem occurs

#### read

```
int read(byte[] inBuf,
       int off,
       int len)
         throws java.io.IOException
```

This method reads bytes into the array until one of the following
 conditions is met:
 
 
 The number of bytes indicated by len is read,

    No more bytes are available to be ready