# Configuring the production environment for case management

## Before you begin

Be sure to have your completed configuration checklist available.

## About this task

Configuring the production environment prepares Case Builder and Case Client for use. You use the IBM® Business Automation
Workflow
Case configuration tool to create a
profile, which is a collection of configuration and deployment tasks. When you provide the required
values for the tasks and run the tasks, you configure all the required settings and deployments for
your production environment.

1. Preparing to run the case configuration tasks for the production environment

Use the case production environment profile created by the BPMConfig command when you run the tasks in the Case configuration tool.
2. Running the Case configuration tool tasks for the production environment

After you saved the edited profile, run the Case configuration tool tasks for the production environment.
3. Configuring production target object store indexes

Your database administrator must create a four-part composite index for each production target object store that is used for case management. That database retrieval index is required for efficiently retrieving the case history in the Event table in target object stores.
4. Configuring email notification

You can optionally enable email notification of workflow activity. Users can configure which notifications they want to receive and their preferred locale. For example, users can choose to be notified when work is assigned or when work is approaching or passes a deadline. Configure email notification on the workflow server, in IBM Content Navigator, and in the Case Client.
5. Verifying the IBM Business Automation Workflow applications in the production environment

After you configure your environment and deploy the applications, you can start and verify the IBM Business Automation Workflow applications in the production environment.
6. Configuring authentication to deploy to a production environment

To install case solutions directly from IBM Workflow Center to IBM Workflow Server, you must give permissions to the user who is associated with the ECM Technical User (EmbeddedECMTechnicalUser) role, see Business Automation Workflow security roles.