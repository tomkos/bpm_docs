# Converting integration services with web service
integrations

## Before you begin

## About this task

- An equivalent service flow that contains a service task that corresponds to the web service
integration component.
- An external service with a binding to the web service server that contains the configuration
information required to access the web service. The external service includes port types and
operations that correspond to the WSDL definition of the web service, and the service task is
configured to invoke the appropriate external service operation. During conversion, if an external
service exists with the same URL and port type, it is used and a new one is not created. If
required, operations are added to the existing external service.
- The conversion process requires access to the server that hosts the web service. If the server
cannot be accessed during conversion, a placeholder service task is created. You can revert to the
latest snapshot and fix the error in the web service server and convert your integration service
again.
- Inline WSDL configuration is not supported in Process Designer . Web service integration tasks that usethe discovery scheme Provide inline configuration are converted toplaceholder service tasks because no equivalent function is available in the Process Designer . You must remodel the service taskmanually using a web service server, in the following way:How to remodel the service task using a web service server:
    1 Using the desktop Process Designer , go to theProcess App Settings .
        1. Create a web services server.
        2. Enter the WSDL URL of your web service and click Discover.
2 In the integration service editor change the web service integration activity
    1. On the Implementation tab, for the discovery scheme, select
From Process Application settings.
    2. Under Process Application Selection, use the Web
Service drop down to select the newly created Web Services server.
    3. Under Operations, make sure that the desired operation is still
selected.
    4. Inspect the Data Mapping tab to ensure that the mapping is still correct.
3. Save the changes.
4. Using the web Process Designer, perform the
following procedure to convert the integration service into a service flow.

## Procedure

To convert an integration service that contains a web service integration
component:

1. Open the process app or toolkit.
2. Open the Process App Settings or Toolkit Settings
editor.
3. In the Service Conversion tab, select the integration services that you
want to convert and click Convert.
4 Click Convert . The following artifacts are created:
    - A service flow with the same name as the integration service.
    - The service flow contains a task that has the same name as the web service integration
component.
    - An external service with a name based on the service that is configured in the web service
integration component.