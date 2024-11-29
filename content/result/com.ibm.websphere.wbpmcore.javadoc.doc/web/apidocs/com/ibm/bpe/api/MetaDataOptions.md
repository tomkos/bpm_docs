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

## Class MetaDataOptions

- java.lang.Object
    - com.ibm.bpe.api.MetaDataOptions

- All Implemented Interfaces:
java.io.Serializable

public final class MetaDataOptions
extends java.lang.Object
implements java.io.Serializable
Describes filtering options for retrieving the meta data of query tables.
Since:
6.2.0.1
See Also:Serialized Form

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Constructor Summary

Constructors 

Constructor and Description

MetaDataOptions()
Default constructor to initialize the meta data options.

MetaDataOptions(java.lang.String primaryQueryTableFilter,
               java.lang.String sourceAttributeFilter,
               boolean userParametersAllowed,
               java.util.Locale locale)
Constructor that creates meta data options from the passed values.
    - Method Summary Methods Modifier and Type Method and Description boolean areUserParametersAllowed () Returns whether query tables that contain user parameters are to be considered. java.util.Locale getLocale () Returns the locale. java.lang.String getPrimaryQueryTableFilter () Returns the primary query table filter. java.lang.String getSourceAttributeFilter () Returns the source attribute filter. void setLocale (java.util.Locale locale) Sets the locale. void setPrimaryQueryTableFilter (java.lang.String primaryQueryTableFilter) Specifies the names of primary query tables. void setSourceAttributeFilter (java.lang.String sourceAttributeFilter) Specifies source attributes names. void setUserParametersAllowed (boolean userParametersAllowed) Specifies whether query tables that contain user parameters are to be considered when querying the meta data of query tables. java.lang.String toString () Returns a string representation of the MetaDataOptions object.

### Method Summary

| Modifier and Type   | Method and Description                                                                                                                                                                |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| boolean             | areUserParametersAllowed() Returns whether query tables that contain user parameters are to be considered.                                                                            |
| java.util.Locale    | getLocale() Returns the locale.                                                                                                                                                       |
| java.lang.String    | getPrimaryQueryTableFilter() Returns the primary query table filter.                                                                                                                  |
| java.lang.String    | getSourceAttributeFilter() Returns the source attribute filter.                                                                                                                       |
| void                | setLocale(java.util.Locale locale) Sets the locale.                                                                                                                                   |
| void                | setPrimaryQueryTableFilter(java.lang.String primaryQueryTableFilter) Specifies the names of primary query tables.                                                                     |
| void                | setSourceAttributeFilter(java.lang.String sourceAttributeFilter) Specifies source attributes names.                                                                                   |
| void                | setUserParametersAllowed(boolean userParametersAllowed) Specifies whether query tables that contain user parameters are to be considered when querying the meta data of query tables. |
| java.lang.String    | toString() Returns a string representation of the MetaDataOptions object.                                                                                                             |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait