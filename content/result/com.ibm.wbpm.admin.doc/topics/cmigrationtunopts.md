# Migration tuning options

| Option                    | Default     | Description                                                                                                                                                                                                                                                                                                                                                                                                                |
|---------------------------|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <thread-pool-size>        | 5           | Set the thread pool size.                                                                                                                                                                                                                                                                                                                                                                                                  |
| <migrate-tasks>           | skip-closed | Choose which tasks will be migrated. The following options are available:  all - Migrate all tasks none - Migrate no tasks skip-closed - Migrate all tasks except closed tasks                                                                                                                                                                                                                                             |
| <defer-ec>                | false       | Choose whether to defer updating the execution context of the tasks. To ensure that corrupt execution contexts are detected during migration, leave the setting to false in the development environment. If it's necessary to improve performance, you can change the value to true in the production environment. When this option is set to true, the execution context will be updated when the task is first accessed. |
| <epv-deploy-default>      | false       | When set to true, the snapshot deployment behavior is changed. A runtime EPV change is applied to each EPV during deployment with an effective date of the deployment time and a value equal to the EPV's default value.                                                                                                                                                                                                   |
| <disable-team-sync>       | false       | When set to true, this prevents team migration from occurring during instance migration.                                                                                                                                                                                                                                                                                                                                   |
| <migrate-instances-count> |             | Specify the maximum number of instances that are migrated during one migration by using the Process Admin Console. If the setting isn't set, there is no limit.                                                                                                                                                                                                                                                            |

```
<server>
  <instance-migration>
    <thread-pool-size>5</thread-pool-size>
    <migrate-tasks>skip-closed<migrate-tasks>
    <defer-ec>false</defer-ec>
    <epv-deploy-default merge="replace">false</epv-deploy-default>   
    <disable-team-sync merge="replace">false</disable-team-sync>
    <migrate-instances-count merge="replace">10000</migrate-instances-count>
</instance-migration>
</server>
```

For more information about making changes in the 100Custom.xml file, see
The 100Custom.xml file and configuration.