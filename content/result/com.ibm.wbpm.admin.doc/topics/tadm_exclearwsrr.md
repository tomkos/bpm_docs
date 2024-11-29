<!-- image -->

# Example: Clearing the cache from the command line

## Before you begin

## About this task

## Procedure

1. From a command line, start wsadmin.
2. From wsadmin, retrieve a reference to a specific ServiceRegistry
MBean.  For example, wsadmin>set wsrrDef [$AdminControl completeObjectName
WebSphere:type=ServiceRegistry,mbeanIdentifier=testWSRR1,*]This
example, uses JACL to set a reference to a ServiceRegistry MBean in
the variable wsrrDef. Note: In a network deployment
environment there might be several instances of each ServiceRegistry
MBean, each of which would require the cache to be cleared.
3. Invoke the expireCache operation on
the ServiceRegistry MBean whose reference you have retrieved. 
For example:wsadmin>$AdminControl invoke $wsrrDef expireCache.

## Results