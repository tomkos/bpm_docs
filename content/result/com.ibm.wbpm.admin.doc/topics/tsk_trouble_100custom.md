# Troubleshooting 100Custom configuration

## About this task

- TeamWorksConfiguration.running.xml is the teamworks configuration settings,
combining system defaults and custom settings.
- TeamWorksConfiguration.system.xml is the teamworks default configuration
settings and does not include custom settings.

```
<!-- @@appended use-portal-for-preview from C:\BAWProfiles\BAW\WC1CNode1Profile\config\cells\WC1CCell\nodes\WC1CNode1\servers\WC1CSingleClusterMember1\process-center\config\system\99Local.xml -->
```

## Procedure

1 Run the following command to generate theTeamworksConfiguration.running.xml andTeamWorksConfiguration.system.xml files in the specified output directory. INSTALL\_ROOT/bin/BPMConfig -validate -profile <Dmgr\_profile\_name> -outputDir <outputDir> TheTeamworksConfiguration.running.xml andTeamWorksConfiguration.system.xml files are generated for each server, and alsoat the cluster level for both Workflow Center and Performance Data Warehouse . Forexample, for a single cluster with one member, the following files are generated:

```
INSTALL\_ROOT/bin/BPMConfig -validate -profile <Dmgr\_profile\_name> -outputDir <outputDir>
```

    - outputDir\cells\PCCell1\clusters\SingleCluster\performance-data-warehouse\TeamWorksConfiguration.running.xml
    - outputDir\cells\PCCell1\clusters\SingleCluster\performance-data-warehouse\TeamWorksConfiguration.system.xml
    - outputDir\cells\PCCell1\clusters\SingleCluster\process-center\TeamWorksConfiguration.running.xml
    - outputDir\cells\PCCell1\clusters\SingleCluster\process-center\TeamWorksConfiguration.system.xml
    - outputDir\cells\PCCell1\nodes\Node1\servers\SingleClusterMember1\performance-data-warehouse\TeamWorksConfiguration.running.xml
    - outputDir\cells\PCCell1\nodes\Node1\servers\SingleClusterMember1\performance-data-warehouse\TeamWorksConfiguration.system.xml
    - outputDir\cells\PCCell1\nodes\Node1\servers\SingleClusterMember1\process-center\TeamWorksConfiguration.running.xml
    - outputDir\cells\PCCell1\nodes\Node1\servers\SingleClusterMember1\process-center\TeamWorksConfiguration.system.xml
2. You can compare the TeamworksConfiguration.running.xml and
TeamWorksConfiguration.system.xml with a comparison editor or the comparison
command. The difference between them should be the custom setting in
1xxCustom.xml.