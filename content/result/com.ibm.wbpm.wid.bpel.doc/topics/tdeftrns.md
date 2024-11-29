<!-- image -->

# Defining transactional behavior

## About this task

For information on setting up transactions see the related
topic on Transactions.

A simple
tools is provided so that you can review the transaction propagation
in your process. right-click in the Assembly editor and select Show
Transaction Highlighting. The transactional highlighting
is displayed for the whole process.

You can highlight the transaction
properties of a subset of the entire process by selecting a specific
activity, right-clicking and selecting Show Transaction
From Here. The transaction propagation associated with
the selected activity and all downstream components are highlighted.

When
you have highlighting enabled, you will find hover help available
for the highlighted activities and wires. This hover help will explain
the highlighting of the interface, reference, wire, component, import
or export over which you are hovering.

| Component        | Highlighting           | Explanation                                                                                                                                                                                                                                                                                                                     |
|------------------|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Interface        | Solid green circle     | The component is configured so that the implementation always joins a propagated transaction.                                                                                                                                                                                                                                   |
|                  | Dotted green circle    | The component is configured so that the implementation sometimes joins a propagated transaction.                                                                                                                                                                                                                                |
|                  | No highlighting        | The component is configured so that the implementation never joins a propagated transaction.                                                                                                                                                                                                                                    |
| Reference        | Solid green box        | Synchronous calls over this reference propagate a transaction.                                                                                                                                                                                                                                                                  |
|                  | Dotted green box       | Synchronous calls over this reference may propagate a transaction.                                                                                                                                                                                                                                                              |
|                  | No highlighting        | Synchronous calls over this reference do not propagate a transaction.                                                                                                                                                                                                                                                           |
| Wire             | Solid green line       | Propagates and joins a transaction                                                                                                                                                                                                                                                                                              |
|                  | Dashed green line      | Some situations propagate and join a transaction, some will not.                                                                                                                                                                                                                                                                |
|                  | No highlighting        | Does not propagate a transaction.                                                                                                                                                                                                                                                                                               |
| Node or activity | Solid green perimeter  | Implementation is invoked synchronously and runs in a global transaction. Equivalently, the transaction qualifier is configured as Global.                                                                                                                                                                                      |
|                  | Dotted green perimeter | Certain components can call one service in one transaction and call another service in a different transaction. This highlighting is applied when a component runs in a global transaction but calls services in this manner. Only long-running BPEL processes and business state machines can carry this special highlighting. |
|                  | Dashed green perimeter | Implementation is invoked synchronously and does not specify that it runs a global transaction. Equivalently, the transaction qualifier is configured as Any.                                                                                                                                                                   |
|                  | No highlighting        | Implementation is invoked asynchronously, or runes with local transactions.                                                                                                                                                                                                                                                     |
| Import           | Solid green perimeter  | A global transaction, if propagated to the import node, is propagated to the service being imported.                                                                                                                                                                                                                            |
|                  | No highlighting        | A global transaction is never propagated to the service being imported.                                                                                                                                                                                                                                                         |
| Export           | Solid green perimeter  | A global transaction can be propagated from the client to the Export, and is further propagated to the export target.                                                                                                                                                                                                           |
|                  | No highlighting        | A global transaction is never propagated from the client to the Export.                                                                                                                                                                                                                                                         |

- Transactional behavior of BPEL processes

BPEL processes are executed as part of transactions. The navigation of a BPEL process can span multiple transactions in the case of long-running processes, or happen as part of one transaction in the case of microflows.