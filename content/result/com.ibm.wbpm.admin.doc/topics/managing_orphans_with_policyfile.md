# Generating an instance migration policy file to manage orphaned tokens

## Before you begin

Make sure that the instances complete if orphaned tokens are created on event gateways before you
migrate an instance.

## About this task

You can enable instance migration to suspend the process after the token operations are performed
so you can make further changes and resume the instance before users can access them. A policy file
is specific to each unique source and target snapshot pair. It contains a section for each process
that contains orphaned activities. Each process section contains a step entry for each orphaned
activity in the process. If there are no orphaned activities for a source and target snapshot pair,
a policy file is still generated but won't contain actions to perform.

## Procedure

- Generate the file in Workflow Center. See Defining the migration policy by using the Process Center console.
- Generate the file by using a wsadmin command. See Defining the instance migration policy by using a wsadmin command.

## What to do next

- Defining the instance migration policy by using the Process Center console

When you migrate from one snapshot to another, you can use the IBM Process Center console to define an instance migration policy for deleting or moving orphaned tokens. An orphaned token is a token associated with an activity that exists in the source snapshot but not in the destination snapshot.
- Defining the instance migration policy by using Workflow Center

When you migrate from one snapshot to another, you can use Workflow Center to define an instance migration policy for deleting or moving orphaned tokens. An orphaned token is a token associated with an activity that exists in the source snapshot but not in the destination snapshot.
- Defining the instance migration policy by using a wsadmin command

When you migrate from one snapshot to another, you can use the BPMCheckOrphanTokens wsadmin command to define an instance migration policy for deleting or moving orphaned tokens. An orphaned token is a token associated with an activity that exists in the source snapshot but not in the destination snapshot.

## Related tasks

- Changing the security policy