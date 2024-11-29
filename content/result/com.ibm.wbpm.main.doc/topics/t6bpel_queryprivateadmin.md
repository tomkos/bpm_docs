<!-- image -->

# Managing private stored queries for other users

## About this task

As the system administrator, you can manage private stored
queries that belong to a specific user.

## Procedure

1. Create a private stored query for the user ID Smith.
For example, the following code snippet creates a stored
query for process instances and saves it with the name CustomerOrdersStartingWithA
for the user ID Smith.
process.createStoredQuery("Smith", "CustomerOrdersStartingWithA",
             "DISTINCT PROCESS\_INSTANCE.PIID, PROCESS\_INSTANCE.NAME",
             "PROCESS\_INSTANCE.NAME LIKE 'A%'",
             "PROCESS\_INSTANCE.NAME",
              (Integer)null, (TimeZone)null, 
              (List)null, (String)null); 
The result of the stored query is
a sorted list of all the process-instance names that begin with the
letter A and their associated process instance IDs (PIID).
2. Run the query defined by the stored query.  QueryResultSet result = process.query
                       ("Smith", "CustomerOrdersStartingWithA",
                         (Integer)null, (Integer)null, (List)null);      
new Integer(0));This action returns
the objects that fulfill the criteria. In this case, all of the customer
orders that begin with A.
3. Get a list of the names of the private queries that belong
to a specific user. For example, the following code
snippet shows how to get a list of private queries that belongs to
the user Smith. 
String[] storedQuery = process.getStoredQueryNames("Smith");
4. View the details of a specific query. The
following code snippet shows how to view the details of the CustomerOrdersStartingWithA
query that is owned by the user Smith.
StoredQueryData storedQuery = process.getStoredQuery
   ("Smith", "CustomerOrdersStartingWithA");
String selectClause = storedQuery.getSelectClause();
String whereClause = storedQuery.getWhereClause();
String orderByClause = storedQuery.getOrderByClause();
Integer threshold = storedQuery.getThreshold();
String owner = storedQuery.getOwner();
If you use the Human Task Manager API to retrieve information
about a stored query, use StoredQuery for the returned
object instead of StoredQueryData.
5. Delete a private stored query. The following
code snippet shows how to delete a private query that is owned by
the user Smith.
process.deleteStoredQuery("Smith", "CustomerOrdersStartingWithA");