# Invoking a REST service

## About this task

You must have a valid and complete OpenAPI 2.0 (or 3.0) specification that includes the necessary
security definitions. The OpenAPI format can be either JSON or YAML. To verify that your OpenAPI
specification is valid, open the file in an OpenAPI editor or a Swagger editor.

To use a REST service in the designer, you discover the service and select the operations that
you want to use. Then, set the server that contains the configuration properties that are required
to invoke the service. An external service is generated containing the operations that you selected
in the discovered service and a reference to the server that you selected. Business objects are also
generated based on the OpenAPI specification.

Service providers update their services periodically, and you might want to rediscover the
updated service so that you can use it. When you discover a service, if an external service
discovered from the same file already exists in the designer, you can either overwrite the existing
service or create a new one. To get the updated version of the REST service, replace the external
service. If you have a service task for the external service, their operations and data mappings are
preserved, unless the operation or data is not included in the new version. If the server connection
information is unchanged, you can keep the reference to the server information.

- To use a REST service, for which the OpenAPI file (previously known as
Swagger) specifies an authentication type other than basic authentication or API key authentication
(as a header or a query string parameter).
- To call a REST service, for which the OpenAPI specification contains objects that have no
properties.
- To call a REST service that specifies file or string/binary types.
- To use MIME types other than application/json,
application/x-www-form-urlencoded with primitive values or arrays with primitive
values, or text/plain with schema type string. Note that a parameter of type string
and format binary in combination with a MIME type other than application/json is
not supported. At run time, the invocation is rejected with an exception.
- To use the property enum for data types boolean, decimal, integer, string +
format=date, and string + format=date-time.
- To use parameter type formData.
- To use data types of type object, in which not all property names are valid
JavaScript identifiers. A name is a valid JavaScript identifier if it starts with a letter,
underscore (\_), or dollar sign ($), and contains only letters, digits, underscores or dollar
signs.

## Procedure

To discover an existing REST service with an OpenAPI specification and generate an
external service that you can use in a service flow, complete the following steps.

1 Create an external service in one of the following ways:
    - Beside Services in the library navigation, click the plus sign (+).
Select External Service. In the New External Service 
page, choose Java, REST or Web service.
    - In the Service Flow editor, select a Service
task. In the Implementation tab for the service, click
New.
2. Select one of the following: 

REST service from URL
Enter the URL of the OpenAPI (Swagger) file. For example,
https://hostname:port/rest-api.json.
Where hostname is the host name and port is the port
number.
REST service from local file
Select the OpenAPI (Swagger) file on your local file system.

Tip: You can discover REST services that have API key security definitions in their
OpenAPI file.
Note: The OpenAPI 2.0 specification allows you to describe headers as parameters of your
REST API. For some headers the OpenAPI 2.0 specification has special constructs that should be used
instead of describing those headers as parameters because they are ignored with OpenAPI 3.0:
Content-Type
Use consumes for request content type. Use produces for
response content type.

Accept
Use produces.
Authorization
Use securityDefinitions, security.

If the OpenAPI definition is protected by HTTP basic authentication, specify user
name and password.
3 You might see one or both of the following:

- A list of operations that can only be invoked by using a script task. These operations will not
be included in the generated external service and are therefore not available in the tool to be
invoked in a service task. To see the reason why, click View explanation.
To invoke these operations, you must use the JavaScript API. To make these operations available
for invocation by using JavaScript, you must generate an external service by completing the service
discovery. For more information, see Invoking a REST service by using JavaScript.
Tip: You can view the operations in the source view of the External Service
editor.
- A list of operations that have warnings in the OpenAPI specification. You can view the warnings
for each operation. If you decide to run such an operation, you might get unexpected results;
regardless of whether you invoke it through a service task or a script task. For more information,
see OpenAPI support for invoking a REST service
4. Click Next.
5. The discovered operations are listed. Select the operations that you want to include in
the external service, and click Next.
6. If the OpenAPI specification was already discovered, you can create a new service or
replace the existing one. Click Next.
7. Set the server that contains the properties used to invoke the REST service. Either
select an existing server, or create a new one based on information in the OpenAPI specification.
Click Finish.

## Results

- The inputs of an operation correspond to the parameters of the operation, as listed in the
OpenAPI file. Additionally, for OpenAPI v3 operations that have a requestBody, an
input is listed that corresponds to the content of the
requestBody. If the x-codegen-request-body-name field is defined
for this operation, its value becomes the name of the input. Otherwise its name is
body or, if there is already a parameter named body,
body\_n where n is a positive integer. Note: x-codegen-request-body-name is a vendor extension that is used by some
tools to control how the request body parameter is named in the case of OpenAPI v3. If your OpenAPI
definition does not use this extension but you want to control the name of the input, add the vendor
extension x-codegen-request-body-name to the appropriate operations as shown in the
following snippet: paths:
  /translateText:
    post:
      operationId: translateText
      x-codegen-request-body-name: input\_parameter\_name\_for\_body
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/translateTextInput'
        required: true
      responses:
        ...

Tip: The x-codegen-request-body-name field has no relevance when you
invoke this operation by using JavaScript.
If the REST Service is an automation service, the parameter that corresponds to the
requestBody does not appear if its type is a complex type; instead its constituents
are listed.
- The outputs of an operation correspond to the responses: one output for each response code that
is listed in the OpenAPI file. If the REST service is an automation service, these outputs do not
appear if they are complex types; instead their constituents are listed.
- In the Details section, the service name and its documentation is shown.
- Selecting Binding shows the binding type of REST,
the server, and (optionally) authentication information. If your server binding properties change,
you can select a different server.In this panel, you can enter authentication information for
invoking the service, for all security definitions that are defined in your OpenAPI specification.
Important: For security definitions of type basic (basic
authentication), the authentication information that you specify here overrides the information
provided for the server. For security definitions of type apiKey and OAuth 2, you
can specify authentication information here, but not in the server.
- Selecting Source shows the OpenAPI specification source in read-only
mode. This is useful for viewing the operations that you want to invoke using JavaScript API.
- In the Data library section, you might see business objects as a result
of generating the REST service. These business objects are only for the external service and are
read-only. Deleting the external service also deletes these business objects.

After your external service is created, you can select it as an implementation of a service task
in a service flow. Select the operation
that you want to use from the operation list and map the inputs and outputs in the Data
Mapping tab. If you are using JavaScript to invoke your operation, enter your JavaScript
in a script task in a service flow. See Creating a service flow and Invoking a REST service by using JavaScript.

If your OpenAPI specification includes security definitions of type apiKey, the
API keys that are used by the selected operation show up on the Data Mapping
tab. You can retrieve the API keys before using it in the service flow and store it in a private
transient variable and map it in the Data Mapping tab. By storing the API key
in a transient variable, as described in Using transient variables in service flows, it will not be
persisted in the database as part of the execution context.

The API keys that you specify here have higher precedence than any that you specify on the
Binding tab.

To catch any errors that might occur in the service, attach a catch all boundary error event to
it, as described in Catching errors by using error boundary events.

- Specifying a REST server

During discovery, the external service is automatically set to point to the REST server. You can modify the server binding properties that your external service uses to invoke a REST API.
- Invoking a REST service by using JavaScript

Invoke a REST service from a script task in a service flow.
- OpenAPI support for invoking a REST service

REST services that are defined in OpenAPI v2 and OpenAPI v3 specification files are supported, however, a few restrictions apply.