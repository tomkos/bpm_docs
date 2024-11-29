# Deployment environment status

| Status icon   | Warning icon   | State                  | Description                                                                                                                            |
|---------------|----------------|------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
|               | None           | Unknown                | The system cannot determine the current state of the deployment environment.                                                           |
|               |                | Incomplete             | The deployment environment is not missing any elements but is incomplete in some way. The warning message contains additional details. |
|               |                | Not configured         | The configuration is known and complete but has not yet been generated.                                                                |
|               |                | Deferred configuration | The deployment environment has been generated but deferred configuration has not been completed.                                       |
|               |                | Unavailable            | The deployment environment is complete but at least one function is unavailable.                                                       |
|               |                | Partially stopped      | The deployment environment is available but at least one function is stopped or partially stopped.                                     |
|               |                | Stopped                | All functions are stopped.                                                                                                             |
|               |                | Partially running      | The deployment environment is available but at least one function is partially running.                                                |
|               |                | Running                | The deployment environment is available and all functions are running.                                                                 |