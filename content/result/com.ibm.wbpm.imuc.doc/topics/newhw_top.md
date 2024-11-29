# Migrating Business Automation Workflow to the
same version on new hardware

You can migrate your IBM® Business Automation Workflow
environment, including applications and running instances, to the same version running on new
hardware. The source and target systems can be running different operating systems. For example, you
can migrate from a Windows system to a Linux system or from a Linux system to a Windows system.

- Moving the deployment environment

To migrate IBM Business Automation Workflow to the same version on new hardware, export the configuration properties from your existing deployment environment, install Business Automation Workflow on the new hardware, and then create the environment using the exported configuration properties files.
- Extracting advanced applications and SIB messages

If you are migrating an Advanced or AdvancedOnly deployment environment, you must extract the advanced Business Automation Workflow applications and service integration bus (SIB) messages from your source environment. For a Standard or Express environment, you can skip this step, but you might want to check if you have persistent messages stored in the SIB tables (see  WebSphere® Application Server data store tables). If you do, you can extract the SIB messages and redeploy them after migration to avoid data loss.
- Dropping the messaging engine tables

If you also want to move your Business Automation Workflow databases, back up and restore them in this step. Even if you are using the existing databases, you must drop the previous service integration bus (SIB) messaging  tables before you start the new deployment environment.
- Deleting the Event Manager instances

If your deployment environment type is not AdvancedOnly, you must delete all Event Manager instances before you start the new deployment environment.
- Deploying advanced applications and SIB messages

If you are migrating an Advanced or AdvancedOnly deployment environment, you must deploy the advanced Business Automation Workflow applications and service integration bus (SIB) messages that you extracted from your source environment. For a Standard or Express environment, if you did not extract any SIB messages, you can skip this step.
- Reconfiguring IBM Business Automation Workflow with an existing external Content Platform Engine or an external IBM Content Navigator

If the external Content Platform Engine or external IBM Content Navigator was configured before migration, you must re-configure them.
- Completing customization

You must complete customization in your new environment to make it consistent with the source environment.