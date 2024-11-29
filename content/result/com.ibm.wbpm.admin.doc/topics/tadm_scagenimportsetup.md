<!-- image -->

# Setting up connectivity for the Generic JMS binding

## Before you begin

## About this task

The application in this
scenario contains a mediation component connection to other applications at both ends by means of
the Generic JMS binding; the application contains an interface with a single two-way
operation.

## Procedure

1. Configure your third-party JMS provider to create a queue manager, queues, and JMS connection
factories and destinations using the provider-specific tools.
2. In Workflow Server, you must define a generic
messaging provider.
3 In Integration Designer , you must perform the followingtasks:
    1. Add an import and export to the application and connect them to a previously-implemented
mediation component.
    2. Add a Generic JMS binding to both the export and the import: Generate binding > Messaging binding > Generate JMS binding .
    3. Set the genericMessagingProviderName property on both the import and export to match the
properties previously defined to Workflow Server.
    4. Set the ExternalJNDIName for the connections and send/receive destinations
to match those defined in your third-party JMS provider tools.
4. Deploy the application to a single server.

Make sure that the third-party JMS provider queue manager is running and available for connection
and that the context to which the generic messaging provider definition points in Workflow Server is available. 
You can build and deploy your application using Integration Designer. Another way to deploy applications is to export
the modules as .zip files and then use the serviceDeploy command of Workflow Server to build and deploy them as EAR files.
5. Start the application.
6. Run the application.

## Results

Similarly, the application will issue requests to
the Generic JMS import send destination and expect responses on the Generic JMS
import receive destination.