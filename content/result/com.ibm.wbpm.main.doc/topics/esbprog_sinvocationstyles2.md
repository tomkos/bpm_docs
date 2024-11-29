<!-- image -->

# Synchronous invocation

Once the service provider has been called, all processing is suspended until the thread returns a
response. This is shown in Figure 1.

Figure 1. Synchronous SCA invocation

<!-- image -->

## Example scenario

Jane wants to transfer money through online banking, to Stephen's bank account. The bank
must ensure that Jane's account is debited, and Stephen's account is credited. Both of the
actions must be completed, and if one of the actions fail then neither of them must occur. If
Jane's bank account is debited, and Stephen's bank account fails to be credited, a
rollback action must occur to credit Jane's bank account, so that money is not lost at any
point of the transaction. A confirmation message will only be sent to Jane if the transfer is
successful.

Synchronous SCA invocation is an applicable style in this situation, because a message is sent to
the service in one thread, and no processing is done by the service requester until the message
returns for processing to continue in the same thread.