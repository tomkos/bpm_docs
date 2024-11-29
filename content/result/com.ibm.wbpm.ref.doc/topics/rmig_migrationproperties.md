# Sample migration.properties files

- If you installed the new version of the product on the same computer as the source environment,
the sample file is install\_root\_24.x/util/migration/resources/migration.properties.
- If you installed the new version of the product on a different
computer and copied the migration files to the source environment,
the sample file is remote\_migration\_utility/util/migration/resources/migration.properties.

The following samples show the information that you might
add to the migration.properties file.

- Sample file for the source environment
- Sample file for the target environment

## Sample file for the source environment

The
following sample shows a source\_migration.properties file.

```
#------------------------------------------------------------------------------------------------------------------------------------
# General instructions for migration properties file:
#   You must edit the properties in this file before you run any migration commands.
#   Each deployment environment requires its own migration.properties file. Make a copy of this file for each deployment environment.
#
# Usage: 
# 1. Before you run the following commands, edit this properties file to point to the source environment,
# including admin.username, admin.password, bpm.home, profile.name. If the source is a network deployment environment
# you also need to edit source.*.cluster.name.
#   --BPMManageApplications (If you want to manage applications on the source environment)
#   --BPMExtractSourceInformation
#	
# 2. Before you run the following commands, edit this properties file to point to the target environment,
# including admin.username, admin.password, bpm.home, profile.name, target.config.property.file
#   --DBUpgrade
#   --BPMManageApplications (If you want to manage applications on the target environment)
#   --BPMMigrate
#   
###############################################################################################
#                              Details for each property
###############################################################################################
# admin.username: 
#       (Required) The user who is authorized to connect to the deployment manager server or stand-alone server through a SOAP connection		
# admin.password:
#       (Required) The password of the user who connects to the deployment manager server or stand-alone server through a SOAP connection
# bpm.home:
#       (Required) The installation root of the BPM product. Make sure the file separators are  / (as in C:/BPM)
#       For WebSphere Lombardi Editions V7.1 or V7.2, specify <WLE\_Install\_Dir>/AppServer
#       Note: You must use the full path. The tilde character "~" which stands for the user's home cannot be used.
#		Example:
#			Windows: bpm.home=c:/IBM/BPM
#			Linux/UNIX: bpm.home=/opt/IBM/BPM
# profile.name:
#       (Required) The name of the deployment manager profile in a network deployment environment or the name
#       of the stand-alone profile in a stand-alone environment
# source.application.cluster.name
# source.support.cluster.name
# source.messaging.cluster.name
# source.web.cluster.name
#       (Required if the source is a network deployment environment of IBM BPM Advanced or Standard or WPS 7.x/6.2.x) The cluster name of each type
#       Edit these names on both source and target environments if you want to keep the mapping between source and target clusters
# target.config.property.file
#       (Required for target environment) The full path of the configuration properties file that you used to create your target environment
#		Example:
#			Windows: target.config.property.file=c:/config.properties
#			Linux/UNIX: target.config.property.file=/opt/config.properties
# use.default.virtual.host
#        (Optional) For Advanced or AdvancedOnly deployment environments: If the value is false or not set, the virtual host values of web applications 
#        are not changed during migration and are the same in the target environment as they were in the source environment. If you set the value to 
#        true, the virtual host values in the source are updated to "default\_host".
#        Available values: false, true
# skip.steps.list:
#       (Optional) This property is only for debugging. It can skip some of the following migration steps:
#           snapshot.message, snapshot.application, snapshot.adapter
#           migrate.scheduler, migrate.message, migrate.application, migrate.adapter
#       Usage example: skip.steps.list=snapshot.message,migrate.message
#------------------------------------------------------------------------------------------------------------------------------------
admin.username=bpmadmin
admin.password=bpmpassw0rd

bpm.home=/opt/BPM/WebSphere/AppServer
profile.name=Dmgr01

#Enter these properties when you are working on the source or target environment
source.application.cluster.name=MyTopPC80.AppTarget
source.messaging.cluster.name=MyTopPC80.Messaging
source.support.cluster.name=MyTopPC80.Support
source.web.cluster.name=MyTopPC80.WebApp
#Enter these properties when you are working on the target environment
target.config.property.file=

#Whether to use default\_host as virtual host for migrated web applications
use.default.virtual.host=false
#(Optional) For debugging
skip.steps.list=
```

## Sample file for the target environment

The
following sample shows a target\_migration.properties file.

```
#------------------------------------------------------------------------------------------------------------------------------------
# General instructions for migration properties file:
#   You must edit the properties in this file before you run any migration commands.
#   Each deployment environment requires its own migration.properties file. Make a copy of this file for each deployment environment.
#
# Usage: 
# 1. Before you run the following commands, edit this properties file to point to the source environment,
# including admin.username, admin.password, bpm.home, profile.name. If the source is a network deployment environment
# you also need to edit source.*.cluster.name.
#   --BPMManageApplications (If you want to manage applications on the source environment)
#   --BPMExtractSourceInformation
#	
# 2. Before you run the following commands, edit this properties file to point to the target environment,
# including admin.username, admin.password, bpm.home, profile.name, target.config.property.file
#   --DBUpgrade
#   --BPMManageApplications (If you want to manage applications on the target environment)
#   --BPMMigrate
#   
###############################################################################################
#                              Details for each property
###############################################################################################
# admin.username: 
#       (Required) The user who is authorized to connect to the deployment manager server or stand-alone server through a SOAP connection		
# admin.password:
#       (Required) The password of the user who connects to the deployment manager server or stand-alone server through a SOAP connection
# bpm.home:
#       (Required) The installation root of the BPM product. Make sure the file separators are  / (as in C:/BPM)
#       For WebSphere Lombardi Editions V7.1 or V7.2, specify <WLE\_Install\_Dir>/AppServer
#       Note: You must use the full path. The tilde character "~" which stands for the user's home cannot be used.
#		Example:
#			Windows: bpm.home=c:/IBM/BPM
#			Linux/UNIX: bpm.home=/opt/IBM/BPM
# profile.name:
#       (Required) The name of the deployment manager profile in a network deployment environment or the name
#       of the stand-alone profile in a stand-alone environment
# source.application.cluster.name
# source.support.cluster.name
# source.messaging.cluster.name
# source.web.cluster.name
#       (Required if the source is a network deployment environment of IBM BPM Advanced or Standard or WPS 7.x/6.2.x) The cluster name of each type
#       Edit these names on both source and target environments if you want to keep the mapping between source and target clusters
# target.config.property.file
#       (Required for target environment) The full path of the configuration properties file that you used to create your target environment
#		Example:
#			Windows: target.config.property.file=c:/config.properties
#			Linux/UNIX: target.config.property.file=/opt/config.properties
# use.default.virtual.host
#        (Optional) For Advanced or AdvancedOnly deployment environments: If the value is false or not set, the virtual host values of web applications 
#        are not changed during migration and are the same in the target environment as they were in the source environment. If you set the value to 
#        true, the virtual host values in the source are updated to "default\_host".
#        Available values: false, true
# skip.steps.list:
#       (Optional) This property is only for debugging. It can skip some of the following migration steps:
#           snapshot.message, snapshot.application, snapshot.adapter
#           migrate.scheduler, migrate.message, migrate.application, migrate.adapter
#       Usage example: skip.steps.list=snapshot.message,migrate.message
#------------------------------------------------------------------------------------------------------------------------------------
admin.username=bpmadmin
admin.password=bpmpassw0rd

bpm.home=/opt/BPM850/WebSphere/AppServer
profile.name=Dmgr01

#Enter these properties when you are working on the source or target environment
source.application.cluster.name=MyTopPC80.AppTarget
source.messaging.cluster.name=MyTopPC80.Messaging
source.support.cluster.name=MyTopPC80.Support
source.web.cluster.name=MyTopPC80.WebApp
#Enter these properties when you are working on the target environment
target.config.property.file=/opt/config85/Advanced-PC-ThreeClusters-Oracle.properties

#Whether to use default\_host as virtual host for migrated web applications
use.default.virtual.host=false
#(Optional) For debugging
skip.steps.list=
```