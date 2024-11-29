<!-- image -->

# Recovery from infrastructure failures

In a long-running process, the Business Flow Manager sends itself
request messages that trigger follow-on navigation. For each incoming
request message, a new transaction is started and the request message
is passed to the Business Flow Manager for processing. Each transaction
consists of the following actions:

- Receive a request message.
- Navigate according to the request.
- Store the state in the database.
- Send request messages that trigger follow-on transactions.

- The retention queue stores failed messages that will be automatically
retried.
- The hold queue stores messages that have failed more times than
the retry limit, and can indicate a more serious infrastructure failure
or a damaged message that cannot be processed.

| Cause                      | Response                                                                                                                                                                                         |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Unavailable infrastructure | In normal processing mode, for a specified time, all messages are kept available until the infrastructure is operational again. This problem might be caused by a database failure, for example. |
| Damaged message            | After a specified number of retries, the message is put into the hold queue. From the hold queue, it can also be moved back to the input queue, to retry the transaction.                        |

If the infrastructure is unavailable, and the retention queue is
full, message processing is switched from normal processing to quiesce
mode. In quiesce mode, the message processing is slowed down
until the infrastructure is available again. When the infrastructure
becomes available, message processing switches back to normal mode.

## Normal message processing

During normal
processing, a message is processed as follows:

- If a message fails three times, it is stored in the retention
queue.
- When a message is in the retention queue, the options are as follows:
    - When a subsequent message is processed successfully, all of the
messages from the retention queue are moved back to the input queue.
For each message, a count is maintained of how often the message is
sent to the retention queue. This count is referred to as the retention
queue traversal count. If this count exceeds the retry limit
for a given message, the message is put in the hold queue.
    - If the next message fails, it is also put in the retention queue.
This process continues until the threshold of maximum messages in
the retention queue is reached. When this threshold is reached, all
of the messages are moved from the retention queue to the input queue,
and message processing is put into quiesce mode.

## Message processing in quiesce mode

In quiesce
mode, processing a message is attempted periodically. Messages that
fail to be processed are put back in the input queue, without incrementing
either the delivery count or the retention queue traversal count.
As soon as a message can be processed successfully, message processing
is switched back to normal mode.

## Retry limit

The retry
limit defines the maximum number of times that a message can be transferred
to the retention queue before it is put in the hold queue.

To
be put in the retention queue, the processing of a message must fail
three times.

For example, if the retry limit is 5, a message
must go to the retention queue five times (it must fail for 3 * 5
= 15 times), before the last retry is started. If the last retry fails
two more times, the message is put in the hold queue. This means that
a message must fail (3 * RetryLimit) + 2 times
before it is put in the hold queue.

In a performance-critical
application running in a reliable infrastructure, the retry limit
should be small: one or two, for example. If the retry limit is set
to zero, a repeatedly failing message is retried three times and then
it goes immediately into the hold queue.

To change this Business
Flow Manager property, click Servers > Clusters > WebSphere application server clusters > cluster\_name,
then on the Configuration tab, in the Business Process Manager section, expand Business Process Choreographer, and click Business Flow Manager.

## Retention queue message limit

The retention
queue message limit defines the maximum number of messages that can
be in the retention queue. If the retention queue overflows, the system
goes into quiesce mode. To make the system enter quiesce mode as soon
as a message fails, set the value to zero. To make Business Flow Manager
more tolerant of infrastructure failures, increase the value.

To
change this Business Flow Manager property, click Servers > Clusters > WebSphere application server clusters > cluster\_name,
then on the Configuration tab, in the Business Process Manager section, expand Business Process Choreographer, and click Business Flow Manager.

## Replay Messages

The administrator can move
the messages from the hold or retention queues back to the internal
queue. This can be done using the administrative console, administrative
scripts, or failed event manager.