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

## Interface BOMode

- public interface BOMode
Allows access to the business object parsing mode configuration at runtime.
 Application logic that would want to provide specific behavior for Lazy Vs Eager
 parsing mode should use this SPI in their design to access the parsing mode.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
BOEAGER 

static java.lang.String
BOLAZY 

static java.lang.String
COPYRIGHT
    - Method Summary

Methods 

Modifier and Type
Method and Description

java.lang.String
getBOMode()
Returns the BO mode (i.e., BOEAGER or BOLAZY) of the current 
 context.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- BOEAGER
static final java.lang.String BOEAGER
See Also:Constant Field Values

- BOLAZY
static final java.lang.String BOLAZY
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getBOMode
java.lang.String getBOMode()
Returns the BO mode (i.e., BOEAGER or BOLAZY) of the current 
 context. If mode was not modified, the default BOEAGER
 configuration will be returned.
Returns:String value: BOEAGER, BOLAZY