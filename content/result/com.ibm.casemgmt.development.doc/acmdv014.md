# Creating and managing case objects by using the workflow REST protocol

- Case management REST resource URIs

Each resource in the workflow REST protocol is identified by a unique URI. This URI includes the resource name and any parameters that are required for the specific method that you are calling.
- Symbolic names

When you design a case, Case Builder assigns symbolic names for metadata objects such as property descriptions, document classes, and folder classes. You use the symbolic names when you refer to these metadata objects in calls to the methods that are provided by the workflow REST protocol.
- Error responses

When a method call fails, the response code that the workflow REST protocol returns indicates the type of error that occurred. For example, the response code 404 Not Found indicates that the method did not find a resource such as the specified solution or case type. The response code 400 Bad Request indicates that a required parameter was not provided or that an incorrect value was specified for a parameter.
- Common JSON payload for cases and case types

The workflow REST protocol defines a JSON payload that is used in the methods that get or return information about a case or case type. This payload is also used by the external data service to obtain case information from an external data source.
- Getting and changing information about deployed solutions

You can use the workflow REST protocol to get information about deployed solutions. This information includes the object stores to which the solutions are deployed and the connection point that identifies the workflow stream, communications port, and isolated region number that is used by the solution.
- Getting information about deployed case types

You can use the workflow REST protocol to access information about the case types. The case types identify the kinds of cases that case workers can create with your application.
- Getting and changing case information

You can use the workflow REST protocol to get and set case data, including case comments, case history, and activities.