# Runtime backup and restoration

## About this task

Because RAM data will be lost during the
backup and restoration procedure, you must depend on global transactions
to keep data integrity.

To ensure overall consistency, all
modified resources inside the scenario design must be included in
the same recovery scope.

For asynchronous invocation, you can
get different replay results because you can have different settings
on the transaction boundaries. Because the transaction cannot pass
through the boundary of caller and partner, a separate transaction
context is required for both caller and partner, so that they can
be restored through the disaster recovery procedure.

<!-- image -->

- The OrderHandling main process is a long-running
process, which itself is contained in a global transaction context.
During the navigation, the transaction might be demarcated by invocation
or human task activity; however, for each partition, it is still wrapped
by a global transaction.
- The CheckCustomerAccountStatus subprocess isa long-running process as the partner of the main process, which iscontained inside a global transaction as well. It will be invokedthrough asynchronous invocation.The implementation for the CheckCustomerAccountStatus BPELprocess is shown in the following figure: CheckCustomerAccountStatus is a long-runningprocess. When you are restoring in the backup environment, thestrings in Snippet and Invoke will be printed.

<!-- image -->

    - The transactional behavior for Receive is Commit After.
    - For Snippet, it is Participates.
    - For Invoke, it is Commit After.

When you are restoring in the backup environment, the
strings in Snippet and Invoke will be printed.

- The UpdateOrderDatabase subprocess is a short-running
process as the partner of the main process, which is contained inside
a global transaction and invoked through asynchronous invocation.
- The CancelOrderandSendNotification component
is an SCA component and invoked as asynchronous one-way.The implementation
for the CancelOrderandSendNotification BPEL process
is shown in the following figure. 

CancelOrderandSendNotification is a microflow,
so by default the transactional behavior is Participates. However,
because the invocation style for InvokeNotification is synchronized
and it is a one-way invocation, only the strings in InvokeNotification
will be printed in the backup environment.

## Procedure

To verify the data for this scenario, complete the following
steps:

1. Generate some load on the environment, and make sure that
some instances are still running.
2. Take a snapshot of the environment.
3. Restore the snapshot to the secondary environment.
4. To observe the behavior of the restored environment, start
the whole environment in an isolated environment that does not share
any resources with the primary environment.

## Results

Through the persistence and transaction support of the underlying implementation, the running
instances will continue to run through the backup and restoration procedure.