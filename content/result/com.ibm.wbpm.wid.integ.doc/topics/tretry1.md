<!-- image -->

# Retrying a failed service invocation

## Before you begin

- Any fault
- Modeled fault
- Unmodeled fault

| Property Name                                                    | Description                                                                                                                                                                                                                                                                                                                                                |
|------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Retry Count                                                      | Count of retry attempts made after the initial failure. If 0, no attempts are made. If Try alternate endpoints is false or if there are no alternate endpoints specified in the SMO headers, all attempts will retry the original service.                                                                                                                 |
| Retry Delay                                                      | The delay, in seconds, before each retry attempt is made. If 0, delay will be dictated by speed of server.                                                                                                                                                                                                                                                 |
| Try Alternate Endpoints(requires Use Dynamic Endpoint to be set) | If the SMO Header contains alternate endpoints, retry calls will be made to them in the order they appear.                                                                                                                                                                                                                                                 |
| Async Timeout                                                    | If this timeout occurs and the Retry Count has not been reached, it is treated as an unmodeled fault and retry will be performed. The retry delay will take place following the Async Timeout. If the Retry Count has been reached, then the Timeout terminal of the Service Invoke primitive, or the fail terminal of the Callout Response node is fired. |

- Retrying the same service

Occurs if the Try alternate endpoints property is false or if no alternate endpoints are provided in the SMO Header.
- Retrying a different service

Occurs if alternate services are available to receive the retry. Only available through the Service Invoke primitive.
- Retrying alternate endpoints of the same service

Finding alternate endpoints with the Endpoint Lookup primitive and retrying them with either the Service Invoke or Callout node primitive.