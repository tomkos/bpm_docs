# Querying relationships between process instances by using JavaScript

## Getting a list of relationships

1. Decide whether you want to check the user's authorization.
2. Get the list of relationships by using the getRelationships() method,
which has the following signature:
TWProcessInstance.getRelationships(checkAuthorization);
checkAuthorization
A Boolean value that the method uses to determine whether it should
check the user's authorization. The default is false.

The getRelationships() method
returns a list of relationships that are associated with the process
instance (BPMRelationship objects).

## Getting a list of independently associated process
instances

1. Decide whether you want to check the user's authorization.
2. Decide whether you want to filter the list of process instances
based on their runtime status.
3. Get the list of process instances by using the getRelatedProcesses() method,
which has the following signature:
TWProcessInstance.getRelatedProcesses(checkAuthorization, statusFilter)

checkAuthorization
A Boolean value that the method uses to determine whether it should
check the user's authorization. The default is false.

statusFilter
A list of strings that filters the results. Valid values are Active,
Completed, Failed, Terminated, Did not Start, and Suspended. 

The getRelatedProcesses() method
returns a list of TWProcessInstance objects.

## Getting a dependent process instance

1. Decide whether you want to check the user's authorization.
2. Get the list of relationships by using the getDependentProcess() method,
which has the following signature:
TWProcessInstance.getDependentProcess(checkAuthorization)

checkAuthorization
A Boolean value that the method uses to determine whether it should
check the user's authorization. The default is false.

The getDependentProcess() method
returns a TWProcessInstance object.

## Getting a list of process instance dependencies

1. Decide whether you want to check the user's authorization.
2. Decide whether you want to filter the list of process instances
based on runtime status.
3. Get the list of relationships by using the getDependedOnProcesses() method,
which has the following signature:
TWProcessInstance.getDependedOnProcesses(checkAuthorization, statusFilter)

checkAuthorization
A Boolean value that the method uses to determine whether it should
check the user's authorization. The default is false.
statusFilter
A list of strings that filters the results. Valid values are Active,
Completed, Failed, Terminated, Did not Start, and Suspended.

The getDependedOnProcesses() method
returns a list of TWProcessInstance objects.