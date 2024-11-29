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

## Interface BfmConfiguration

- All Superinterfaces:
java.io.Serializable

public interface BfmConfiguration
extends java.io.Serializable
This interface returns Business Flow Manager configuration settings.
Since:
7.5

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static int
SYSTEM\_TYPE\_WLE 

static int
SYSTEM\_TYPE\_WPS
Symbolic constants for the system types described by this configuration.
    - Method Summary

Methods 

Modifier and Type
Method and Description

java.lang.String
getBuildLevel()
Returns the build level of the Business Flow Manager configuration.

java.lang.String
getSystemID()
Returns the system ID of the Business Flow Manager installation.

int
getSystemType()
Returns the type of the Business Flow Manager installation.

java.lang.String
getVersion()
Returns the version of the Business Flow Manager configuration.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- SYSTEM\_TYPE\_WPS
static final int SYSTEM\_TYPE\_WPS
Symbolic constants for the system types described by this configuration.
See Also:Constant Field Values

- SYSTEM\_TYPE\_WLE
static final int SYSTEM\_TYPE\_WLE
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getVersion
java.lang.String getVersion()
Returns the version of the Business Flow Manager configuration.
 
Returns:String -
   The version of the Business Flow Manager configuration, for example, 7.5.0.
    - getBuildLevel
java.lang.String getBuildLevel()
Returns the build level of the Business Flow Manager configuration.
 
Returns:String -
   The build level of the Business Flow Manager configuration.
    - getSystemID
java.lang.String getSystemID()
Returns the system ID of the Business Flow Manager installation.
 
Returns:String -
   The system ID of the Business Flow Manager installation.
    - getSystemType
int getSystemType()
Returns the type of the Business Flow Manager installation.
 
Returns:int -
   The type of the Business Flow Manager installation, in this case, SYSTEM\_TYPE\_WPS.