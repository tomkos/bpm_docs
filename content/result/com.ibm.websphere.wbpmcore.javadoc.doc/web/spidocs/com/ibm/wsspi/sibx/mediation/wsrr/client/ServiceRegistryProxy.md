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

## Interface ServiceRegistryProxy

- public interface ServiceRegistryProxy
The interface that can be used to communicate with a service registry and its cache

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
$sccsid 

static java.lang.String
COPYRIGHT
    - Method Summary

Methods 

Modifier and Type
Method and Description

int
cacheDepth()
Return the number of queries that are currently cached.

void
clearCache()
Clear the cache for this service registry proxy.

java.lang.String
create(DataGraphType dataGraphList)
Create an object in the service registry that matches a given dataGraphType

void
delete(java.lang.String bsiUri)
Delete the object within the registry with the supplied bsrURI

ServiceRegistryDataGraphList
get(java.lang.String bsiUri)
Retrieve an object from the service registry that matches a given bsiUri.

ServiceRegistryDataGraphList
get(java.lang.String bsiUri,
   int depth)
Retrieve an object from the service registry that matches a given bsiUri.

boolean
isConnectionSuccessful()
Test that this Service Registry can be connected to.

ServiceRegistryDataGraphList
namedQuery(java.lang.String namedQuery,
          java.lang.String[] params)
Given a named query and array of parameters, return all the content and values that are matched in WSRR.

ServiceRegistryDataGraphList
namedQuery(java.lang.String namedQuery,
          java.lang.String[] params,
          com.ibm.wsspi.monitoring.EventPoint eventPoint)
Given a named query and array of parameters, return all the content and values that are matched in WSRR.

ServiceRegistryDataGraphList
query(java.lang.String queryStatement)
Given a query statement, return all the content and values that are matched in WSRR.

ServiceRegistryDataGraphList
query(java.lang.String queryStatement,
     int depth)
Given a query statement and the depth of the search, return all the content and values that are matched in WSRR.

ServiceRegistryDataGraphList
query(java.lang.String queryStatement,
     int depth,
     boolean noContent)
Given a query statement, the depth of the search and if any content will be returned 
 or not, return the values that are matched in WSRR.

ServiceRegistryDataGraphList
query(java.lang.String queryStatement,
     int depth,
     boolean noContent,
     com.ibm.wsspi.monitoring.EventPoint eventPoint)
Given a query statement, the depth of the search and if any content will be returned 
 or not, return the values that are matched in WSRR.

void
update(DataGraphType dataGraphList)
Update an object in the service registry that matches a given dataGraphType

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- $sccsid
static final java.lang.String $sccsid
See Also:Constant Field Values

- Method Detail

### Method Detail

    - query
ServiceRegistryDataGraphList query(java.lang.String queryStatement,
                                 int depth,
                                 boolean noContent,
                                 com.ibm.wsspi.monitoring.EventPoint eventPoint)
                                   throws ServiceRegistryProxyException
Given a query statement, the depth of the search and if any content will be returned 
 or not, return the values that are matched in WSRR.
Parameters:queryStatement - The XPath querydepth - The search depth. -1 for infinite depthnoContent - True if no document content is to be retrieved from the searcheventPoint - event point for monitoring events.
Returns:A ServiceRegistryDataGraphList object containing the list of matching DataGraphType objects and a time stamp for the query
Throws:
ServiceRegistryProxyException
    - query
ServiceRegistryDataGraphList query(java.lang.String queryStatement,
                                 int depth,
                                 boolean noContent)
                                   throws ServiceRegistryProxyException
Given a query statement, the depth of the search and if any content will be returned 
 or not, return the values that are matched in WSRR.
Parameters:queryStatement - The XPath querydepth - The search depth. -1 for infinite depthnoContent - True if no document content is to be retrieved from the search
Returns:A ServiceRegistryDataGraphList object containing the list of matching DataGraphType objects and a time stamp for the query
Throws:
ServiceRegistryProxyException
    - query
ServiceRegistryDataGraphList query(java.lang.String queryStatement,
                                 int depth)
                                   throws ServiceRegistryProxyException
Given a query statement and the depth of the search, return all the content and values that are matched in WSRR.
 Equivalent to calling query(queryStatement, depth, false).
Parameters:queryStatement - The XPath querydepth - The search depth. -1 for infinite depth
Returns:A ServiceRegistryDataGraphList object containing the list of matching DataGraphType objects and a time stamp for the query
Throws:
ServiceRegistryProxyException
    - query
ServiceRegistryDataGraphList query(java.lang.String queryStatement)
                                   throws ServiceRegistryProxyException
Given a query statement, return all the content and values that are matched in WSRR.
 Equivalent to calling query(queryStatement, -1, false).
Parameters:queryStatement - The XPath query
Returns:A ServiceRegistryDataGraphList object containing the list of matching DataGraphType objects and a time stamp for the query
Throws:
ServiceRegistryProxyException
    - namedQuery
ServiceRegistryDataGraphList namedQuery(java.lang.String namedQuery,
                                      java.lang.String[] params)
                                        throws ServiceRegistryProxyException
Given a named query and array of parameters, return all the content and values that are matched in WSRR.
Parameters:namedQuery - The named query being calledparams - A String array containing the required parameters
Returns:A ServiceRegistryDataGraphList object containing the list of matching DataGraphType objects and a time stamp for the query
Throws:
ServiceRegistryProxyException
    - namedQuery
ServiceRegistryDataGraphList namedQuery(java.lang.String namedQuery,
                                      java.lang.String[] params,
                                      com.ibm.wsspi.monitoring.EventPoint eventPoint)
                                        throws ServiceRegistryProxyException
Given a named query and array of parameters, return all the content and values that are matched in WSRR.
Parameters:namedQuery - The named query being calledparams - A String array containing the required parameterseventPoint - event point for monitoring events.
Returns:A ServiceRegistryDataGraphList object containing the list of matching DataGraphType objects and a time stamp for the query
Throws:
ServiceRegistryProxyException
    - isConnectionSuccessful
boolean isConnectionSuccessful()
                               throws ServiceRegistryProxyException
Test that this Service Registry can be connected to. Return true if the connection
 have been successful.
Throws:
ServiceRegistryProxyException
    - get
ServiceRegistryDataGraphList get(java.lang.String bsiUri,
                               int depth)
                                 throws ServiceRegistryProxyException
Retrieve an object from the service registry that matches a given bsiUri.
Parameters:bsiUri - The WSRR bsiURI stringdepth - The search depth. -1 for infinite depth
Returns:A ServiceRegistryDataGraphList object containing the list of matching DataGraphType objects and a time stamp for the query
Throws:
ServiceRegistryProxyException
    - get
ServiceRegistryDataGraphList get(java.lang.String bsiUri)
                                 throws ServiceRegistryProxyException
Retrieve an object from the service registry that matches a given bsiUri.
 Equivalent to calling get(bsiUri, -1).
Parameters:bsiUri - The WSRR bsiURI string
Returns:A ServiceRegistryDataGraphList object containing the list of matching DataGraphType objects and a time stamp for the query
Throws:
ServiceRegistryProxyException
    - create
java.lang.String create(DataGraphType dataGraphList)
                        throws ServiceRegistryProxyException
Create an object in the service registry that matches a given dataGraphType
Parameters:A - DataGraphType object containing the object to create
Returns:bsrUri The WSRR bsiURI of the create object in WSRR
Throws:
ServiceRegistryProxyException
    - delete
void delete(java.lang.String bsiUri)
            throws ServiceRegistryProxyException
Delete the object within the registry with the supplied bsrURI
Parameters:bsiUri - The WSRR bsiURI string
Throws:
ServiceRegistryProxyException
    - update
void update(DataGraphType dataGraphList)
            throws ServiceRegistryProxyException
Update an object in the service registry that matches a given dataGraphType
Parameters:A - DataGraphType object containing the object to update
Throws:
ServiceRegistryProxyException
    - clearCache
void clearCache()
Clear the cache for this service registry proxy.
    - cacheDepth
int cacheDepth()
Return the number of queries that are currently cached.