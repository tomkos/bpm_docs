# Searching processes and tasks

```
Display all of the tasks for the Service Order Process that are active now or have been completed in the last 24 hours.
```

- For more information about Process Portal saved searches, see
Searches and saved searches.
- Reference information for the TWSearch object is available on the JavaScript API in processes and service flows page.

## Structure of a TWSearch query

1. Define the columns of data that you want to retrieve. See Columns.
2. Define any filters that you want to apply to a column. See Search filters.
3. Define the sort order for the returned records. See Search result order.
4. Define how results are organized. See Search result organization.
5. Execute the search and parse the results into a list of complex
variables. See Search execution.

```
var search = new TWSearch();
```

## Columns

```
var colInstanceId = new TWSearchColumn();
colInstanceId.type = TWSearchColumn.Types.ProcessInstance;
colInstanceId.name = TWSearchColumn.ProcessInstanceColumns.ID;
```

```
TWSearchColumn.Types.ProcessInstance
TWSearchColumn.Types.Task
TWSearchColumn.Types.BusinessData
```

The names for ProcessInstance and Task column types are
predefined and non-editable. Column names for the BusinessData type are defined in
the BPD definitions when a variable is marked as Available in Search. For
more information about searching on business data, see Making business data available in searches and views.

```
var colServiceOrderNumber = new TWSearchColumn;
colServiceOrderNumber.type = TWSearchColumn.Types.BusinessData;
colServiceOrderNumber.name = "serviceOrderNumber";
```

```
search.columns =
     new Array(
       colInstanceStatus,
     colInstanceId,
     colInstanceName,
     colTaskId,
     colTaskStatus,
     colClosedDateTime,
     colDueDateTime,
     );
```

## Search filters

```
var colInstanceName = new TWSearchColumn();
colInstanceName.type = TWSearchColumn.Types.ProcessInstance;
colInstanceName.name = TWSearchColumn.ProcessInstanceColumns.Name;
     
var condInstanceName = new TWSearchCondition;
condInstanceName.column = colInstanceName;
condInstanceName.operator = TWSearchCondition.Operations.StartsWith;
condInstanceName.value = "Service Order Fulfillment:";
```

```
var colDueDateTime = new TWSearchColumn;
colDueDateTime.type = TWSearchColumn.Types.Task;
colDueDateTime.name = TWSearchColumn.TaskColumns.DueDate;
  
var condDueDateTimeBefore = new TWSearchCondition;
condDueDateTimeBefore.column = colDueDateTime;
condDueDateTimeBefore.operator = TWSearchCondition.Operations.LessThan;
condDueDateTimeBefore.value = tw.local.dueDateBefore.format("MM/dd/yyyy HH:mm:ss", "PST");
 
var condDueDateTimeAfter = new TWSearchCondition;
condDueDateTimeAfter.column = colDueDateTime;
condDueDateTimeAfter.operator = TWSearchCondition.Operations.GreaterThan;
condDueDateTimeAfter.value = tw.local.dueDateAfter.format("MM/dd/yyyy HH:mm:ss", "PST");
```

```
var conditions = new Array(condInstanceName, condInstanceStatus, condTaskStatus);
search.conditions = conditions;
```

To
apply exclusive conditions (exclusive OR), you must execute multiple
searches and combine them yourself.

```
var conditions = new Array(condInstanceName, condInstanceStatus, condTaskStatus);
 if(tw.local.fieldRepIdentifier != "All") {
 conditions.push(condFieldRepIdentifier);
 }
 search.conditions = conditions;
```

## Search result order

```
var orderInstanceId = new TWSearchOrdering();
orderInstanceId .column = colInstanceId;
orderInstanceId .order = TWSearchOrdering.Orders.Ascending;
```

```
search.orderBy = new Array(orderInstanceId );
```

## Search result organization

```
search.organizedBy = TWSearch.OrganizeByTypes.Task;
```

## Search execution

```
var results = search.execute();
```

The TWSearch object
also supports the executeForProcessInstances and executeForTasks methods,
which take the same parameters and return native JavaScript arrays
but with different return types. The executeForTasks method
returns a TWTask[] array of tasks while executeForProcessInstances returns
a TWProcessInstance[] array of process instances.

If
you want to use these results outside of your script block, you must
parse them and initialize equivalent variables.

```
tw.local.serviceOrderTasks = new tw.object.listOf.ServiceOrderTask();
 for(var i = 0; i < results.rows.length; i++) {
   var row = results.rows[i];
   tw.local.serviceOrderTasks[i] = new tw.object.ServiceOrderTask();
 
   tw.local.serviceOrderTasks[i].processInstanceId = row.values[0].toString();
   tw.local.serviceOrderTasks[i].processInstanceName = row.values[1].toString();
   tw.local.serviceOrderTasks[i].taskId = row.values[2].toString();
   tw.local.serviceOrderTasks[i].taskStatus = row.values[3].toString();
   if(null != row.values[4])
   {
     tw.local.serviceOrderTasks[i].closedDate = row.values[4].toString();
   }
   if(null != row.values[5])
   {
     tw.local.serviceOrderTasks[i].dueDate = row.values[5].toString();
   }   
 }
```

If you are writing code to process TWSearch results and check values for null, you should
consider specifying the null on the left side of the operator rather than on the right side, as
shown in the above example code fragment. Otherwise, it is possible that the following error may be
output to the SystemErr.log file:

```
SystemErr     R RHINO USAGE WARNING: Missed Context.javaToJS()  
conversion:                                                     
Rhino runtime detected object Tue May 05 08:00:00 EDT 2020 of   
class java.util.Date where it expected String, Number, Boolean  
or Scriptable instance. Please check your code for missing      
Context.javaToJS() call.
```