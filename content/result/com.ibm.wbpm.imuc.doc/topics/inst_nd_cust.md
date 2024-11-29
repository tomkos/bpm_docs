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