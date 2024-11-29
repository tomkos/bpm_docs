# Limitations of the MQ binding

## No publish-subscribe message distribution

The
publish-subscribe method of distributing messages is not currently
supported by the MQ binding though WMQ itself supports publish-subscribe.
However, the MQ JMS binding does support this method of distribution.

## Shared receive queues

- Each MQ import must have a different receive queue because the
MQ import binding assumes all messages on the receive queue are responses
to requests that it sent. If the receive queue is shared by more than
one import, responses could be received by the wrong import and will
fail to be correlated with the original request message.
- Each MQ export should have a different receive queue, because
otherwise you cannot predict which export will get any particular
request message.
- MQ imports and exports can point to the same send queue.