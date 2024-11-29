# Deploying advanced applications
and SIB messages

## Procedure

To deploy the
advanced applications and SIB messages
and re-create the scheduler tasks, complete the following steps in
the target environment:

1. Update the target\_install\_root/util/migration/resources/migration.properties file
to point to your target environment. Update the following
properties:admin.username=admin
admin.password=admin

bpm.home=E:/bpm
profile.name=DmgrProfile

source.application.cluster.name=
source.support.cluster.name=
source.messaging.cluster.name=
# Use the properties file that you used to create the deployment environment
target.config.property.file=
2. Run
the BPMManageApplications command
to disable the automatic starting of your applications and schedulers.
 install\_root/bin/BPMManageApplications -autoStart false -target -propertiesFile source\_migration\_properties\_file
3. Start the target environment, including servers, nodes, and the deployment manager.
4. Add a deployment\_environment\_name.DBUpgrade.success
file in the deployment\_manager\_profile/logs folder to skip
the check for database upgrading that is part of the BPMMigrate command.
5 Run the BPMMigrate command to deploy applications, import SIBmessages, and re-create scheduler tasks. BPMMigrate -backupFolder folder\_path -propertiesFile migration\_properties\_file Ifthe BPMMigrate command runs out of memory, increase the Java heap size. You can increase the heap size to more than 512 if you have more memory on your system.

```
BPMMigrate -backupFolder folder\_path  -propertiesFile migration\_properties\_file
```

    - Edit install\_root/bin/wsadmin.sh.
Find PERF\_JVM\_OPTIONS and increase the value of -Xmx256m to
-Xmx512m.
    - Edit install\_root\bin\wsadmin.bat.
Find PERFJAVAOPTION and increase the value of -Xmx256m to
-Xmx512m.
6. Run the BPMManageApplications command
again to enable the autostart of applications and scheduler daemons.
 BPMManageApplications -autoStart true -target -propertiesFile migration\_properties\_file
7. Restart the servers.