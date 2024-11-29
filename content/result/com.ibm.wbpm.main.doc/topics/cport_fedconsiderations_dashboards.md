# Federation considerations for dashboards, processes, and services
in Process Portal

| Policy type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                       |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PER\_SYSTEM    | Displays one launchable entity per version per federated system. Use this policy for launchable entities that work on system-specific information, such as dashboard services.This policy type is the default policy for dashboard services on BPD systems. It also applies to other service types, such as the url service type.                                                                                                 |
| FEDERATED     | Returns one launchable entity per version across all federated systems. For example, if the same version of a launchable entity exists on three federated systems, only one launchable entity is displayed.This policy type is the default policy for non-dashboard entities on BPD systems and for all launchable entities on BPEL systems.                                                                                      |
| GLOBAL        | Displays only one launchable entity across all versions and all federated systems. Use this policy to suppress older or non-default versions of a launchable entity from being displayed in Process Portal.On BPD systems, when multiple versions of launchable entities are consolidated, the default version is displayed.  On both BPD and BPEL systems, if a default version is not defined, the latest version is displayed. |

- To favor a federated system, give this system a higher launch list priority, for example,
launchListPriority="1". Lower-priority federated systems are used as backup only if
the higher priority federated system is not currently available.
- To load balance requests across the federated systems, set the launchListPriority attribute
to the same value on each federated system.

```
<ibmPfs\_launchableEntity
   systemType="${system.type}"
   containerName="${container.name}"
   containerId="${container.id}"
   entityName="${entity.name}"
   entityId="${entity.id}"
   entityType="${entity.type}"
   entitySubtype="${entity.subtype}"
   version="${version}"
   versionLabel="${version.label}"
   federationPolicy="FEDERATED|PER\_SYSTEM|GLOBAL"
/>
```

| Launchable entity attribute    | BPD attribute                                            | BPEL attribute                                                                       |
|--------------------------------|----------------------------------------------------------|--------------------------------------------------------------------------------------|
| systemType                     | systemType=SYSTEM\_TYPE\_WLE                               | systemType=SYSTEM\_TYPE\_WPS                                                           |
| containerName                  | processAppAcronym                                        | processAppAcronym                                                                    |
| containerId                    | processAppId                                             | processAppAcronym                                                                    |
| entityName                     | display                                                  | name                                                                                 |
| entityId                       | itemID                                                   | tkid                                                                                 |
| entityType                     | launchableEntityTypePossible values are PROCESS, SERVICE | launchableEntityTypePossible values are PROCESS, COLLABORATION\_TASK, INVOCATION\_TASK |
| entitySubtype                  | subtype                                                  | kind                                                                                 |
| version                        | snapshotID                                               | validFromTime                                                                        |
| versionLabel                   | snapshotName                                             | validFromTime                                                                        |

- Configure all launchable entities in the APP1 BPD application
to use the FEDERATED policy:<ibmPfs\_launchableEntity federationPolicy="FEDERATED"
   containerName="APP1"/>
- Configure a specific launchable entity in the APP1 BPD application
to use the FEDERATED policy:<ibmPfs\_launchableEntity federationPolicy="FEDERATED"
   containerName="APP1" entityName="MyService"/>
- Configure a specific launchable entity type in the APP1 BPD application
to use the FEDERATED policy:<ibmPfs\_launchableEntity federationPolicy="FEDERATED"
   containerName="APP1" entityType="PROCESS"/>

- If the same snapshot is always the default snapshot across all
federated systems, this snapshot is the default snapshot for the federation
policy.
- If the default snapshot for a process application varies across
federated systems, the latest default snapshot across all federated
systems is chosen as the default snapshot for the federated results.
- If a launchable entity doesn't exist in any default snapshot,
it doesn't have a default snapshot.