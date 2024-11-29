# Setting up and configuring VCS integration

## Procedure

To set up and configure VCS integration:

1 Create a directory on a network shared directory to serve as a sandbox for the VCSintegration. This sandbox provides a staging area for the solution files that are to be stored in the VCS.
    - In a cluster environment, the network shared directory must be available to all nodes. You
can make the directory available to all nodes by mapping the file system on one server so that the
file system is available to other nodes in the cluster. Alternatively, you can use a file storage
device to make the network shared directory available to all nodes.
    - In a standalone environment, the network shared directory can be the local file
system.Note: When you run the BPMConfig.sh -update -profile Dmgr01 -de De1
-networkDirectory command to switch to a new path, you should use a different path rather
than the Business Automation Workflow default path. If you mount it to an external file system that
uses the default network shared directory
BAW\_INSTALL\_ROOT/CaseManagement/properties/, it might result in loss of the
original files.
2. Create the scripts that Case Builder runs to commit and deliver
to the VCS the changes that are made to a solution in Case Builder.
For more information about creating the scripts, see Commit and deliver scripts.
3 Optional: Create custom scripts to automate the deployment of solutions to other environments, such asstaging or production environments. You can create a single script to do the following tasks: Tip: Instead of using a custom script to extract the solution assets, you can usethe user interface for your VCS to download the solution assets.

1. Extract solution assets that are associated with a specific label from the VCS.
2. Call the IBM Business Automation
Workflow configuration tool to
import the solution assets to the target environment.
3. Call the IBM Business Automation
Workflow configuration tool to
deploy the solution to the target environment.
4. If the VCS requires additional credentials, configure a keystore or other solution for handling
sensitive parameters, such as the credentials for the VCS user. 

Case Builder does not pass sensitive parameters, such as
passwords, to the VCS scripts. Therefore, the scripts must look up the credentials based on the
FileNet® P8 user that does a commit or deliver, or on nonsensitive
parameters that are collected from the user.
5 Enable and configure the VCS integration by running the BPMConfig command. Forexample, the command might look like: BPMConfig.sh -update -profile DmgrProfile -de De1 -component CaseManager -enableVCS true -vcsSandboxPath /VCS -vcsHeartbeatInterval 60 -vcsCommitTimeout 120 -vcsDeliverTimeout 600 Where To disable VCS integration, you might use a command similar to:BPMConfig.sh -update -profile DmgrProfile -de De1 -component CaseManager -enableVCS false For more information on the command and its parameters, see BPMConfig command-line utility .

```
BPMConfig.sh -update -profile DmgrProfile -de De1 -component CaseManager -enableVCS true -vcsSandboxPath /VCS -vcsHeartbeatInterval 60 -vcsCommitTimeout 120 -vcsDeliverTimeout 600
```

- vcsHeartbeatInterval is the time in seconds that must elapse between periodic
updates from your commit and deliver scripts before a commit or deliver operation fails. The
heartbeat interval measures the activity of your commit and delivers scripts. You specify this
interval to detect problems in script execution before the script times out. For example, the
heartbeat can alert you to problems such as the script hanging or Case Builder terminating unexpectedly.
The heartbeat is determined by the time that the output.txt file was last
modified. Therefore, your script must periodically check the status of its own threads and update
output.txt.
If you do not want to check for a heartbeat, leave this field
blank.
- vcsCommitTimeout is the maximum time in seconds that must elapse before the
commit and deliver scripts time out.
- vcsDeliverTimeout is the time in seconds for a VCS integration deliver script
to run before the deliver operation is marked as a failure.

```
BPMConfig.sh -update -profile DmgrProfile -de De1 -component CaseManager -enableVCS false
```

6. In the configuration tool, run the Deploy Case Builder
task.

## Results

In Case Builder, your commit script is run automatically when a
user clicks Commit on the Manage Solutions page. A
Deliver action that runs your deliver script appears in the More
Actions menu on the Manage Solutions page.