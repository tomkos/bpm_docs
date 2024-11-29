# Creating a REST service

## Procedure

To create the REST service:

1. Open the designer.
2. In the library, select Exposed Automation
Services > + > REST
service.
3. Name the REST service.
The REST service editor opens.
4 Add an operation for each business function that you want to expose. To add an operation,click Add . In the operation details, name the operation andspecify the service flow or process that provides the implementation for the operation. For theimplementation, you can: For more information about service flows and how to create them, see Creating a service flow . For more information about processes and how to create them, see Creating a process . Inputs and outputs can use the simple typesthat are included with the product, such as String , Integer ,Boolean , Decimal , Date , or Time ,from the System Data toolkit or custom business objects. Types from other system toolkits are notsupported. Tip: Make sure that there aren't multiple business objects with the same namein the dependency chain of your exposed REST automation service and its interface. Note: Only ASCII characters are allowed in the following: Rationale: From the exposed REST automation service definition, avalid OpenAPI definition is generated that adheres to the respective specifications. After you edit the REST service, click Save or FinishEditing .
    - Create a new service flow or process by clicking New.
    - Select an existing service flow or process by clicking Select.
    - The name of an operation
    - The names of the business objects that are referenced by the inputs or outputs of the automation
service implementation (for example, service flow and process)
5. Optional: For consumers other than automation service
consumers: 
To develop an external client, see the OpenAPI definition for the REST service as it exists and
is available in the development environment, by clicking the OpenAPI definition URL in the
Behavior section of the REST service editor.

## Results

To invoke a REST service, the appropriate snapshot must be activated.

In the development environment, the REST service on the tip or the default track can be invoked
directly. Make sure to make the track the default to open the OpenAPI definition URL in REST service
directly.

In a test, staging, or production runtime environment, the consumer can either invoke the REST
automation service from the default snapshot or consume the REST automation service from a dedicated
snapshot.

```
http://host\_name[:port]/[custom\_prefix/]automationservices/rest/process\_app\_acronym/[snapshot\_acronym/]rest\_service\_name/docs
```

- host\_name is the host name.
- port is the optional port number.
- custom\_prefix is an optional custom prefix
- process\_app\_acronym is the acronym of the process app
- snapshot\_acronym is the optional snapshot acronym that, if not specified,
resolves to either the tip of the default branch in the development environment, or to the default
snapshot in a runtime environment.
- rest\_service\_name is the name of the REST service.

These REST services can be called by all authenticated users by using basic authentication or Zen
API key authentication. See Authorizing HTTP requests by using the Zen API
key for more information.