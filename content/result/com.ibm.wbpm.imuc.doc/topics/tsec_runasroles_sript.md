# Defining RunAs roles user assignments for system applications

## About this task

- IBM\_BPM\_PerformanceDW\_supportDeploymentTarget
- IBM\_BPM\_Teamworks\_applicationDeploymentTarget
- BPEContainer\_\_applicationDeploymentTarget
- TaskContainer\_\_applicationDeploymentTarget

Where the suffix is either the application cluster or
the stand-alone server (for IBM Business Process Manager
Express and IBM Integration
Designer's
Unit Test Environment (UTE)), and the support cluster or stand-alone
server:  \_clusterName  or  \_nodeName\_serverName.

- Standalone environmentwsadmin -username WAS\_admin -password WAS\_admin\_password -f bpmModifyMapRunAsRole.py -usr user -pwd pwd -nodeName node -serverName server -applicationName appNamewhere
WAS\_admin is
the administrative user name 
WAS\_admin\_password is
the administrative password
user is
the user to be set for the RunAs roles 
pwd is
the pwd to be set for the RunAs roles 
node is
the name of the node 
server is
the name of the server 
appName is
the name of the application
- Clustered environmentwsadmin -username WAS\_admin -password WAS\_admin\_password -f bpmModifyMapRunAsRole.py -usr user -pwd pwd -clusterName cluster -applicationName appNamewhere
WAS\_admin is
the administrative user name 
WAS\_admin\_password is
the administrative password 
user is
the user to be set for the RunAs roles 
pwd is
the pwd to be set for the RunAs roles 
cluster is
the name of the cluster
appName is
the name of the application