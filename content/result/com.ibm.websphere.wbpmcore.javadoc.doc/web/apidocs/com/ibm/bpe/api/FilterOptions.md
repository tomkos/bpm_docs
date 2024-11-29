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

## Class FilterOptions

- java.lang.Object
    - com.ibm.bpe.api.FilterOptions

- All Implemented Interfaces:
java.io.Serializable

public final class FilterOptions
extends java.lang.Object
implements java.io.Serializable
Describes filtering options for a query against a query table.
 These options are additionally applied to any filters defined for the query table.
Since:
6.2
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

FilterOptions()
Default constructor to initialize the filter options.

FilterOptions(java.lang.String selectedAttributes,
             java.lang.String queryCondition,
             java.lang.String sortAttributes,
             java.lang.Integer threshold,
             java.lang.Integer skipCount,
             java.util.TimeZone timeZone,
             java.util.Locale locale,
             java.lang.Boolean distinctRows)
Constructor that builds a filter option from the passed values.
    - Method Summary Methods Modifier and Type Method and Description java.util.Locale getLocale () Returns the locale. java.lang.String getQueryCondition () Returns the query condition. java.lang.String getSelectedAttributes () Returns the specifically selected attributes. java.lang.Integer getSkipCount () Returns the number of entities or rows to be skipped. java.lang.String getSortAttributes () Returns the names of attributes that are to be sorted. java.lang.Integer getThreshold () Returns the threshold. java.util.TimeZone getTimeZone () Returns the time zone. java.lang.Boolean isDistinctRows () Returns whether only distinct rows are to be returned. void setDistinctRows (java.lang.Boolean distinctRows) Sets whether rows should be distinct. void setLocale (java.util.Locale locale) Sets the locale. void setQueryCondition (java.lang.String queryCondition) Sets the query condition. void setSelectedAttributes (java.lang.String selectedAttributes) Sets the attributes to be selected for a query. void setSkipCount (java.lang.Integer skipCount) Sets the skip count. void setSortAttributes (java.lang.String sortAttributes) Sets the attributes to be sorted. void setThreshold (java.lang.Integer threshold) Sets the threshold. void setTimeZone (java.util.TimeZone timeZone) Sets the time zone. java.lang.String toString () Returns a string representation of the FilterOptions object.

### Method Summary

| Modifier and Type   | Method and Description                                                                                     |
|---------------------|------------------------------------------------------------------------------------------------------------|
| java.util.Locale    | getLocale() Returns the locale.                                                                            |
| java.lang.String    | getQueryCondition() Returns the query condition.                                                           |
| java.lang.String    | getSelectedAttributes() Returns the specifically selected attributes.                                      |
| java.lang.Integer   | getSkipCount() Returns the number of entities or rows to be skipped.                                       |
| java.lang.String    | getSortAttributes() Returns the names of attributes that are to be sorted.                                 |
| java.lang.Integer   | getThreshold() Returns the threshold.                                                                      |
| java.util.TimeZone  | getTimeZone() Returns the time zone.                                                                       |
| java.lang.Boolean   | isDistinctRows() Returns whether only distinct rows are to be returned.                                    |
| void                | setDistinctRows(java.lang.Boolean distinctRows) Sets whether rows should be distinct.                      |
| void                | setLocale(java.util.Locale locale) Sets the locale.                                                        |
| void                | setQueryCondition(java.lang.String queryCondition) Sets the query condition.                               |
| void                | setSelectedAttributes(java.lang.String selectedAttributes) Sets the attributes to be selected for a query. |
| void                | setSkipCount(java.lang.Integer skipCount) Sets the skip count.                                             |
| void                | setSortAttributes(java.lang.String sortAttributes) Sets the attributes to be sorted.                       |
| void                | setThreshold(java.lang.Integer threshold) Sets the threshold.                                              |
| void                | setTimeZone(java.util.TimeZone timeZone) Sets the time zone.                                               |
| java.lang.String    | toString() Returns a string representation of the FilterOptions object.                                    |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait