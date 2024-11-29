# Get Repository Name service

| Name   | Description                                                                                                                       | Data type   |
|--------|-----------------------------------------------------------------------------------------------------------------------------------|-------------|
| input  | The input to the service. The Case server ID as in tw.system.currentProcessInstance.parentCase.caseServerId can be used as input. | Any         |

| Name   | Description                                                                       | Data type   |
|--------|-----------------------------------------------------------------------------------|-------------|
| result | The target object store name would be set in the tw.local.results.objectStoreName | Any         |
| error  | Any execution error would be caught in the AjaxError object.                      | AjaxError   |