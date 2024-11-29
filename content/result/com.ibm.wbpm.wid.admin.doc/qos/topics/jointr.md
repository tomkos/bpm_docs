<!-- image -->

# Join transaction qualifier

- For all of its interfaces
- For an individual interface
- For an individual operation of an interface

- True  - If the implementation runs in a
global transaction, it will join any transaction propagated by a client.
- False  - The implementation will not join
any transaction propagated by a client.

Application: The
join transaction qualifier is applied when the client invokes this
service synchronously. If this qualifier is present and the client
makes an asynchronous invocation, the qualifier is ignored; transactions
are not propagated over asynchronous invocations. A runtime error
does not result under these conditions. This qualifier simply directs
the component to run under a propagated transaction if one is propagated.

When
you specify that a transaction should be joined, the transaction qualifier
should be specified for the component implementation and the qualifier
should be set to "global" or "any". (This setting is checked and the
handler produces an error if the qualifier is not set this way.) Since
it only takes affect on synchronous invocations, the preferred interaction
style of the interface should be set to "synchronous" or "any". (This
setting is not checked by validation.) This qualifier is typically
used only when the component will perform the operation in a short
amount of time. If your component is likely to take a long time to
perform an operation, you should not specify this qualifier. If you
do, then you should set it to "false" so that the component will not
join in any propagated transaction.

A component implemented
with a long-running BPEL process or a business state machine cannot
join a client transaction, because these implementations are invoked
asynchronously. The transaction qualifier must be set to "false".

## Programming notes

| Interface - Join Transaction qualifier   | Implementation - Transaction Value qualifier   | Resulting behavior of the target component                                                                                          |
|------------------------------------------|------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| True                                     | Global                                         | The component runs in a propagated transaction if one is present. Otherwise, the runtime processes create a new global transaction. |
| True                                     | Local                                          | Runtime processes generate an error. These qualifier settings are incompatible.                                                     |
| True                                     | Any                                            | The component runs in a propagated transaction if one is present. Otherwise, it runs in a local transaction.                        |
| False                                    | Global                                         | The component runs in a new global transaction.                                                                                     |
| False                                    | Local                                          | The component runs in a local transaction.                                                                                          |
| False                                    | Any                                            | The component runs in a local transaction.                                                                                          |