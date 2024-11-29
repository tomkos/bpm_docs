# Nodes may fail to synchronize automatically when two deployment
environments exist in the same cell

In this case, you may see exceptions in the administrative
console that indicate that the nodes cannot be synchronized because
another node synchronization is already in progress. For example:

```
ADMS0204E: The system is unable to generate synchronization request for node: Node2.
Another node synchronization operation might be in progress on the same node.
```

If this situation occurs, you can generally resolve the
problem by manually synchronizing the nodes again.