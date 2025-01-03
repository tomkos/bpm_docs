# Testing your solution

## About this task

You can view the solution deployment status in the solution summary view on the Manage
Solutions page.

## Procedure

To validate and test your solution:

1. From the Manage Solutions page, click Commit to
make all of your edits and updates available for deployment.
2 From the Manage Solutions page, click Deploy in thesolution summary to deploy the solution to your project area. Deployment is a process that runs in the background. You can work on other solutions while thesolution is being deployed. If multiple users are editing the same solution, a list of lockeditems is shown, and you are prompted to continue to deploy the solution, or to cancel deploying thesolution. If you continue to deploy the solution, it does not contain any uncommitted changes. The Deploy action deploys only the artifacts that changed sincethe last time you deployed the solution. In some situations, you must redeploy all solutionartifacts. For example, you must redeploy all solution artifacts in the following instances: To redeploy all solution artifacts, click the Click to see moreactions icon and select Redeploy All . After you have redeployedall solution artifacts, click the Actions icon and select RefreshSolutions . Note: In an IBM WorkflowCenter augmentedenvironment Workflow Server , redeploying alllegacy case solutions updates the default case solution playback Case Client from the previous IBM Business AutomationWorkflow desktop to the new IBM Business AutomationWorkflow desktop.

If multiple users are editing the same solution, a list of locked
items is shown, and you are prompted to continue to deploy the solution, or to cancel deploying the
solution. If you continue to deploy the solution, it does not contain any uncommitted changes.

    - You modified or added a globalization file, one of the Resource.js files, for the solution in
the development object store.
    - You updated the solution workflow file (global XPDL), but changed nothing else in the
solution.
    - The solution is an older version that was created in IBM® Business Automation
Workflow. You must redeploy all
solution artifacts to ensure that when you click Test, the runtime URL
includes the baw desktop ID rather than the old
icm desktop ID.
    - The desktop ID associated with the project area is changed. You must redeploy the solution
artifacts to ensure that when you click Test, the runtime URL includes the
new desktop ID.

To redeploy all solution artifacts, click the Click to see more
actions icon and select Redeploy All. After you have redeployed
all solution artifacts, click the Actions icon and select Refresh
Solutions.

3 Click Test to open Case Client .

1. The first time that you test your solution expand your solution in the list of available
solutions, click Manage Roles, and add yourself as a user to one or more
roles.
2. Click Add Case to add a case to the solution. Verify
that the preconditions for the case are met.
3. Open and complete a work item from the in-basket to verify that the page works
correctly.
4. Verify that case types, tasks, and roles are created and working. 
To verify that the other components in the solution work correctly, open and test other pages
and cases. You can search for cases by going to the case pages and searching for a case by
date.

## What to do next

If
you are done testing this solution and all other solutions in the project area, you can click Actions > Reset Test Environment on the Manage Solutions page.