# Optional:
Configuring the Content Services toolkit

## Before you begin

- GraphQL must be installed on WebSphere Application
Server 9.x. It can be installed
with Content Platform Engine server, if
the server is WebSphere Application
Server
9.
- If the Content Platform Engine server
is WebSphere Application
Server 8.5.5.x,
GraphQL can be installed on a separate WebSphere Application
Server 9.x . In addition, GraphQL
must work with an external Content Platform Engine server (it cannot work
with the Business Automation Workflow
embedded Content Platform Engine).

## Procedure

1 You can configure the single sign-on between Business Automation Workflow and GraphQL WebSphere ApplicationServer , and GraphQL WebSphere ApplicationServer and Content Platform Engine server. For detailedsteps, see Deploy Content Services GraphQL API into a traditional WebSphereApplication Server environment . The limitations are:
    - Content service GraphQL must be installed on WebSphere Application
Server 9.x.
    - To use the Content Services toolkit view, an external Content Platform Engine server must be used
(embedded Content Platform Engine is not
supported).
    - Since the SSL needs to be configured between Business Automation Workflow and GraphQL server, the
WebSphere Application
Server federated
repository must be configured for GraphQL. This requirement is the same for external Content Platform Engine, see the note in Configuring single sign-on with LTPA for an external Content Platform
Engine
2. Run the setBPMExternalECM command or updateBPMExternalECM command to set GraphQL endpoint with the -GraphqlEndpoint
content\_services\_graphql\_endpoint parameter.