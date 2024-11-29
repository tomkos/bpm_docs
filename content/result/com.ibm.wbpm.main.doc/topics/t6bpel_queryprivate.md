<!-- image -->

# Working with your private stored queries

## Procedure

1. Create a private stored query. For example,
the following code snippet creates a stored query for process instances
and saves it with a specific name. If a user ID is not specified,
it is assumed that the stored query is a private stored query for
the logged-on user.
process.createStoredQuery("CustomerOrdersStartingWithA",
             "DISTINCT PROCESS\_INSTANCE.PIID, PROCESS\_INSTANCE.NAME",
             "PROCESS\_INSTANCE.NAME LIKE 'A%'",
             "PROCESS\_INSTANCE.NAME",
              (Integer)null, (TimeZone)null); 
This query returns a sorted list
of all the process-instance names that begin with the letter A and
their associated process instance IDs (PIID).
2. Run the query defined by the stored query.  QueryResultSet result = process.query("CustomerOrdersStartingWithA", 
               new Integer(0));This
action returns the objects that fulfill the criteria. In this case,
all of the customer orders that begin with A.
3. Get a list of the names of the stored queries that the
logged-on user can access. The following code snippet
shows how to get both the public and the private stored queries that
the user can access.
String[] storedQuery = process.getStoredQueryNames();
4. View the details of a specific query. The
following code snippet shows how to view the details of the CustomerOrdersStartingWithA
query that is owned by the user Smith.
StoredQueryData storedQuery = process.getStoredQuery
   ("CustomerOrdersStartingWithA");
String selectClause = storedQuery.getSelectClause();
String whereClause = storedQuery.getWhereClause();
String orderByClause = storedQuery.getOrderByClause();
Integer threshold = storedQuery.getThreshold();
String owner = storedQuery.getOwner();
If you use the Human Task Manager API to retrieve information
about a stored query, use StoredQuery for the returned
object instead of StoredQueryData.
5. Delete a private stored query. The following
code snippet shows how to delete a private stored query.
process.deleteStoredQuery("CustomerOrdersStartingWithA");