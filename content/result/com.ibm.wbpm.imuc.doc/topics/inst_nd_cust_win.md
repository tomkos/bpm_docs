# Installing IBM Business Automation
Workflow using a custom
installation and configuration path

Use the custom installation option to install IBM Business Automation
Workflow if you need installation or configuration options
that the typical installation option does not provide, if you want to install silently, or if you
want to install the product on an existing installation of WebSphere® Application
Server.

If you want to configure case management to use an external Content Platform Engine, use the BPMConfig command with one
of the property template files from
install\_root/BPM/samples/config/externalcpe. Make sure the
bpm.de.useExternalCPE property is set to true and the DeAdminAlias
and CellAdminAlias users are not in the LDAP user repository, which will be configured later. After
configuring the deployment environment, follow the instructions in Configuring an existing external Content Platform Engine.

If you want to configure case management to use a new external IBM Content
Navigator (with an embedded Content Platform Engine), use the BPMConfig command with
one of the property template files from
install\_root/BPM/samples/config/externalicn. Make sure the
bpm.de.useExternalNavigator property is set to true and the
DeAdminAlias and CellAdminAlias users are not in the LDAP user repository, which will be configured
later. After configuring the deployment environment, follow the instructions in Configuring IBM Business Automation Workflow with an external IBM Content Navigator.

- Installing IBM Business Automation Workflow

With custom installation, you can choose to install IBM Business Automation Workflow interactively or silently.
- Granting write permission of files and directories to nonadministrative users for profile creation or augmentation

If you are not the user who installed the product, you must have write permission to selected directories within the IBM Business Automation Workflow installation. The product installer can grant this permission or create a group with permission to create or augment profiles.
- Configuring profiles and creating a network deployment environment

After you install the product, you must create or augment a deployment manager and one or more managed-node profiles to define the runtime environment. Before starting the deployment manager, you must have configured the databases that are to be used with IBM Business Automation Workflow. For IBM Business Automation Workflow Enterprise Service Bus, you must create an AdvancedOnly deployment environment. PostgreSQL is not supported for Business Automation Workflow Enterprise Service Bus.
- Loading the database with system information in a network deployment environment

When you create a deployment environment, the bootstrapProcessServerData command must be completed successfully before you try to start or use Workflow Server or Workflow Center.