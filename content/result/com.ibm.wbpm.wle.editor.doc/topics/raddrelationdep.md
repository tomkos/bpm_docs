# Adding a dependent relationship between process instances by
using JavaScript

## The current instance depends on another instance

You
can add a dependency relationship where the current instance
becomes dependent on the instance that is passed into the method.
This relationship prevents completion of the current process instance
until the instance that it depends on completes.

1. Decide whether you want to check the user's authorization.
2. Get the instance ID of the process instance to which you want
to add the relationship.
3. Add a relationship by using the addDependencyOnProcess() method,
which has the following signature:TWProcessInstance.addDependencyOnProcess(processInstanceID, description, checkAuthorization);

processInstanceID
The process instance ID of the process instance to which you want
to add the relationship. The current process becomes dependent on
this process and cannot complete until this process instance completes. 

Description
A string that describes the relationship. To update
the description, use the relationship.updateDescription() method.

checkAuthorization
A Boolean value that is used by the method to determine whether
it should check the user's authorization. The default is false.

The addDependencyOnProcess() method
returns a Relationship object, which contains
the details of the relationship.

```
1  var process = tw.system.startProcessByName("Test BPD", null, false);
 2  var relation = process.addDependencyOnProcess(processInstanceID, "relationship to a child process", false);
```

1  Starts the process Test
BPD without checking the user's authorization.

2  Adds
a dependent relationship where Test BPD depends on the instance with
ID processInstanceID, with the description relationship
to a child process without checking the user's authorization.

## Another instance depends on the current instance

You
can add a dependent relationship where the instance that
is passed into the method depends on the current process instance.
This relationship prevents the dependent process instance from completing
until the current process instance completes.

1. Decide whether you want to check the user's authorization.
2. Get the instance ID of the process instance to which you want
to add the relationship.
3. Add a relationship by using the addDependentProcess() method,
which has the following signature:TWProcessInstance.addDependentProcess(processInstanceID, description, checkAuthorization);

processInstanceID
The process instance ID of the process instance to which you want
to add the relationship. The process instance becomes dependent on
the current process and cannot complete until the current process
instance completes. 

Description
A string that describes the relationship.

checkAuthorization
A Boolean value that is used by the method to determine whether
it should check the user's authorization. The default is false.

The addDependentProcess() method
returns a  Relationship object which contains
the details of the relationship.

```
1  var process = tw.system.startProcessByName("Test BPD", null, false);
 2  var relation = process.addDependentProcess(processInstanceID, "relationship to a child process", false);
```

1  Starts the process Test
BPD without checking the user's authorization.

2  Adds
a dependent relationship where the instance with ID processInstanceID depends
on the process instance Test BPD, with the description relationship
to a child process without checking the user's authorization.