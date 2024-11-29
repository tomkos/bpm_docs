<!-- image -->

# User-specific access conditions

The access condition that is added depends on whether the user
is a system administrator.

## Queries invoked by users who are not system administrators

The
generated SQL WHERE clause combines the API where
clause with an access control condition that is specific to the user.
The query retrieves only those objects that the user is authorized
to access, that is, only those objects for which the user has a work
item. A work item represents the assignment of a user or user group
to an authorization role of a business object, such as a task or process.
If, for example, the user, John Smith, is a member of the potential
owners role of a given task, a work item object exists that represents
this relationship.

```
FROM TASK TA, WORK\_ITEM WI
WHERE WI.OBJECT\_ID = TA.TKIID
AND ( WI.OWNER\_ID = 'user' 
      OR WI.OWNER\_ID = null AND WI.EVERYBODY = true )
```

```
"WORK\_ITEM.REASON == WORK\_ITEM.REASON.REASON\_POTENTIAL\_OWNER"
```

```
FROM TASK TA, WORK\_ITEM WI
WHERE WI.OBJECT\_ID = TA.TKIID
AND ( WI.OWNER\_ID = 'JohnSmith' 
      OR WI.OWNER\_ID = null AND WI.EVERYBODY = true)
AND WI.REASON = 1
```

This also means that if John
Smith wants to see the activities and tasks for which he is a process
reader or a process administrator and for which he does not have a
work item, then a property from the PROCESS\_INSTANCE view must be
added to the select, where, or order-by clause of the query, for example,
PROCESS\_INSTANCE.PIID.

If group work items are enabled, an additional
access condition is added to the WHERE clause that
allows a user to access objects that the group has access to.

## Queries invoked by system administrators

System
administrators can invoke the query method to retrieve
objects that have associated work items. In this case, a join with
the WORK\_ITEM view is added to the generated SQL query, but no access
control condition for the WORK\_ITEM.OWNER\_ID.

```
FROM TASK TA, WORK\_ITEM WI
WHERE WI.OBJECT\_ID = TA.TKIID
```

## queryAll queries

This
type of query can be invoked only by system administrators or system
monitors. Neither conditions for access control nor a join to the
WORK\_ITEM view are added. This type of query returns all of the data
for all of the objects.