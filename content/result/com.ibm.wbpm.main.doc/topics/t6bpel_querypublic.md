<!-- image -->

# Managing public stored queries

## About this task

As the system administrator, you can create, view, and
delete public stored queries. If you do not specify a user ID
in the API call, it is assumed that the stored query is a public stored
query.

## Procedure

1. Create a public stored query. For example,
the following code snippet creates a stored query for process instances
and saves it with the name CustomerOrdersStartingWithA.
process.createStoredQuery("CustomerOrdersStartingWithA",
             "DISTINCT PROCESS\_INSTANCE.PIID, PROCESS\_INSTANCE.NAME",
             "PROCESS\_INSTANCE.NAME LIKE 'A%'",
             "PROCESS\_INSTANCE.NAME",
              (Integer)null, (TimeZone)null); 
The result of the stored query is
a sorted list of all the process-instance names that begin with the
letter A and their associated process instance IDs (PIID).
2. Run the query defined by the stored query.  QueryResultSet result = process.query("CustomerOrdersStartingWithA", 
               new Integer(0), null);This
action returns the objects that fulfill the criteria. In this case,
all of the customer orders that begin with A.
3. List the names of the available public stored queries.
The following code snippet shows how to limit the list of
returned queries to just the public queries. 
String[] storedQuery = process.getStoredQueryNames(StoredQueryData.KIND\_PUBLIC);
4. Optional: Check the query that is defined by
a specific stored query. A stored private query can
have the same name as a stored public query. If these names are the
same, the private stored query is returned. The following code snippet
shows how to return only the public query with the specified name.
If you use the Human Task Manager API to retrieve information about
a stored query, use StoredQuery for the returned
object instead of StoredQueryData.StoredQueryData storedQuery = process.getStoredQuery
   (StoredQueryData.KIND\_PUBLIC, "CustomerOrdersStartingWithA");
String selectClause = storedQuery.getSelectClause();
String whereClause = storedQuery.getWhereClause();
String orderByClause = storedQuery.getOrderByClause();
Integer threshold = storedQuery.getThreshold();
String owner = storedQuery.getOwner();
5. Delete a public stored query. The following
code snippet shows how to delete the stored query that you created
in step 1.
process.deleteStoredQuery("CustomerOrdersStartingWithA");