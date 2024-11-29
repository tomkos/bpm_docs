<!-- image -->

<!-- image -->

# setStateObserver.py administrative script

## Location

```
install\_root\ProcessChoreographer\admin
install\_root/ProcessChoreographer/admin
```

## Syntax

```
install\_root/bin/wsadmin.sh 
install\_root\bin\wsadmin

-f setStateObserver.py 
     -bfm 
     -cluster clusterName
     -conntype NONE
     -enable {DEF | AuditLog | TaskHistory | IndexerLog}
     -disable {DEF | AuditLog | TaskHistory | IndexerLog}
     -htm 
     -profileName profileName
```

## Parameters

## Examples

The following example shows how to enable
DEF logging for BPEL process events on myCluster:

Enter the following
command:

```
wsadmin.sh -f setStateObserver.py -cluster myCluster -enable DEF -bfm
```

Enter the following command:

```
wsadmin -f setStateObserver.py -cluster myCluster -enable DEF -bfm
```