<!-- image -->

# Administering IBM Business Automation
Workflow tasks

## Before you begin

## About this task

- For general information on providing clients with a description
of a web service, see Making deployed web services applications
available to clients.
- For information on the PEPartnerLink item attribute, which is
used to specify the endpoint address in FileNet® P8, see Deployment configuration
formats in the FileNet P8 documentation.

- Security considerations for integrating BPEL processes with IBM Business Automation Workflow tasks

If you select Use security to access the web service from the case management task when you create the web service module in Integration Designer, user name and password credentials are supplied when a IBM Business Automation Workflow task invokes a web service module on Workflow Server. You can optionally select Use a secure socket (SSL) connection to provide an additional level of security for the request from IBM Business Automation Workflow to IBM Business Automation Workflow.
- Policy sets and binding considerations for IBM Business Automation Workflow tasks

If you select Use security to access the web service from the case management task when you create the web service module in Integration Designer, a default policy set is applied to the export. If you select a long-running BPEL process, a default policy set is applied to both the export and import.