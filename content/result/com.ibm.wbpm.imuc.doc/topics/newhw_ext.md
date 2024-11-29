# Extracting advanced applications
and SIB messages

## Before you begin

## Procedure

To extract the advanced applications
and SIB messages,
complete the following steps in the source environment:

1. Update the
source\_install\_root/util/migration/resources/migration.properties
file to point to your source environment. Update the following
properties:admin.username=admin
admin.password=admin

bpm.home=E:/bpm8560
profile.name=DmgrProfile

source.application.cluster.name=
source.support.cluster.name=
source.messaging.cluster.name=Note: If the target deployment environment secure socket layer (SSL)
setting has a custom configuration, then you must rename the existing
target\_environment\_directory/util/migration/resources/ssl.client.props
file, and copy the ssl.client.props file from the
target\_dmgr\_profile/properties/ directory into the
target\_environment\_directory/util/migration/resources/
directory.
2. Run the BPMManageApplications command
to disable the automatic starting of your applications and schedulers.
 install\_root/bin/BPMManageApplications -autoStart false -source -propertiesFile source\_migration\_properties\_file
3. Restart your source environment, including servers,
nodes,
and the deployment manager.
4. Run the BPMExtractSourceInformation command
to extract the advanced applications and SIB messages and create a
snapshot in the folder that you specify.  BPMExtractSourceInformation -backupFolder folder\_path  -propertiesFile migration\_properties\_file
5. Stop your source environment.