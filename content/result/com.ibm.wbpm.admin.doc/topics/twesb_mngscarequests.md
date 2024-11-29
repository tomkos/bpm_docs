<!-- image -->

# Administering the throughput of SCA requests

## About this task

When an SCA module is running, requests normally flow through the enterprise service bus without
needing to be managed. Sometimes, you might want to check the throughput of a request, check the
contents of a request, or if some problem has occurred, delete a request. You might also want to
take other actions such as to monitor the overall throughput of requests, or change the reliability
setting for requests.

Requests are handled as messages by the service integration technologies of the underlying
WebSphere® Application
Server. For this reason, actions to manage
requests are managed by using the WebSphere Application
Server tasks
to act on service integration messages.

## Procedure

- List messages on a message point

SCA requests that are being processed are held on queue points of the SCA.SYSTEM.bus. By using
the administrative console, you can list the SCA requests either through a queue destination for a
component of the SCA module, or through the messaging engine that hosts a queue point; for example: Service integration > Buses > SCA.SYSTEM.localhostNode01Cell.Bus > Destinations > StockQuoteService\_Export > Queue points > StockQuoteService\_Export@localhostNode01.server1-SCA.SYSTEM.localhostNode01Cell.Bus > Runtime > Messages
- Delete messages on a message point

Under exceptional circumstances, you might need to delete one or more messages that exist on a
message point for a selected bus destination or messaging engine. You should not normally need to
delete messages on a message point. This task is intended as part of a troubleshooting
procedure.
- View data in a data store.

A messaging engine maintains both volatile and durable data in its data store, including
messages, transaction states, and communication channel states. You can use the database tools to
view data in the data store for a messaging engine.
- Change the message reliability.

Messages have a quality of service attribute that specifies the reliability of message delivery.
You can select a reliability to suit your requirements for assured delivery, and system
performance.