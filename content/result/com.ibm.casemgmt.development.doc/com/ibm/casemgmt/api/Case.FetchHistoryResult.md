- Overview
- Package
- Class
- Tree
- Deprecated
- Index
- Help

- Prev Class
- Next Class

- Frames
- No Frames

- All Classes

- Summary:
- Nested |
- Field |
- Constr |
- Method

- Detail:
- Field |
- Constr |
- Method

## Class Case.FetchHistoryResult

- java.lang.Object
    - com.ibm.casemgmt.api.Case.FetchHistoryResult

- Enclosing class: Case public static final class Case.FetchHistoryResult extends java.lang.Object Represents information returned from fetching case history. An instance of this class provides two pieces of information: ID status: ID review by David Newhall

```
public static final class Case.FetchHistoryResult
extends java.lang.Object
```

A list of objects implementing the Content Engine Java API
        IndependentObject interface. These objects are obtained by 
        performing a query for the history event objects that contain
        the properties that were audited as part of the case 
        history.
An optional continuation token for requesting more results. 
        Typically, the overall result set is large and only a partial
        list of the overall history event objects is returned at
        any time. A continuation token is returned that can then
        be passed back when requesting the next set of results.

- ========== METHOD SUMMARY ===========
    - Method Summary All Methods Instance Methods Concrete Methods Modifier and Type Method and Description java.lang.String getContinuationToken () Returns a value that can be used to obtain additional results if the list returned from getResults() is incomplete. java.util.List<com.filenet.api.core.IndependentObject> getResults () Returns the list of history event objects that contain the properties that were audited as part of this case's history.

### Method Summary

| Modifier and Type                                      | Method and Description                                                                                                                        |
|--------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| java.lang.String                                       | getContinuationToken() Returns a value that can be used to obtain additional results  if the list returned from getResults() is   incomplete. |
| java.util.List<com.filenet.api.core.IndependentObject> | getResults() Returns the list of history event objects that contain   the properties that were audited as part of this case's history.        |

- Methods inherited from class java.lang.Object
equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait