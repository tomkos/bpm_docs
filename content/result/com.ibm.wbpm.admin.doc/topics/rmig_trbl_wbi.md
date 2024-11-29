# BPMConfig -migrate troubleshooting

The BPMConfig -migrate command works correctly if the deployment
environment was created by the Deployment Environment wizard and the name of the deployment
environment is shown in the administrative console under Servers > Deployment Environment.

If the cluster names are shown in the administrative console under Servers > Deployment Environment > deployment\_environment\_name, the command also gets the cluster names; otherwise, it prompts you for them. The
deployment environment information is kept in the wbi-topologies.xml file.

- If you have only one deployment environment, the BPMConfig -migrate command
uses the default deployment environment name De1 and prompts for the cluster names
to export the source deployment environment configuration.
- If there is more than one deployment environment, the BPMConfig -migrate
command does not run.

- If no deployment environments are shown in the administrative console under Servers > Deployment Environment, the BPMConfig -migrate command confirms whether to continue to
export the source configuration. If yes, it uses the provided deployment environment name and asks
for cluster name information to export the source configuration. If no, it does not run.
- If at least one deployment environment is shown in the administrative console under Servers > Deployment Environment, the BPMConfig -migrate command lists the available deployment
environments and prompts you to choose one.

```
2015-11-25 11:05.03.107 com.ibm.bpm.config.export.utils.WBITopologyReader.getAllDesInSourceEnv(): RETURN
2015-11-25 11:05.03.107 com.ibm.bpm.config.export.utils.WBITopologyReader.getAllClusterNamesInSourceEnv(): RETURN All 
of clusters [{null={Messaging=WPS7c\_RGR, Support=WPS7c\_RGR, AppTarget=WPS7c\_RGR}}]
2015-11-25 11:05.03.107 com.ibm.bpm.config.BPMConfig.main(): null
java.lang.NullPointerException
	at com.ibm.bpm.config.export.utils.WBITopologyReader.getClusterNameInSourceEnv(WBITopologyReader.java:101)
	at com.ibm.bpm.config.export.utils.WBITopologyReader.getNodeNamesForClusterUsingCapabilityInSourceEnv(WBITopologyReader.java:146)
	at com.ibm.bpm.config.export.utils.WBITopologyReader.getNodeNamesForApplicationClusterInSourceEnv(WBITopologyReader.java:114)
	at com.ibm.bpm.config.util.tw.LocalTWConfigurationLoader.findDeploymentTargetForMigration(LocalTWConfigurationLoader.java:275)
	at com.ibm.bpm.config.util.tw.LocalTWConfigurationLoader.<init>(LocalTWConfigurationLoader.java:76)
	at com.ibm.bpm.config.util.tw.TWConfigurationFactory.loadLocalConfig(TWConfigurationFactory.java:78)
	at com.ibm.bpm.config.export.helper.LombardiXMLPopulateHelper.populateLombardiXMLProperties(LombardiXMLPopulateHelper.java:86)
	at com.ibm.bpm.config.export.helper.LombardiXMLPopulateHelper.populate(LombardiXMLPopulateHelper.java:69)
	at com.ibm.bpm.config.export.handler.GenericExportConfigHandler.populateLombardiXMLProperties(GenericExportConfigHandler.java:235)
	at com.ibm.bpm.config.export.handler.GenericExportConfigHandler.populateAllSupportedProperties(GenericExportConfigHandler.java:105)
	at com.ibm.bpm.config.export.handler.V80ExportConfigHandler.populateAllSupportedProperties(V80ExportConfigHandler.java:168)
	at com.ibm.bpm.config.BPMConfig$Actions.migrate(BPMConfig.java:4504)
	at com.ibm.bpm.config.cli.MigrateAction.runInner(MigrateAction.java:127)
	at com.ibm.bpm.config.cli.AbstractConfigAction.run(AbstractConfigAction.java:128)
	at com.ibm.bpm.config.cli.MigrateAction.run(MigrateAction.java:34)
	at com.ibm.bpm.config.BPMConfig.main(BPMConfig.java:282)
```

```
ClassNotFoundException: Class 'WBITopology' not found. (file://path\_to\_wbi-topologies.xml, 2,80)
```

1. In the
deployment\_manager\_profile/config/cells/cell\_name
directory, rename the wbi-topologies.xml file to another name.
2. Run the BPMConfig - migrate file without the -de parameter.
When you are prompted, enter the cluster names based on the source environment configuration.
3. After you have successfully run the command, restore the wbi-topologies.xml
file. It is a good idea to keep the copy (under the other name) so you have a backup.