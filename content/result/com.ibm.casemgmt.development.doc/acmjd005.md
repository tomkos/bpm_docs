# Case class

- createPendingInstance
- fetchInstance

A factory method such as fetchInstance obtains
an instance that represents an existing Case object.
State information about the object, such as its list of properties,
is fetched from the repository and maintained in the returned instance.
A Case instance can also be obtained without a fetch
operation by calling the getFetchlessInstance method.
With this method, no call is made to the server to verify that the
object exists in the repository, allows certain operations to be run
in a more efficient manner, since the original fetch of the object
is bypassed.

Once a Case instance is obtained,
other methods can be called to run various operations on the object,
such as modifying its properties, fetching the history of the case,
or adding comments.

## Related reference

- CaseMgmtObjectStore class
- CaseType class
- DeployedSolution class