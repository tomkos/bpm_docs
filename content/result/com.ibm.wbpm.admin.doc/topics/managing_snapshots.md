# Managing snapshots

- Creating snapshots, comparing, setting status, and validating

In the classic Workflow Center, you can create snapshots for process applications and toolkits and you can compare the snapshots to view the changes between them. To manage the development of your toolkit and process applications (such as testing, approvals, and reuse), you can set status for snapshots.  Additionally, you can review the validation errors and warnings at the snapshot level before you perform critical actions such as sharing or installing them.
- Cloning projects and toolkits

In IBM Workflow Center, you can produce a clone or copy of either a project or toolkit by using the Clone and Create Copy features. These functions allow for the convenient replication of projects or toolkits, and the efficient generation of more instances of case projects as needed.
- Archiving and deleting projects and toolkits

If a project or toolkit is no longer used, you can archive it. When you archive a project or toolkit, it no longer appears in the list on the Home page in IBM Workflow Center or the list in the classic Workflow Center. Before you can open an archived project or toolkit in IBM Process Designer, you must restore it.
- Importing and exporting projects and toolkits

You can import projects and toolkits from other IBM Workflow Center repositories, and you can also export projects toolkits.
- Undeploying a project or toolkit tip

The tip is the current working version of a project or toolkit. You can use Workflow Center to undeploy a project or toolkit tip from the Workflow Center server.
- Snapshot and process instance migration

You can migrate process instances and snapshot data from one snapshot to another. Various strategies and settings help ensure migration is successful.
- Comparing and opening snapshots in the desktop Process Designer (deprecated)

You can compare previously created snapshots in the Process Designer desktop editor. You can see information about the snapshots, such as the time they were created and any processes that were added to them. You can also open a snapshot to view the contents at that particular point in time. For example, if you want to see a BPD or service diagram in a previous snapshot.
- Creating snapshots from the revision history in the desktop Process Designer (deprecated)

In addition to capturing snapshots of your ongoing efforts in the desktop Process Designer, you also can create snapshots from previous points in time by using the entries in the revision history. For example, if you need a snapshot of your project as it existed before several new items were added, you can use the revision history to locate the point in time that meets your needs.
- Activating snapshots for use with Process Portal

If you want exposed items within particular snapshots to display in IBM Process Portal while those items are being developed in (and reside on) the Workflow Center server, you need to activate the snapshot that contains the version of the items that you want to display. For example, if you are developing a process and you want to start the process in Process Portal, you need to activate the snapshot that contains the version of the process that you want to start.
- Deactivating snapshots on a Workflow Center server

If you previously activated a snapshot on the Workflow Center server, you can deactivate it.
- Archiving snapshots

If a project or a toolkit snapshot is no longer used, you can archive it. When you archive a snapshot, it no longer appears in the list of snapshots for the project. You must restore a snapshot if you want to edit it or perform any other actions on it.
- Undeploying a snapshot on a Workflow Center server

If a process application snapshot contains advanced content generated in IBM Integration Designer (for example, SCA modules or BPEL processes), you can use Workflow Center to undeploy a snapshot from the Workflow Center server.
- Deleting unnamed snapshots from a Workflow Center server, automated method

You can configure IBM Workflow Center to automatically delete unnamed snapshots that you no longer need to keep on the server. Automatic deletion never removes named snapshots.
- Deleting unneeded snapshots from a Workflow Center server manually

Every time that a Process Designer user saves work, an unnamed snapshot is created. Hundreds of unnamed snapshots quickly accumulate. Over time, you can also accumulate snapshots that were once active but are no longer used. Deleting the snapshots that are not used or needed is good practice for several reasons.