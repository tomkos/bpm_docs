<!-- image -->

# Parameters in stored queries

```
String whereClause =
  "TASK.STATE = TASK.STATE.STATE\_READY
  AND WORK\_ITEM.REASON = WORK\_ITEM.REASON.REASON\_POTENTIAL\_OWNER
  AND TASK\_CPROP.NAME = 'company' AND TASK\_CPROP.STRING\_VALUE = 'ACME Co.'";
```

```
String whereClause =
  "TASK.STATE = TASK.STATE.STATE\_READY
  AND WORK\_ITEM.REASON = WORK\_ITEM.REASON.REASON\_POTENTIAL\_OWNER
  AND TASK\_CPROP.NAME = 'company' AND TASK\_CPROP.STRING\_VALUE = '@param1'";
```

- Parameters can only be used in the where clause.
- Parameters are strings.
- Parameters are replaced at run time using string replacement.
If you need special characters you must specify these in the where clause
or passed-in at run time as part of the parameter.
- Parameter names consist of the string @param concatenated
with an integer number. The lowest number is 1, which points to the
first item in the list of parameters that is passed to the query API
at run time.
- A parameter can be used multiple times within a where clause;
all occurrences of the parameter are replaced by the same value.