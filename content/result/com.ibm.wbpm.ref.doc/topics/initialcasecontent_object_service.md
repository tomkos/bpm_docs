# Initialize Case Content Objects service

The following input and output-mapping tables help you to use the service properly.

| Name     | Description                                                                                                                                      | Data type   |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| caseType | The case type that is passed as input to the Initialize Case Content Objects service. Map this config option to tw.local.caseType.               | String      |
| tosName  | The target object store name that is passed as input to the Initialize Case Content Objects service. Map this config option to tw.local.tosName. | String      |
| caseId   | The case instance ID that is passed as input to the Initialize Case Content Objects service. Map this config option to tw.local.caseId.          | String      |

| Name           | Description                                                                                                                                                                                                                                                 | Data type   |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| caseProperties | The caseProperties of type ANY that receives the output from the execution of the Initialize Case Content Objects service. The value of type ANY is set in the caseProperties of type caseType. Map the output result (ANY) to tw.local.caseProperties ANY. | Any         |