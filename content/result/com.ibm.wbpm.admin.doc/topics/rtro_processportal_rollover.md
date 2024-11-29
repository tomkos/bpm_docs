# Process Portal does
not support automatic session rollover

## Overview

When you are working in a network
deployment environment with a proxy, you are not directly connecting
to a node in the cluster. If the node being accessed becomes unavailable
while running a task, the submission of the coach fails.

```
com.lombardisoftware.core.TeamWorksException: You have been automatically logged out for security reasons
```

## Resolving the problem

To resolve this problem,
log back in to Process Portal. You
are then associated with a new node and can complete the task on that
node.