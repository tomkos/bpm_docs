# Using process instrumentation data for cache tuning

In the Server Admin area of the Process Admin
Console, you can select Monitoring > Instrumentation to
display process instrumentation data in the Instrumentation monitor.
If the displayed data indicates an unexpectedly high number of cache
misses for the cache settings, you might be able to edit the 100Custom.xml files
and override the problematic default values of the cache settings;
however, not all caches are configurable. The persistent object (PO)
factory cache settings and repository cache settings are reflected
in the PO Factory and Repository sections
of the Instrumentation monitor. In some situations, you might need
to override the default values for the cache settings with new values.

For more information about using the Instrumentation monitor to display or log process
instrumentation data, see the topic Capturing process instrumentation data. For information about cache and cache-related settings that are not reflected in the
Instrumentation monitor, see the topic Cache and cache-related settings.

## Unconfigurable caches

- ContextAndTypeTreeElements
- ContextTreeElements
- Dependency
- ManagedAssets
- ProjectDependency
- SOAPConnector.XMLTypeDescriptors
- UUIDListKey
- Version Details
- VersionSummaryId
- WebAPIUserID
- XMLTypeDescriptorContextContextAndTypeTreeElements

## PO factory cache settings and repository cache settings

For
both PO factory cache settings and repository cache settings, a cache
hit rate of 90% is considered to be quite satisfactory. However, cache
misses higher than 50% require some investigation. To improve the
ratio of cache hits to cache misses, you can specify new values for
the cache settings in the 100Custom.xml files.
The new values will override the existing default values for the cache
settings that are typically located in other XML configuration files,
such as the 00Static.xml files. Generally, cache
setting modification is an iterative task.

For
information about the use and location of the 100Custom.xml files
and the associated XML configuration files, see the topic The 100Custom.xml file and configuration and its subtopics.

The
PO factory cache settings and repository cache settings that are reflected
in the Instrumentation monitor are described in the following sections:

- PO factory
cache settings
- Repository
cache settings

## PO factory cache settings

A
persistent object (PO) factory is a class that is used to create persistent
objects. There is a PO factory for each persistent object type and
each PO factory has a cache for caching persistent objects of that
type.

There are two types of PO factory settings in Business Automation Workflow: versioned
and unversioned. For a versioned persistent object, each time
an object is changed, the new object is saved separately and does
not overwrite the old version. This allows you to view changes over
time. For an unversioned persistent object, only the latest
modification is retained and older versions are discarded.

The
following table lists the versioned and unversioned persistent objects
that are located in the PO Factory > Cache Hits and PO
Factory > Cache Misses sections of the Instrumentation
monitor. The table also lists the corresponding PO factory cache settings
that you might need to override to improve the ratio of cache hits
to cache misses. All cache settings are enabled in the XML configuration
files unless indicated otherwise.

| Type of PO in the Instrumentation monitor                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Setting and description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Setting to add or update in the 100Custom.xml file                                                                                                                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| One of:    Artifact  BPDArtifactReference  BPDParameter  BlueprintSubscription  BPDEvent  BPDParameter  Coach  CoachResource  CoachView  Connector  Contribution  ESArtifact  EnvironmentVariable    EnvironmentVariableSet  Epv  EpvVar  EventSubscription  ExtendedProperty  ExtendedPropertySet  HistoricalScenario  InfoPathForm  Layout  ManagedAsset  Metric  Participant  ProjectDefaults  ProjectDependency  RefPO  Report  ReportVariable  ResourceBundleGroup  SLA  Scoreboard  SimulationScenario  TimingInterval  TrackingGroup  UITheme  UserAttributeDefinition  WebService | default-versioned-po-cache-size This setting controls the number of objects in the versioned persistent object (PO) cache. The default value is 5000. For low-volume environments with relatively few process applications and coaches, the default value may be sufficient. However, for more complex environments with many process applications or coaches, you may want to increase this value so that the process applications and coaches are held in the cache after their initial use. This step can improve response time when accessing these process applications and coaches. Whenever the process instrumentation data indicates that there is an excessive number of PO factory cache misses, you can increase the value of the versioned PO cache. You may need to iterate through multiple values until you determine the best value for your particular scenario. After changing the value, check the process instrumentation data again and adapt the value as needed. The setting is located in the applicable 00Static.xml files, but updates to the default value of the setting must be made by adding the setting to the 100Custom.xml files. | <common>    <default-versioned-po-cache-size merge="replace">7000</default-versioned-po-cache-size> </common>                                                                                                                                                      |
| One of:    BPMSnapshotStatus  CaseProperty  ECMObject  EnvironmentType  GovernanceAssignment  GovernanceEvent  MonitorProjectInterchange  PCIndexAction  PCIndexer  PCRegistration  Priority  ProjectSubscribed  ProjectSubscription  RepositoryLog  SharedToolKitUsage  Snapshot  TimePeriod                                                                                                                                                                                                                                                                                             | default-unversioned-po-cache-size This setting controls the number of objects in the unversioned persistent object (PO) cache. The default value is 1000. For low-volume environments with relatively few process applications and coaches, the default value may be sufficient. However, for more complex environments with many process applications or coaches, you may want to increase this value so that the process applications and coaches are held in the cache after their initial use. This step can improve response time when accessing these process applications and coaches. If the process instrumentation data indicates that there is an excessive number of PO factory cache misses, you can increase the value of the unversioned PO cache. You may need to iterate through multiple values until you determine the best value for your particular scenario. After changing the value, check the process instrumentation data again and adapt the value as needed. The setting is located in the applicable 00Static.xml files, but updates to the default value of the setting must be made by adding the setting to the 100Custom.xml files. | <common>    <default-unversioned-po-cache-size merge="replace">2000</default-unversioned-po-cache-size> </common>                                                                                                                                                  |
| One of:    Project  ContentObject  ContentObjectInstance                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | time-based-project-cache-enable The time-based-project-cache-enable setting specifies whether the persistent object (PO) cache is a time-based cache. This setting is enabled by default. The expiration interval is controlled by po-cache-expiration-interval, whose default value is 20 seconds. The cache is reset if it expires after the specified expiration interval. As the cache is read after it is reset, sometimes you might see cache miscounts that are higher than the cache size.   default-unversioned-PO-cache-size The default-unversioned-PO-cache-size setting controls the number of objects in the unversioned persistent object (PO) cache. The default value is 1000. The setting is located in the applicable 00Static.xml files, but updates to the default value of the setting must be made by adding the setting to the 100Custom.xml files.                                                                                                                                                                                                                                                                                          | <common>    <time-based-project-cache-enable>true</time-based-project-cache-enable>    <po-cache-expiration-interval>20000</po-cache-expiration-interval>    <default-unversioned-po-cache-size merge="replace">2000</default-unversioned-po-cache-size> </common> |

## Repository cache settings

The
following table lists the repository cache settings that are reflected
in the Repository section of the Instrumentation
monitor. In some situations, you may need to override the cache setting
values to improve the ratio of cache hits to cache misses. All cache
settings are enabled in the XML configuration files unless indicated
otherwise.

| Name                   | Setting and description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Setting to add or update in the 100Custom.xml file                                                                                            |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Branch context cache   | branch-context-max-cache-size This setting specifies the maximum number of branch contexts that are held in the Branch Manager cache, which contains metadata about the contents of snapshots in memory and is used to improve performance of certain operations. The default value is 64. The setting is located in the applicable .00Static.xml files, but updates to the default value of the setting must be made by adding the setting to the 100Custom.xml files. If your process applications are especially large and there are memory issues in the Business Automation Workflow server, it may be necessary to reduce the value of the setting, particularly on runtime servers where a new branch is created for each deployed snapshot. Similarly, for a process server in a memory-constrained environment, reducing the Branch Manager cache size can reduce heap memory for large process applications. However, you may need to increase the value of the setting if the authored process application has a large number of dependencies on toolkits. A toolkit with one business object takes less than 1 MB of memory for the branch cache entry and the snapshot cache. The Process Portal application uses about 11 MB of memory. The system data toolkit uses several hundred MB of memory. There is a difference in memory usage because of the complexity of the relationships between the artifacts in the project and the volume of artifacts in each project. Therefore, it is difficult to precisely predict the amount of additional memory that will be used when you are tuning the branch cache. To calculate the optimal value for speed at the expense of memory on a Workflow Server environment with multiple process applications deployed, one approach is to take a row count of table LSW\_BRANCH in the database, multiply this number by 1.1, and then use the result as the value for the branch-context-max-cache-size setting. This approach assumes that all process applications are in relatively frequent use and that you want their contexts in memory. If a single process application is deployed, the optimal value is the number of dependencies of this process application plus one.Note: Whenever a new process application or snapshot is deployed or deleted from the Workflow Server environment, you need to consider adapting the cache size. | <server>    <repository>      <snapshot-cache-size-per-branch merge="replace">128</snapshot-cache-size-per-branch>    </repository> </server> |
| Snapshot context cache | snapshot-cache-size-per-branch This setting specifies the number of snapshots that are cached for a single branch in Workflow Center. The default value is 64. In Workflow Server environments, you can retain the default value because this setting is ignored on Workflow Server. Each deployed snapshot is deployed to a unique branch on Workflow Server, which means that the snapshot cache contains only one entry. The snapshot cache is tuned independently from the branch cache. Each branch cache entry contains a snapshot cache. In Workflow Center, all the snapshots on a branch use the same branch cache entry; therefore, the number of entries in the snapshot cache might be more than one. The number of entries that are needed depends on the number of snapshots that have been accessed. Snapshots are accessed when the snapshot is activated or when Process Designer users view artifacts, play back artifacts, or do both at a specific snapshot version. Therefore, tuning the snapshot cache size is necessary only for the Workflow Center server. The necessity to tune the snapshot cache is based on anticipated usage patterns. Snapshot cache entries can be quite large because they depend on application content. It is not uncommon for snapshot cache entries to reach several hundred MBs. The size depends on the complexity and volume of the artifacts in a given snapshot. For very large projects and process applications, reducing the value of the snapshot-cache-size-per-branch setting can reduce heap memory requirements (but with a corresponding degradation of performance due to more frequent database usage).  The setting is located in the applicable 00Static.xml files, but updates to the default value of the setting must be made by adding the setting to the 100Custom.xml files.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | <server>    <repository>      <snapshot-cache-size-per-branch merge="replace">128</snapshot-cache-size-per-branch>    </repository> </server> |