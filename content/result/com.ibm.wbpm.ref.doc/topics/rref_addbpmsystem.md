# addBPMSystem command

The addBPMSystem command is run using
the AdminTask object of the wsadmin scripting client.

## Location

Start the wsadmin scripting client
from the deployment\_manager\_profile/bin directory.

## Syntax

```
addBPMSystem 
-bpmCellName cell\_name
-bpmSystemType BPEL | BPD
-bpmHostName host\_name
-bpmPort port
-bpmTransportType http | https
[-bpmNodeName node\_name -bpmServerName server\_name]
[-bpmClusterName cluster\_name]
[-processServicesContextRoot context\_root]
[-taskServicesContextRoot context\_root]
```

## Parameters

- the context root for the bfmrestapi.war file of the
BPEContainer application was changed
- the context root for the bpmrest.war file of the
IBM\_BPM\_Teamworks application was changed

- the context root for the taskrestapi.war file of the
TaskContainer application was changed.
- the context root for the bpmrest.war file of the
IBM\_BPM\_Teamworks application was changed.

## Examples

```
AdminTask.addBPMSystem('[-bpmCellName remoteCell
-bpmClusterName RemoteCell.AppCluster
-bpmSystemType BPEL -bpmHostName remoteHostname -bpmPort 443
-bpmTransportType https]')
```