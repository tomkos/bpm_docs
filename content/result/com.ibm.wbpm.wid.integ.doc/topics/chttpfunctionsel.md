<!-- image -->

# Prepackaged HTTP function selectors

The following HTTP function selectors can be used with the HTTP
binding.

| Function selector                                                          | Description                                                                                                                                                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HTTP function selector based on the TargetFunctionName header              | This function selector uses the TargetFunctionName HTTP header property from the client to determine which operation to invoke at run time from the export.                                                                                                                                                                                                    |
| HTTP function selector based on the URL and HTTP method                    | This function selector uses the relative path from the URL appended with the HTTP method from the client to determine the native operation defined on the export. For example, if the URL is http://www.ibm.com/SampleWeb/SearchFlightInfExport1/findFlight and the HTTP method is GET, then the native method will be /SearchFlightInfExport1/findFlight@get. |
| HTTP service gateway function selector based on URL with an operation name | This function selector should be used in conjunction with an HTTP binding using the service gateway interface. It determines the method to invoke based on the URL and if operationMode = oneway has been appended to the request URL.                                                                                                                         |
| One operation function selector                                            | For an interface with only one operation, this function selector returns the one operation available.                                                                                                                                                                                                                                                          |

## Related concepts

- Overview of HTTP data bindings
- Prepackaged HTTP data format transformations
- Overview of HTTP function selectors

## Related reference

- Data handlers
- Prepackaged HTTP fault selectors