# Optional: Deploying IBM Business Automation
Workflow in CP4BA

## Before you begin

## Procedure

1 Prepare for Business Automation Workflow and add it toCloud Pak for Business Automation deployment.
    1 Prepare the capabilities of Business Automation Workflow , Application Engine , and Business Automation Navigator .

Prepare the capabilities of Business Automation Workflow, Application Engine, and Business Automation Navigator.

        1. For Business Automation Workflow,
complete the tasks in Preparing to install Business Automation Workflow Runtime and
Workstream Services.
        2. For Content Platform Engine,
complete the steps in Preparing to install FileNet Content Manager.
        3. For Business Automation Navigator,
complete the steps in Preparing to install Business Automation Navigator.
2 Prepare the custom resource (CR).
    1. Create a copy of the custom resource that you created in 'Deploying required Cloud Pak for Business Automation components' in Installing a CP4BA Process Federation Server deployment.
    2. Get the CR pattern templates from Custom resource pattern templates.
3 Add Business Automation Workflow toCloud Pak for Business Automation customresource.Refer to the custom resource pattern templates in Step b.ii. to add the following sections:

Refer to the custom resource pattern templates in Step b.ii. to add the following sections:

- datasource\_configuration
- baw\_configuration
- ecm\_configuration
- navigator\_configuration
- initialize\_configuration
4 Update the shared\_configuration section.

1. Add the following attributes:# The encryption key created by the PFS deployment
       encryption\_key\_secret: "<Required>"
       sc\_deployment\_baw\_license: "production"
       sc\_deployment\_fncm\_license: "production"
       sc\_deployment\_patterns: workflow
2. Modify encryption\_key\_secret to use the same secret as Process Federation Server. The Process Federation Server CR deploys the
secret. The name is in format  <PFS\_CR\_name>-encryption-key.
3. IBM Business Automation
Workflow on containers
requires IBM Content Management
Interoperability Services for Content Manager (CMIS)
to integrate with Content Platform Engine. Add CMIS to  sc\_optional\_components. For example, the parameter might look
similar to: sc\_optional\_components: elasticsearch, cmis
2. Apply your custom resource.
3 Complete the post-deployment tasks by following the instructions in Completing post-installation tasks . If Business Automation Workflow is deployed and postinstallation tasks are complete, skip this step.

1. Complete the steps in Completing post-installation tasks for Business Automation Workflow Authoring, Runtime,
and Workstream Services.
2. Complete the steps in Completing post-installation tasks for FileNet Content
Manager.
3. Complete the steps in Completing post-installation tasks for Business Automation
Navigator.