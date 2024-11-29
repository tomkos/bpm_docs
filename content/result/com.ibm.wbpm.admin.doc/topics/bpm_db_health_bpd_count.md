# Counting process instances

## Using the Process Admin Console

1. Click Server Admin > Workflow Admin > Health Management.
2. Select the command Count Processes.
3. Specify values for the command's parameters.
4. Click Submit.
5. If there is an error, you will see the error message.
6. If there is no error, you see how many instances in the system
match the criteria.

## Using a REST API call

Call the operations REST API GET
https://host:port/ops/std/bpm/processes/count.

- To count all process instances that are in the states finished or terminated:GET https://host:port/ops/std/bpm/processes/count?states=finished,terminated
- To count all process instances that are in the states finished or terminated that
ended before 2016-07-16T19:20:30-06:00:GET https://host:port/ops/std/bpm/processes/count?states=finished,terminated
       &ended\_before=2016-07-16T19:20:30-06:00Remember: If you need to specify a time zone that is ahead of
UTC, you must encode the + symbol as %2B.
For example, for the Central European Time zone +01:00,
you must use %2B01:00 in your URL. Alternatively,
you can specify a UTC date, for example ended\_after=2016-01-01T01:00:00Z.
- To count all process instances of snapshots V2 and V3 of
the process application that has the acronym XYZ and
are in the state stopped:GET https://host:port/ops/std/bpm/processes/count?container=XYZ
       &versions=V2,V3&states=stopped