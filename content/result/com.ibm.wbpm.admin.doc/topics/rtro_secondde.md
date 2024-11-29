# Errors when you create second deployment environment

```
[5/20/14 2:29:06:258 EDT] 00000227 DataSourceCon E DSRA8040I: Failed to connect to the DataSource.  Encountered "": java.io.FileNotFoundException: /opt/bpm85/WebSphere/AppServer/profiles/Node1Profile/config/cells/PSCell1/clusters/WPSDE3.AppCluster/resources.xml (No such file or directory)
```

```
[5/20/14 2:28:50:333 EDT] 0000040c AppBinaryProc I ADMA7021I: Distribution of application BSpaceHelp\_WPSDE3.AppCluster completed successfully. [5/20/14 2:29:01:998 EDT] 000003b2 FfdcProvider  W com.ibm.ws.ffdc.impl.FfdcProvider logIncident FFDC1003I: FFDC Incident emitted on /opt/bpm85/WebSphere/AppServer/profiles/DmgrProfile/logs/ffdc/dmgr\_f1d486d1\_14.05.20\_02.29.01.9963874838721197826278.txt 
com.ibm.wps.hm.rest.system.ApplicationHealthParameter.getClusterMember 432
[5/20/14 2:29:08:786 EDT] 00000523 FfdcProvider  W com.ibm.ws.ffdc.impl.FfdcProvider logIncident FFDC1003I: FFDC Incident emitted on /opt/bpm85/WebSphere/AppServer/profiles/DmgrProfile/logs/ffdc/dmgr\_3eea2fb2\_14.05.20\_02.29.08.7854652312342454021904.txt com.ibm.wps.hm.rest.system.DataSourceHealthParameter.updateDataSourceStatus 353
[5/20/14 2:29:10:317 EDT] 00000502 MultiSyncMana A  ADMS0207I: Node Synchronization state for node: Node2 - initiate time: 2014.05.20 at 02:27:07:778 EDT
result: In Progress
Update occurred
```