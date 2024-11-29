<!-- image -->

# Repairing activities that stopped because a join, loop, or
counter evaluation failed

## About this task

You can set the value of a join condition for any type
of activity, the value of a loop condition of a while or repeat-until
activity. You can also set the values of start and final counters,
and the maximum number of completed branches for a forEach activity.
The value that you set for the completed branches depends on the definition
of the forEach activity in the process model. If an early exit condition
is specified in the model, set a value for the maximum completed branches.
If an early exit condition is not specified, set the value of the
maximum completed branches to null.

The
following sample shows how to set the value of a loop condition.

## Procedure

1 List the activities that stopped because the evaluationof a loop condition failed. FilterOptions fo = new FilterOptions();fo.setSelectedAttributes("AIID");fo.setQueryCondition("STATE=STATE\_STOPPED AND STOP\_REASON=STOP\_REASON\_IMPLEMENTATION\_FAILED AND (KIND=KIND\_WHILE OR KIND=KIND\_REPEAT\_UNTIL)");EntityResultSet result = process.queryEntities("ACTIVITY", fo, null, null); Similarly,you can list the activities that stopped because the evaluation ofa join condition or a forEach counter failed. STOP\_REASON=STOP\_REASON\_IMPLEMENTATION\_FAILED AND (KIND=KIND\_FOR\_EACH\_SERIAL OR KIND=KIND\_FOR\_EACH\_PARALLEL) Thisaction returns the activities for the CustomerOrder process instancethat stopped because the evaluation of a loop condition failed.

```
FilterOptions fo = new FilterOptions();
fo.setSelectedAttributes("AIID");
fo.setQueryCondition("STATE=STATE\_STOPPED AND STOP\_REASON=STOP\_REASON\_IMPLEMENTATION\_FAILED AND (KIND=KIND\_WHILE OR KIND=KIND\_REPEAT\_UNTIL)");
EntityResultSet result = process.queryEntities("ACTIVITY", fo, null, null);
```

    - For a failed join condition, use the following expression:STOP\_REASON=STOP\_REASON\_ACTIVATION\_FAILED
    - For a failed forEach counter, use the following expression:

```
STOP\_REASON=STOP\_REASON\_IMPLEMENTATION\_FAILED AND 
(KIND=KIND\_FOR\_EACH\_SERIAL OR 
KIND=KIND\_FOR\_EACH\_PARALLEL)
```

This
action returns the activities for the CustomerOrder process instance
that stopped because the evaluation of a loop condition failed.

2. Provide the value of the loop condition, for example, true.
if (result.getEntities().size() > 0)
{
  Entity activityEntity = (Entity) result.getEntities().get(0);
  AIID aiid = (AIID) activityEntity.getAttributeValue("AIID");
  process.forceLoopCondition(aiid, true);
}
  This action sets the value of
the loop condition for the activity to true and the navigation of
the process instance continues. 
Similarly, you can set the
value of a join condition (process.forceJoinCondition(aiid,
true);) or the values of forEach activity counters (process.forceForEachCounterValues(aiid,
1, 5, new Integer(2));).