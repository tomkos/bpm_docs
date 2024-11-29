<!-- image -->

# Querying and replaying failed messages, using the administrative
console

## About this task

## Procedure

1 For the Business Flow Manager, the most flexible way tocheck and reply and messages on the hold queue, is to use the administrativeconsole page for the failed event manager.
    1. Click Servers > Deployment
Environments > deployment\_environment\_name > Failed Event Manager > Search failed events,
for Event type, select BFM hold then
click OK.
    2. If the search results contains any messages, you can
select any of them then either click Resubmit to
replay the messages, or Delete to delete them
from the hold queue without replaying them.
2 To check how many messages are in the hold and retentionqueues, and replay them using the Business Process Choreographer administrativeconsole pages:

1. Click Servers > Clusters > WebSphere application server clusters > cluster\_name,
then on the Configuration tab, in the Business Process Manager section, expand Business Process Choreographer.
2 Choose one of the following options: The number of messages in the hold queue andretention queue are displayed on the Runtime tabunder General Properties .
    - For BPEL processes, click Business Flow Manager.
    - For human tasks, click Human Task Manager.
3 If either the hold queue or the retention queue containsmessages, you can move the messages to the internal work queue. Click one of the following options: Important: The replay buttons are only visible tousers who have administrator or operator authority.

Click one of the following options:

- For BPEL processes: Replay Hold Queue or Replay
Retention Queue
- For human tasks: Replay Hold Queue

## Results

- Refreshing the failed message counts

Use the administrative console to refresh the count of failed messages for BPEL processes or human tasks.

<!-- image -->