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

## Interface MQDataOutput

- All Known Implementing Classes:
MQDataOutputStream

public interface MQDataOutput
An MQDataOutput implementation allows read access to some underlying store of
 semi-structured binary data. It provides read methods for character data,
 integer data, floating-point data, packed decimal data and serialized Java
 objects. It converts between different representations of this data (e.g.
 EBCDIC/ASCII character data, big-endian and little-endian integer data) driven
 by the CCSID and encoding properties. It is intended for writing WebSphere MQ
 message data, and uses WMQ conventions.

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
getCCSID()
Returns the Coded Character Set Identifier currently used for
 character write operations

int
getDataOffset()
Returns the current offset of the cursor, relative to the position where
 this MQDataOutput object was originally created.

DecimalEncoding
getDecimalEncoding()
Returns the DecimalEncoding currently used for packed-decimal write operations.

int
getEncoding()
Return the WMQ encoding identifier representing the three encodings (integer,
 floating-point and packed-decimal) currently used for numeric write operations.

FloatEncoding
getFloatEncoding()
Returns the FloatEncoding currently used for floating-point write operations.

IntegerEncoding
getIntegerEncoding()
Returns the IntegerEncoding currently used for integer write operations.

void
setCCSID(int ccsid)
Sets the Coded Character Set Identifier to be used for subsequent
 character write operations.

void
setDecimalEncoding(DecimalEncoding de)
Sets the DecimalEncoding to be used for subsequent packed-decimal
 write operations.

void
setEncoding(int encoding)
Sets all three encoding values - integer, floating-point and packed-decimal,
 using the WMQ encoding identifier.

void
setFloatEncoding(FloatEncoding fe)
Sets the FloatEncoding to be used for subsequent floating-point
 write operations.

void
setIntegerEncoding(IntegerEncoding ie)
Sets the IntegerEncoding to be uesd for subsequence integer write
 operations.

void
writeByte(byte b)
Writes a single (signed) byte

void
writeBytes(byte[] b)
Writes an array of bytes

void
writeBytes(byte[] b,
          int off,
          int len,
          byte pad)
Writes a portion of an array of bytes into a fixed-length field, truncating
 or padding as appropriate.

void
writeDecimal(int fieldLen,
            java.math.BigInteger bi)
Writes a packed-decimal integer into a fixed-length field.

void
writeDecimal2(short s)
Writes a two-byte packed decimal integer.

void
writeDecimal4(int i)
Writes a four-byte packed decimal integer.

void
writeDecimal8(long l)
Writes an eight-byte packed decimal integer.

void
writeDouble(double d)
Writes a double as eight bytes, according to the current floating-point encoding.

void
writeFloat(float f)
Writes a float as four bytes, according to the current floating-point encoding.

void
writeInt(int i)
Writes an int as four bytes.

void
writeLong(long l)
Writes a long as eight bytes.

void
writeMQBYTE(byte b)
Writes a single (signed) byte

void
writeMQBYTE(byte[] b)
Writes an array of bytes

void
writeMQBYTE(int fieldLen,
           byte[] b)
Writes an array of bytes, truncated or null-padded as
 necessary, into a fixed-length field.

void
writeMQBYTE(int fieldLen,
           byte[] b,
           byte pad)
Writes an array of bytes, truncated or padded as necessary, into a
 fixed-length field.

void
writeMQBYTE(int fieldLen,
           byte[] b,
           int off)
Writes an array of bytes, from an offset and truncated or null-padded as
 necessary, into a fixed-length field

void
writeMQBYTE(int fieldLen,
           byte[] b,
           int off,
           byte pad)
Writes an array of bytes, from an offset and truncated or padded as
 necessary, into a fixed-length field

void
writeMQBYTE16(byte[] b)
Writes a 16-byte field from a byte array, truncated or null-padded as necessary.

void
writeMQBYTE16(byte[] b,
             int off)
Writes a 16-byte field from a byte array, starting at a given offset, and
 truncating or null-padding as necessary.

void
writeMQBYTE24(byte[] b)
Writes a 24-byte field from a byte array, truncated or null-padded as necessary.

void
writeMQBYTE24(byte[] b,
             int off)
Writes a 24-byte field from a byte array, starting at a given offset, and
 truncating or null-padding as necessary.

void
writeMQBYTE32(byte[] b)
Writes a 32-byte field from a byte array, truncated or null-padded as necessary.

void
writeMQBYTE32(byte[] b,
             int off)
Writes a 32-byte field from a byte array, starting at a given offset, and
 truncating or null-padding as necessary.

void
writeMQBYTE8(byte[] b)
Writes an 8-byte field from a byte array, truncated or null-padded as necessary.

void
writeMQBYTE8(byte[] b,
            int off)
Writes an 8-byte field from a byte array, starting at a given offset, and
 truncating or null-padding as necessary.

void
writeMQCHAR(char c)
Writes a character to the stream as a single byte, converted according
 to the current CCSID.

void
writeMQCHAR(char[] c)
Writes an array of characters to the stream, converted according to the
 current CCSID.

void
writeMQCHAR(int fieldLen,
           char[] c)
Writes a fixed-length field from an array of characters, converted according
 to the current CCSID, and truncated or space-padded as necessary.

void
writeMQCHAR(int fieldLen,
           char[] c,
           char pad)
Writes a fixed-length field from an array of characters, converted according
 to the current CCSID, and truncated or padded as necessary.

void
writeMQCHAR(int fieldLen,
           char[] c,
           int off)
Writes a fixed-length field from an offset into an array of characters,
 converted according to the current CCSID, and truncated or space-padded
 as necessary.

void
writeMQCHAR(int fieldLen,
           char[] c,
           int off,
           char pad)
Writes a fixed-length field from an offset into an array of characters,
 converted according to the current CCSID, and truncated or padded
 as necessary.

void
writeMQCHAR(int fieldLen,
           java.lang.String s)
Writes a fixed-length field from a String, converted according
 to the current CCSID, and truncated or space-padded as necessary.

void
writeMQCHAR(int fieldLen,
           java.lang.String s,
           char pad)
Writes a fixed-length field from a String, converted according
 to the current CCSID, and truncated or padded as necessary.

void
writeMQCHAR(java.lang.String s)
Writes a String to the stream, converted according to the
 current CCSID.

void
writeMQCHAR12(char[] c)
Writes a 12-byte field from a character array, converted according
 to the current CCSID, and truncated or space-padded as necessary.

void
writeMQCHAR12(char[] c,
             int off)
Writes a 12-byte field from an offset into a character array,
 converted according to the current CCSID, and truncated or space- padded
 as necessary

void
writeMQCHAR12(java.lang.String s)
Writes a 12-byte field from a String, converted according to the current
 CCSID, and truncated or space-padded as necessary

void
writeMQCHAR128(char[] c)
Writes a 128-byte field from a character array, converted according
 to the current CCSID, and truncated or space-padded as necessary.

void
writeMQCHAR128(char[] c,
              int off)
Writes a 128-byte field from an offset into a character array,
 converted according to the current CCSID, and truncated or space- padded
 as necessary

void
writeMQCHAR128(java.lang.String s)
Writes a 128-byte field from a String, converted according to the current
 CCSID, and truncated or space-padded as necessary

void
writeMQCHAR16(char[] c)
Writes a 16-byte field from a character array, converted according
 to the current CCSID, and truncated or space-padded as necessary.

void
writeMQCHAR16(char[] c,
             int off)
Writes a 16-byte field from an offset into a character array,
 converted according to the current CCSID, and truncated or space- padded
 as necessary

void
writeMQCHAR16(java.lang.String s)
Writes a 16-byte field from a String, converted according to the current
 CCSID, and truncated or space-padded as necessary

void
writeMQCHAR20(char[] c)
Writes a 20-byte field from a character array, converted according
 to the current CCSID, and truncated or space-padded as necessary.

void
writeMQCHAR20(char[] c,
             int off)
Writes a 20-byte field from an offset into a character array,
 converted according to the current CCSID, and truncated or space- padded
 as necessary

void
writeMQCHAR20(java.lang.String s)
Writes a 20-byte field from a String, converted according to the current
 CCSID, and truncated or space-padded as necessary

void
writeMQCHAR24(char[] c)
Writes a 24-byte field from a character array, converted according
 to the current CCSID, and truncated or space-padded as necessary.

void
writeMQCHAR24(char[] c,
             int off)
Writes a 24-byte field from an offset into a character array,
 converted according to the current CCSID, and truncated or space- padded
 as necessary

void
writeMQCHAR24(java.lang.String s)
Writes a 24-byte field from a String, converted according to the current
 CCSID, and truncated or space-padded as necessary

void
writeMQCHAR256(char[] c)
Writes a 256-byte field from a character array, converted according
 to the current CCSID, and truncated or space-padded as necessary.

void
writeMQCHAR256(char[] c,
              int off)
Writes a 256-byte field from an offset into a character array,
 converted according to the current CCSID, and truncated or space- padded
 as necessary

void
writeMQCHAR256(java.lang.String s)
Writes a 256-byte field from a String, converted according to the current
 CCSID, and truncated or space-padded as necessary

void
writeMQCHAR28(char[] c)
Writes a 28-byte field from a character array, converted according
 to the current CCSID, and truncated or space-padded as necessary.

void
writeMQCHAR28(char[] c,
             int off)
Writes a 28-byte field from an offset into a character array,
 converted according to the current CCSID, and truncated or space- padded
 as necessary

void
writeMQCHAR28(java.lang.String s)
Writes a 28-byte field from a String, converted according to the current
 CCSID, and truncated or space-padded as necessary

void
writeMQCHAR32(char[] c)
Writes a 32-byte field from a character array, converted according
 to the current CCSID, and truncated or space-padded as necessary.

void
writeMQCHAR32(char[] c,
             int off)
Writes a 32-byte field from an offset into a character array,
 converted according to the current CCSID, and truncated or space- padded
 as necessary

void
writeMQCHAR32(java.lang.String s)
Writes a 32-byte field from a String, converted according to the current
 CCSID, and truncated or space-padded as necessary

void
writeMQCHAR4(char[] c)
Writes a 4-byte field from a character array, converted according
 to the current CCSID, and truncated or space-padded as necessary.

void
writeMQCHAR4(char[] c,
            int off)
Writes a 4-byte field from an offset into a character array,
 converted according to the current CCSID, and truncated or space- padded
 as necessary

void
writeMQCHAR4(java.lang.String s)
Writes a 4-byte field from a String, converted according to the current
 CCSID, and truncated or space-padded as necessary

void
writeMQCHAR48(char[] c)
Writes a 48-byte field from a character array, converted according
 to the current CCSID, and truncated or space-padded as necessary.

void
writeMQCHAR48(char[] c,
             int off)
Writes a 48-byte field from an offset into a character array,
 converted according to the current CCSID, and truncated or space- padded
 as necessary

void
writeMQCHAR48(java.lang.String s)
Writes a 48-byte field from a String, converted according to the current
 CCSID, and truncated or space-padded as necessary

void
writeMQCHAR64(char[] c)
Writes a 64-byte field from a character array, converted according
 to the current CCSID, and truncated or space-padded as necessary.

void
writeMQCHAR64(char[] c,
             int off)
Writes a 64-byte field from an offset into a character array,
 converted according to the current CCSID, and truncated or space- padded
 as necessary

void
writeMQCHAR64(java.lang.String s)
Writes a 64-byte field from a String, converted according to the current
 CCSID, and truncated or space-padded as necessary

void
writeMQCHAR8(char[] c)
Writes an 8-byte field from a character array, converted according
 to the current CCSID, and truncated or space-padded as necessary.

void
writeMQCHAR8(char[] c,
            int off)
Writes an 8-byte field from an offset into a character array,
 converted according to the current CCSID, and truncated or space- padded
 as necessary

void
writeMQCHAR8(java.lang.String s)
Writes an 8-byte field from a String, converted according to the current
 CCSID, and truncated or space-padded as necessary

void
writeMQINT32(int i)
Writes an int as four bytes.

void
writeMQINT64(long l)
Writes a long as eight bytes.

void
writeMQLONG(int i)
Writes an int as four bytes.

void
writeMQSHORT(short s)
Writes a short as two bytes.

void
writeMQUINT32(long l)
Writes four-byte unsigned integer.

void
writeMQUINT64(java.math.BigInteger i)
Writes an eight-byte unsigned integer.

void
writeMQULONG(long l)
Writes a four-byte unsigned integer.

void
writeMQUSHORT(int s)
Writes a two-byte unsigned short integer.

void
writeObject(java.lang.Object object)
Writes a Serializable java Object to the stream

void
writeShort(short s)
Writes a short as two bytes.

void
writeUCS2Char(char c)
Writes a single Unicode character as two-byte UCS-2.

void
writeUTF(java.lang.String s)
Writes a String using UTF-8.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - setCCSID
void setCCSID(int ccsid)
              throws java.io.IOException
Sets the Coded Character Set Identifier to be used for subsequent
 character write operations.
Parameters:ccsid - new CCSID value
Throws:
java.nio.charset.UnsupportedCharsetException - if the JDK does not support
 this character set
java.io.IOException
    - getCCSID
int getCCSID()
             throws java.io.IOException
Returns the Coded Character Set Identifier currently used for
 character write operations
Returns:current CCSID value
Throws:
java.io.IOException
    - setIntegerEncoding
void setIntegerEncoding(IntegerEncoding ie)
                        throws java.io.IOException
Sets the IntegerEncoding to be uesd for subsequence integer write
 operations. IntegerEncoding.UNDEFINED is treated as IntegerEncoding.NORMAL.
Parameters:ie - new integer encoding value
Throws:
java.io.IOExceptionSee Also:IntegerEncoding
    - getIntegerEncoding
IntegerEncoding getIntegerEncoding()
                                   throws java.io.IOException
Returns the IntegerEncoding currently used for integer write operations.
Returns:current integer encoding
Throws:
java.io.IOExceptionSee Also:IntegerEncoding
    - setFloatEncoding
void setFloatEncoding(FloatEncoding fe)
                      throws java.io.IOException
Sets the FloatEncoding to be used for subsequent floating-point
 write operations. FloatEncoding.UNDEFINED is treated as
 FloatEncoding.IEEE\_NORMAL.
Parameters:fe - new floating-point encoding value
Throws:
java.io.IOExceptionSee Also:FloatEncoding
    - getFloatEncoding
FloatEncoding getFloatEncoding()
                               throws java.io.IOException
Returns the FloatEncoding currently used for floating-point write operations.
Returns:current floating-point encoding
Throws:
java.io.IOExceptionSee Also:FloatEncoding
    - setDecimalEncoding
void setDecimalEncoding(DecimalEncoding de)
                        throws java.io.IOException
Sets the DecimalEncoding to be used for subsequent packed-decimal
 write operations. DecimalEncoding.UNDEFINED is treated as
 DecimalEncoding.NORMAL
Parameters:de - new packed-decimal encoding value
Throws:
java.io.IOExceptionSee Also:DecimalEncoding
    - getDecimalEncoding
DecimalEncoding getDecimalEncoding()
                                   throws java.io.IOException
Returns the DecimalEncoding currently used for packed-decimal write operations.
Returns:current packed-decimal encoding
Throws:
java.io.IOExceptionSee Also:DecimalEncoding
    - setEncoding
void setEncoding(int encoding)
                 throws java.io.IOException
Sets all three encoding values - integer, floating-point and packed-decimal,
 using the WMQ encoding identifier. These will be used for subsequent numeric
 write operations.
Parameters:encoding - integer representation of the new encoding
Throws:
java.lang.IllegalArgumentException - if passed an unrecognised encoding identifier
java.io.IOException
    - getEncoding
int getEncoding()
                throws java.io.IOException
Return the WMQ encoding identifier representing the three encodings (integer,
 floating-point and packed-decimal) currently used for numeric write operations.
Returns:integer representation of the current encoding
Throws:
java.io.IOException
    - getDataOffset
int getDataOffset()
                  throws java.io.IOException
Returns the current offset of the cursor, relative to the position where
 this MQDataOutput object was originally created. Behaviour is undefined
 if the underlying data source has been manipulated without going through
 this MQDataOutput object.
Returns:number of bytes read or skipped
Throws:
java.io.IOException
    - writeByte
void writeByte(byte b)
               throws java.io.IOException
Writes a single (signed) byte
Throws:
java.io.IOException
    - writeBytes
void writeBytes(byte[] b)
                throws java.io.IOException
Writes an array of bytes
Parameters:b - array to write
Throws:
java.lang.NullPointerException - if b is null
java.io.IOException
    - writeBytes
void writeBytes(byte[] b,
              int off,
              int len,
              byte pad)
                throws java.io.IOException
Writes a portion of an array of bytes into a fixed-length field, truncating
 or padding as appropriate.
 If the array is not long enough to fill the field, the remainder of
 the field is padded with a given byte.
Parameters:b - source byte arrayoff - Offset of the start of the portion of b to writelen - Number of bytes to writepad - Padding byte to use if b is not long enough to provide len bytes after off.
Throws:
java.lang.NullPointerException - if b is null
java.lang.IllegalArgumentException - if len is negative
java.lang.IndexOutOfBoundsException - if off is negative or greater than the length of b
java.io.IOException
    - writeMQBYTE
void writeMQBYTE(byte b)
                 throws java.io.IOException
Writes a single (signed) byte
Throws:
java.io.IOException
    - writeMQBYTE
void writeMQBYTE(byte[] b)
                 throws java.io.IOException
Writes an array of bytes
Parameters:b - array to write
Throws:
java.lang.NullPointerException - if b is null
java.io.IOException
    - writeMQBYTE
void writeMQBYTE(int fieldLen,
               byte[] b)
                 throws java.io.IOException
Writes an array of bytes, truncated or null-padded as
 necessary, into a fixed-length field.
Parameters:fieldLen - Length of data to writeb - source byte array
Throws:
java.lang.NullPointerException - if b is null
java.lang.IllegalArgumentException - if fieldLen is negative
java.io.IOException
    - writeMQBYTE
void writeMQBYTE(int fieldLen,
               byte[] b,
               byte pad)
                 throws java.io.IOException
Writes an array of bytes, truncated or padded as necessary, into a
 fixed-length field.
Parameters:fieldLen - Length of data to writeb - source byte arraypad - byte to pad with if necessary
Throws:
java.lang.NullPointerException - if b is null
java.lang.IllegalArgumentException - if fieldLen is negative
java.io.IOException
    - writeMQBYTE
void writeMQBYTE(int fieldLen,
               byte[] b,
               int off)
                 throws java.io.IOException
Writes an array of bytes, from an offset and truncated or null-padded as
 necessary, into a fixed-length field
Parameters:fieldLen - Length of data to writeb - source byte arrayoff - offset of the start of the portion of b to write
Throws:
java.lang.NullPointerException - if b is null
java.lang.IllegalArgumentException - if fieldLen is negative
java.lang.IndexOutOfBoundsException - if off is negative or greater than the length of b
java.io.IOException
    - writeMQBYTE
void writeMQBYTE(int fieldLen,
               byte[] b,
               int off,
               byte pad)
                 throws java.io.IOException
Writes an array of bytes, from an offset and truncated or padded as
 necessary, into a fixed-length field
Parameters:fieldLen - Length of data to writeb - source byte arrayoff - offset of the start of the portion of b to writepad - value to use for padding
Throws:
java.lang.NullPointerException - if b is null
java.lang.IllegalArgumentException - if fieldLen is negative
java.lang.IndexOutOfBoundsException - if off is negative or greater than the length of b
java.io.IOException
    - writeMQBYTE8
void writeMQBYTE8(byte[] b)
                  throws java.io.IOException
Writes an 8-byte field from a byte array, truncated or null-padded as necessary.
Parameters:b - source byte array
Throws:
java.lang.NullPointerException - if b is null
java.io.IOException
    - writeMQBYTE8
void writeMQBYTE8(byte[] b,
                int off)
                  throws java.io.IOException
Writes an 8-byte field from a byte array, starting at a given offset, and
 truncating or null-padding as necessary.
Parameters:b - source byte arrayoff - offset into b of start of data
Throws:
java.lang.NullPointerException - if b is null
java.lang.IndexOutOfBoundsException - if off is negative or greater than the length of b
java.io.IOException
    - writeMQBYTE16
void writeMQBYTE16(byte[] b)
                   throws java.io.IOException
Writes a 16-byte field from a byte array, truncated or null-padded as necessary.
Parameters:b - source byte array
Throws:
java.lang.NullPointerException - if b is null
java.io.IOException
    - writeMQBYTE16
void writeMQBYTE16(byte[] b,
                 int off)
                   throws java.io.IOException
Writes a 16-byte field from a byte array, starting at a given offset, and
 truncating or null-padding as necessary.
Parameters:b - source byte arrayoff - offset into b of start of data
Throws:
java.lang.NullPointerException - if b is null
java.lang.IndexOutOfBoundsException - if off is negative or greater than the length of b
java.io.IOException
    - writeMQBYTE24
void writeMQBYTE24(byte[] b)
                   throws java.io.IOException
Writes a 24-byte field from a byte array, truncated or null-padded as necessary.
Parameters:b - source byte array
Throws:
java.lang.NullPointerException - if b is null
java.io.IOException
    - writeMQBYTE24
void writeMQBYTE24(byte[] b,
                 int off)
                   throws java.io.IOException
Writes a 24-byte field from a byte array, starting at a given offset, and
 truncating or null-padding as necessary.
Parameters:b - source byte arrayoff - offset into b of start of data
Throws:
java.lang.NullPointerException - if b is null
java.lang.IndexOutOfBoundsException - if off is negative or greater than the length of b
java.io.IOException
    - writeMQBYTE32
void writeMQBYTE32(byte[] b)
                   throws java.io.IOException
Writes a 32-byte field from a byte array, truncated or null-padded as necessary.
Parameters:b - source byte array
Throws:
java.lang.NullPointerException - if b is null
java.io.IOException
    - writeMQBYTE32
void writeMQBYTE32(byte[] b,
                 int off)
                   throws java.io.IOException
Writes a 32-byte field from a byte array, starting at a given offset, and
 truncating or null-padding as necessary.
Parameters:b - source byte arrayoff - offset into b of start of data
Throws:
java.lang.NullPointerException - if b is null
java.lang.IndexOutOfBoundsException - if off is negative or greater than the length of b
java.io.IOException
    - writeMQCHAR
void writeMQCHAR(char c)
                 throws java.io.IOException
Writes a character to the stream as a single byte, converted according
 to the current CCSID. Fails if the character is not represented by
 a single byte.
Throws:
java.io.IOException - if the character is not represented by a single byte,
 or for unexpected error
    - writeMQCHAR
void writeMQCHAR(char[] c)
                 throws java.io.IOException
Writes an array of characters to the stream, converted according to the
 current CCSID.
Parameters:c - character array to write.
Throws:
java.lang.NullPointerException - if c is null
java.io.IOException
    - writeMQCHAR
void writeMQCHAR(int fieldLen,
               char[] c)
                 throws java.io.IOException
Writes a fixed-length field from an array of characters, converted according
 to the current CCSID, and truncated or space-padded as necessary.
Parameters:fieldLen - number of bytes to writec - character array to write.
Throws:
java.lang.NullPointerException - if c is null
java.lang.IllegalArgumentException - if fieldLen is negative
java.io.IOException
    - writeMQCHAR
void writeMQCHAR(int fieldLen,
               char[] c,
               char pad)
                 throws java.io.IOException
Writes a fixed-length field from an array of characters, converted according
 to the current CCSID, and truncated or padded as necessary.
Parameters:fieldLen - number of bytes to writec - character array to write.pad - character to use for padding
Throws:
java.lang.NullPointerException - if c is null
java.lang.IllegalArgumentException - if fieldLen is negative
java.io.IOException
    - writeMQCHAR
void writeMQCHAR(int fieldLen,
               char[] c,
               int off)
                 throws java.io.IOException
Writes a fixed-length field from an offset into an array of characters,
 converted according to the current CCSID, and truncated or space-padded
 as necessary.
Parameters:fieldLen - number of bytes to writec - character array to write.off - offset of start of data in c
Throws:
java.lang.NullPointerException - if c is null
java.lang.IllegalArgumentException - if fieldLen is negative
java.lang.IndexOutOfBoundsException - if off is negative or greater than the length of c
java.io.IOException
    - writeMQCHAR
void writeMQCHAR(int fieldLen,
               char[] c,
               int off,
               char pad)
                 throws java.io.IOException
Writes a fixed-length field from an offset into an array of characters,
 converted according to the current CCSID, and truncated or padded
 as necessary.
Parameters:fieldLen - number of bytes to writec - character array to write.off - offset of start of data in cpad - character to use for padding
Throws:
java.lang.NullPointerException - if c is null
java.lang.IllegalArgumentException - if fieldLen is negative
java.lang.IndexOutOfBoundsException - if off is negative or greater than the length of c
java.io.IOException
    - writeMQCHAR
void writeMQCHAR(java.lang.String s)
                 throws java.io.IOException
Writes a String to the stream, converted according to the
 current CCSID.
Parameters:s - String to write.
Throws:
java.lang.NullPointerException - if s is null
java.io.IOException
    - writeMQCHAR
void writeMQCHAR(int fieldLen,
               java.lang.String s)
                 throws java.io.IOException
Writes a fixed-length field from a String, converted according
 to the current CCSID, and truncated or space-padded as necessary.
Parameters:fieldLen - number of bytes to writes - String to write.
Throws:
java.lang.NullPointerException - if s is null
java.lang.IllegalArgumentException - if fieldLen is negative
java.io.IOException
    - writeMQCHAR
void writeMQCHAR(int fieldLen,
               java.lang.String s,
               char pad)
                 throws java.io.IOException
Writes a fixed-length field from a String, converted according
 to the current CCSID, and truncated or padded as necessary.
Parameters:fieldLen - number of bytes to writes - String to write.pad - character to use for padding
Throws:
java.lang.NullPointerException - if s is null
java.lang.IllegalArgumentException - if fieldLen is negative
java.io.IOException
    - writeMQCHAR4
void writeMQCHAR4(char[] c)
                  throws java.io.IOException
Writes a 4-byte field from a character array, converted according
 to the current CCSID, and truncated or space-padded as necessary.
Parameters:c - source character array
Throws:
java.lang.NullPointerException - if c is null
java.io.IOException
    - writeMQCHAR4
void writeMQCHAR4(char[] c,
                int off)
                  throws java.io.IOException
Writes a 4-byte field from an offset into a character array,
 converted according to the current CCSID, and truncated or space- padded
 as necessary
Parameters:c - source character arrayoff - offset into c
Throws:
java.lang.NullPointerException - if c is null
java.lang.IndexOutOfBoundsException - if off is negative, or greater than the length of c
java.io.IOException
    - writeMQCHAR4
void writeMQCHAR4(java.lang.String s)
                  throws java.io.IOException
Writes a 4-byte field from a String, converted according to the current
 CCSID, and truncated or space-padded as necessary
Parameters:s - String to write
Throws:
java.lang.NullPointerException - if s is null
java.io.IOException
    - writeMQCHAR8
void writeMQCHAR8(char[] c)
                  throws java.io.IOException
Writes an 8-byte field from a character array, converted according
 to the current CCSID, and truncated or space-padded as necessary.
Parameters:c - source character array
Throws:
java.lang.NullPointerException - if c is null
java.io.IOException
    - writeMQCHAR8
void writeMQCHAR8(char[] c,
                int off)
                  throws java.io.IOException
Writes an 8-byte field from an offset into a character array,
 converted according to the current CCSID, and truncated or space- padded
 as necessary
Parameters:c - source character arrayoff - offset into c
Throws:
java.lang.NullPointerException - if c is null
java.lang.IndexOutOfBoundsException - if off is negative, or greater than the length of c
java.io.IOException
    - writeMQCHAR8
void writeMQCHAR8(java.lang.String s)
                  throws java.io.IOException
Writes an 8-byte field from a String, converted according to the current
 CCSID, and truncated or space-padded as necessary
Parameters:s - String to write
Throws:
java.lang.NullPointerException - if s is null
java.io.IOException
    - writeMQCHAR12
void writeMQCHAR12(char[] c)
                   throws java.io.IOException
Writes a 12-byte field from a character array, converted according
 to the current CCSID, and truncated or space-padded as necessary.
Parameters:c - source character array
Throws:
java.lang.NullPointerException - if c is null
java.io.IOException
    - writeMQCHAR12
void writeMQCHAR12(char[] c,
                 int off)
                   throws java.io.IOException
Writes a 12-byte field from an offset into a character array,
 converted according to the current CCSID, and truncated or space- padded
 as necessary
Parameters:c - source character arrayoff - offset into c
Throws:
java.lang.NullPointerException - if c is null
java.lang.IndexOutOfBoundsException - if off is negative, or greater than the length of c
java.io.IOException
    - writeMQCHAR12
void writeMQCHAR12(java.lang.String s)
                   throws java.io.IOException
Writes a 12-byte field from a String, converted according to the current
 CCSID, and truncated or space-padded as necessary
Parameters:s - String to write
Throws:
java.lang.NullPointerException - if s is null
java.io.IOException
    - writeMQCHAR16
void writeMQCHAR16(char[] c)
                   throws java.io.IOException
Writes a 16-byte field from a character array, converted according
 to the current CCSID, and truncated or space-padded as necessary.
Parameters:c - source character array
Throws:
java.lang.NullPointerException - if c is null
java.io.IOException
    - writeMQCHAR16
void writeMQCHAR16(char[] c,
                 int off)
                   throws java.io.IOException
Writes a 16-byte field from an offset into a character array,
 converted according to the current CCSID, and truncated or space- padded
 as necessary
Parameters:c - source character arrayoff - offset into c
Throws:
java.lang.NullPointerException - if c is null
java.lang.IndexOutOfBoundsException - if off is negative, or greater than the length of c
java.io.IOException
    - writeMQCHAR16
void writeMQCHAR16(java.lang.String s)
                   throws java.io.IOException
Writes a 16-byte field from a String, converted according to the current
 CCSID, and truncated or space-padded as necessary
Parameters:s - String to write
Throws:
java.lang.NullPointerException - if s is null
java.io.IOException
    - writeMQCHAR20
void writeMQCHAR20(char[] c)
                   throws java.io.IOException
Writes a 20-byte field from a character array, converted according
 to the current CCSID, and truncated or space-padded as necessary.
Parameters:c - source character array
Throws:
java.lang.NullPointerException - if c is null
java.io.IOException
    - writeMQCHAR20
void writeMQCHAR20(char[] c,
                 int off)
                   throws java.io.IOException
Writes a 20-byte field from an offset into a character array,
 converted according to the current CCSID, and truncated or space- padded
 as necessary
Parameters:c - source character arrayoff - offset into c
Throws:
java.lang.NullPointerException - if c is null
java.lang.IndexOutOfBoundsException - if off is negative, or greater than the length of c
java.io.IOException
    - writeMQCHAR20
void writeMQCHAR20(java.lang.String s)
                   throws java.io.IOException
Writes a 20-byte field from a String, converted according to the current
 CCSID, and truncated or space-padded as necessary
Parameters:s - String to write
Throws:
java.lang.NullPointerException - if s is null
java.io.IOException
    - writeMQCHAR24
void writeMQCHAR24(char[] c)
                   throws java.io.IOException
Writes a 24-byte field from a character array, converted according
 to the current CCSID, and truncated or space-padded as necessary.
Parameters:c - source character array
Throws:
java.lang.NullPointerException - if c is null
java.io.IOException
    - writeMQCHAR24
void writeMQCHAR24(char[] c,
                 int off)
                   throws java.io.IOException
Writes a 24-byte field from an offset into a character array,
 converted according to the current CCSID, and truncated or space- padded
 as necessary
Parameters:c - source character arrayoff - offset into c
Throws:
java.lang.NullPointerException - if c is null
java.lang.IndexOutOfBoundsException - if off is negative, or greater than the length of c
java.io.IOException
    - writeMQCHAR24
void writeMQCHAR24(java.lang.String s)
                   throws java.io.IOException
Writes a 24-byte field from a String, converted according to the current
 CCSID, and truncated or space-padded as necessary
Parameters:s - String to write
Throws:
java.lang.NullPointerException - if s is null
java.io.IOException
    - writeMQCHAR28
void writeMQCHAR28(char[] c)
                   throws java.io.IOException
Writes a 28-byte field from a character array, converted according
 to the current CCSID, and truncated or space-padded as necessary.
Parameters:c - source character array
Throws:
java.lang.NullPointerException - if c is null
java.io.IOException
    - writeMQCHAR28
void writeMQCHAR28(char[] c,
                 int off)
                   throws java.io.IOException
Writes a 28-byte field from an offset into a character array,
 converted according to the current CCSID, and truncated or space- padded
 as necessary
Parameters:c - source character arrayoff - offset into c
Throws:
java.lang.NullPointerException - if c is null
java.lang.IndexOutOfBoundsException - if off is negative, or greater than the length of c
java.io.IOException
    - writeMQCHAR28
void writeMQCHAR28(java.lang.String s)
                   throws java.io.IOException
Writes a 28-byte field from a String, converted according to the current
 CCSID, and truncated or space-padded as necessary
Parameters:s - String to write
Throws:
java.lang.NullPointerException - if s is null
java.io.IOException
    - writeMQCHAR32
void writeMQCHAR32(char[] c)
                   throws java.io.IOException
Writes a 32-byte field from a character array, converted according
 to the current CCSID, and truncated or space-padded as necessary.
Parameters:c - source character array
Throws:
java.lang.NullPointerException - if c is null
java.io.IOException
    - writeMQCHAR32
void writeMQCHAR32(char[] c,
                 int off)
                   throws java.io.IOException
Writes a 32-byte field from an offset into a character array,
 converted according to the current CCSID, and truncated or space- padded
 as necessary
Parameters:c - source character arrayoff - offset into c
Throws:
java.lang.NullPointerException - if c is null
java.lang.IndexOutOfBoundsException - if off is negative, or greater than the length of c
java.io.IOException
    - writeMQCHAR32
void writeMQCHAR32(java.lang.String s)
                   throws java.io.IOException
Writes a 32-byte field from a String, converted according to the current
 CCSID, and truncated or space-padded as necessary
Parameters:s - String to write
Throws:
java.lang.NullPointerException - if s is null
java.io.IOException
    - writeMQCHAR48
void writeMQCHAR48(char[] c)
                   throws java.io.IOException
Writes a 48-byte field from a character array, converted according
 to the current CCSID, and truncated or space-padded as necessary.
Parameters:c - source character array
Throws:
java.lang.NullPointerException - if c is null
java.io.IOException
    - writeMQCHAR48
void writeMQCHAR48(char[] c,
                 int off)
                   throws java.io.IOException
Writes a 48-byte field from an offset into a character array,
 converted according to the current CCSID, and truncated or space- padded
 as necessary
Parameters:c - source character arrayoff - offset into c
Throws:
java.lang.NullPointerException - if c is null
java.lang.IndexOutOfBoundsException - if off is negative, or greater than the length of c
java.io.IOException
    - writeMQCHAR48
void writeMQCHAR48(java.lang.String s)
                   throws java.io.IOException
Writes a 48-byte field from a String, converted according to the current
 CCSID, and truncated or space-padded as necessary
Parameters:s - String to write
Throws:
java.lang.NullPointerException - if s is null
java.io.IOException
    - writeMQCHAR64
void writeMQCHAR64(char[] c)
                   throws java.io.IOException
Writes a 64-byte field from a character array, converted according
 to the current CCSID, and truncated or space-padded as necessary.
Parameters:c - source character array
Throws:
java.lang.NullPointerException - if c is null
java.io.IOException
    - writeMQCHAR64
void writeMQCHAR64(char[] c,
                 int off)
                   throws java.io.IOException
Writes a 64-byte field from an offset into a character array,
 converted according to the current CCSID, and truncated or space- padded
 as necessary
Parameters:c - source character arrayoff - offset into c
Throws:
java.lang.NullPointerException - if c is null
java.lang.IndexOutOfBoundsException - if off is negative, or greater than the length of c
java.io.IOException
    - writeMQCHAR64
void writeMQCHAR64(java.lang.String s)
                   throws java.io.IOException
Writes a 64-byte field from a String, converted according to the current
 CCSID, and truncated or space-padded as necessary
Parameters:s - String to write
Throws:
java.lang.NullPointerException - if s is null
java.io.IOException
    - writeMQCHAR128
void writeMQCHAR128(char[] c)
                    throws java.io.IOException
Writes a 128-byte field from a character array, converted according
 to the current CCSID, and truncated or space-padded as necessary.
Parameters:c - source character array
Throws:
java.lang.NullPointerException - if c is null
java.io.IOException
    - writeMQCHAR128
void writeMQCHAR128(char[] c,
                  int off)
                    throws java.io.IOException
Writes a 128-byte field from an offset into a character array,
 converted according to the current CCSID, and truncated or space- padded
 as necessary
Parameters:c - source character arrayoff - offset into c
Throws:
java.lang.NullPointerException - if c is null
java.lang.IndexOutOfBoundsException - if off is negative, or greater than the length of c
java.io.IOException
    - writeMQCHAR128
void writeMQCHAR128(java.lang.String s)
                    throws java.io.IOException
Writes a 128-byte field from a String, converted according to the current
 CCSID, and truncated or space-padded as necessary
Parameters:s - String to write
Throws:
java.lang.NullPointerException - if s is null
java.io.IOException
    - writeMQCHAR256
void writeMQCHAR256(char[] c)
                    throws java.io.IOException
Writes a 256-byte field from a character array, converted according
 to the current CCSID, and truncated or space-padded as necessary.
Parameters:c - source character array
Throws:
java.lang.NullPointerException - if c is null
java.io.IOException
    - writeMQCHAR256
void writeMQCHAR256(char[] c,
                  int off)
                    throws java.io.IOException
Writes a 256-byte field from an offset into a character array,
 converted according to the current CCSID, and truncated or space- padded
 as necessary
Parameters:c - source character arrayoff - offset into c
Throws:
java.lang.NullPointerException - if c is null
java.lang.IndexOutOfBoundsException - if off is negative, or greater than the length of c
java.io.IOException
    - writeMQCHAR256
void writeMQCHAR256(java.lang.String s)
                    throws java.io.IOException
Writes a 256-byte field from a String, converted according to the current
 CCSID, and truncated or space-padded as necessary
Parameters:s - String to write
Throws:
java.lang.NullPointerException - if s is null
java.io.IOException
    - writeUCS2Char
void writeUCS2Char(char c)
                   throws java.io.IOException
Writes a single Unicode character as two-byte UCS-2.
 The byte order is determined by the current integer encoding.
Parameters:c - character to write
Throws:
java.io.IOException
    - writeUTF
void writeUTF(java.lang.String s)
              throws java.io.IOException
Writes a String using UTF-8. The String is preceeded by two bytes
 which give the length of the string. Compatible with DataInput.readUTF().
Parameters:s - String to write
Throws:
java.lang.NullPointerException - if s is null
java.io.IOExceptionSee Also:DataOutput.writeUTF(String)
    - writeShort
void writeShort(short s)
                throws java.io.IOException
Writes a short as two bytes. The byte order is determined by the
 current integer encoding.
Parameters:s - short to write
Throws:
java.io.IOExceptionSee Also:DataOutput.writeShort(int)
    - writeMQSHORT
void writeMQSHORT(short s)
                  throws java.io.IOException
Writes a short as two bytes. The byte order is determined by the
 current integer encoding.
Parameters:s - short to write
Throws:
java.io.IOException
    - writeMQUSHORT
void writeMQUSHORT(int s)
                   throws java.io.IOException
Writes a two-byte unsigned short integer. The byte order is determined
 by the current integer encoding.
Parameters:s - integer to write
Throws:
java.lang.IllegalArgumentException - if s is out-of-range for a two-byte unsigned integer;
 that is, less than 0 or greater than 65535.
java.io.IOException
    - writeInt
void writeInt(int i)
              throws java.io.IOException
Writes an int as four bytes. The byte order is determined by the
 current integer encoding.
Parameters:i - int to write
Throws:
java.io.IOExceptionSee Also:DataOutput.writeInt(int)
    - writeMQLONG
void writeMQLONG(int i)
                 throws java.io.IOException
Writes an int as four bytes. The byte order is determined by the
 current integer encoding.
Parameters:i - int to write
Throws:
java.io.IOException
    - writeMQULONG
void writeMQULONG(long l)
                  throws java.io.IOException
Writes a four-byte unsigned integer. The byte order is determined
 by the current integer encoding.
Parameters:l - integer to write
Throws:
java.lang.IllegalArgumentException - if l is out-of-range for a four-byte unsigned integer;
 that is, less than 0 or greater than 4294967295.
java.io.IOException
    - writeMQINT32
void writeMQINT32(int i)
                  throws java.io.IOException
Writes an int as four bytes. The byte order is determined by the
 current integer encoding.
Parameters:i - int to write
Throws:
java.io.IOExceptionSee Also:DataOutput.writeInt(int)
    - writeMQUINT32
void writeMQUINT32(long l)
                   throws java.io.IOException
Writes four-byte unsigned integer. The byte order is determined
 by the current integer encoding.
Parameters:l - integer to write
Throws:
java.lang.IllegalArgumentException - if i is out-of-range for a four-byte unsigned integer;
 that is, less than 0 or greater than 4294967295.
java.io.IOException
    - writeLong
void writeLong(long l)
               throws java.io.IOException
Writes a long as eight bytes. The byte order is determined by the
 current integer encoding.
Parameters:l - long to write
Throws:
java.io.IOExceptionSee Also:DataOutput.writeInt(int)
    - writeMQINT64
void writeMQINT64(long l)
                  throws java.io.IOException
Writes a long as eight bytes. The byte order is determined by the
 current integer encoding.
Parameters:l - long to write
Throws:
java.io.IOException
    - writeMQUINT64
void writeMQUINT64(java.math.BigInteger i)
                   throws java.io.IOException
Writes an eight-byte unsigned integer. The byte order is determined
 by the current integer encoding.
Parameters:i - integer to write
Throws:
java.lang.NullPointerException - if i is null
java.lang.IllegalArgumentException - if i is out-of-range for an eight-byte unsigned integer;
 that is, less than 0 or greater than 18446744073709551615.
java.io.IOException
    - writeFloat
void writeFloat(float f)
                throws java.io.IOException
Writes a float as four bytes, according to the current floating-point encoding.
 If the S390 encoding is used, this uses the short HFP format. Note that conversion
 to this format from a Java float may lose precision.
Parameters:f - float to write
Throws:
java.io.IOExceptionSee Also:DataOutput.writeFloat(float)
    - writeDouble
void writeDouble(double d)
                 throws java.io.IOException
Writes a double as eight bytes, according to the current floating-point encoding.
 If the S390 encoding is used, this uses the long HFP format. Note that conversion
 to this format from a Java double may lose precision.
Parameters:d - float to write
Throws:
java.io.IOExceptionSee Also:DataOutput.writeDouble(double)
    - writeDecimal
void writeDecimal(int fieldLen,
                java.math.BigInteger bi)
                  throws java.io.IOException
Writes a packed-decimal integer into a fixed-length field. The current packed-decimal
 encoding determines the byte order.
Parameters:fieldLen - number of bytes to writebi - the BigInteger to write as packed-decimal.
Throws:
java.lang.NullPointerException - if bi is null
java.lang.IllegalArgumentException - if fieldLen is less than 1, or if bi is out-of-range for
 the given fieldLen; that is, if abs(fieldLen) >= 10(2*fieldLen-1)
java.io.IOException - if a malformed packed-decimal is encountered, or for other error.
    - writeDecimal2
void writeDecimal2(short s)
                   throws java.io.IOException
Writes a two-byte packed decimal integer. The current packed-decimal encoding
 determines the byte order
Parameters:s - integer to write as packed-decimal
Throws:
java.lang.IllegalArgumentException - if s is not between -999 and 999 inclusive
java.io.IOException
    - writeDecimal4
void writeDecimal4(int i)
                   throws java.io.IOException
Writes a four-byte packed decimal integer. The current packed-decimal encoding
 determines the byte order
Parameters:i - integer to write as packed-decimal
Throws:
java.lang.IllegalArgumentException - if s is not between -9999999 and 9999999 inclusive
java.io.IOException
    - writeDecimal8
void writeDecimal8(long l)
                   throws java.io.IOException
Writes an eight-byte packed decimal integer. The current packed-decimal encoding
 determines the byte order
Parameters:l - integer to write as packed-decimal
Throws:
java.lang.IllegalArgumentException - if s is not between -1015 and 1015 exclusive
java.io.IOException
    - writeObject
void writeObject(java.lang.Object object)
                 throws java.io.IOException
Writes a Serializable java Object to the stream
Parameters:object - object to serialize
Throws:
java.io.NotSerializableException - if object a non-Serializable object is encountered
java.io.IOExceptionSee Also:ObjectOutput.writeObject(Object)