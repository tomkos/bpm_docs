<!-- image -->

# Merging workspace and Process Center repository changes

## Before you begin

## About this task

You can refresh your workspace with relevant changes that
have taken place on the Workflow Center,
and publish, deploy and undeploy the process application from your Integration Designer workspace
to the Workflow Center.

## Procedure

1. Right-click the process application or toolkit in your
workspace that you want to synchronize with the Workflow Center.
2 Click the option that you want:
    - Refresh from Process Center. Merges
all changes on the Workflow Center that
do not conflict with your workspace.
    - Publish to Process Center. Refreshes
 your Integration Designer workspace
by pulling changes from Workflow Center,
and then pushes Integration Designer merges
and changes back Workflow Center. Note: In
versions earlier than Business Automation Workflow 8.5.6,
the Publish option also deployed the process
application to the Process Center server. Publish to Process
Center no longer includes deploy. To deploy your process
application after publish, use the Deploy option.
    - Deploy to Process Center. Refreshes
 your Integration Designer workspace
by pulling changes from Workflow Center,
then publishes, and then deploys the process application to Workflow Center server.
    - Undeploy. Removes the Advanced Integration
service artifacts and the associated business level application (BLA)
from the Workflow Centerserver.
3. The process application or toolkit is updated. Should there
be a conflict because an element in your workspace and an element
in the Workflow Center are
identical then you are warned if you want to proceed. If you proceed,
the element in the Workflow Center is
overridden. See Synchronizing artifacts in the workspace and the Workflow Center repository.

## What to do next

As time moves forward you will make updates to the WSDL
files you created. For synchronization purposes, the Refresh and Publish
command assumes you will make your updates with the Interface editor
or the Business Object editor where you created your WSDL file. Always
use these editors for updates. If you use another editor such as a
text editor, the result will be no synchronization with the Workflow Center.