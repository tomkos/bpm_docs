<!-- image -->

# Deleting BPEL process instances

## Using the Process Admin Console

1. Click Server Admin > Workflow Admin > Health Management.
2. Select the command Delete BPEL Processes.
3. Specify values for the command's parameters.
4. Click Submit.
5. If there is an error, the error message is displayed. Otherwise
you get confirmation that the command was submitted and a link that
you can click to count how many instances that match the deletion
criteria are still in the database. You can refresh the count to check
the progress of the deletion.

## Using a REST API call

Call the operations REST API DELETE
https://host:port/ops/adv/bpm/processes.

- To delete all instances that are in the states finished, terminated and failed:DELETE https://host:port/ops/adv/bpm/processes
- To delete all instances that are in the states terminated and failed for
the process template myTemplate which is valid from 2016-07-16T19:20:30-06:00:DELETE https://host:port/ops/adv/bpm/processes?states=terminated,failed
       &model=myTemplate&valid\_from=2016-07-16T19:20:30-06:00Remember: If you need to specify a time zone that is ahead of
UTC, you must encode the + symbol as %2B.
For example, for the Central European Time zone +01:00,
you must use %2B01:00 in your URL. Alternatively,
you can specify a UTC date, for example ended\_after=2016-01-01T01:00:00Z.

## Using a wsadmin command

To
delete BPEL process instances from the Business Process Choreographer
database, see deleteCompletedProcessInstances.py administrative script.

- Counting BPEL process instances

You can use the Process Admin Console or a REST API call to count the number of BPEL process instances that are in an end state and that match specified criteria before you decide whether to delete them.