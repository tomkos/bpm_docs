# Using IBM ODM business
rules

## What you do in IBM ODM

1. Use the Rule Designer to create a business rule.
2. Use the Decision Center to deploy your decision service project
to the Rule Execution Server.
3 In the Rule Execution Server console:
    1. Navigate to the Ruleset View of the project that you want to use
in your Business Automation Workflow process.
    2. Click Retrieve HTDS Description File.
    3. For the service protocol type, select REST.
    4. For the format, select OpenAPI-JSON.
    5. Click Download to save the file locally or click
View and copy the URL. You must specify this file or the URL later in
Business Automation Workflow
Process Designer to discover the IBM ODM decision service as an external REST service.Note: If
your rule-set is secured you must add the security=basic option to the URL so that
the OpenAPI specification contains a security definition and Business Automation Workflow sends the security credentials. The options are
described in the IBM ODM documentation topic Endpoint URIs.

## What you do in Business Automation Workflow to discover
the IBM ODM decision
service

1. From the library, click to create a new External Service.
2. In the New External Service page, select Java,
REST or Web service and click Next.
3. Select Browse local files (Swagger) and
browse to select the OpenAPI specification file that you downloaded
from IBM ODM then
click Next.
4. If you see a list of operations that require JavaScript to invoke
them, click Next.
5. You see a list of discovered operations. Select the operations
that you want to include in the external service then click Next.
6. Select Create a new server and click Finish.
You will configure the server in a later step. An external service
is created.
7 To explore the generated artifacts:
    - To display the business objects that were discovered in the OpenAPI
specification, in the library, click Data .
    - To display an operation with its input and output parameters,
in the library, click Services, then select
the external service that you created.
8 To configure the server:

1. Under Process App Settings click Server.
2. For the server type, select REST Server.
3. For Host name, specify the hostname of
the IBM ODM server.
4. Make sure that Secure server is selected
and that SSL configuration is specified.
5. Select Authentication machanism and specify
values for User name and Password.

## What you do in Business Automation Workflow to use
the IBM ODM decision
service in a service flow

1. Create a service flow.
2. Use a service task to invoke an operation of the external service.
3. For Implementation, specify the external
service.
4. For Operation, select the operation to
use.
5. Specify data mappings as required by the operation.