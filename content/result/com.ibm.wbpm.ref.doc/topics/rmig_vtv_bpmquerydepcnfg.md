# BPMQueryDeploymentConfiguration command-line utility

- Applications that embed WebSphere Adapters
- WebSphere Adapters configured at node or cluster scope

- The entries between <applications> and </applications>
represent applications that embed WebSphere Adapters.
- The entries between <clusters> and </clusters> represent
WebSphere Adapters configured at specific cluster scope.
- The entries between <nodes> and </nodes> represent
WebSphere Adapters configured at specific node scope.

Edit the generated XML file to mark which WebSphere Adapter instances to update to version 8.0
during runtime migration.

## Prerequisites

Before invoking the BPMQueryDeploymentConfiguration command, stop all servers
and node agents associated with the profile that is being extracted.

## Location

The BPMQueryDeploymentConfiguration command-line utility is in the
target\_install\_root/bin directory.

Errors are logged in the snapshot directory in a file whose name begins with
BPMQueryDeploymentConfiguration and ends with .error.

## Syntax

```
BPMQueryDeploymentConfiguration 
source\_install\_root 
source\_profile\_name 
snapshot\_directory
```

## Parameters

## Examples

The following example extracts the deployment configuration for profile 1 in the
BPM620 source installation root directory to the directory
/MigrationSnapshots/ProcServer620/profiles/profile1:

- BPMQueryDeploymentConfiguration.sh /opt/ibm/WebSphere/ProcServer620 profile1 /MigrationSnapshots/ProcServer620
- BPMQueryDeploymentConfiguration.bat "C:\Program Files\IBM\WebSphere\ProcServer620" profile1 c:\MigrationSnapshots\ProcServer620