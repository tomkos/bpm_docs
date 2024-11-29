# Copying a solution to another development environment

## Procedure

To copy a solution package to a different development
design object store:

1. If your solution contains assets that were created outside of Business Automation Workflow, in 
FileNet®
 Deployment Manager, create a
deploy package that contains the assets. Then, use Administration Console for Content Platform
Engine to add the deploy
package to the source server design object store in the solution folder.
If your solution contains marking sets, you must manually recreate the marking sets and the
properties that use the marking sets in the target environment.
2. In the Business Automation Workflow
administration client, export the case management solution package from the source development
environment case management design object store to the server where you run the administration
client.
3. In the administration client, import the solution package from the local server where you run
the administration client to the target environment design object store.
4. In the administration client or Case Builder, deploy the solution package
in the target environment.
5. If your solution contains assets that were created outside of Business Automation Workflow, download the assets
from the target environment design object store (from Step 3), and then in FileNet Deployment
Manager, expand the assets in the
target environment and then import the assets to the target object store.

See the FileNet Deployment
Manager
documentation for details on the steps in this procedure: Deploying IBM
FileNet P8 applications > Prepare data for deployment > How
to... > Prepare Content Engine data > Manage deploy
packages

## What to do next

If your solution is associated with a process
application, and you copy or move the solution
to a different environment, you must also copy or move the process
application.