<!-- image -->

# Setting qualifiers and transactions

The system tries to anticipate your needs by generating qualifiers when
you add interfaces and references and when you generate an implementation
or synchronize from an implementation. You can also add your own qualifiers
to the module.

The following topics introduce the quality of service qualifiers and explain how transactions are handled in IBM® Integration
Designer. They also explain how to view and change the qualifiers in the assembly editor. A separate section provides reference details about each qualifier.

- Quality of service: Qualifiers for business services

Quality of service (QoS) qualifiers define how much management must be provided for a component at run time. These qualifiers propagate transactions and control the quality and timing of message delivery.
- Transactions

Setting up transactions in an SOA environment can be an intricate exercise. The assembly editor provides aids to make it easier to understand the way transactions will be processed, but you should understand the mechanics of transactions before you try to create them.
- Viewing and changing qualifier settings

The assembly editor applies qualifiers to create the best pattern that it can determine to propagate transactions and to guarantee message delivery. The editor also provides ways to see the transaction pattern and change settings.
- Adding qualities of service qualifiers

Quality of service qualifiers are specified for interfaces, partner references, and implementations in the assembly editor. You can add qualifiers to supplement or replace the ones generated by the editor.
- Processing events in a sequence

You can use an event sequencing qualifier when you need to ensure that events are processed in order and that one event is completely processed before the next one is processed.