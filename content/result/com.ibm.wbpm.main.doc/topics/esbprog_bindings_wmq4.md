<!-- image -->

# Using dynamic WebSphere MQ endpoints

Using a mediation flow component, you can specify a target import and dynamic endpoint address
using mediation primitives such as the Message Element Setter mediation primitive.

Figure 1 shows a mediation module that includes an
import, which is not wired to the mediation flow component. The import is configured to use Service
Provider 1. Using the mediation flow component, the target import is specified in the SMO, and the
unwired import is invoked. Other imports can be selected instead, if they are available. If you
specify a target endpoint in the SMO, it overrides the imports reference to Service Provider 1, and
replaces it with Service Provider 2. The service that is invoked at run time, is decided on a
message by message basis.

Figure 1. Mediation module with an unwired import which is configured to use service provider 1

<!-- image -->

- /headers/SMOHeader/Target/address
- /headers/SMOHeader/Target/@bindingType
- /headers/SMOHeader/Target/@import
- /headers/SMOHeader/AlternateTarget/address
- /headers/SMOHeader/AlternateTarget/@bindingType
- /headers/SMOHeader/AlternateTarget/@import

The address field includes the dynamic invocation target service URI for
requests. When requests are routed, the @bindingType field provides further
details about the URI. It indicates the type of binding that is used during a dynamic invocation.
When requests are routed, the @import field provides the name of a target
import that is used for dynamic invocation.

```
>>-wmq:--+------------+--+-------+--/msg/queue/--queueName-
         '-//hostname-'  '-:port-'  
-+-------+--+---------------------------+-><
  '-@qmgr-'  '-?connectQueueManager=qmgr-'
```

In each URI, the queueName and optional destination queue manager,
qmgr override the destination queue specified on the import binding. The
hostname, port, and connectQueueManager,
override the connection information on the import binding.

Examples of a valid WebSphere MQ URI are:

```
wmq:/msg/queue/queueName 
wmq:/msg/queue/queueName@qmgr
wmq://hostname/msg/queue/queueName
wmq://hostname/msg/queue/queueName@qmgr 
wmq://hostname:port/msg/queue/queueName
wmq://hostname:port/msg/queue/queueName@qmgr
```