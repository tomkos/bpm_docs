# Overview: Integrating external services

The following sections describe some possible external service
integrations.

## REST services

- Invoking a REST service
- Invoking a REST service by using JavaScript

## Web services

For information about discovering and invoking web services from workflows, see Invoking a web service.

## IBM Operational Decision
Manager business
rules

For more information about using Operational Decision Manager business
rules and decision services, see Using IBM ODM business rules.

## IBM Watson services

Watson
provides artificial intelligence (AI) services that you can integrate in your process applications
by using the Workflow REST service integration capabilities. For information about the services that
are available, see Watson Documentation.

## IBM Cloud services

Requests to IBM® Cloud
services must be authenticated. Some
service instances, require that you authenticate to the API by using IBM Cloud Identity and Access
Management (IAM) tokens. You can pass a bearer token in an Authorization header or
an API key.

Tokens support authenticated requests without embedding service credentials in every call.

API keys use basic authentication. If you pass in an API key, specify the string
apikey for the user name and the value of the API key as the password.

- For information about the IAM Identity Services API and to download the OpenAPI definition, see
IAM
Identity Services API.
- For information about using a Watson service API key to get an IAM token, see Generating an IBM Cloud IAM token by using an API key.

## Blockchain and Hyperledger Composer services

- For a tutorial that explains how to make your business processes react to blockchain events, see
the developerWorks article Enable business processes to react to blockchain events.
- For information about using Hyperledger Composer, see Build Blockchain applications and business networks
your way.

## IBM App
Connect

You can use IBM App
Connect to integrate data,
apps and APIs across hybrid cloud environments. This allows connectivity with services such as
Salesforce, Marketo, Google sheets, Google Drive, and Dropbox. The integration with IBM App Connect
supports both outbound invocations and event-driven inbound invocations from and to your process
applications. To learn more about using IBM App
Connect, see IBM App
Connect.

The following figure illustrates how IBM App
Connect can be used to
integrate common app services with process apps that are running on prem or on cloud.

<!-- image -->

- To prepare an external service integration, go to your IBM App
Connect dashboard,
download the OpenAPI specification for the REST service that you want to use as an external service
in a workflow. Also, note the IBM App
Connect username and
password that is needed to invoke the service.
- To invoke an API that is provided by your IBM App Connect instance from a process application,
use the to create a new external service based on the OpenAPI specification that you downloaded from
IBM App
Connect, and
enter the IBM App
Connect
username and password on the settings tab for the appropriate REST server.

- To invoke a Workflow API from an IBM App
Connect event-driven flow,
specify the application event that will trigger the Workflow API call, for example, the Google
Sheets new spreadsheet event, add an HTTP invoke method, and specify the Workflow REST API call,
including basic authorization HTTP header. For more information about using Workflow APIs to start a
process, see Starting a process by using a REST API call.
- For a general tutorial that shows how to call out from App Connect to any HTTP endpoint, see
Calling out to an API endpoint by using the invoke method for the
HTTP application.