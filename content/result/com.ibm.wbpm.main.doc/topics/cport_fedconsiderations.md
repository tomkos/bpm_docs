# Federation considerations for Process Portal

Differences in behavior can be observed when Process Portal runs in federated environments instead of on
a single system.

## Entries in the Dashboards and Launch
list

| Single system                                                                                       | Federated environment                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| One entry for each exposed dashboard, custom dashboard, launchable process, and launchable service. | The Work and other saved search dashboards are federated, which means you see only one entry for each dashboard in the list. However, the ready-to-use dashboards (Processes, Team Performance, Process Performance) are not federated, which means you see one dashboard entry in the list for each federated system. The federation behavior of custom dashboards and launchable processes and services is configurable. You can configure these entities so that they have only one entry in the Dashboards list or an entry for each federated system. For more information, see Federation considerations for dashboards, processes, and services in Process Portal. |

| Single system                                                                                                                                                               | Federated environment                                   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| Launch list items do not refresh automatically, for example if you disable startable business process definitions. The list refreshes after you sign off and sign in again. | The Launch list refreshes automatically at each change. |

## Tasks

| Single system                 | Federated environment                                                          |
|-------------------------------|--------------------------------------------------------------------------------|
| Only BPD tasks are available. | BPD and BPEL tasks from federated systems are consolidated into a single list. |

| Single system                                                                                              | Federated environment                                                                                                                                                                                                                                                                                                                                         |
|------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| If BPD tasks are implemented with coach-based human services, you can complete them within Process Portal. | If BPD tasks are implemented with coach-based human services, you can complete them within Process Portal. For BPD and BPEL tasks that are implemented with external activities, Process Portal opens a new window to complete the task. For information about using external activities, see Integrating custom web-based user interfaces in Process Portal. |

| Single system                                                                                                                                                                                                    | Federated environment                                                                                                                                                                                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| In the Process Portal table view, BPD tasks can be displayed by priority level, sorted on their priority level, and filtered on their priority level or on the status of the process instance in saved searches. | In the Process Portal table view, the following limitations apply: The priority level of BPEL tasks is not shown. You cannot sort BPEL tasks nor mixed BPEL-BPD tasks by priority level. You cannot filter BPEL tasks on their priority level or on the status of the process instance in a saved search. |

| Single system                                               | Federated environment                                                                                                                                    |
|-------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| For tasks such as View Instance, all actions are available. | The actions depend on the systems in the federated environment. For more information, see Actions available in Process Portal in federated environments. |

## Notification

| Single system                                                                                                                                                                                                                                                  | Federated environment       |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| You can receive notifications directly in Process Portal in the following situations.  A new task is assigned to you or your user group. You are mentioned in a post on a process that you are participating in. An activity in a process instance is updated. | Notifications are disabled. |

## Saved searches

| Single system                                          | Federated environment                        |
|--------------------------------------------------------|----------------------------------------------|
| You can organize saved searches by task or by process. | Saved searches are always organized by task. |

| Single system                                                         | Federated environment                                                                                                                                                                                                                                                                                 |
|-----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| You can share saved searches with everyone and with individual teams. | You can share saved searches with everyone, and also with individual teams but with some restrictions. Saved searches can only be shared with BPD process teams that are defined by process applications that are deployed on federated IBM® Business Automation Workflow V18.0.0.1 servers or later. |

| Single system                                                                                                           | Federated environment                                                                                                  |
|-------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| Restricting the rights to create and update saved searches to a user or group of users is done through action policies. | Restricting the rights to create and update saved searches to a user or group of users is done through security roles. |

| Single system                                                                                                                                             | Federated environment                                                                                                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| The following fields support full-text search. bpdName instanceName taskActivityName taskSubject                                                          | The following fields support full-text search. bpdName instanceName instanceProcessApp instanceSnapshot taskActivityName taskSubject                                                                           |
| The query syntax in full-text searches is available and supported. For more information about saved searches, see Process Portal dashboards: Search tips. | The query syntax in full-text searches is available. For a full-text search, you can search on multiple words and use wildcards (*,?,~). For more information, see Searches using the FullTextSearch operator. |
| The quick-filter colon syntax, such as subject:, is supported. For example: $dueOn:5/23/17                                                                | The quick-filter colon syntax (:) is not supported.                                                                                                                                                            |

## Social features

| Single system                                                                                                                                                                                 | Federated environment                    |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|
| By default, these social features are available. You can disable them by using the com.ibm.bpm.portal.disableSocial custom property. For more information, see Configuring custom properties. | These social features are not available. |

## Online status indicator

| Single system                       | Federated environment                                                                                                                                         |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| You can see which users are online. | The online status indicator uses CometD messaging, which is not available in federated environments. Therefore, the online status indicator is not available. |

- Federation considerations for dashboards, processes, and services in Process Portal

In federated environments, you can configure how many times a launchable entity, such as a dashboard, in a process application that is installed on different federated systems is shown in the navigation in Process Portal. Federation policies determine how multiple occurrences of the same entity are handled.
- Actions available in Process Portal in federated environments

Process Portal can be configured for a single system or for a federated environment. The actions that you can take in Process Portal depend on the configuration.
- Federated systems and authorization for saved searches

Authorization for creating, updating, and deleting shared saved searches is determined by the corresponding security roles for the com.ibm.bpm.federated.rest.authorization REST service. These roles are set in the <authorization-roles> section of the Liberty server.xml configuration file.