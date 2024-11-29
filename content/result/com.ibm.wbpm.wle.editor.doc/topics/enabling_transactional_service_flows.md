# Enabling transactional service flows

To run a transactional service flow, you can enable the feature to execute a service flow
within a single transaction. This feature handles the various service flow activities by using a
dedicated linkage to the service flow engine. Activities like the SQL Integration capability that
reads and stores business data to underlying DB systems can rollback these activities if an error
occurred.

The transactional capability is also passed to linked service flows but these linked service
flows must have the checkbox marked to execute the service flow in a single transaction.

External services that are called must support the propagation of these local transactions
according to achieve a consistent execution behavior.