# CaseMgmtObjectStore class

- fetchInstance
- getFetchlessInstance

All of the information contained in an instance of CaseMgmtObjectStore is
managed by a cache that is internal to the workflow Java™ API.
The same information can be accessed whether the instance was obtained with or without a fetch
operation, but the fetchInstance method runs only an initial check to ensure that
the referenced object store is valid.

## Related reference

- Case class
- CaseType class
- DeployedSolution class