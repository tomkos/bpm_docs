# REST API programming for BPDs and BPEL processes

Each REST API has a schema for the request content. Each parameter
is of type string, boolean, or integer.
The framework tries to parse the client input to the type that is
specified in the schema. For a string parameter,
values are passed as strings, whether they are a character string,
a Boolean, or a number. For example, the word value is
parsed as the "value" string, the number 42 is
parsed as the "42" string, and the Boolean value true is
parsed as the "true" string. Moreover, for Boolean
and number types, string values that can be parsed as Boolean or numbers
respectively are also accepted. But if a string value is passed and
cannot be parsed to a Boolean or number, a 400 error
is returned. For example, "T" is not a valid
value for a Boolean parameter.

- Resource URIs for BPD and BPEL resources

The resource URIs represent the resources.
- HTTP methods supported by the BPD and BPEL REST APIs

The HTTP methods provide the operations, such as create, read, update, and delete that you can perform on artifacts.
- HTTP header fields and generic URI parameters

The URIs for the BPD and BPEL REST resources support certain HTTP header fields and generic URI parameters.
- Testing REST APIs

A test tool is provided for the BPD, BPEL, and federated REST APIs. You can use this tool to help you learn about the REST APIs, and to test those APIs that you are planning to use in your application.
- REST APIs and federated environments

Business Automation Workflow provides two different styles of federated REST APIs: Process Federation Server REST APIs and the federated Business Automation Workflow REST APIs. The APIs differ in the way that client requests are handled.
- Authorization control for runtime REST API calls

Use authorization roles and action policies to enable users for specific actions on workflow entities such as tasks, processes, users, groups, and teams.