# DeployedSolution class

- fetchInstance
- getFetchlessInstance

If
a DeployedSolution instance is obtained by calling fetchInstance,
the method verifies that the referenced object store is valid and
that the solution name refers to a valid solution. If the object store
or solution is invalid, then the method throws an exception. If getFetchlessInstance is
called, no such verification occurs. However, an exception might be
thrown later if another method is called that requires that the identifiers
used to reference the object store is valid.

Much of the information contained in a DeployedSolution instance is managed by a
cache that is internal to the workflow Java™ API. All of the
information can be retrieved whether the object was obtained with or without a fetch, but the
fetchInstance method runs only an initial check to ensure that the referenced
solution is valid.

## Related reference

- Case class
- CaseMgmtObjectStore class
- CaseType class