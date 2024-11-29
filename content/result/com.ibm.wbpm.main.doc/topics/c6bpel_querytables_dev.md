<!-- image -->

# Query table development

Supplemental and composite query tables in Business Process Choreographer are developed
during application development using the Query Table Builder. Predefined query tables cannot be
developed or deployed. They are available when Business Process Choreographer is installed and
provide a simple view on the artifacts in the Business Process Choreographer database
schema.

The Query Table Builder is available as an Eclipse plug-in and can be downloaded on the
SupportPacs site. Look for PA71 WebSphere Process Server - Query Table Builder. To access the link,
see the related references section of this topic.

| Step                       | Who                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|----------------------------|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. Analysis                | Business analyst, client developer | Analyze which query tables are needed in the client application. Questions to be answered are:  How many task or process lists are provided to the user? Are there task or process lists that can share the same query table?  What kind of authorization is used? Instance-based authorization, role-based authorization, or none?  Are there other query tables already defined in the system that can be reused? Must the query tables provide the content in multiple languages? If so, the selection criteria on attached query tables should be LOCALE=$LOCALE. |
| 2. Query table development | Client developer, business analyst | Develop the query tables that are used in the client application. Try to specify the definition of the query tables such that the best performance is achieved with query table queries.                                                                                                                                                                                                                                                                                                                                                                              |
| 3. Query table deployment  | Administrator                      | Query tables must be deployed to the runtime before they can be used. This step is done using the manageQueryTable.py wsadmin command.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 4. Query table queries     | Client developer                   | To run queries against query tables is the last step of query table development. The client developer must know the name of the query table and its attributes.                                                                                                                                                                                                                                                                                                                                                                                                       |

The following is sample code, which uses the query table API to query a query table. Examples 1
and 2 are provided to query the predefined query table TASK for simplicity reasons. Examples 3 and 4
query a composite query table, which is assumed to be deployed on the system. In application
development, you should use composite query tables rather than directly querying the predefined
query tables.

## Example 1

```
// get the naming context and lookup the Business
   // Flow Manager Enterprise JavaBeans home; note that the Business Flow 
   // Manager Enterprise JavaBeans home should be cached for performance 
   // reasons; also, it is assumed that there's an Enterprise JavaBeans 
   // reference to the local business flow manager Enterprise JavaBeans
   Context ctx = new InitialContext();
   LocalBusinessFlowManagerHome home = 
   	(LocalBusinessFlowManagerHome) 
   	ctx.lookup("java:comp/env/ejb/BFM");
   
   // if the human task manager Enterprise JavaBeans is used, do:
   // LocalHumanTaskManagerHome home =
   //   (LocalHumanTaskManagerHome) ctx.lookup("java:comp/env/ejb/HTM");
   // assuming that a EJB reference to the human task manager EJB
   // has been defined
   
   // create the business flow manager client-side stub
   LocalBusinessFlowManager bfm = home.create();
   // if the human task manager EJB is used, do:
   // LocalHumanTaskManager htm = home.create();
   // note that the human task manager Enterprise JavaBeans provides the
   // same methods as the business flow manager Enterprise JavaBeans 
   // *************************************************
   // ******************* example 1 *******************
   // *************************************************
   
   // run a query against the TASK predefined query 
   // table; this relates to a simple My ToDo's task list
   EntityResultSet ers = null;
   ers = bfm.queryEntities("TASK", null, null, null);
   
   // print the result to STDOUT
   EntityInfo entityInfo = ers.getEntityInfo();
   List attList = entityInfo.getAttributeInfo();
   int attSize = attList.size();

   Iterator iter = ers.getEntities().iterator();
   while (iter.hasNext()) {
   	System.out.print("Entity: ");
   	Entity entity = (Entity) iter.next();
   	for (int i = attSize - 1; i >= 0; i--) {
   		AttributeInfo ai = (AttributeInfo) attList.get(i);
   		System.out.print(
      	entity.getAttributeValue(ai.getName()));
   	}
   	System.out.println();
   }
```

## Example 2

```
// *************************************************
   // ******************* example 2 *******************
   // *************************************************
   
   // same example as example 1, but using the row-based
   // query approach
   RowResultSet rrs = null;
   rrs = bfm.queryRows("TASK", null, null, null);
   
   attList = rrs.getAttributeInfo();
   attSize = attList.size();

   // print the result to STDOUT
   while (rrs.next()) {
   	System.out.print("Row: ");
   	for (int i = attSize - 1; i >= 0; i--) {
   		AttributeInfo ai = (AttributeInfo) attList.get(i);
   		System.out.print(
      	rrs.getAttributeValue(ai.getName()));
   	}
   	System.out.println();
   }
```

## Example 3

```
// *************************************************
   // ******************* example 3 *******************
   // *************************************************
   
   // run a query against a composite query table
   // that has been deployed on the system before;
   // the name is assumed to be COMPANY.TASK\_LIST
   ers = bfm.queryEntities(
   		"COMPANY.TASK\_LIST", null, null, null);
^
   // 	print the result to STDOUT ...
```

## Example 4

```
// *************************************************
   // ******************* example 4 *******************
   // *************************************************
   
   // query against the same query table as in example 3,
   // but with customized options
   FilterOptions fo = new FilterOptions();

   // return only objects which are in state ready
   fo.setQueryCondition("STATE=STATE\_READY");
   
   // sort by the id of the object
   fo.setSortAttributes("ID");
   
   // limit the number of entities to 50
   fo.setThreshold(50);
   
   // only get a sub-set of the defined attributes
   // on the query table
   fo.setSelectedAttributes("ID, STATE, DESCRIPTION");
   
   AuthorizationOptions ao = new AuthorizationOptions();
   
   // do not return objects that everybody is allowed
   // to see
   ao.setEverybodyUsed(Boolean.FALSE);
   
   ers = bfm.queryEntities(
   		"COMPANY.TASK\_LIST", fo, ao, null);

   // 	print the result to STDOUT ...
```