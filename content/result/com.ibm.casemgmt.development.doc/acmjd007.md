# CaseType class

- fetchInstance
- getFetchlessInstance

Much of the information contained in a CaseType instance is managed by a cache
that is internal to the workflow Java™ API. All of the
information can be retrieved, whether the instance was obtained with or without a fetch operation.
However, the fetchInstance method runs only an initial check to ensure that the
referenced case type is valid.

## Related reference

- Case class
- CaseMgmtObjectStore class
- DeployedSolution class