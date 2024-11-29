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

## Interface MQDataInput

- All Known Implementing Classes:
MQDataInputStream

public interface MQDataInput
An MQDataInput implementation allows read access to some underlying store of
 semi-structured binary data. It provides read methods for character data,
 integer data, floating-point data, packed decimal data and serialized Java
 objects. It converts between different representations of this data (e.g.
 EBCDIC/ASCII character data, big-endian and little-endian integer data) driven
 by the CCSID and encoding properties. It is intended for reading WebSphere MQ
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
 character read operations

int
getDataOffset()
Returns the current offset of the cursor, relative to the position where
 this MQDataOutput object was originally created.

DecimalEncoding
getDecimalEncoding()
Returns the DecimalEncoding currently used for packed-decimal read operations.

int
getEncoding()
Return the WMQ encoding identifier representing the three encodings (integer,
 floating-point and packed-decimal) currently used for numeric read operations.

FloatEncoding
getFloatEncoding()
Returns the FloatEncoding currently used for floating-point read operations.

IntegerEncoding
getIntegerEncoding()
Returns the IntegerEncoding currently used for integer read operations.

byte
readByte()
Reads a single (signed) byte.

byte[]
readBytes(int length)
Reads a number of (signed) bytes from the stream, returning them as an array.

java.math.BigInteger
readDecimal(int length)
Reads a number of bytes as a packed-decimal integer.

short
readDecimal2()
Reads two bytes as a packed-decimal integer.

int
readDecimal4()
Reads four bytes as a packed-decimal integer.

long
readDecimal8()
Reads eight bytes as a packed-decimal integer.

double
readDouble()
Reads eight bytes as a floating-point number, interpreted according to the
 current floating-point encoding.

float
readFloat()
Reads four bytes as a floating-point number, interpreted according to the
 current floating-point encoding.

void
readFully(byte[] b)
Reads bytes into the parameter byte array.

void
readFully(byte[] b,
         int off,
         int len)
Reads some number of bytes into a bytearray beginning from a given
 offset into the byte array.

int
readInt()
Reads four bytes as a signed integer.

long
readLong()
Reads eight bytes as a signed long integer.

byte
readMQBYTE()
Reads a single (signed) byte.

byte[]
readMQBYTE(int length)
Reads a number of (signed) bytes from the stream, returning them as an array.

byte[]
readMQBYTE16()
Reads 16 bytes from the stream, returning them as an array.

byte[]
readMQBYTE24()
Reads 24 bytes from the stream, returning them as an array.

byte[]
readMQBYTE32()
Reads 32 bytes from the stream, returning them as an array.

byte[]
readMQBYTE8()
Reads 8 bytes from the stream, returning them as an array.

char
readMQCHAR()
Reads a single byte from the stream and converts it to a character,
 using the current CCSID.

java.lang.String
readMQCHAR(int length)
Reads a number of bytes from the stream and converts them into
 a String, using the current CCSID.

java.lang.String
readMQCHAR12()
Reads 12 bytes from the stream and converts them into a String, using
 the current CCSID.

java.lang.String
readMQCHAR128()
Reads 128 bytes from the stream and converts them into a String, using
 the current CCSID.

java.lang.String
readMQCHAR16()
Reads 16 bytes from the stream and converts them into a String, using
 the current CCSID.

java.lang.String
readMQCHAR20()
Reads 20 bytes from the stream and converts them into a String, using
 the current CCSID.

java.lang.String
readMQCHAR24()
Reads 24 bytes from the stream and converts them into a String, using
 the current CCSID.

java.lang.String
readMQCHAR256()
Reads 256 bytes from the stream and converts them into a String, using
 the current CCSID.

java.lang.String
readMQCHAR28()
Reads 28 bytes from the stream and converts them into a String, using
 the current CCSID.

java.lang.String
readMQCHAR32()
Reads 32 bytes from the stream and converts them into a String, using
 the current CCSID.

java.lang.String
readMQCHAR4()
Reads 4 bytes from the stream and converts them into a String, using
 the current CCSID.

java.lang.String
readMQCHAR48()
Reads 48 bytes from the stream and converts them into a String, using
 the current CCSID.

java.lang.String
readMQCHAR64()
Reads 64 bytes from the stream and converts them into a String, using
 the current CCSID.

java.lang.String
readMQCHAR8()
Reads 8 bytes from the stream and converts them into a String, using
 the current CCSID.

int
readMQINT32()
Reads four bytes as a signed integer.

long
readMQINT64()
Reads eight bytes as a signed long integer.

int
readMQLONG()
Reads four bytes as a signed integer.

short
readMQSHORT()
Reads two bytes as a signed short.

long
readMQUINT32()
Reads four bytes as an unsigned integer.

java.math.BigInteger
readMQUINT64()
Reads eight bytes as an unsigned integer.

long
readMQULONG()
Reads four bytes as an unsigned integer.

int
readMQUSHORT()
Reads two bytes as an unsigned integer.

java.lang.Object
readObject()
Reads a serialized Java Object from the stream

short
readShort()
Reads two bytes as a signed short.

char
readUCS2Char()
Reads two bytes from the stream and interprets it as a Unicode character.

java.lang.String
readUTF()
Reads a UTF-8 encoded string from the stream.

void
setCCSID(int ccsid)
Sets the Coded Character Set Identifier to be used for subsequent
 character read operations.

void
setDecimalEncoding(DecimalEncoding de)
Sets the DecimalEncoding to be used for subsequent packed-decimal
 read operations.

void
setEncoding(int encoding)
Sets all three encoding values - integer, floating-point and packed-decimal,
 using the WMQ encoding identifier.

void
setFloatEncoding(FloatEncoding fe)
Sets the FloatEncoding to be used for subsequent floating-point
 read operations.

void
setIntegerEncoding(IntegerEncoding ie)
Sets the IntegerEncoding to be uesd for subsequence integer read
 operations.

int
skipBytes(int n)
Attempts to skip over a number of bytes, returning the number of bytes
 actually skipped.

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
 character read operations.
Parameters:ccsid - new CCSID value
Throws:
java.nio.charset.UnsupportedCharsetException - if the JDK does not support
 this character set
java.io.IOException
    - getCCSID
int getCCSID()
             throws java.io.IOException
Returns the Coded Character Set Identifier currently used for
 character read operations
Returns:current CCSID value
Throws:
java.io.IOException
    - setIntegerEncoding
void setIntegerEncoding(IntegerEncoding ie)
                        throws java.io.IOException
Sets the IntegerEncoding to be uesd for subsequence integer read
 operations. IntegerEncoding.UNDEFINED is treated as IntegerEncoding.NORMAL.
Parameters:ie - new integer encoding value
Throws:
java.io.IOExceptionSee Also:IntegerEncoding
    - getIntegerEncoding
IntegerEncoding getIntegerEncoding()
                                   throws java.io.IOException
Returns the IntegerEncoding currently used for integer read operations.
Returns:current integer encoding
Throws:
java.io.IOExceptionSee Also:IntegerEncoding
    - setFloatEncoding
void setFloatEncoding(FloatEncoding fe)
                      throws java.io.IOException
Sets the FloatEncoding to be used for subsequent floating-point
 read operations. FloatEncoding.UNDEFINED is treated as
 FloatEncoding.IEEE\_NORMAL.
Parameters:fe - new floating-point encoding value
Throws:
java.io.IOExceptionSee Also:FloatEncoding
    - getFloatEncoding
FloatEncoding getFloatEncoding()
                               throws java.io.IOException
Returns the FloatEncoding currently used for floating-point read operations.
Returns:current floating-point encoding
Throws:
java.io.IOExceptionSee Also:FloatEncoding
    - setDecimalEncoding
void setDecimalEncoding(DecimalEncoding de)
                        throws java.io.IOException
Sets the DecimalEncoding to be used for subsequent packed-decimal
 read operations. DecimalEncoding.UNDEFINED is treated as
 DecimalEncoding.NORMAL
Parameters:de - new packed-decimal encoding value
Throws:
java.io.IOExceptionSee Also:DecimalEncoding
    - getDecimalEncoding
DecimalEncoding getDecimalEncoding()
                                   throws java.io.IOException
Returns the DecimalEncoding currently used for packed-decimal read operations.
Returns:current packed-decimal encoding
Throws:
java.io.IOExceptionSee Also:DecimalEncoding
    - setEncoding
void setEncoding(int encoding)
                 throws java.io.IOException
Sets all three encoding values - integer, floating-point and packed-decimal,
 using the WMQ encoding identifier. These will be used for subsequent numeric
 read operations.
Parameters:encoding - integer representation of the new encoding
Throws:
java.lang.IllegalArgumentException - if passed an unrecognised encoding identifier
java.io.IOException
    - getEncoding
int getEncoding()
                throws java.io.IOException
Return the WMQ encoding identifier representing the three encodings (integer,
 floating-point and packed-decimal) currently used for numeric read operations.
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
    - skipBytes
int skipBytes(int n)
              throws java.io.IOException
Attempts to skip over a number of bytes, returning the number of bytes
 actually skipped.
Parameters:n - number of bytes to attempt to skip
Returns:number of bytes actually skipped; 0 if at the end of the stream.
Throws:
java.io.IOExceptionSee Also:DataInput.skipBytes(int)
    - readByte
byte readByte()
              throws java.io.IOException
Reads a single (signed) byte.
Returns:byte read from stream
Throws:
java.io.EOFException - if at the end of the stream
java.io.IOException
    - readBytes
byte[] readBytes(int length)
                 throws java.io.IOException
Reads a number of (signed) bytes from the stream, returning them as an array.
Parameters:length - number of bytes to read
Returns:an array containing the read bytes
Throws:
java.io.EOFException - if at the end of the stream
java.io.IOException
    - readMQBYTE
byte readMQBYTE()
                throws java.io.IOException
Reads a single (signed) byte.
Returns:byte read from stream
Throws:
java.io.EOFException - if at the end of the stream
java.io.IOException
    - readMQBYTE
byte[] readMQBYTE(int length)
                  throws java.io.IOException
Reads a number of (signed) bytes from the stream, returning them as an array.
Parameters:length - number of bytes to read
Returns:an array containing the read bytes
Throws:
java.io.EOFException - if at the end of the stream
java.io.IOException
    - readMQBYTE8
byte[] readMQBYTE8()
                   throws java.io.IOException
Reads 8 bytes from the stream, returning them as an array.
Returns:an array containing the read bytes
Throws:
java.io.EOFException - if at the end of the stream
java.io.IOException
    - readMQBYTE16
byte[] readMQBYTE16()
                    throws java.io.IOException
Reads 16 bytes from the stream, returning them as an array.
Returns:an array containing the read bytes
Throws:
java.io.EOFException - if at the end of the stream
java.io.IOException
    - readMQBYTE24
byte[] readMQBYTE24()
                    throws java.io.IOException
Reads 24 bytes from the stream, returning them as an array.
Returns:an array containing the read bytes
Throws:
java.io.EOFException - if at the end of the stream
java.io.IOException
    - readMQBYTE32
byte[] readMQBYTE32()
                    throws java.io.IOException
Reads 32 bytes from the stream, returning them as an array.
Returns:an array containing the read bytes
Throws:
java.io.EOFException - if at the end of the stream
java.io.IOException
    - readFully
void readFully(byte[] b)
               throws java.io.IOException
Reads bytes into the parameter byte array.
Parameters:b - byte array to read into
Throws:
java.lang.NullPointerException - if b is null
java.io.EOFException - if the stream does not have enough data left to
 fill the byte array
java.io.IOExceptionSee Also:DataInput.readFully(byte[])
    - readFully
void readFully(byte[] b,
             int off,
             int len)
               throws java.io.IOException
Reads some number of bytes into a bytearray beginning from a given
 offset into the byte array.
Parameters:b - byte array to read intooff - starting index in the byte arraylen - number of bytes to read
Throws:
java.lang.NullPointerException - if b is null
java.lang.IndexOutOfBoundsException - if off is negative, len is negative, or
 off+len is greater than the length of b
java.io.EOFException - if the stream ends before len bytes have been read
java.io.IOExceptionSee Also:DataInput.readFully(byte[], int, int)
    - readMQCHAR
char readMQCHAR()
                throws java.io.IOException
Reads a single byte from the stream and converts it to a character,
 using the current CCSID. Fails if the next byte in the stream does
 not completely represent a single character.
Returns:a byte from the stream as a character
Throws:
java.io.EOFException - at end of stream
java.io.IOException - if the next byte does not completely represent
 a single character, or for unexpected errors.
    - readMQCHAR
java.lang.String readMQCHAR(int length)
                            throws java.io.IOException
Reads a number of bytes from the stream and converts them into
 a String, using the current CCSID.
Parameters:length - number of bytes to read
Throws:
java.nio.charset.CharacterCodingException - if conversion fails
java.io.EOFException - at end of stream
java.io.IOException
    - readMQCHAR4
java.lang.String readMQCHAR4()
                             throws java.io.IOException
Reads 4 bytes from the stream and converts them into a String, using
 the current CCSID.
Returns:String read from the stream
Throws:
java.nio.charset.CharacterCodingException - if conversion fails
java.io.EOFException - at end of stream
java.io.IOException
    - readMQCHAR8
java.lang.String readMQCHAR8()
                             throws java.io.IOException
Reads 8 bytes from the stream and converts them into a String, using
 the current CCSID.
Returns:String read from the stream
Throws:
java.nio.charset.CharacterCodingException - if conversion fails
java.io.EOFException - at end of stream
java.io.IOException
    - readMQCHAR12
java.lang.String readMQCHAR12()
                              throws java.io.IOException
Reads 12 bytes from the stream and converts them into a String, using
 the current CCSID.
Returns:String read from the stream
Throws:
java.nio.charset.CharacterCodingException - if conversion fails
java.io.EOFException - at end of stream
java.io.IOException
    - readMQCHAR16
java.lang.String readMQCHAR16()
                              throws java.io.IOException
Reads 16 bytes from the stream and converts them into a String, using
 the current CCSID.
Returns:String read from the stream
Throws:
java.nio.charset.CharacterCodingException - if conversion fails
java.io.EOFException - at end of stream
java.io.IOException
    - readMQCHAR20
java.lang.String readMQCHAR20()
                              throws java.io.IOException
Reads 20 bytes from the stream and converts them into a String, using
 the current CCSID.
Returns:String read from the stream
Throws:
java.nio.charset.CharacterCodingException - if conversion fails
java.io.EOFException - at end of stream
java.io.IOException
    - readMQCHAR24
java.lang.String readMQCHAR24()
                              throws java.io.IOException
Reads 24 bytes from the stream and converts them into a String, using
 the current CCSID.
Returns:String read from the stream
Throws:
java.nio.charset.CharacterCodingException - if conversion fails
java.io.EOFException - at end of stream
java.io.IOException
    - readMQCHAR28
java.lang.String readMQCHAR28()
                              throws java.io.IOException
Reads 28 bytes from the stream and converts them into a String, using
 the current CCSID.
Returns:String read from the stream
Throws:
java.nio.charset.CharacterCodingException - if conversion fails
java.io.EOFException - at end of stream
java.io.IOException
    - readMQCHAR32
java.lang.String readMQCHAR32()
                              throws java.io.IOException
Reads 32 bytes from the stream and converts them into a String, using
 the current CCSID.
Returns:String read from the stream
Throws:
java.nio.charset.CharacterCodingException - if conversion fails
java.io.EOFException - at end of stream
java.io.IOException
    - readMQCHAR48
java.lang.String readMQCHAR48()
                              throws java.io.IOException
Reads 48 bytes from the stream and converts them into a String, using
 the current CCSID.
Returns:String read from the stream
Throws:
java.nio.charset.CharacterCodingException - if conversion fails
java.io.EOFException - at end of stream
java.io.IOException
    - readMQCHAR64
java.lang.String readMQCHAR64()
                              throws java.io.IOException
Reads 64 bytes from the stream and converts them into a String, using
 the current CCSID.
Returns:String read from the stream
Throws:
java.nio.charset.CharacterCodingException - if conversion fails
java.io.EOFException - at end of stream
java.io.IOException
    - readMQCHAR128
java.lang.String readMQCHAR128()
                               throws java.io.IOException
Reads 128 bytes from the stream and converts them into a String, using
 the current CCSID.
Returns:String read from the stream
Throws:
java.nio.charset.CharacterCodingException - if conversion fails
java.io.EOFException - at end of stream
java.io.IOException
    - readMQCHAR256
java.lang.String readMQCHAR256()
                               throws java.io.IOException
Reads 256 bytes from the stream and converts them into a String, using
 the current CCSID.
Returns:String read from the stream
Throws:
java.nio.charset.CharacterCodingException - if conversion fails
java.io.EOFException - at end of stream
java.io.IOException
    - readUCS2Char
char readUCS2Char()
                  throws java.io.IOException
Reads two bytes from the stream and interprets it as a Unicode character.
 The byte-order is determined by the current integer encoding.
Returns:a character read from the stream
Throws:
java.io.EOFException - at end of stream
java.io.IOException
    - readUTF
java.lang.String readUTF()
                         throws java.io.IOException
Reads a UTF-8 encoded string from the stream. The first two bytes of the
 stream give the length of the string. This is compatible with DataInput.writeUTF().
Returns:a String, read from the stream
Throws:
java.io.EOFException - at end of stream
java.io.UTFDataFormatException - if the stream does not contain a valid UTF-8 string
java.io.IOExceptionSee Also:DataInput.readUTF()
    - readShort
short readShort()
                throws java.io.IOException
Reads two bytes as a signed short. The byte order is determined
 by the current integer encoding.
Returns:the read short
Throws:
java.io.EOFException - at end of stream
java.io.IOExceptionSee Also:DataInput.readShort()
    - readMQSHORT
short readMQSHORT()
                  throws java.io.IOException
Reads two bytes as a signed short. The byte order is determined
 by the current integer encoding.
Returns:the read short
Throws:
java.io.EOFException - at end of stream
java.io.IOException
    - readMQUSHORT
int readMQUSHORT()
                 throws java.io.IOException
Reads two bytes as an unsigned integer. The byte order is determined
 by the current integer encoding.
Returns:a two-byte unsigned integer, as an int
Throws:
java.io.EOFException - at end of stream
java.io.IOException
    - readInt
int readInt()
            throws java.io.IOException
Reads four bytes as a signed integer. The byte order is determined
 by the current integer encoding.
Returns:the read int
Throws:
java.io.EOFException - at end of stream
java.io.IOExceptionSee Also:DataInput.readInt()
    - readMQLONG
int readMQLONG()
               throws java.io.IOException
Reads four bytes as a signed integer. The byte order is determined
 by the current integer encoding.
Returns:the read int
Throws:
java.io.EOFException - at end of stream
java.io.IOException
    - readMQULONG
long readMQULONG()
                 throws java.io.IOException
Reads four bytes as an unsigned integer. The byte order is determined
 by the current integer encoding.
Returns:a four-byte unsigned integer, as a long
Throws:
java.io.EOFException - at end of stream
java.io.IOException
    - readMQINT32
int readMQINT32()
                throws java.io.IOException
Reads four bytes as a signed integer. The byte order is determined
 by the current integer encoding.
Returns:the read int
Throws:
java.io.EOFException - at end of stream
java.io.IOException
    - readMQUINT32
long readMQUINT32()
                  throws java.io.IOException
Reads four bytes as an unsigned integer. The byte order is determined
 by the current integer encoding.
Returns:a four-byte unsigned integer, as a long
Throws:
java.io.EOFException - at end of stream
java.io.IOException
    - readLong
long readLong()
              throws java.io.IOException
Reads eight bytes as a signed long integer. The byte order is determined
 by the current integer encoding.
Returns:the read long
Throws:
java.io.EOFException - at end of stream
java.io.IOExceptionSee Also:DataInput.readLong()
    - readMQINT64
long readMQINT64()
                 throws java.io.IOException
Reads eight bytes as a signed long integer. The byte order is determined
 by the current integer encoding.
Returns:the read long
Throws:
java.io.EOFException - at end of stream
java.io.IOException
    - readMQUINT64
java.math.BigInteger readMQUINT64()
                                  throws java.io.IOException
Reads eight bytes as an unsigned integer. The byte order is determined
 by the current integer encoding.
Returns:an eight-byte unsigned integer, as a BigInteger
Throws:
java.io.EOFException - at end of stream
java.io.IOException
    - readFloat
float readFloat()
                throws java.io.IOException
Reads four bytes as a floating-point number, interpreted according to the
 current floating-point encoding. If the S390 encoding is used, this is the
 short HFP format. Note that conversion from this format to a Java float may
 lose precision.
Returns:a four-byte precision floating point number.
Throws:
java.io.EOFException - at end of stream
java.io.IOExceptionSee Also:DataInput.readFloat()
    - readDouble
double readDouble()
                  throws java.io.IOException
Reads eight bytes as a floating-point number, interpreted according to the
 current floating-point encoding. If the S390 encoding is used, this is the
 long HFP format. Note that conversion from this format to a Java double may
 lose precision.
Returns:an eight-byte precision floating point number.
Throws:
java.io.EOFException - at end of stream
java.io.IOExceptionSee Also:DataInput.readFloat()
    - readDecimal
java.math.BigInteger readDecimal(int length)
                                 throws java.io.IOException
Reads a number of bytes as a packed-decimal integer. The current packed-decimal
 encoding determines the byte order.
 Unsigned packed-decimals are treated as positive; this method cannot distinguish
 between positive and negative zero.
Parameters:length - number of bytes to read
Returns:the read packed-decimal number, as a BigInteger.
Throws:
java.io.EOFException - at end of stream
java.io.IOException - if a malformed packed-decimal is encountered, or for other error.
    - readDecimal2
short readDecimal2()
                   throws java.io.IOException
Reads two bytes as a packed-decimal integer. The current packed-decimal
 encoding determines the byte order.
 Unsigned packed-decimals are treated as positive; this method cannot distinguish
 between positive and negative zero.
Returns:the read packed-decimal number, as a short, between -999 and 999 inclusive.
Throws:
java.io.EOFException - at end of stream
java.io.IOException - if a malformed packed-decimal is encountered, or for other error.
    - readDecimal4
int readDecimal4()
                 throws java.io.IOException
Reads four bytes as a packed-decimal integer. The current packed-decimal
 encoding determines the byte order.
 Unsigned packed-decimals are treated as positive; this method cannot distinguish
 between positive and negative zero.
Returns:the read packed-decimal number, as an int, between -9999999 and 9999999 inclusive.
Throws:
java.io.EOFException - at end of stream
java.io.IOException - if a malformed packed-decimal is encountered, or for other error.
    - readDecimal8
long readDecimal8()
                  throws java.io.IOException
Reads eight bytes as a packed-decimal integer. The current packed-decimal
 encoding determines the byte order.
 Unsigned packed-decimals are treated as positive; this method cannot distinguish
 between positive and negative zero.
Returns:the read packed-decimal number, as a long, between -1015 and 1015 exclusive
Throws:
java.io.EOFException - at end of stream
java.io.IOException - if a malformed packed-decimal is encountered, or for other error.
    - readObject
java.lang.Object readObject()
                            throws java.io.IOException,
                                   java.lang.ClassNotFoundException
Reads a serialized Java Object from the stream
Returns:a deserialized Object.
Throws:
java.io.IOException
java.lang.ClassNotFoundExceptionSee Also:ObjectInput.readObject()