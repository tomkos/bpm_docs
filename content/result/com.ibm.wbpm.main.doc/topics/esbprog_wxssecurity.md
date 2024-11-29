<!-- image -->

# WebSphere eXtreme
Scale security aspects

If you are using a distributed environment, you can encrypt your eXtreme Scale communication using SSL.

If your WXSDefinition has security enabled , the WebSphere eXtreme
Scale mediation primitives automatically use the WebSphere Application
Server Common Secure Interoperability Protocol Version 2
(CSIV2) settings defined in the WebSphere Application
Server global
security settings. The eXtreme Scale catalog server manages SSL
separately and cannot be managed by the CSIV2 settings.

## IBM Business Automation Workflow Server Configuration

In the WebSphere eXtreme
Scale definition ensure security is
enabled. This will ensure the existing CSIV2 configuration is used.

## Catalog Server and Container Server Configuration

If your container server is running in a WebSphere Application
Server environment then the CSIV2 settings will be used.
However, if your container server is a stand-alone server then SSL must be enabled and configured
along with the catalog server.

## Key Store and Trust Store Configuration

If your catalog server is remote to the IBM Business Automation Workflow server then the local key store and trust
store must be configured with the certificates required to authenticate with the IBM Business Automation Workflow server. In the stand-alone container server
you must also define a key store and trust store, which then authenticate with the catalog
server.

Full details about how to enable security on WebSphere eXtreme
Scale can be found in the WebSphere eXtreme
Scale documentation.