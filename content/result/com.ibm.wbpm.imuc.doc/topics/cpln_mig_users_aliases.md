# Default users and authentication aliases removed from IBM Business Automation Workflow

IBM Business Automation
Workflow uses role-based user
assignments to access interfaces, process applications, and toolkits. Based on this change, the
default users from previous products have been removed. In addition, many of the authentication
aliases have been removed. Before you migrate, check the list of default users and authentication
aliases that have been removed.

If
your applications are using aliases that have been removed, you must
re-create them manually in the target environment after migration.
If your applications are using users that have been removed, you must
assign the required security roles to them again after migration.

## Default users removed from IBM Business Automation Workflow

- bpmadmin
- bpmAuthor
- tw\_admin
- tw\_author
- tw\_portal\_admin
- tw\_runtime\_server
- tw\_user
- tw\_webservice

## Authentication aliases removed from IBM Business Automation Workflow

- Bspace\_Auth\_Alias
- WPSDB\_Auth\_Alias
- WPSDB\_Auth\_Alias\_XAR
- SCA\_Auth\_Alias
- BPC\_Auth\_Alias
- BPMPrimaryAdmin\_Auth\_Alias
- BPMAdmin\_Auth\_Alias
- BPMAuthor\_Auth\_Alias
- BPMUser\_Auth\_Alias
- BPMWebservice\_Auth\_Alias
- RALSecurity\_Auth\_Alias
- processdblogon
- processdblogon\_XAR
- performancedblogon
- performancedblogon\_XAR
- PROCSVR\_Auth\_Alias
- PERFDW\_Auth\_Alias