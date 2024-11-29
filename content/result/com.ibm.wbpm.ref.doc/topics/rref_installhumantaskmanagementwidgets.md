# installHumanTaskManagementWidgets command

## Syntax

```
installHumanTaskManagementWidgets
-clusterName cluster\_name
-serverName server\_name -nodeName node\_name
```

## Required parameters

If you specify
the clusterName parameter, do not specify the serverName and nodeName parameters.

## Example

```
AdminTask.installHumanTaskManagementWidgets('-clusterClusterName Support')
AdminConfig.save()
```