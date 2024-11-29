<!-- image -->

# Counting BPEL process instances

## Using the Process Admin Console

1. Click Server Admin > Workflow Admin > Health Management.
2. Select the command Count BPEL Processes.
3. Specify values for the command's parameters.
4. Click Submit.
5. If there is an error, you will see the error message.
6. If there is no error, you see how many instances in the system
match the criteria.

## Using a REST API call

Call the operations REST API GET
https://host:port/ops/adv/bpm/processes/count.

- To count how many BPEL instances are in the states finished, terminated and failed:GET https://host:port/ops/adv/bpm/processes/count
- To count how many BPEL instances are in the state finished that
ended between 2015-07-16T12:00:00-06:00 and 2016-08-26T12:34:56-06:00,
and were started by the user user7GET https://host:port/ops/adv/bpm/processes/count?states=finished
    &ended\_after=2015-07-16T12:00:00-06:00&ended\_before=2016-08-26T12:34:56-06:00
    &starter=user7
- To count all instances that are in the states terminated and failed for
the process template myTemplate which is valid from 2016-07-16T19:20:30-06:00:GET https://host:port/ops/adv/bpm/processes/count?states=terminated,failed
    &model=myTemplate&valid\_from=2016-07-16T19:20:30-06:00Remember: If you need to specify a time zone that is ahead of
UTC, you must encode the + symbol as %2B.
For example, for the Central European Time zone +01:00,
you must use %2B01:00 in your URL. Alternatively,
you can specify a UTC date, for example ended\_after=2016-01-01T01:00:00Z.