# Installation and profile creation log files

Table 1 shows the log file names, locations,
and descriptions for success and failure for IBM Business Automation Workflow.

Some
directory paths, file names, and indicator values in Table 1 contain
spaces to allow the entries to fit in the table cells. The actual
directory paths, file names, and indicator values do not contain spaces.

The
variable install\_root represents the installation
directory of IBM Business Automation Workflow. The
variable profile\_root represents the root location
of a profile.

For more information see Installation directories for the product and profiles.

| Log name and location                                                                                                                                                                       | Log description                                                                                                                                                                                                                                                                                   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Agent data location/logsTypically: C:\Documents and Settings\All Users\Application Data\IBM\Installation Manager\logs Agent data location/logs Typically: /var/ibm/InstallationManager/logs | Installation Manager log file directory under the Agent data location. For more information on the Agent data location refer to the Installation Manager documentation. Contains log information for Business Process Manager and WebSphere Application Server installations and uninstallations. |
| install\_root/logs/wbi/install/installconfig\_server.log  install\_root\logs\wbi\install\installconfig\_server.log                                                                              | Logs configuration actions that run at the end of the installation process to configure components, install system applications, and create Windows shortcuts and registry entries.                                                                                                               |
| install\_root/logs/manageprofiles/pmt.log  install\_root\logs\manageprofiles\pmt.log                                                                                                          | Logs all events from the Profile Management Tool.                                                                                                                                                                                                                                                 |
| install\_root/logs/manageprofiles/profile\_name\_create.log  install\_root\logs\manageprofiles\profile\_name\_create.log                                                                          | Traces all events that occur during the creation of the named profile. Created when a profile is created during a typical installation, custom installation (only Advanced PS), when using the Profile Management Tool, or when using the manageprofiles command-line utility.                    |
| install\_root/logs/manageprofiles/profile\_name\_augment.log  install\_root\logs\manageprofiles\profile\_name\_augment.log                                                                        | Traces all events that occur during the augmentation of the named profile. Created when a profile is augmented, when using the Profile Management Tool, or when using the manageprofiles command-line utility.                                                                                    |
| install\_root/logs/manageprofiles/profile\_name\_delete.log  install\_root\logs\manageprofiles\profile\_name\_delete.log                                                                          | Traces all events that occur during the deletion of the named profile. Created when profile deletion is performed with the manageprofiles command-line utility.                                                                                                                                   |
| install\_root/logs/wbi/uninstall/uninstallconfig\_server.log  install\_root\logs\wbi\uninstall\uninstallconfig\_server.log                                                                      | Logs all configuration actions that run during uninstallation events relating to IBM Business Process Manager.                                                                                                                                                                                    |