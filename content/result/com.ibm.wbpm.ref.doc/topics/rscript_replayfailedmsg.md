<!-- image -->

# replayFailedMessages.py administrative script

## Prerequisites

- Run the script in the connected mode, that is,
do not use the wsadmin -conntype none option.
- At least one cluster member must be running.
- Include the wsadmin -user and -password options
to specify a user ID that has operator authority.

## Location

```
install\_root\ProcessChoreographer\admin
install\_root/ProcessChoreographer/admin
```

## Syntax

```
-f replayFailedMessages.py
       -cluster cluster\_name
       -queue replayQueue
       [ -bfm | -htm ]
```

## Parameters

- holdQueue (this is the default value)
- retentionQueue (only valid when the -bfm option
is specified)
- both (not valid when the -htm option
is specified)