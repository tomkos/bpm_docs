<!-- image -->

# Filtering data using variables in queries

## About this task

You can define variables that are used by a process at
run time in its process model. For these variables, you declare which
parts can be queried.

For example, John Smith, calls his insurance
company's service number to find out the progress of his insurance
claim for his damaged car. The claims administrator uses the customer
ID to the find the claim.

## Procedure

1. Optional: List the properties of the variables
in a process that can be queried. Use the process template
ID to identify the process. You can skip this step if you know which
variables can be queried.
List variableProperties = process.getQueryProperties(ptid);
for (int i = 0; i < variableProperties.size(); i++)
{
   QueryProperty queryData = (QueryProperty)variableProperties.get(i);
   String variableName = queryData.getVariableName(); 
   String name         = queryData.getName();
   int mappedType      = queryData.getMappedType(); 
   ...
}
2. List the process instances with variables that match the
filter criteria.  For this process, the customer ID
is modeled as part of the variable customerClaim that can be queried.
You can therefore use the customer's ID to find the claim.
QueryResultSet result = process.query
    ("PROCESS\_INSTANCE.NAME, QUERY\_PROPERTY.STRING\_VALUE",
		   "QUERY\_PROPERTY.VARIABLE\_NAME = 'customerClaim' AND " + 
		   "QUERY\_PROPERTY.NAME = 'customerID' AND " +
		   "QUERY\_PROPERTY.STRING\_VALUE like 'Smith%'",
      (String)null, (Integer)null, 
      (Integer)null, (TimeZone)null );
This action returns
a query result set that contains the process instance names and the
values of the customer IDs for customers whose IDs start with Smith.