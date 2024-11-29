# OutOfMemoryErrors after migration

```
2,115,840,672 (48.54%)[88]9 org/apache/axis2/context/ConfigurationContext 0x99b8aa38
            2,115,838,152 (48.54%)[176]33 org/apache/axis2/engine/AxisConfiguration 0x96f59228
              2,030,303,824 (46.57%) [48]1 java/util/concurrent/ConcurrentHashMap 0x96f59708
                [..]2,030,303,776 (46.57%)[80]16 array of java/util/concurrent/ConcurrentHashMap$Segment 0x99b8cc88
                      1,774,689,352(40.71%)[32]2 java/util/concurrent/ConcurrentHashMap$Segment 0x96f5c5f0
                         [..]1,774,689,296(40.71%)[4,112]375 array of java/util/concurrent/ConcurrentHashMap$HashEntry 0x1104b7dd0
                              302,843,912(6.95%)[24]3 java/util/concurrent/ConcurrentHashMap$HashEntry 0x114b92370
                              284,064,808(6.52%)[24]2 java/util/concurrent/ConcurrentHashMap$HashEntry 0xcfc63250
```

More memory is required because the default behavior of JAX-WS applications changed between
WebSphere® Application
Server V6, V7, and V8.  Because Business Automation Workflow relies on WebSphere Application
Server, you might see this problem when you migrate
WebSphere Application
Server with Business Automation Workflow.

```
jaxws.share.dynamic.ports.enable = true
```