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

## Interface InlineCustomProperty

- All Superinterfaces:
CustomProperty, java.io.Serializable

public interface InlineCustomProperty
extends CustomProperty
Describes an inline custom property.
 
 Inline custom properties allow a user to add additional properties to an object beyond
 those provided and managed by the Business Flow Manager.
 In contrast to non-inline custom properties, inline custom properties are an integral part of
 the associated object. This can result in more efficient queries.
Since:
7.5.1

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static java.lang.String
CUSTOM\_TEXT\_1
Constant to name the first inline custom property out of a set of eight.

static java.lang.String
CUSTOM\_TEXT\_2
Constant to name the second inline custom property out of a set of eight.

static java.lang.String
CUSTOM\_TEXT\_3
Constant to name the third inline custom property out of a set of eight.

static java.lang.String
CUSTOM\_TEXT\_4
Constant to name the fourth inline custom property out of a set of eight.

static java.lang.String
CUSTOM\_TEXT\_5
Constant to name the fifth inline custom property out of a set of eight.

static java.lang.String
CUSTOM\_TEXT\_6
Constant to name the sixth inline custom property out of a set of eight.

static java.lang.String
CUSTOM\_TEXT\_7
Constant to name the seventh inline custom property out of a set of eight.

static java.lang.String
CUSTOM\_TEXT\_8
Constant to name the eighth inline custom property out of a set of eight.
    - Method Summary

### Method Summary

- Methods inherited from interface com.ibm.bpe.api.CustomProperty
getName, getValue