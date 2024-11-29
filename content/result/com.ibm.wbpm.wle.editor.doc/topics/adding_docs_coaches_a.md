# Choosing the type of documents to attach to a heritage coach (deprecated)

## Before you begin

The Document Attachment control works with IBM® Business Automation Workflow documents
or documents stored in an Enterprise Content Management (ECM) repository. Business Automation Workflow documents
are any documents that your users can access by browsing their file
system or via a URL. To use the Document Attachment control to access
documents from an ECM repository, you can configure the control to
work with IBM Content Integrator
Enterprise Edition, enabling users to access documents from FileNet® P8 Content Manager and IBM Content Manager.

Before
you can access documents from an ECM repository using the Document
Attachment control, IBM Content
Integrator SOA web services must be deployed on an application server.
The IBM Content Integrator Information
Center provides information about the WAR file that you can use for
deployment and instructions for configuring the WAR file. See Deploying > Deploying SOA Web Services in the IBM Content
Integrator documentation.

## Procedure

The following steps describe how to establish which type
of documents you want to display and upload using the Document Attachment
control:

1. Open the service that contains the heritage coach that you want to work with, and then click
the Coaches tab.
2. Drag a Document Attachment control from the palette onto
the design area.
3. While the Document Attachment control is selected, click
the Document Attachment option in the properties if not already selected.
4 In the Behavior section, select a ConnectionType from the drop-down list:
    - Business Automation Workflow documents
    - IBM Content Integrator
5 If you selected IBM Content Integrator forthe Connection Type , complete the followingsteps:

1. Click the Connection option in the properties.
2. Provide the following information:  
Table 1. Input required for connection properties

Property
Description

IBM Content
Integrator (ICI) Web Service URL
Select the environment variable
that contains the root URL of the deployed application (SOA web services).
The name of this environment variable is the name of the target IBM Content Integrator server configuration.
See Adding a server configuration for information on defining
an IBM Content Integrator server
configuration. 

Repository ID
Select the environment variable
that contains the name of the IBM Content
Integrator connector that you want to use to access the ECM repository.
The name of this environment variable is the name of the target IBM Content Integrator server configuration
with a \_connectorName suffix. For example, if your
server configuration is named iciService, the connector
name will be contained in an environment variable named iciService\_connectorName.
See Adding a server configuration for information on defining
an IBM Content Integrator server
configuration. 

User name
User name required to log in to the
ECM repository.

Password
Password required to log in to ECM
repository.

## What to do next

Configure the control to display and upload documents for your connection type. By configuring
the control, you can attach documents to the heritage coach for which you configured the connection
type.