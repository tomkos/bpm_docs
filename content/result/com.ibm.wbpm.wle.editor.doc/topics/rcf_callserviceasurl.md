# Calling a dynamically selected client-side human service version (snapshot)

By using name-based parameters instead of the original ID-based parameters, you can keep the URL
unchanged regardless of what updates to the service or process application are made and deployed.

- processApp: The short name or the acronym of the process
application.
- serviceName: The name of the client-side human service.
- snapshotName: (Optional) The name of the snapshot to use. When this parameter is not specified, the
default snapshot is used on the workflow
server, and the latest version (or tip of the default branch or track) is used on Workflow Center.

- modelID: The ID of the client-side human service. When
modelID is present, the serviceName parameter is
ignored.
- branchID: The ID of the branch or track on Workflow Center. When
processApp and serviceName are used, you can use
branchID to identify the branch in which to find the client-side human service.
When snapshotName is also present, branchID is
ignored.
- snapshotID: The ID of the snapshot. When snapshotID is used,
processApp, snapshotName, and
branchID are ignored.

```
http://hostname:port/contextRootPrefix/executecf?processApp=SYSRP&serviceName=RESPONSIVE\_WORK
```

For more information about how to configure a custom context root, see the section
for the -update parameter in the BPMConfig command-line utility topic.